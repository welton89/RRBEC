# Documento de Requisitos do Aplicativo de Gestão do Bar

## 1. Introdução

### 1.1. Propósito

Este documento detalha os requisitos funcionais, não funcionais, regras de negócio e requisitos de sistema para o desenvolvimento de um aplicativo web de gestão para o bar, a ser desenvolvido em Django/Python. Este aplicativo centralizará o controle de todas as operações do bar, incluindo as funcionalidades já existentes nos aplicativos mobile (BarApp e GarçomApp), além de novas funcionalidades de gestão empresarial.

### 1.2. Escopo

O aplicativo de gestão será uma plataforma web acessível por navegadores, destinada a administradores e gerentes do bar. Ele englobará a gestão de clientes, produtos, tickets, ingressos, karaokê, comandas, funcionários, salários, estoque e dashboards de resultados.

### 1.3. Público-alvo

- **Administradores:** Usuários com acesso total ao sistema, responsáveis pela configuração e gestão estratégica.
    
- **Gerentes:** Usuários com acesso a funcionalidades operacionais e de relatórios.
    
- **Funcionários Administrativos:** Usuários com acesso a funcionalidades específicas, como gestão de estoque ou folha de pagamento.
    

## 2. Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer aos usuários do aplicativo de gestão.

### 2.1. Gerenciamento de Usuários (Clientes e Garçons)

- **RFGSA001 - Gerenciar Clientes (BarApp):** O sistema deve permitir que o administrador visualize, edite e exclua cadastros de clientes do BarApp.
    
- **RFGSA002 - Gerenciar Garçons (GarçomApp):** O sistema deve permitir que o administrador cadastre, edite (nome, usuário, senha) e exclua garçons que utilizarão o GarçomApp.
    
- **RFGSA003 - Gerenciar Permissões de Garçons:** O sistema deve permitir que o administrador atribua diferentes níveis de permissão aos garçons (e.g., acesso a comandas, acesso a karaokê).
    

### 2.2. Gerenciamento de Cardápio e Produtos

- **RFGSA004 - Cadastrar Produto:** O sistema deve permitir que o administrador cadastre novos produtos no cardápio (nome, descrição, preço, imagem, categoria).
    
- **RFGSA005 - Editar Produto:** O sistema deve permitir que o administrador edite informações de produtos existentes.
    
- **RFGSA006 - Excluir Produto:** O sistema deve permitir que o administrador exclua produtos do cardápio.
    
- **RFGSA007 - Gerenciar Categorias de Produtos:** O sistema deve permitir o cadastro, edição e exclusão de categorias de produtos.
    
- **RFGSA008 - Gerenciar Disponibilidade de Produtos:** O sistema deve permitir que o administrador marque produtos como disponíveis ou indisponíveis no cardápio do BarApp.
    

### 2.3. Gerenciamento de Tickets

- **RFGSA009 - Visualizar Tickets Vendidos:** O sistema deve exibir uma lista de todos os tickets vendidos, com detalhes (produto, comprador, data de compra, status).
    
- **RFGSA010 - Consultar Histórico de Tickets:** O sistema deve permitir a consulta do histórico de uso e transferência de tickets.
    
- **RFGSA011 - Configurar Prazo de Validade de Tickets:** O sistema deve permitir que o administrador configure o prazo de validade padrão para os tickets.
    
- **RFGSA012 - Configurar Limite de Compra de Tickets:** O sistema deve permitir que o administrador configure o limite de compra de tickets por produto por usuário.
    

### 2.4. Gerenciamento de Eventos e Ingressos

- **RFGSA013 - Cadastrar Evento:** O sistema deve permitir que o administrador cadastre novos eventos (nome, data, hora, descrição, preço do ingresso, imagem).
    
- **RFGSA014 - Editar Evento:** O sistema deve permitir que o administrador edite informações de eventos existentes.
    
- **RFGSA015 - Excluir Evento:** O sistema deve permitir que o administrador exclua eventos.
    
- **RFGSA016 - Visualizar Ingressos Vendidos:** O sistema deve exibir uma lista de todos os ingressos vendidos para eventos.
    
- **RFGSA017 - Consultar Status de Ingressos:** O sistema deve permitir verificar o status de uso de cada ingresso.
    

### 2.5. Gerenciamento da Fila do Karaokê

