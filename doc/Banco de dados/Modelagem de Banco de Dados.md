# Modelagem de Banco de Dados para BarApp, GarçomApp e Gestão do Bar

Este documento apresenta a modelagem de banco de dados proposta para suportar as funcionalidades dos aplicativos BarApp (cliente), GarçomApp (interno) e o novo Aplicativo de Gestão do Bar, incluindo as entidades, seus atributos e os relacionamentos entre elas.

## 1. Visão Geral do Modelo

O modelo de dados é projetado para ser relacional, utilizando chaves primárias (PK) e chaves estrangeiras (FK) para estabelecer os relacionamentos. Os tipos de dados são genéricos e devem ser adaptados ao SGBD (Sistema Gerenciador de Banco de Dados) escolhido (e.g., PostgreSQL, MySQL, SQL Server).

## 2. Tabelas e Atributos

### 2.1. `Usuarios` (Clientes do BarApp)

Armazena as informações dos usuários que utilizam o aplicativo cliente.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_usuario`|UUID|PK (Chave Primária)|
|`nome_completo`|VARCHAR(255)|NOT NULL|
|`email`|VARCHAR(255)|NOT NULL, UNIQUE|
|`senha_hash`|VARCHAR(255)|NOT NULL (Armazenar hash da senha)|
|`id_google`|VARCHAR(255)|NULLABLE, UNIQUE (Para login social)|
|`data_cadastro`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`ultimo_login`|TIMESTAMP|NULLABLE|
|`limite_tickets_produto`|INTEGER|DEFAULT 10 (Regra de negócio: limite de tickets por produto)|

### 2.2. `Garcons` (Usuários do GarçomApp)

Armazena as informações dos funcionários do bar que utilizam o aplicativo interno.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_garcom`|UUID|PK|
|`nome_completo`|VARCHAR(255)|NOT NULL|
|`usuario`|VARCHAR(50)|NOT NULL, UNIQUE (Nome de usuário para login)|
|`senha_hash`|VARCHAR(255)|NOT NULL (Armazenar hash da senha)|
|`data_cadastro`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`ativo`|BOOLEAN|NOT NULL, DEFAULT TRUE|

### 2.3. `Produtos`
![[Product]]

Armazena os itens do cardápio do bar.

| Atributo         | Tipo de Dado   | Restrições/Observações                                    |
| ---------------- | -------------- | --------------------------------------------------------- |
| `id_produto`     | UUID           | PK                                                        |
| `nome`           | VARCHAR(255)   | NOT NULL                                                  |
| `descricao`      | TEXT           | NULLABLE                                                  |
| `preco`          | DECIMAL(10, 2) | NOT NULL                                                  |
| `custo_unitario` | DECIMAL(10, 2) | NULLABLE (Para cálculo de lucratividade)                  |
| `estoque_atual`  | INTEGER        | NOT NULL, DEFAULT 0                                       |
| `estoque_minimo` | INTEGER        | DEFAULT 0 (Para alertas de estoque baixo)                 |
| `url_imagem`     | VARCHAR(255)   | NULLABLE                                                  |
| `disponivel`     | BOOLEAN        | NOT NULL, DEFAULT TRUE (Indica se está no cardápio ativo) |
| `id_categoria`   | UUID           | FK para `CategoriasProduto`                               |

### 2.4. `CategoriasProduto`

Armazena as categorias dos produtos do cardápio.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_categoria`|UUID|PK|
|`nome_categoria`|VARCHAR(100)|NOT NULL, UNIQUE|

### 2.5. `Tickets`

Armazena os tickets comprados pelos clientes.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_ticket`|UUID|PK|
|`id_usuario`|UUID|FK para `Usuarios` (Usuário que comprou o ticket)|
|`id_produto`|UUID|FK para `Produtos`|
|`data_compra`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`data_validade`|TIMESTAMP|NULLABLE (Prazo de validade do ticket)|
|`status`|ENUM|NOT NULL ('comprado', 'utilizado', 'transferido')|
|`data_uso`|TIMESTAMP|NULLABLE (Data e hora em que o ticket foi utilizado)|
|`id_comanda_origem`|UUID|NULLABLE, FK para `Comandas` (Se o ticket foi gerado de uma comanda paga)|

### 2.6. `HistoricoTickets`

Registra o histórico de eventos de cada ticket (compra, uso, transferência).

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_historico`|UUID|PK|
|`id_ticket`|UUID|FK para `Tickets`|
|`tipo_evento`|ENUM|NOT NULL ('compra', 'uso', 'transferencia_enviada', 'transferencia_recebida')|
|`data_evento`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`id_usuario_origem`|UUID|NULLABLE, FK para `Usuarios` (Usuário que enviou/usou)|
|`id_usuario_destino`|UUID|NULLABLE, FK para `Usuarios` (Usuário que recebeu)|
|`observacoes`|TEXT|NULLABLE|

### 2.7. `CestasCompras`

Representa a cesta de compras temporária de um usuário.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_cesta`|UUID|PK|
|`id_usuario`|UUID|FK para `Usuarios`|
|`data_criacao`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`status`|ENUM|NOT NULL ('ativa', 'finalizada', 'cancelada')|

