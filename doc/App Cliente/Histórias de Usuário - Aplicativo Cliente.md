# Histórias de Usuário do Aplicativo BarApp

Este documento apresenta as histórias de usuário para o aplicativo BarApp, focando na perspectiva do usuário e no valor que cada funcionalidade entrega.

## 1. Gerenciamento de Usuários

- **HU001 - Cadastro:**
    
    - **Como um** novo cliente,
        
    - **Eu quero** me cadastrar no aplicativo,
        
    - **Para que** eu possa acessar todas as funcionalidades e personalizar minha experiência.
        
    - **Critérios de Aceitação:**
        
        - Dados de cadastro (nome, e-mail, senha) são coletados.
            
        - E-mail é validado para formato correto.
            
        - Senha atende aos requisitos de segurança (e.g., mínimo de 8 caracteres, maiúscula, minúscula, número).
            
        - Usuário é autenticado e redirecionado para a tela principal após o cadastro.
            
- **HU002 - Alteração de Senha:**
    
    - **Como um** usuário cadastrado,
        
    - **Eu quero** alterar minha senha,
        
    - **Para que** eu possa manter minha conta segura.
        
    - **Critérios de Aceitação:**
        
        - Usuário deve informar a senha atual corretamente.
            
        - Nova senha deve ser confirmada e atender aos requisitos de segurança.
            
        - Sistema deve informar sucesso ou falha na alteração da senha.
            
- **HU003 - Login Social (Google):**
    
    - **Como um** cliente com conta Google,
        
    - **Eu quero** fazer login usando minha conta Google,
        
    - **Para que** eu não precise criar e lembrar de mais uma senha.
        
    - **Critérios de Aceitação:**
        
        - Opção de login com Google está visível na tela de login.
            
        - Usuário é redirecionado para a autenticação do Google.
            
        - Após autenticação, usuário é logado no aplicativo.
            

## 2. Cardápio e Compra de Tickets

- **HU004 - Visualização do Cardápio:**
    
    - **Como um** cliente,
        
    - **Eu quero** visualizar o cardápio de produtos do bar,
        
    - **Para que** eu possa escolher o que consumir.
        
    - **Critérios de Aceitação:**
        
        - Cardápio exibe nome, preço, descrição e imagem para cada produto.
            
        - Cardápio é fácil de navegar.
            
- **HU005 - Compra de Ticket:**
    
    - **Como um** cliente,
        
    - **Eu quero** comprar tickets para produtos do cardápio,
        
    - **Para que** eu possa ter meus produtos garantidos e evitar filas no caixa.
        
    - **Critérios de Aceitação:**
        
        - É possível selecionar a quantidade de tickets para um produto.
            
        - Sistema aplica limite de compra por produto/usuário.
            
        - Tickets são adicionados à cesta de compras.
            
- **HU006 - Visualização da Cesta de Compras:**
    
    - **Como um** cliente,
        
    - **Eu quero** ver os itens que adicionei à minha cesta,
        
    - **Para que** eu possa revisar meu pedido antes de pagar.
        
    - **Critérios de Aceitação:**
        
        - Cesta exibe nome do produto, quantidade e subtotal.
            
        - Total da compra é exibido.
            
        - É possível remover itens da cesta.
            

## 3. Carteira e Uso de Tickets

- **HU007 - Visualização da Carteira de Tickets:**
    
    - **Como um** cliente,
        
    - **Eu quero** ver todos os tickets que comprei e ainda não usei,
        
    - **Para que** eu saiba o que tenho disponível para consumir.
        
    - **Critérios de Aceitação:**
        
        - Carteira exibe tickets disponíveis, com nome do produto e quantidade.
            
        - Prazo de validade dos tickets é exibido claramente.
            
- **HU008 - Visualização do Histórico de Tickets:**
    
    - **Como um** cliente,
        
    - **Eu quero** ver meu histórico de tickets comprados e usados,
        
    - **Para que** eu possa acompanhar meus gastos e consumo.
        
    - **Critérios de Aceitação:**
        
        - Histórico exibe data e hora da compra.
            
        - Histórico exibe data e hora do uso (se aplicável).
            
        - Tickets usados e não usados são diferenciados visualmente.
            
