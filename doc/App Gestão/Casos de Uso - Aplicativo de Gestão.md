# Casos de Uso do Aplicativo de Gestão do Bar

Este documento descreve os principais casos de uso para o aplicativo de gestão do bar, detalhando as interações entre os atores e o sistema.

## Atores

- **Administrador:** Usuário com acesso total ao sistema.
    
- **Gerente:** Usuário com acesso operacional e de relatórios.
    
- **Funcionário Administrativo:** Usuário com acesso a módulos específicos (e.g., estoque, folha de pagamento).
    
- **Sistema de Pagamento:** Serviço externo para processamento de transações.
    
- **Sistema de Cozinha:** Sistema responsável pelo gerenciamento de pedidos na cozinha.
    

## Casos de Uso

### 1. Gerenciamento de Usuários (Clientes e Garçons)

#### CUGSA001: Gerenciar Clientes

- **Nome:** Gerenciar Clientes
    
- **Ator:** Administrador
    
- **Descrição:** Permite ao administrador visualizar, editar e excluir informações de clientes do BarApp.
    
- **Fluxo Principal:**
    
    1. Administrador acessa o módulo de "Clientes".
        
    2. Sistema exibe lista de clientes.
        
    3. Administrador seleciona cliente para visualizar/editar/excluir.
        
    4. Sistema realiza a ação solicitada.
        

#### CUGSA002: Gerenciar Garçons

- **Nome:** Gerenciar Garçons
    
- **Ator:** Administrador
    
- **Descrição:** Permite ao administrador cadastrar, editar e excluir garçons.
    
- **Fluxo Principal:**
    
    1. Administrador acessa o módulo de "Garçons".
        
    2. Sistema exibe lista de garçons.
        
    3. Administrador seleciona opção para "Cadastrar Novo Garçom", "Editar Garçom" ou "Excluir Garçom".
        
    4. Sistema realiza a ação e atualiza o registro de garçons.
        

### 2. Gerenciamento de Cardápio e Produtos

#### CUGSA003: Gerenciar Produtos do Cardápio

- **Nome:** Gerenciar Produtos do Cardápio
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite gerenciar produtos, incluindo cadastro, edição, exclusão e status de disponibilidade.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Cardápio/Produtos".
        
    2. Sistema exibe lista de produtos.
        
    3. Ator seleciona opção para "Adicionar Produto", "Editar Produto", "Excluir Produto" ou "Alterar Disponibilidade".
        
    4. Sistema realiza a ação e atualiza o cardápio.
        

### 3. Gerenciamento de Tickets e Ingressos

#### CUGSA004: Consultar Tickets

- **Nome:** Consultar Tickets
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite visualizar e consultar detalhes de tickets vendidos e seus históricos.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Tickets".
        
    2. Sistema exibe lista de tickets.
        
    3. Ator pode filtrar por produto, usuário, status, data.
        
    4. Ator seleciona ticket para ver histórico de uso/transferência.
        

#### CUGSA005: Gerenciar Eventos e Ingressos

- **Nome:** Gerenciar Eventos e Ingressos
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite gerenciar eventos e os ingressos associados.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Eventos".
        
    2. Sistema exibe lista de eventos.
        
    3. Ator seleciona opção para "Cadastrar Novo Evento", "Editar Evento", "Excluir Evento".
        
    4. Ator pode visualizar lista de ingressos vendidos para um evento específico.
        

### 4. Gerenciamento da Fila do Karaokê

#### CUGSA006: Gerenciar Fila do Karaokê (Admin)

- **Nome:** Gerenciar Fila do Karaokê (Admin)
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite o controle total da fila do karaokê.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Karaokê".
        
    2. Sistema exibe a fila em tempo real.
        
    3. Ator pode adicionar, editar, remover ou reordenar pessoas na fila.
        

### 5. Gerenciamento de Comandas

#### CUGSA007: Gerenciar Comandas (Admin)