### 2.8. `ItensCesta`

Armazena os produtos dentro de uma cesta de compras.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_item_cesta`|UUID|PK|
|`id_cesta`|UUID|FK para `CestasCompras`|
|`id_produto`|UUID|FK para `Produtos`|
|`quantidade`|INTEGER|NOT NULL, > 0|
|`preco_unitario`|DECIMAL(10, 2)|NOT NULL|

### 2.9. `MetodosPagamento`

Tabela de lookup para os métodos de pagamento aceitos.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_metodo`|INTEGER|PK|
|`nome_metodo`|VARCHAR(50)|NOT NULL, UNIQUE ('Pix', 'Credito', 'Debito')|

### 2.10. `CartoesCadastrados`

Armazena os tokens de cartões de crédito/débito para pagamentos futuros. **Importante: Nunca armazenar dados sensíveis do cartão diretamente.**

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_cartao`|UUID|PK|
|`id_usuario`|UUID|FK para `Usuarios`|
|`ultimos_digitos`|VARCHAR(4)|NULLABLE (Para exibição ao usuário)|
|`bandeira`|VARCHAR(50)|NULLABLE|
|`token_pagamento`|VARCHAR(255)|NOT NULL (Token gerado pelo gateway de pagamento)|
|`data_cadastro`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`ativo`|BOOLEAN|NOT NULL, DEFAULT TRUE|

### 2.11. `Eventos`

Armazena as informações dos eventos do bar.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_evento`|UUID|PK|
|`nome_evento`|VARCHAR(255)|NOT NULL|
|`data_evento`|TIMESTAMP|NOT NULL|
|`descricao`|TEXT|NULLABLE|
|`preco_ingresso`|DECIMAL(10, 2)|NOT NULL|
|`url_imagem`|VARCHAR(255)|NULLABLE|
|`ativo`|BOOLEAN|NOT NULL, DEFAULT TRUE|

### 2.12. `Ingressos`

Armazena os ingressos comprados pelos clientes para eventos.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_ingresso`|UUID|PK|
|`id_usuario`|UUID|FK para `Usuarios`|
|`id_evento`|UUID|FK para `Eventos`|
|`nome_ingresso`|VARCHAR(255)|NULLABLE (Ex: "Ingresso Pista", "Ingresso VIP")|
|`data_compra`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`data_uso`|TIMESTAMP|NULLABLE (Data e hora em que o ingresso foi validado)|
|`status`|ENUM|NOT NULL ('comprado', 'utilizado')|

### 2.13. `FilaKaraoke`

Gerencia a fila de pessoas para o karaokê.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_fila_karaoke`|UUID|PK|
|`nome_cantor`|VARCHAR(255)|NOT NULL|
|`nome_musica`|VARCHAR(255)|NULLABLE|
|`posicao`|INTEGER|NOT NULL, UNIQUE (Ordem na fila)|
|`data_entrada`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`status`|ENUM|NOT NULL ('na_fila', 'cantando', 'cantou')|

### 2.14. `Comandas`

Armazena as comandas de consumo dos clientes.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_comanda`|UUID|PK|
|`id_garcom`|UUID|FK para `Garcons` (Garçom que abriu a comanda)|
|`id_usuario_cliente`|UUID|NULLABLE, FK para `Usuarios` (Se o cliente for identificado no app)|
|`numero_mesa`|VARCHAR(50)|NULLABLE|
|`nome_cliente`|VARCHAR(255)|NULLABLE (Nome do cliente, se não for usuário do app)|
|`data_abertura`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`data_fechamento`|TIMESTAMP|NULLABLE|
|`status`|ENUM|NOT NULL ('aberta', 'aguardando_pagamento', 'paga', 'fechada')|
|`valor_total`|DECIMAL(10, 2)|NOT NULL, DEFAULT 0.00|

### 2.15. `ItensComanda`

Armazena os produtos adicionados a cada comanda.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_item_comanda`|UUID|PK|
|`id_comanda`|UUID|FK para `Comandas`|
|`id_produto`|UUID|FK para `Produtos`|
|`quantidade`|INTEGER|NOT NULL, > 0|
|`preco_unitario`|DECIMAL(10, 2)|NOT NULL|
|`status_cozinha`|ENUM|NOT NULL ('na_fila', 'preparando', 'pronto', 'entregue')|
|`observacoes`|TEXT|NULLABLE|

### 2.16. `PagamentosComanda`

