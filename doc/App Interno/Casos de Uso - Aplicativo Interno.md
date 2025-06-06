# Casos de Uso do Aplicativo GarçomApp

Este documento descreve os principais casos de uso do aplicativo GarçomApp, detalhando as interações entre os atores (garçons) e o sistema.

## Atores

- **Garçom:** Funcionário do bar que utiliza o aplicativo.
    
- **Cliente (BarApp):** Usuário do aplicativo do cliente que interage com o garçom via QR Codes.
    
- **Sistema de Cozinha:** Sistema responsável pelo gerenciamento de pedidos na cozinha.
    
- **Sistema de Pagamento:** Serviço externo para processamento de pagamentos.
    

## Casos de Uso

### 1. Autenticação

#### CUG001: Realizar Login

- **Nome:** Realizar Login
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom acesse o aplicativo com suas credenciais.
    
- **Fluxo Principal:**
    
    1. Garçom acessa a tela de login.
        
    2. Garçom insere usuário e senha.
        
    3. Sistema valida as credenciais.
        
    4. Sistema autentica o garçom e o redireciona para a tela principal.
        

### 2. Gerenciamento de Tickets e Ingressos

#### CUG002: Validar Ticket de Produto

- **Nome:** Validar Ticket de Produto
    
- **Ator:** Garçom, Cliente (BarApp)
    
- **Descrição:** Permite que o garçom valide um ticket de produto apresentado pelo cliente.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona a opção "Validar Ticket".
        
    2. Sistema ativa a câmera para leitura de QR Code.
        
    3. Garçom escaneia o QR Code do ticket no BarApp do cliente.
        
    4. Sistema valida o ticket (existência, validade, não utilizado).
        
    5. Sistema exibe confirmação de validação e marca o ticket como utilizado.
        

#### CUG003: Validar Ingresso de Evento

- **Nome:** Validar Ingresso de Evento
    
- **Ator:** Garçom, Cliente (BarApp)
    
- **Descrição:** Permite que o garçom valide um ingresso de evento apresentado pelo cliente.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona a opção "Validar Ingresso".
        
    2. Sistema ativa a câmera para leitura de QR Code.
        
    3. Garçom escaneia o QR Code do ingresso no BarApp do cliente.
        
    4. Sistema valida o ingresso (existência, validade, não utilizado).
        
    5. Sistema exibe confirmação de validação e marca o ingresso como utilizado.
        

### 3. Gerenciamento da Fila do Karaokê

#### CUG004: Visualizar Fila do Karaokê

- **Nome:** Visualizar Fila do Karaokê
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom veja a ordem das pessoas para cantar.
    
- **Fluxo Principal:**
    
    1. Garçom acessa a tela do Karaokê.
        
    2. Sistema exibe a lista de pessoas na fila em tempo real.
        

#### CUG005: Gerenciar Fila do Karaokê

- **Nome:** Gerenciar Fila do Karaokê
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom adicione, edite ou remova pessoas da fila do karaokê.
    
- **Fluxo Principal - Adicionar:**
    
    1. Garçom seleciona "Adicionar à Fila".
        
    2. Garçom insere nome da pessoa e, opcionalmente, música.
        
    3. Sistema adiciona a pessoa ao final da fila.
        
- **Fluxo Principal - Editar/Mover:**
    
    1. Garçom seleciona uma pessoa na fila.
        
    2. Garçom arrasta para mudar a posição ou edita os detalhes.
        
    3. Sistema atualiza a fila.
        
- **Fluxo Principal - Remover:**
    
    1. Garçom seleciona uma pessoa na fila.
        
    2. Garçom confirma a remoção.
        
    3. Sistema remove a pessoa da fila.
        

### 4. Gerenciamento de Comandas

#### CUG006: Visualizar Comandas

- **Nome:** Visualizar Comandas
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom veja o status de todas as comandas.
    
- **Fluxo Principal:**
    
    1. Garçom acessa a tela de Comandas.
        
    2. Sistema exibe listas separadas de "Comandas Abertas" e "Comandas Aguardando Pagamento".
        

#### CUG007: Abrir Nova Comanda