- **Nome:** Gerenciar Comandas (Admin)
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite visualizar, editar e fechar comandas.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Comandas".
        
    2. Sistema exibe lista de comandas com seus status.
        
    3. Ator seleciona comanda para ver detalhes, editar itens, alterar status ou fechar.
        

### 6. Gerenciamento de Funcionários

#### CUGSA008: Gerenciar Dados de Funcionários

- **Nome:** Gerenciar Dados de Funcionários
    
- **Ator:** Administrador, Funcionário Administrativo (RH)
    
- **Descrição:** Permite o cadastro e a manutenção dos dados dos funcionários.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Funcionários".
        
    2. Sistema exibe lista de funcionários.
        
    3. Ator seleciona opção para "Cadastrar Novo Funcionário", "Editar Dados" ou "Excluir Funcionário".
        
    4. Sistema atualiza o cadastro de funcionários.
        

### 7. Gestão de Pagamentos de Salário

#### CUGSA009: Registrar Pagamento de Salário

- **Nome:** Registrar Pagamento de Salário
    
- **Ator:** Administrador, Funcionário Administrativo (RH)
    
- **Descrição:** Permite registrar os pagamentos de salário e gerar holerites.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Folha de Pagamento".
        
    2. Ator seleciona funcionário e insere detalhes do pagamento (valor, período).
        
    3. Sistema registra o pagamento e gera o holerite.
        

#### CUGSA010: Consultar Histórico de Pagamentos

- **Nome:** Consultar Histórico de Pagamentos
    
- **Ator:** Administrador, Funcionário Administrativo (RH)
    
- **Descrição:** Permite visualizar o histórico de pagamentos de salário por funcionário.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Folha de Pagamento".
        
    2. Ator seleciona funcionário para ver seu histórico de pagamentos.
        

### 8. Gestão de Estoque e Entrada de Mercadorias

#### CUGSA011: Registrar Entrada de Mercadoria

- **Nome:** Registrar Entrada de Mercadoria
    
- **Ator:** Administrador, Funcionário Administrativo (Estoque)
    
- **Descrição:** Permite registrar a entrada de novos produtos no estoque.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Estoque/Entrada de Mercadorias".
        
    2. Ator seleciona produto, quantidade, fornecedor e custo.
        
    3. Sistema registra a entrada e atualiza o estoque do produto.
        

#### CUGSA012: Gerenciar Estoque

- **Nome:** Gerenciar Estoque
    
- **Ator:** Administrador, Funcionário Administrativo (Estoque)
    
- **Descrição:** Permite visualizar o estoque atual e gerenciar fornecedores.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Estoque".
        
    2. Sistema exibe o estoque atual de todos os produtos.
        
    3. Ator pode gerenciar fornecedores (cadastrar, editar, excluir).
        

### 9. Dashboard de Resultados e Relatórios

#### CUGSA013: Visualizar Dashboard de Vendas

- **Nome:** Visualizar Dashboard de Vendas
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite visualizar gráficos e métricas de vendas.
    
- **Fluxo Principal:**
    
    1. Ator acessa o "Dashboard de Vendas".
        
    2. Sistema exibe métricas como total de vendas, vendas por produto/período/garçom.
        

#### CUGSA014: Visualizar Dashboard de Lucratividade

- **Nome:** Visualizar Dashboard de Lucratividade
    
- **Ator:** Administrador, Gerente
    
- **Descrição:** Permite visualizar gráficos e métricas de lucratividade.
    
- **Fluxo Principal:**
    
    1. Ator acessa o "Dashboard de Lucratividade".
        
    2. Sistema exibe receita, custos e lucro bruto.
        

#### CUGSA015: Gerar Relatórios

- **Nome:** Gerar Relatórios
    
- **Ator:** Administrador, Gerente, Funcionário Administrativo
    
- **Descrição:** Permite gerar diversos relatórios para análise.
    
- **Fluxo Principal:**
    
    1. Ator acessa o módulo de "Relatórios".
        
    2. Ator seleciona o tipo de relatório (estoque, financeiro, desempenho de funcionários).
        
    3. Ator define filtros (período, funcionário, produto).
        
    4. Sistema gera o relatório e permite exportação.