Registra os pagamentos efetuados para as comandas (total ou parcial).

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_pagamento_comanda`|UUID|PK|
|`id_comanda`|UUID|FK para `Comandas`|
|`id_usuario`|UUID|NULLABLE, FK para `Usuarios` (Se pago via BarApp)|
|`valor_pago`|DECIMAL(10, 2)|NOT NULL|
|`id_metodo_pagamento`|INTEGER|FK para `MetodosPagamento`|
|`data_pagamento`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`tipo_pagamento`|ENUM|NOT NULL ('total', 'parcial')|
|`id_transacao_gateway`|VARCHAR(255)|NULLABLE (ID da transação no gateway de pagamento)|

### 2.17. `Notificacoes`

Armazena as notificações para usuários (clientes ou garçons).

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_notificacao`|UUID|PK|
|`id_usuario_destino`|UUID|NOT NULL (FK para `Usuarios` ou `Garcons` ou `Funcionarios`)|
|`tipo_usuario_destino`|ENUM|NOT NULL ('cliente', 'garcom', 'gestao')|
|`tipo_notificacao`|ENUM|NOT NULL ('pagamento_comanda', 'pedido_pronto', 'transferencia_ticket_recebida', 'estoque_baixo', 'novo_cadastro_cliente', 'novo_evento_criado')|
|`mensagem`|TEXT|NOT NULL|
|`data_envio`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`lida`|BOOLEAN|NOT NULL, DEFAULT FALSE|
|`referencia_id`|UUID|NULLABLE (ID do ticket, comanda, etc. relacionado)|

### 2.18. `Funcionarios` (Usuários do Aplicativo de Gestão)

Armazena informações de todos os funcionários, incluindo aqueles que usam o GarçomApp e os administrativos.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_funcionario`|UUID|PK|
|`nome_completo`|VARCHAR(255)|NOT NULL|
|`cpf`|VARCHAR(14)|NOT NULL, UNIQUE|
|`data_contratacao`|DATE|NOT NULL|
|`salario_base`|DECIMAL(10, 2)|NOT NULL|
|`cargo`|VARCHAR(100)|NOT NULL|
|`dados_bancarios`|TEXT|NULLABLE (Informações para pagamento, criptografadas)|
|`usuario_sistema`|VARCHAR(50)|NULLABLE, UNIQUE (Para login no app de gestão)|
|`senha_hash_sistema`|VARCHAR(255)|NULLABLE (Hash da senha para login no app de gestão)|
|`ativo`|BOOLEAN|NOT NULL, DEFAULT TRUE|
|`id_garcom_associado`|UUID|NULLABLE, FK para `Garcons` (Se for também um garçom)|

### 2.19. `PagamentosSalario`

Registra os pagamentos de salário efetuados aos funcionários.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_pagamento`|UUID|PK|
|`id_funcionario`|UUID|FK para `Funcionarios`|
|`valor_bruto`|DECIMAL(10, 2)|NOT NULL|
|`descontos`|DECIMAL(10, 2)|NOT NULL, DEFAULT 0.00|
|`valor_liquido`|DECIMAL(10, 2)|NOT NULL|
|`data_pagamento`|DATE|NOT NULL|
|`periodo_referencia`|VARCHAR(20)|NOT NULL (Ex: "2025-05")|
|`holerite_url`|VARCHAR(255)|NULLABLE (URL para PDF do holerite, se gerado)|

### 2.20. `Fornecedores`

Armazena informações dos fornecedores de mercadorias.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_fornecedor`|UUID|PK|
|`nome_fantasia`|VARCHAR(255)|NOT NULL|
|`razao_social`|VARCHAR(255)|NULLABLE|
|`cnpj`|VARCHAR(18)|NULLABLE, UNIQUE|
|`contato`|VARCHAR(255)|NULLABLE (Telefone, E-mail)|
|`endereco`|TEXT|NULLABLE|

### 2.21. `EntradasMercadoria`

Registra as entradas de mercadorias no estoque.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_entrada`|UUID|PK|
|`id_fornecedor`|UUID|FK para `Fornecedores`|
|`data_entrada`|TIMESTAMP|NOT NULL, DEFAULT CURRENT_TIMESTAMP|
|`numero_nota_fiscal`|VARCHAR(100)|NULLABLE|
|`valor_total`|DECIMAL(10, 2)|NOT NULL|
|`observacoes`|TEXT|NULLABLE|
|`id_funcionario_responsavel`|UUID|FK para `Funcionarios` (Quem registrou a entrada)|

### 2.22. `ItensEntradaMercadoria`

