# Casos de Uso do Aplicativo BarApp

Este documento descreve os principais casos de uso do aplicativo BarApp, detalhando as interações entre os atores (usuários) e o sistema.

## Atores

- **Usuário:** Cliente do bar que utiliza o aplicativo.
    
- **Garçom/Atendente:** Funcionário do bar que interage com o aplicativo para validar tickets/comandas.
    
- **Sistema de Pagamento:** Serviço externo responsável por processar transações financeiras.
    
- **Sistema de Autenticação Social (Google):** Serviço externo para autenticação via conta Google.
    

## Casos de Uso

### 1. Gerenciamento de Usuários

#### CU001: Cadastrar Usuário

- **Nome:** Cadastrar Usuário
    
- **Ator:** Usuário
    
- **Descrição:** Permite que um novo usuário crie uma conta no aplicativo.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela de cadastro.
        
    2. Usuário preenche os campos obrigatórios (nome, e-mail, senha).
        
    3. Sistema valida os dados.
        
    4. Sistema cria a conta do usuário e o autentica.
        

#### CU002: Alterar Senha

- **Nome:** Alterar Senha
    
- **Ator:** Usuário
    
- **Descrição:** Permite que um usuário autenticado modifique sua senha de acesso.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela de alteração de senha.
        
    2. Usuário informa a senha atual e a nova senha (duas vezes para confirmação).
        
    3. Sistema valida a senha atual e a nova senha.
        
    4. Sistema atualiza a senha do usuário.
        

#### CU003: Realizar Login Social (Google)

- **Nome:** Realizar Login Social (Google)
    
- **Ator:** Usuário, Sistema de Autenticação Social (Google)
    
- **Descrição:** Permite que o usuário faça login usando sua conta Google.
    
- **Fluxo Principal:**
    
    1. Usuário seleciona a opção "Login com Google".
        
    2. Sistema redireciona para a tela de autenticação do Google.
        
    3. Usuário autentica-se com sua conta Google.
        
    4. Sistema de Autenticação Social retorna os dados do usuário para o BarApp.
        
    5. BarApp cria ou vincula a conta do usuário e o autentica.
        

### 2. Cardápio e Tickets

#### CU004: Visualizar Cardápio

- **Nome:** Visualizar Cardápio
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário navegue pelos produtos disponíveis no bar.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela do cardápio.
        
    2. Sistema exibe a lista de produtos com nome, preço, descrição e imagem.
        

#### CU005: Adicionar Ticket à Cesta

- **Nome:** Adicionar Ticket à Cesta
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário selecione um produto e adicione tickets correspondentes à sua cesta de compras.
    
- **Fluxo Principal:**
    
    1. Usuário visualiza o cardápio.
        
    2. Usuário seleciona um produto e a quantidade de tickets desejada.
        
    3. Sistema adiciona os tickets à cesta de compras do usuário.
        

#### CU006: Visualizar Cesta de Compras

- **Nome:** Visualizar Cesta de Compras
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário revise os itens selecionados antes de finalizar a compra.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela da cesta de compras.
        
    2. Sistema exibe os produtos, quantidades e valor total na cesta.
        

#### CU007: Comprar Tickets

- **Nome:** Comprar Tickets
    
- **Ator:** Usuário, Sistema de Pagamento
    
- **Descrição:** Permite que o usuário finalize a compra dos tickets na cesta de compras.
    
- **Fluxo Principal:**
    
    1. Usuário está na tela da cesta de compras.
        
    2. Usuário seleciona a opção "Finalizar Compra".
        
    3. Usuário escolhe o método de pagamento.
        
    4. Sistema de Pagamento processa a transação.
        
    5. Sistema registra os tickets comprados na carteira do usuário.
        

#### CU008: Visualizar Carteira de Tickets

- **Nome:** Visualizar Carteira de Tickets
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário veja os tickets que possui e ainda não utilizou.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela da carteira de tickets.
        
    2. Sistema exibe a lista de tickets disponíveis, com detalhes e prazo de validade.
        

#### CU009: Visualizar Histórico de Tickets

- **Nome:** Visualizar Histórico de Tickets
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário consulte o registro de todos os tickets comprados e utilizados.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela de histórico de tickets.
        
    2. Sistema exibe a lista de tickets com datas de compra e uso.
        

#### CU010: Transferir Ticket

- **Nome:** Transferir Ticket
    
- **Ator:** Usuário (remetente), Usuário (destinatário)
    
- **Descrição:** Permite que um usuário transfira um ou mais tickets para outro usuário.
    
