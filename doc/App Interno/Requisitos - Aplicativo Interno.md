# Documento de Requisitos do Aplicativo GarçomApp

## 1. Introdução

### 1.1. Propósito

Este documento tem como objetivo detalhar os requisitos funcionais, não funcionais, regras de negócio e requisitos de sistema para o desenvolvimento do aplicativo mobile "GarçomApp". O aplicativo visa otimizar as operações internas do bar, permitindo que os garçons gerenciem tickets, ingressos, a fila do karaokê, comandas de consumo e acompanhem o status dos pedidos da cozinha.

### 1.2. Escopo

O aplicativo GarçomApp será uma solução mobile disponível para as plataformas Android e iOS (ou uma única plataforma, a ser definida), de uso exclusivo da equipe do bar (garçons). Ele permitirá a interação com os clientes através de QR Codes e a gestão de processos internos.

### 1.3. Público-alvo

- **Garçons/Atendentes:** Profissionais do bar que utilizarão o aplicativo para gerenciar as operações diárias.
    

## 2. Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer aos garçons.

### 2.1. Autenticação e Acesso

- **RFG001 - Login de Garçom:** O sistema deve permitir que o garçom faça login utilizando suas credenciais de acesso (usuário e senha fornecidos pelo bar).
    

### 2.2. Gerenciamento de Tickets e Ingressos

- **RFG002 - Leitura e Validação de Ticket:** O sistema deve permitir que o garçom leia o QR Code de um ticket gerado pelo cliente (no BarApp) e valide seu uso.
    
- **RFG003 - Leitura e Validação de Ingresso:** O sistema deve permitir que o garçom leia o QR Code de um ingresso gerado pelo cliente (no BarApp) e valide sua entrada no evento.
    
- **RFG004 - Registro de Uso:** Após a validação, o sistema deve registrar o ticket/ingresso como utilizado, com data e hora.
    

### 2.3. Gerenciamento da Fila do Karaokê

- **RFG005 - Visualização da Fila do Karaokê:** O sistema deve exibir a fila atual de pessoas para o karaokê em tempo real.
    
- **RFG006 - Adicionar Pessoa à Fila:** O sistema deve permitir que o garçom adicione uma pessoa à fila do karaokê (e.g., nome, música).
    
- **RFG007 - Editar Posição na Fila:** O sistema deve permitir que o garçom altere a posição de uma pessoa na fila.
    
- **RFG008 - Remover Pessoa da Fila:** O sistema deve permitir que o garçom remova uma pessoa da fila.
    
- **RFG009 - Marcar Próximo a Cantar:** O sistema deve permitir que o garçom marque a próxima pessoa a cantar.
    

### 2.4. Gerenciamento de Comandas

- **RFG010 - Visualização de Comandas Abertas:** O sistema deve exibir uma lista de todas as comandas abertas no bar.
    
- **RFG011 - Visualização de Comandas Aguardando Pagamento:** O sistema deve exibir uma lista de comandas que foram solicitadas para pagamento pelo cliente e estão aguardando confirmação.
    
- **RFG012 - Abrir Nova Comanda:** O sistema deve permitir que o garçom abra uma nova comanda, associando-a a um cliente (opcional) e/ou mesa.
    
- **RFG013 - Editar Informações da Comanda:** O sistema deve permitir que o garçom edite informações da comanda, como nome do cliente e número da mesa.
    
- **RFG014 - Adicionar Produto à Comanda:** O sistema deve permitir que o garçom adicione produtos do cardápio a uma comanda aberta.
    
- **RFG015 - Fechar Comanda:** O sistema deve permitir que o garçom marque uma comanda como fechada após o pagamento.
    
- **RFG016 - Gerar QR Code para Pagamento (Comanda):** O sistema deve permitir que o garçom gere um QR Code para que o cliente pague a comanda (total ou parcial) via Pix através do BarApp.
    

### 2.5. Acompanhamento de Pedidos da Cozinha

- **RFG017 - Visualização do Andamento de Pedidos:** O sistema deve exibir o status dos pedidos enviados para a cozinha (e.g., "na fila", "preparando", "pronto").
    
- **RFG018 - Detalhes do Pedido:** O garçom deve poder visualizar os detalhes de cada pedido (itens, comanda associada).
    

### 2.6. Notificações

- **RFG019 - Notificação de Pagamento de Comanda:** O sistema deve notificar o garçom quando o pagamento de uma comanda sob sua responsabilidade for efetuado pelo cliente via BarApp.
    
- **RFG020 - Notificação de Pedido Pronto:** O sistema deve notificar o garçom quando um prato/pedido da cozinha estiver pronto para ser entregue.
    

## 3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais descrevem as qualidades do sistema.

### 3.1. Usabilidade