Detalha os itens de cada entrada de mercadoria.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_item_entrada`|UUID|PK|
|`id_entrada`|UUID|FK para `EntradasMercadoria`|
|`id_produto`|UUID|FK para `Produtos`|
|`quantidade`|INTEGER|NOT NULL, > 0|
|`custo_unitario_compra`|DECIMAL(10, 2)|NOT NULL (Custo na data da compra)|

### 2.23. `Permissoes`

Define os tipos de permissão para os usuários do aplicativo de gestão.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_permissao`|UUID|PK|
|`nome_permissao`|VARCHAR(100)|NOT NULL, UNIQUE (Ex: 'gerenciar_produtos', 'ver_dashboard_vendas')|
|`descricao`|TEXT|NULLABLE|

### 2.24. `FuncionarioPermissoes`

Tabela de ligação para atribuir permissões a funcionários.

|Atributo|Tipo de Dado|Restrições/Observações|
|---|---|---|
|`id_funcionario_permissao`|UUID|PK|
|`id_funcionario`|UUID|FK para `Funcionarios`|
|`id_permissao`|UUID|FK para `Permissoes`|

## 3. Relacionamentos

Abaixo estão os principais relacionamentos entre as tabelas, incluindo as novas adições:

- **`Usuarios`**
    
    - `Usuarios.id_usuario` 1:N `Tickets.id_usuario`
        
    - `Usuarios.id_usuario` 1:N `CartoesCadastrados.id_usuario`
        
    - `Usuarios.id_usuario` 1:N `Ingressos.id_usuario`
        
    - `Usuarios.id_usuario` 1:N `HistoricoTickets.id_usuario_origem`
        
    - `Usuarios.id_usuario` 1:N `HistoricoTickets.id_usuario_destino`
        
    - `Usuarios.id_usuario` 1:N `CestasCompras.id_usuario`
        
    - `Usuarios.id_usuario` 1:N `Comandas.id_usuario_cliente` (Opcional)
        
    - `Usuarios.id_usuario` 1:N `PagamentosComanda.id_usuario` (Opcional)
        
    - `Usuarios.id_usuario` 1:N `Notificacoes.id_usuario_destino` (quando `tipo_usuario_destino` é 'cliente')
        
- **`Garcons`**
    
    - `Garcons.id_garcom` 1:N `Comandas.id_garcom`
        
    - `Garcons.id_garcom` 1:N `Notificacoes.id_usuario_destino` (quando `tipo_usuario_destino` é 'garcom')
        
    - `Garcons.id_garcom` 1:1 `Funcionarios.id_garcom_associado` (Opcional, se um garçom também for um funcionário de gestão)
        
- **`Produtos`**
    
    - `Produtos.id_produto` 1:N `Tickets.id_produto`
        
    - `Produtos.id_produto` 1:N `ItensCesta.id_produto`
        
    - `Produtos.id_produto` 1:N `ItensComanda.id_produto`
        
    - `Produtos.id_produto` 1:N `ItensEntradaMercadoria.id_produto`
        
    - `Produtos.id_categoria` N:1 `CategoriasProduto.id_categoria`
        
- **`Tickets`**
    
    - `Tickets.id_ticket` 1:N `HistoricoTickets.id_ticket`
        
- **`CestasCompras`**
    
    - `CestasCompras.id_cesta` 1:N `ItensCesta.id_cesta`
        
- **`Eventos`**
    
    - `Eventos.id_evento` 1:N `Ingressos.id_evento`
        
- **`Comandas`**
    
    - `Comandas.id_comanda` 1:N `ItensComanda.id_comanda`
        
    - `Comandas.id_comanda` 1:N `PagamentosComanda.id_comanda`
        
    - `Comandas.id_comanda` 1:N `Tickets.id_comanda_origem` (Opcional)
        
- **`MetodosPagamento`**
    
    - `MetodosPagamento.id_metodo` 1:N `PagamentosComanda.id_metodo_pagamento`
        
- **`Funcionarios`**
    
    - `Funcionarios.id_funcionario` 1:N `PagamentosSalario.id_funcionario`
        
    - `Funcionarios.id_funcionario` 1:N `EntradasMercadoria.id_funcionario_responsavel`
        
    - `Funcionarios.id_funcionario` 1:N `FuncionarioPermissoes.id_funcionario`
        
    - `Funcionarios.id_funcionario` 1:N `Notificacoes.id_usuario_destino` (quando `tipo_usuario_destino` é 'gestao')
        
- **`Fornecedores`**
    
    - `Fornecedores.id_fornecedor` 1:N `EntradasMercadoria.id_fornecedor`
        
- **`EntradasMercadoria`**
    
    - `EntradasMercadoria.id_entrada` 1:N `ItensEntradaMercadoria.id_entrada`
        
- **`Permissoes`**
    
    - `Permissoes.id_permissao` 1:N `FuncionarioPermissoes.id_permissao`
        

Esta modelagem expandida fornece uma base robusta para o desenvolvimento de todos os três aplicativos, garantindo a integridade, a organização e a escalabilidade dos dados para as operações do bar.