- **Fluxo Principal:**
    
    1. Usuário (remetente) seleciona tickets na carteira para transferência.
        
    2. Sistema gera um QR Code para a transferência.
        
    3. Usuário (destinatário) lê o QR Code gerado pelo remetente.
        
    4. Sistema remove os tickets da carteira do remetente e adiciona à carteira do destinatário.
        

#### CU011: Receber Ticket

- **Nome:** Receber Ticket
    
- **Ator:** Usuário (destinatário), Usuário (remetente)
    
- **Descrição:** Permite que um usuário receba tickets transferidos por outro usuário.
    
- **Fluxo Principal:**
    
    1. Usuário (destinatário) acessa a função de "Receber Ticket" e ativa a câmera.
        
    2. Usuário (destinatário) escaneia o QR Code de transferência gerado pelo remetente.
        
    3. Sistema valida o QR Code e adiciona os tickets à carteira do destinatário.
        

#### CU012: Utilizar Ticket

- **Nome:** Utilizar Ticket
    
- **Ator:** Usuário, Garçom/Atendente
    
- **Descrição:** Permite que o usuário troque um ticket por um produto no bar.
    
- **Fluxo Principal:**
    
    1. Usuário seleciona um ticket na carteira para uso.
        
    2. Sistema gera um QR Code único para o ticket.
        
    3. Garçom/Atendente lê o QR Code com um dispositivo próprio.
        
    4. Sistema valida o ticket e o marca como utilizado, registrando a data e hora.
        

### 3. Pagamento

#### CU013: Efetuar Pagamento da Cesta

- **Nome:** Efetuar Pagamento da Cesta
    
- **Ator:** Usuário, Sistema de Pagamento
    
- **Descrição:** Processa o pagamento dos tickets na cesta de compras. (Já coberto em CU007, mas pode ser um caso de uso separado para o processo de pagamento em si).
    
- **Fluxo Principal:**
    
    1. Usuário confirma os itens na cesta.
        
    2. Usuário seleciona o método de pagamento (Pix, Cartão de Crédito/Débito).
        
    3. Se for Pix, sistema exibe QR Code/código.
        
    4. Se for cartão, usuário insere dados ou seleciona cartão cadastrado.
        
    5. Sistema integra com o Sistema de Pagamento para finalizar a transação.
        
    6. Sistema confirma o pagamento e atualiza o status dos tickets.
        

#### CU014: Cadastrar Cartão de Crédito/Débito

- **Nome:** Cadastrar Cartão de Crédito/Débito
    
- **Ator:** Usuário, Sistema de Pagamento
    
- **Descrição:** Permite que o usuário armazene dados de cartão para pagamentos futuros.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a seção de gerenciamento de pagamentos.
        
    2. Usuário seleciona a opção "Adicionar Cartão".
        
    3. Usuário insere os dados do cartão (número, validade, CVV, nome do titular).
        
    4. Sistema de Pagamento tokeniza e armazena os dados do cartão de forma segura.
        
    5. Sistema confirma o cadastro do cartão.
        

#### CU015: Efetuar Pagamento da Comanda

- **Nome:** Efetuar Pagamento da Comanda
    
- **Ator:** Usuário, Garçom/Atendente, Sistema de Pagamento
    
- **Descrição:** Permite que o usuário visualize e pague sua comanda de consumo.
    
- **Fluxo Principal:**
    
    1. Garçom/Atendente fornece um QR Code da comanda ao usuário.
        
    2. Usuário escaneia o QR Code da comanda.
        
    3. Sistema exibe os detalhes da comanda (itens, valores, total).
        
    4. Usuário seleciona a opção de pagamento (total ou parcial) e o método (Pix, Cartão).
        
    5. Sistema de Pagamento processa a transação.
        
    6. Sistema atualiza o status da comanda no sistema do bar.
        

### 4. Eventos e Karaokê

#### CU016: Comprar Ingresso para Evento

- **Nome:** Comprar Ingresso para Evento
    
- **Ator:** Usuário, Sistema de Pagamento
    
- **Descrição:** Permite que o usuário adquira ingressos para eventos do bar.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela de eventos.
        
    2. Usuário seleciona um evento e a quantidade de ingressos.
        
    3. Usuário prossegue para o pagamento (similar ao CU007).
        
    4. Sistema registra os ingressos na seção de ingressos do usuário.
        

#### CU017: Visualizar Fila do Karaokê

- **Nome:** Visualizar Fila do Karaokê
    
- **Ator:** Usuário
    
- **Descrição:** Permite que o usuário veja a ordem das pessoas para cantar no karaokê.
    
- **Fluxo Principal:**
    
    1. Usuário acessa a tela do karaokê.
        
    2. Sistema exibe a fila atualizada em tempo real.