- **RNFG001 - Interface Otimizada para Garçons:** A interface deve ser projetada para uso rápido e eficiente em um ambiente de bar, com botões grandes e fluxo otimizado para as tarefas mais frequentes.
    
- **RNFG002 - Tempo de Resposta:** O tempo de resposta do aplicativo para todas as interações do garçom não deve exceder 2 segundos.
    
- **RNFG003 - Consistência Visual:** A interface deve seguir um padrão visual consistente.
    
- **RNFG004 - Feedback Visual e Sonoro:** O sistema deve fornecer feedback claro (visual e/ou sonoro) para ações importantes, como validação de QR Code ou recebimento de notificações.
    

### 3.2. Desempenho

- **RNFG005 - Carregamento Rápido:** O aplicativo deve carregar em no máximo 3 segundos.
    
- **RNFG006 - Sincronização em Tempo Real:** As informações de fila do karaokê, status de pedidos da cozinha e comandas devem ser atualizadas em tempo real.
    
- **RNFG007 - Estabilidade:** O aplicativo deve ser estável e não apresentar travamentos ou falhas frequentes durante o uso contínuo.
    

### 3.3. Segurança

- **RNFG008 - Autenticação de Garçons:** O sistema deve garantir que apenas garçons autorizados possam acessar o aplicativo.
    
- **RNFG009 - Controle de Acesso:** Diferentes níveis de permissão podem ser implementados para garçons, se necessário (e.g., apenas visualizar, ou também editar).
    
- **RNFG010 - Integridade dos Dados:** Os dados de tickets, ingressos e comandas devem ser protegidos contra manipulação indevida.
    

### 3.4. Confiabilidade

- **RNFG011 - Disponibilidade:** O aplicativo deve estar disponível 99,9% do tempo durante o horário de funcionamento do bar.
    
- **RNFG012 - Tratamento de Erros:** O sistema deve lidar com erros de forma robusta, exibindo mensagens claras e permitindo a recuperação.
    
- **RNFG013 - Persistência de Dados:** Todas as informações de comandas, fila e status de pedidos devem ser armazenadas de forma persistente.
    

### 3.5. Manutenibilidade

- **RNFG014 - Código Limpo:** O código-fonte deve ser bem documentado, modular e fácil de entender para futuras manutenções e evoluções.
    
- **RNFG015 - Atualizações:** O aplicativo deve permitir atualizações e novas funcionalidades de forma eficiente.
    

### 3.6. Compatibilidade

- **RNFG016 - Compatibilidade Mobile:** O aplicativo deve ser compatível com as versões mais recentes dos sistemas operacionais Android e iOS (ou a plataforma escolhida).
    
- **RNFG017 - Responsividade:** A interface do aplicativo deve se adaptar a diferentes tamanhos de tela de dispositivos móveis.
    

## 4. Regras de Negócio (RN)

As regras de negócio são as políticas e restrições que governam o funcionamento do bar e do aplicativo para garçons.

### 4.1. Tickets e Ingressos

- **RNG001 - Validação Única:** Cada QR Code de ticket ou ingresso só pode ser validado uma única vez.
    
- **RNG002 - Validação de Prazo:** O sistema deve verificar o prazo de validade do ticket/ingresso antes de permitir a validação.
    

### 4.2. Comandas

- **RNG003 - Associação de Comanda:** Cada comanda deve estar associada a uma mesa ou cliente (se identificado).
    
- **RNG004 - Fechamento de Comanda:** Uma comanda só pode ser fechada após o pagamento total.
    
- **RNG005 - Pagamento Parcial:** O sistema deve permitir o registro de pagamentos parciais em uma comanda.
    

### 4.3. Karaokê

- **RNG006 - Ordem da Fila:** A fila do karaokê deve seguir a ordem de adição, a menos que seja explicitamente alterada pelo garçom.
    

## 5. Requisitos de Sistema (RS)

Os requisitos de sistema definem as necessidades de infraestrutura e tecnologia.

### 5.1. Plataformas

- **RSG001 - Desenvolvimento Mobile:** O aplicativo deve ser desenvolvido para dispositivos móveis (Android e/ou iOS).
    

### 5.2. Integrações

- **RSG002 - Integração com BarApp (Cliente):** O GarçomApp deve ser capaz de ler QR Codes gerados pelo BarApp do cliente (tickets, ingressos, comandas).
    
- **RSG003 - Integração com Sistema de Cozinha:** O GarçomApp deve se comunicar com o sistema da cozinha para visualizar o status dos pedidos.
    
- **RSG004 - Integração com Sistema de Pagamento:** O GarçomApp deve interagir com o gateway de pagamento para gerar QR Codes de Pix para comandas.
    
- **RSG005 - Integração com Sistema de Gerenciamento do Bar:** O GarçomApp deve se integrar com o sistema de gerenciamento principal do bar para atualização de cardápio, registro de comandas e gerenciamento de usuários garçons.