# Histórias de Usuário do Aplicativo GarçomApp

Este documento apresenta as histórias de usuário para o aplicativo GarçomApp, focando na perspectiva do garçom e no valor que cada funcionalidade entrega para a operação do bar.

## 1. Autenticação

- **HUG001 - Login:**
    
    - **Como um** garçom,
        
    - **Eu quero** fazer login no aplicativo,
        
    - **Para que** eu possa acessar minhas ferramentas de trabalho.
        
    - **Critérios de Aceitação:**
        
        - Garçom insere usuário e senha.
            
        - Sistema valida as credenciais.
            
        - Garçom é redirecionado para a tela principal do aplicativo.
            

## 2. Gerenciamento de Tickets e Ingressos

- **HUG002 - Validação de Ticket:**
    
    - **Como um** garçom,
        
    - **Eu quero** ler o QR Code de um ticket de produto do cliente,
        
    - **Para que** eu possa validar a compra e entregar o produto.
        
    - **Critérios de Aceitação:**
        
        - Câmera é ativada para leitura do QR Code.
            
        - Sistema valida o ticket (existência, validade, não utilizado).
            
        - Sistema exibe mensagem de sucesso ou erro na validação.
            
        - Ticket é marcado como utilizado no sistema.
            
- **HUG003 - Validação de Ingresso:**
    
    - **Como um** garçom,
        
    - **Eu quero** ler o QR Code de um ingresso de evento do cliente,
        
    - **Para que** eu possa validar a entrada do cliente no evento.
        
    - **Critérios de Aceitação:**
        
        - Câmera é ativada para leitura do QR Code.
            
        - Sistema valida o ingresso (existência, validade, não utilizado).
            
        - Sistema exibe mensagem de sucesso ou erro na validação.
            
        - Ingresso é marcado como utilizado no sistema.
            

## 3. Gerenciamento da Fila do Karaokê

- **HUG004 - Visualização da Fila do Karaokê:**
    
    - **Como um** garçom,
        
    - **Eu quero** visualizar a fila de pessoas para o karaokê,
        
    - **Para que** eu possa gerenciar a ordem das apresentações.
        
    - **Critérios de Aceitação:**
        
        - Fila é exibida em tempo real.
            
        - Nomes das pessoas na fila são visíveis.
            
- **HUG005 - Gerenciamento da Fila do Karaokê:**
    
    - **Como um** garçom,
        
    - **Eu quero** adicionar, editar e remover pessoas da fila do karaokê,
        
    - **Para que** eu possa manter a fila organizada e justa.
        
    - **Critérios de Aceitação:**
        
        - É possível adicionar um novo nome à fila.
            
        - É possível arrastar e soltar nomes para mudar a posição na fila.
            
        - É possível remover um nome da fila.
            
        - A fila é atualizada instantaneamente para todos os usuários.
            

## 4. Gerenciamento de Comandas

- **HUG006 - Visualização de Comandas:**
    
    - **Como um** garçom,
        
    - **Eu quero** visualizar todas as comandas abertas e as aguardando pagamento,
        
    - **Para que** eu tenha controle sobre o consumo das mesas e pagamentos pendentes.
        
    - **Critérios de Aceitação:**
        
        - Listas de comandas abertas e aguardando pagamento são exibidas.
            
        - Informações básicas da comanda (mesa, nome do cliente, valor total) são visíveis.
            
- **HUG007 - Abrir Nova Comanda:**
    
    - **Como um** garçom,
        
    - **Eu quero** abrir uma nova comanda,
        
    - **Para que** eu possa registrar o consumo de um novo cliente/mesa.
        
    - **Critérios de Aceitação:**
        
        - É possível associar a comanda a uma mesa e/ou nome de cliente.
            
        - A nova comanda é criada e aparece na lista de comandas abertas.
            
- **HUG008 - Adicionar Produto à Comanda:**
    
    - **Como um** garçom,
        
    - **Eu quero** adicionar produtos à comanda de um cliente,
        
    - **Para que** o consumo seja registrado e o pedido enviado para a cozinha/bar.
        
    - **Critérios de Aceitação:**
        
        - É possível selecionar produtos do cardápio e suas quantidades.
            
        - O valor da comanda é atualizado automaticamente.
            
        - Pedidos são enviados para a cozinha/bar.
            
- **HUG009 - Gerar QR Code para Pagamento da Comanda:**
    
    - **Como um** garçom,
        
    - **Eu quero** gerar um QR Code para o cliente pagar a comanda via Pix,
        
    - **Para que** o cliente possa pagar de forma autônoma e rápida.
        
    - **Critérios de Aceitação:**
        
        - É possível selecionar a comanda e a opção de gerar QR Code.
            
        - É possível definir se o pagamento é total ou parcial.
            
        - Um QR Code Pix válido é exibido na tela.
            
- **HUG010 - Fechar Comanda:**
    
    - **Como um** garçom,
        
    - **Eu quero** fechar uma comanda,
        
    - **Para que** eu possa indicar que o consumo foi pago e a mesa está liberada.
        
    - **Critérios de Aceitação:**
        
        - A comanda só pode ser fechada se o valor total estiver pago.
            
        - A comanda é removida da lista de comandas abertas.
            

## 5. Acompanhamento de Pedidos e Notificações

- **HUG011 - Visualização do Andamento de Pedidos da Cozinha:**
    
    - **Como um** garçom,
        
    - **Eu quero** ver o status dos pedidos que enviei para a cozinha,
        
    - **Para que** eu saiba quando posso buscar os produtos para entregar aos clientes.
        
    - **Critérios de Aceitação:**
        
        - Lista de pedidos exibe o status ("na fila", "preparando", "pronto").
            
        - Informações da comanda associada ao pedido são visíveis.
            
- **HUG012 - Receber Notificação de Pagamento de Comanda:**
    
    - **Como um** garçom,
        
    - **Eu quero** ser notificado quando uma comanda sob minha responsabilidade for paga pelo cliente,
        
    - **Para que** eu possa agilizar o fechamento da mesa ou verificar o pagamento.
        
    - **Critérios de Aceitação:**
        
        - Uma notificação (e.g., push, sonora) é exibida no aplicativo.
            
        - A notificação indica qual comanda foi paga.
            
- **HUG013 - Receber Notificação de Pedido Pronto:**
    
    - **Como um** garçom,
        
    - **Eu quero** ser notificado quando um pedido da cozinha estiver pronto,
        
    - **Para que** eu possa buscá-lo e entregar ao cliente sem demora.
        
    - **Critérios de Aceitação:**
        
        - Uma notificação (e.g., push, sonora) é exibida no aplicativo.
            
        - A notificação indica qual pedido está pronto e a qual comanda pertence.