- **RFGSA018 - Visualizar Fila do Karaokê:** O sistema deve exibir a fila do karaokê em tempo real, permitindo ao administrador acompanhar e gerenciar.
    
- **RFGSA019 - Gerenciar Fila do Karaokê (Admin):** O sistema deve permitir que o administrador adicione, edite, exclua e altere a posição de pessoas na fila do karaokê.
    

### 2.6. Gerenciamento de Comandas

- **RFGSA020 - Visualizar Todas as Comandas:** O sistema deve exibir uma lista completa de todas as comandas (abertas, aguardando pagamento, pagas, fechadas).
    
- **RFGSA021 - Detalhes da Comanda:** O sistema deve permitir que o administrador visualize os detalhes de cada comanda (itens, valores, histórico de pagamentos).
    
- **RFGSA022 - Editar Comanda (Admin):** O sistema deve permitir que o administrador edite qualquer informação de uma comanda (itens, status, etc.).
    
- **RFGSA023 - Fechar Comanda (Admin):** O sistema deve permitir que o administrador feche uma comanda manualmente.
    
- **RFGSA024 - Gerar Relatório de Comandas:** O sistema deve gerar relatórios de comandas por período, garçom, status, etc.
    

### 2.7. Gerenciamento de Funcionários

- **RFGSA025 - Cadastrar Funcionário:** O sistema deve permitir o cadastro de novos funcionários (nome, CPF, cargo, data de contratação, salário base, dados bancários).
    
- **RFGSA026 - Editar Dados do Funcionário:** O sistema deve permitir a edição dos dados cadastrais dos funcionários.
    
- **RFGSA027 - Excluir Funcionário:** O sistema deve permitir a exclusão de registros de funcionários.
    
- **RFGSA028 - Gerenciar Cargos:** O sistema deve permitir o cadastro, edição e exclusão de cargos e suas descrições.
    

### 2.8. Gestão de Pagamentos de Salário

- **RFGSA029 - Registrar Pagamento de Salário:** O sistema deve permitir o registro de pagamentos de salário para funcionários (valor, data, período de referência).
    
- **RFGSA030 - Gerar Holerite:** O sistema deve gerar holerites (recibos de pagamento) para os funcionários, contendo detalhes do salário, descontos e benefícios.
    
- **RFGSA031 - Visualizar Histórico de Pagamentos:** O sistema deve exibir o histórico de pagamentos de salário por funcionário.
    

### 2.9. Gestão de Estoque e Entrada de Mercadorias

- **RFGSA032 - Registrar Entrada de Mercadoria:** O sistema deve permitir o registro de entrada de mercadorias no estoque (produto, quantidade, data, fornecedor, custo unitário).
    
- **RFGSA033 - Atualizar Estoque:** O sistema deve atualizar automaticamente o estoque dos produtos após a entrada de mercadorias.
    
- **RFGSA034 - Visualizar Estoque Atual:** O sistema deve exibir o estoque atual de todos os produtos.
    
- **RFGSA035 - Alerta de Estoque Baixo:** O sistema deve gerar alertas quando o estoque de um produto atingir um nível mínimo configurável.
    
- **RFGSA036 - Gerenciar Fornecedores:** O sistema deve permitir o cadastro, edição e exclusão de informações de fornecedores.
    

### 2.10. Dashboard de Resultados e Relatórios

- **RFGSA037 - Dashboard de Vendas:** O sistema deve exibir um dashboard com métricas de vendas (total de vendas, vendas por produto, vendas por período, vendas por garçom).
    
- **RFGSA038 - Dashboard de Lucratividade:** O sistema deve exibir um dashboard com métricas de lucratividade (receita, custo de mercadoria vendida, lucro bruto).
    
- **RFGSA039 - Relatório de Estoque:** O sistema deve gerar relatórios detalhados sobre o estoque (movimentação, valor do estoque).
    
- **RFGSA040 - Relatório de Desempenho de Funcionários:** O sistema deve gerar relatórios sobre o desempenho dos garçons (e.g., número de comandas abertas, valor total de vendas).
    
- **RFGSA041 - Relatório Financeiro:** O sistema deve gerar relatórios financeiros consolidados (receitas, despesas, fluxo de caixa).
    

## 3. Requisitos Não Funcionais (RNF)

### 3.1. Usabilidade

- **RNFGSA001 - Interface Web Intuitiva:** A interface web deve ser intuitiva, responsiva e fácil de navegar para administradores e gerentes.
    