- **Nome:** Abrir Nova Comanda
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom crie uma nova comanda para um cliente/mesa.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona "Abrir Nova Comanda".
        
    2. Garçom insere nome do cliente (opcional) e/ou número da mesa.
        
    3. Sistema cria e exibe a nova comanda.
        

#### CUG008: Adicionar Produto à Comanda

- **Nome:** Adicionar Produto à Comanda
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom adicione itens do cardápio a uma comanda existente.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona uma comanda aberta.
        
    2. Garçom navega pelo cardápio e seleciona produtos e quantidades.
        
    3. Sistema adiciona os produtos à comanda e atualiza o total.
        
    4. Sistema envia o pedido para a cozinha (se aplicável).
        

#### CUG009: Editar Informações da Comanda

- **Nome:** Editar Informações da Comanda
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom atualize o nome do cliente ou a mesa associada a uma comanda.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona uma comanda.
        
    2. Garçom edita o nome do cliente ou o número da mesa.
        
    3. Sistema atualiza as informações da comanda.
        

#### CUG010: Gerar QR Code para Pagamento da Comanda

- **Nome:** Gerar QR Code para Pagamento da Comanda
    
- **Ator:** Garçom, Cliente (BarApp), Sistema de Pagamento
    
- **Descrição:** Permite que o garçom gere um QR Code para o cliente pagar a comanda via Pix.
    
- **Fluxo Principal:**
    
    1. Garçom seleciona uma comanda.
        
    2. Garçom seleciona a opção "Gerar QR Code para Pagamento".
        
    3. Garçom pode escolher pagamento total ou parcial (informando o valor).
        
    4. Sistema gera um QR Code (e.g., Pix) e o exibe para o cliente.
        
    5. Cliente escaneia o QR Code e efetua o pagamento via BarApp.
        
    6. Sistema de Pagamento notifica o GarçomApp sobre o pagamento.
        

#### CUG011: Fechar Comanda

- **Nome:** Fechar Comanda
    
- **Ator:** Garçom
    
- **Descrição:** Permite que o garçom marque uma comanda como paga e fechada.
    
- **Fluxo Principal:**
    
    1. Garçom verifica que a comanda foi totalmente paga.
        
    2. Garçom seleciona a comanda e a opção "Fechar Comanda".
        
    3. Sistema marca a comanda como fechada e a remove da lista de comandas abertas.
        

### 5. Acompanhamento de Pedidos e Notificações

#### CUG012: Visualizar Andamento de Pedidos da Cozinha

- **Nome:** Visualizar Andamento de Pedidos da Cozinha
    
- **Ator:** Garçom, Sistema de Cozinha
    
- **Descrição:** Permite que o garçom acompanhe o status dos pedidos enviados para a cozinha.
    
- **Fluxo Principal:**
    
    1. Garçom acessa a tela de "Pedidos da Cozinha".
        
    2. Sistema exibe a lista de pedidos com seus status ("na fila", "preparando", "pronto").
        

#### CUG013: Receber Notificação de Pagamento de Comanda

- **Nome:** Receber Notificação de Pagamento de Comanda
    
- **Ator:** Garçom, Sistema de Pagamento
    
- **Descrição:** O sistema notifica o garçom quando uma comanda sob sua responsabilidade é paga pelo cliente.
    
- **Fluxo Principal:**
    
    1. Pagamento da comanda é efetuado pelo cliente via BarApp.
        
    2. Sistema de Pagamento envia notificação ao GarçomApp.
        
    3. GarçomApp exibe uma notificação (e.g., push notification, alerta no app) informando sobre o pagamento.
        

#### CUG014: Receber Notificação de Pedido Pronto

- **Nome:** Receber Notificação de Pedido Pronto
    
- **Ator:** Garçom, Sistema de Cozinha
    
- **Descrição:** O sistema notifica o garçom quando um pedido da cozinha está pronto para ser entregue.
    
- **Fluxo Principal:**
    
    1. Sistema de Cozinha marca um pedido como "pronto".
        
    2. Sistema de Cozinha envia notificação ao GarçomApp.
        
    3. GarçomApp exibe uma notificação informando que o pedido está pronto.