- **HU009 - Transferência de Ticket (Gerar QR Code):**
    
    - **Como um** cliente,
        
    - **Eu quero** transferir tickets para outro usuário,
        
    - **Para que** eu possa presentear amigos ou dividir tickets.
        
    - **Critérios de Aceitação:**
        
        - É possível selecionar tickets da carteira para transferência.
            
        - Um QR Code único é gerado para a transferência.
            
        - Tickets são removidos da carteira do remetente após a transferência ser concluída.
            
- **HU010 - Recebimento de Ticket (Ler QR Code):**
    
    - **Como um** cliente,
        
    - **Eu quero** receber tickets de outro usuário lendo um QR Code,
        
    - **Para que** eu possa aceitar tickets transferidos por amigos.
        
    - **Critérios de Aceitação:**
        
        - Funcionalidade de leitura de QR Code é acessível.
            
        - Após a leitura de um QR Code válido, tickets são adicionados à carteira do destinatário.
            
- **HU011 - Uso de Ticket:**
    
    - **Como um** cliente,
        
    - **Eu quero** usar um ticket da minha carteira para pegar um produto,
        
    - **Para que** eu possa consumir o que comprei.
        
    - **Critérios de Aceitação:**
        
        - Ao tocar no ticket, um QR Code único é gerado.
            
        - QR Code é lido pelo garçom.
            
        - Ticket é marcado como usado no sistema.
            

## 4. Pagamento

- **HU012 - Pagamento da Cesta:**
    
    - **Como um** cliente,
        
    - **Eu quero** pagar minha cesta de tickets,
        
    - **Para que** eu possa ter os tickets na minha carteira.
        
    - **Critérios de Aceitação:**
        
        - Opções de pagamento (Pix, Crédito, Débito) são apresentadas.
            
        - Transação é processada com sucesso pelo método escolhido.
            
        - Tickets são liberados para a carteira após confirmação do pagamento.
            
- **HU013 - Cadastro de Cartão:**
    
    - **Como um** cliente,
        
    - **Eu quero** cadastrar meus cartões de pagamento,
        
    - **Para que** eu possa pagar mais rapidamente em compras futuras.
        
    - **Critérios de Aceitação:**
        
        - Dados do cartão são coletados de forma segura.
            
        - Cartão é armazenado para uso futuro.
            
        - Opção de selecionar cartão cadastrado aparece nas telas de pagamento.
            
- **HU014 - Pagamento da Comanda:**
    
    - **Como um** cliente,
        
    - **Eu quero** visualizar e pagar minha comanda de consumo pelo aplicativo,
        
    - **Para que** eu tenha controle dos meus gastos e agilidade no pagamento.
        
    - **Critérios de Aceitação:**
        
        - É possível escanear um QR Code da comanda fornecido pelo garçom.
            
        - Comanda exibe itens consumidos e valor total.
            
        - É possível efetuar o pagamento total ou parcial da comanda.
            
        - Status da comanda é atualizado após o pagamento.
            

## 5. Eventos e Karaokê

- **HU015 - Compra de Ingresso para Evento:**
    
    - **Como um** cliente,
        
    - **Eu quero** comprar ingressos para eventos do bar,
        
    - **Para que** eu possa garantir minha entrada e participar das festas.
        
    - **Critérios de Aceitação:**
        
        - Lista de eventos disponíveis é exibida com detalhes (nome, data, preço).
            
        - É possível selecionar a quantidade de ingressos.
            
        - Pagamento é processado com sucesso.
            
        - Ingressos aparecem na minha seção de ingressos.
            
- **HU016 - Visualização da Fila do Karaokê:**
    
    - **Como um** cliente,
        
    - **Eu quero** visualizar a fila de pessoas para cantar no karaokê,
        
    - **Para que** eu possa saber quando será minha vez ou a de meus amigos.
        
    - **Critérios de Aceitação:**
        
        - Fila é exibida em tempo real.
            
        - Nomes das pessoas na fila são visíveis.
            
        - Ordem da fila é clara.