- **RNFGSA002 - Painéis de Controle Claros:** Os dashboards e relatórios devem apresentar informações de forma clara e visualmente atraente.
    
- **RNFGSA003 - Geração de Relatórios:** Relatórios devem ser exportáveis em formatos comuns (e.g., PDF, CSV, Excel).
    

### 3.2. Desempenho

- **RNFGSA004 - Tempo de Resposta:** O tempo de resposta para operações de gestão e carregamento de dashboards não deve exceder 5 segundos.
    
- **RNFGSA005 - Capacidade de Processamento:** O sistema deve ser capaz de processar um grande volume de dados de vendas, estoque e funcionários sem lentidão.
    

### 3.3. Segurança

- **RNFGSA006 - Autenticação de Administradores:** O sistema deve garantir que apenas usuários autorizados (administradores, gerentes) possam acessar o painel de gestão.
    
- **RNFGSA007 - Controle de Acesso Baseado em Papéis (RBAC):** O sistema deve implementar um controle de acesso robusto, onde diferentes papéis de usuário (administrador, gerente, etc.) têm permissões específicas.
    
- **RNFGSA008 - Proteção de Dados Sensíveis:** Informações financeiras, de funcionários e de clientes devem ser armazenadas e transmitidas de forma criptografada e segura.
    
- **RNFGSA009 - Auditoria:** O sistema deve registrar logs de auditoria para ações críticas realizadas pelos usuários de gestão.
    

### 3.4. Confiabilidade

- **RNFGSA010 - Disponibilidade:** O sistema deve estar disponível 99,5% do tempo.
    
- **RNFGSA011 - Integridade dos Dados:** O sistema deve garantir a integridade e consistência de todos os dados financeiros e de estoque.
    
- **RNFGSA012 - Backup e Recuperação:** Deve haver um plano de backup e recuperação de desastres para os dados do sistema.
    

### 3.5. Manutenibilidade

- **RNFGSA013 - Arquitetura Modular:** O sistema deve ser desenvolvido com uma arquitetura modular para facilitar a manutenção e a adição de novas funcionalidades.
    
- **RNFGSA014 - Documentação Interna:** O código e a arquitetura do sistema devem ser bem documentados.
    

### 3.6. Compatibilidade

- **RNFGSA015 - Compatibilidade com Navegadores:** O sistema deve ser compatível com os principais navegadores web modernos (Chrome, Firefox, Edge, Safari).
    
- **RNFGSA016 - Responsividade Web:** A interface deve ser responsiva e adaptável a diferentes tamanhos de tela (desktops, tablets).
    

## 4. Regras de Negócio (RN)

### 4.1. Funcionários e Salários

- **RNGSA001 - Salário Base:** Cada funcionário deve ter um salário base definido.
    
- **RNGSA002 - Período de Pagamento:** Salários são pagos em períodos definidos (e.g., mensalmente).
    
- **RNGSA003 - Descontos Legais:** O sistema deve calcular e aplicar descontos legais (e.g., impostos, previdência) nos holerites.
    

### 4.2. Estoque

- **RNGSA004 - Atualização de Estoque:** A venda de produtos (via tickets ou comandas) deve decrementar automaticamente o estoque.
    
- **RNGSA005 - Custo Médio Ponderado:** O sistema deve calcular o custo médio ponderado dos produtos em estoque para fins de lucratividade.
    

## 5. Requisitos de Sistema (RS)

### 5.1. Tecnologia

- **RSGSA001 - Framework:** O sistema será desenvolvido utilizando o framework Django (Python).
    
- **RSGSA002 - Banco de Dados:** Será utilizado um banco de dados relacional (e.g., PostgreSQL, MySQL).
    
- **RSGSA003 - Servidor Web:** O sistema será hospedado em um servidor web (e.g., Nginx, Apache).
    

### 5.2. Integrações

- **RSGSA004 - Integração com BarApp e GarçomApp:** O sistema de gestão atuará como o backend central para os aplicativos mobile, gerenciando seus dados.
    
- **RSGSA005 - Integração com Gateway de Pagamento:** O sistema de gestão deve ter acesso às informações de transações do gateway de pagamento.
    
- **RSGSA006 - Integração com Sistema de Cozinha:** O sistema de gestão deve se comunicar com o sistema da cozinha para gerenciar o status dos pedidos.