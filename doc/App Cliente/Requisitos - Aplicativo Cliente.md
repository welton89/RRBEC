estou desenvolvendo um aplicativo mobile para um bar, onde: poderá ver o cardápio, haverá venda e armazenamento de tickets, para que depois possa ser trocado por produto no local, venda de ingressos para eventos, visualizar fila de pessoa que vão cantar no karaokê, visualizar e efetuar pagamento da sua comanda de consumo.
algumas características do app:
* o usuário pode efetuar um Cadastro
* pode Alterar sua senha
* pode fazer Login social(com uma conta Google)
* visualizar o cardápio de produtos disponíveis com nome, preço, descrição e imagem
* Comprar ticket referente ao produto
* deve haver um limite de compra de tickets de um mesmo produto por usuário
* deve haver uma carteira de tickets para ser armazenados os tickets comprados
* os tickets podem ter prazo de validade
* o usuário pode ver seu histórico de tickets (data e hora da compra e de uso)
* deve haver uma "cesta de compra" onde o usuário pode ir armazenando os tickets para depois efetuar o pagamento dos mesmo
* o pagamento pode ser via pix, credito, ou debito
* o usuário pode Transferir seus tickets para outro usuário através da geração de um qrcode
* o usuário pode receber transferença de tickets de outro usuário através da leitura de um qrcode 
* para usar o ticket basta tocar e o app vai gerar um qrcode que será lido pelo garçom
* o usuário poderá cadastrar cartões para facilitar pagamentos futuros

* o aplicativo poderá vender ingressos para eventos do bar 
* Ingressos podem ser nomeados
* Possibilidade de acompanhar a própria comanda de consumo através da leitura de um qrcode fornecido pelo o garçom, e efetuar o pagamento da mesma pelo app




# Documento de Requisitos do Aplicativo BarApp

## 1. Introdução

### 1.1. Propósito

Este documento tem como objetivo detalhar os requisitos funcionais, não funcionais, regras de negócio e requisitos de sistema para o desenvolvimento do aplicativo mobile "BarApp". O aplicativo visa aprimorar a experiência do cliente em um bar, oferecendo funcionalidades como visualização de cardápio, compra e gerenciamento de tickets de produtos, venda de ingressos para eventos, acompanhamento da fila do karaokê e pagamento de comandas de consumo.

### 1.2. Escopo

O aplicativo BarApp será uma solução mobile disponível para as plataformas Android e iOS, permitindo que os usuários realizem as ações descritas neste documento. O escopo inicial não inclui funcionalidades para a equipe do bar (garçons, gerentes), que serão consideradas em fases futuras, exceto pela interação de leitura de QR Codes.

### 1.3. Público-alvo

- **Usuários Finais:** Clientes do bar que desejam interagir com o estabelecimento de forma digital.
    
- **Garçons/Atendentes:** Profissionais do bar que precisarão ler QR Codes gerados pelo aplicativo para validação de tickets e comandas.
    

## 2. Requisitos Funcionais (RF)

Os requisitos funcionais descrevem as funcionalidades que o sistema deve oferecer aos usuários.

### 2.1. Gerenciamento de Usuários

- **RF001 - Cadastro de Usuário:** O sistema deve permitir que um novo usuário realize seu cadastro, fornecendo informações como nome completo, e-mail e senha.
    
- **RF002 - Alteração de Senha:** O sistema deve permitir que um usuário autenticado altere sua senha.
    
- **RF003 - Login:** O sistema deve permitir que um usuário autenticado faça login utilizando e-mail e senha.
    
- **RF004 - Login Social (Google):** O sistema deve permitir que um usuário faça login utilizando sua conta Google.
    
- **RF005 - Recuperação de Senha:** O sistema deve permitir que um usuário recupere sua senha através de um processo seguro (e.g., envio de link para o e-mail cadastrado).
    
- **RF006 - Gerenciamento de Perfil:** O sistema deve permitir que o usuário visualize e edite suas informações de perfil (exceto e-mail de cadastro).
    

### 2.2. Gerenciamento de Cardápio

- **RF007 - Visualização do Cardápio:** O sistema deve exibir o cardápio completo de produtos disponíveis no bar.
    
- **RF008 - Detalhes do Produto:** Para cada item do cardápio, o sistema deve exibir nome, preço, descrição e imagem.
    

### 2.3. Compra e Gerenciamento de Tickets

- **RF009 - Compra de Ticket:** O sistema deve permitir que o usuário selecione um produto do cardápio e compre tickets referentes a ele.
    
- **RF010 - Adicionar à Cesta de Compras:** O sistema deve permitir que o usuário adicione tickets de diferentes produtos a uma "cesta de compras" antes de finalizar o pagamento.
    
- **RF011 - Visualização da Cesta de Compras:** O sistema deve exibir todos os itens adicionados à cesta de compras, com seus respectivos nomes, quantidades e valores totais.
    
- **RF012 - Remoção de Item da Cesta:** O sistema deve permitir que o usuário remova itens da cesta de compras.
    
- **RF013 - Visualização da Carteira de Tickets:** O sistema deve exibir uma "carteira" com todos os tickets comprados e ainda não utilizados pelo usuário.
    
- **RF014 - Detalhes do Ticket na Carteira:** Para cada ticket na carteira, o sistema deve exibir o nome do produto, quantidade, data de compra e, se aplicável, prazo de validade.
    
- **RF015 - Visualização do Histórico de Tickets:** O sistema deve exibir o histórico de tickets do usuário, incluindo data e hora da compra e data e hora de uso (se já utilizado).
    

### 2.4. Pagamento

- **RF016 - Seleção de Método de Pagamento:** O sistema deve permitir que o usuário selecione o método de pagamento para a cesta de compras (Pix, Cartão de Crédito, Cartão de Débito).
    
- **RF017 - Processamento de Pagamento (Pix):** O sistema deve gerar um QR Code Pix ou código "copia e cola" para que o usuário efetue o pagamento.
    
- **RF018 - Processamento de Pagamento (Cartão):** O sistema deve integrar com uma plataforma de pagamento para processar transações de cartão de crédito/débito.
    
- **RF019 - Cadastro de Cartões:** O sistema deve permitir que o usuário cadastre múltiplos cartões de crédito/débito para pagamentos futuros.
    
- **RF020 - Seleção de Cartão Cadastrado:** O sistema deve permitir que o usuário selecione um cartão previamente cadastrado para realizar pagamentos.
    

### 2.5. Transferência de Tickets

- **RF021 - Geração de QR Code para Transferência:** O sistema deve permitir que o usuário selecione um ou mais tickets de sua carteira e gere um QR Code para transferência para outro usuário.
    
- **RF022 - Leitura de QR Code para Recebimento:** O sistema deve permitir que o usuário utilize a câmera do dispositivo para ler um QR Code de transferência e receber tickets de outro usuário.
    

### 2.6. Utilização de Tickets

- **RF023 - Geração de QR Code para Uso:** O sistema deve permitir que o usuário selecione um ticket na carteira e gere um QR Code único para que o garçom possa validá-lo e trocá-lo pelo produto.
    
- **RF024 - Validação de Uso de Ticket:** O sistema deve registrar a data e hora do uso do ticket após a leitura bem-sucedida pelo garçom.
    

### 2.7. Venda de Ingressos para Eventos

- **RF025 - Visualização de Eventos:** O sistema deve exibir uma lista dos eventos disponíveis no bar, com nome do evento, data, hora, descrição e preço do ingresso.
    
- **RF026 - Compra de Ingresso:** O sistema deve permitir que o usuário compre ingressos para eventos.
    
- **RF027 - Visualização de Ingressos Comprados:** O sistema deve exibir os ingressos comprados pelo usuário.
    
- **RF028 - Geração de QR Code do Ingresso:** O sistema deve permitir que o usuário gere um QR Code para cada ingresso comprado, para validação na entrada do evento.
    

### 2.8. Karaokê

- **RF029 - Visualização da Fila do Karaokê:** O sistema deve exibir a fila atual de pessoas que vão cantar no karaokê, em tempo real.
    

### 2.9. Comanda de Consumo

- **RF030 - Acompanhamento da Comanda:** O sistema deve permitir que o usuário leia um QR Code fornecido pelo garçom para visualizar sua comanda de consumo em tempo real.
    
- **RF031 - Detalhes da Comanda:** A comanda deve exibir os itens consumidos, quantidades, preços unitários e valor total.
    
- **RF032 - Pagamento da Comanda:** O sistema deve permitir que o usuário efetue o pagamento total ou parcial da comanda de consumo através dos métodos de pagamento disponíveis (Pix, Cartão de Crédito, Cartão de Débito).
    

## 3. Requisitos Não Funcionais (RNF)

Os requisitos não funcionais descrevem as qualidades do sistema.

### 3.1. Usabilidade

- **RNF001 - Interface Intuitiva:** A interface do usuário deve ser intuitiva e fácil de usar, mesmo para usuários com pouca familiaridade com aplicativos.
    
- **RNF002 - Tempo de Resposta:** O tempo de resposta do aplicativo para todas as interações do usuário não deve exceder 3 segundos.
    
- **RNF003 - Consistência Visual:** A interface deve seguir um padrão visual consistente em todas as telas e funcionalidades.
    
- **RNF004 - Feedback ao Usuário:** O sistema deve fornecer feedback claro e imediato para todas as ações do usuário (e.g., sucesso na compra, erro de login).
    

### 3.2. Desempenho

- **RNF005 - Carregamento Rápido:** O aplicativo deve carregar em no máximo 5 segundos na primeira inicialização.
    
- **RNF006 - Escalabilidade:** O sistema deve ser capaz de suportar um grande volume de usuários simultâneos (e.g., 1000 usuários ativos) sem degradação significativa de desempenho.
    
- **RNF007 - Otimização de Imagens:** As imagens do cardápio e eventos devem ser otimizadas para carregamento rápido sem comprometer a qualidade visual.
    

### 3.3. Segurança

- **RNF008 - Autenticação Segura:** O sistema deve garantir que as credenciais de login dos usuários sejam armazenadas e transmitidas de forma segura (e.g., criptografia, hashing de senhas).
    
- **RNF009 - Proteção de Dados Pessoais:** As informações pessoais e de pagamento dos usuários devem ser protegidas contra acesso não autorizado e vazamento de dados.
    
- **RNF010 - Transações Seguras:** Todas as transações financeiras devem ser processadas através de gateways de pagamento seguros e certificados.
    
- **RNF011 - Validação de QR Code:** Os QR Codes gerados para tickets e ingressos devem ser únicos, com validade limitada e antifraude.
    

### 3.4. Confiabilidade

- **RNF012 - Disponibilidade:** O aplicativo deve estar disponível 99,9% do tempo.
    
- **RNF013 - Tratamento de Erros:** O sistema deve lidar com erros de forma graciosa, exibindo mensagens claras e úteis ao usuário.
    
- **RNF014 - Persistência de Dados:** Todos os dados do usuário (cadastro, tickets, histórico, cartões) devem ser armazenados de forma persistente e recuperáveis.
    

### 3.5. Manutenibilidade

- **RNF015 - Código Limpo:** O código-fonte deve ser bem documentado, modular e fácil de entender para futuras manutenções e evoluções.
    
- **RNF016 - Atualizações:** O aplicativo deve permitir atualizações e novas funcionalidades sem exigir reinstalação completa por parte do usuário, sempre que possível.
    

### 3.6. Compatibilidade

- **RNF017 - Compatibilidade Mobile:** O aplicativo deve ser compatível com as versões mais recentes dos sistemas operacionais Android e iOS (e.g., últimas 3 versões).
    
- **RNF018 - Responsividade:** A interface do aplicativo deve se adaptar a diferentes tamanhos de tela e orientações (retrato/paisagem) de dispositivos móveis.
    

## 4. Regras de Negócio (RN)

As regras de negócio são as políticas e restrições que governam o funcionamento do bar e do aplicativo.

### 4.1. Tickets

- **RN001 - Limite de Compra de Tickets:** Cada usuário terá um limite máximo de tickets de um mesmo produto que pode comprar em uma única transação ou em um período de tempo (a ser definido pelo bar, e.g., 10 tickets do mesmo produto por dia).
    
- **RN002 - Validade do Ticket:** Tickets comprados podem ter um prazo de validade (e.g., 30 dias a partir da data da compra, ou até o fechamento do bar no dia da compra).
    
- **RN003 - Uso Único do Ticket:** Cada ticket gerado para uso (QR Code) pode ser utilizado apenas uma vez.
    
- **RN004 - Transferência de Tickets:** Tickets podem ser transferidos entre usuários, e a responsabilidade pela validade e uso passa para o novo proprietário.
    
- **RN005 - Tickets Não Reembolsáveis:** Uma vez comprado, tickets não são reembolsáveis (a menos que haja uma política de exceção do bar).
    

### 4.2. Pagamento

- **RN006 - Métodos de Pagamento:** Os métodos de pagamento aceitos são Pix, Cartão de Crédito e Cartão de Débito.
    
- **RN007 - Pagamento da Comanda:** A comanda de consumo pode ser paga total ou parcialmente pelo aplicativo.
    

### 4.3. Eventos

- **RN008 - Ingressos Nomeados:** Ingressos para eventos podem ter nomes específicos (e.g., "Ingresso Pista", "Ingresso VIP").
    
- **RN009 - Validação de Ingresso:** Cada ingresso comprado gera um QR Code único para validação na entrada do evento, permitindo apenas um acesso por ingresso.
    

## 5. Requisitos de Sistema (RS)

Os requisitos de sistema definem as necessidades de infraestrutura e tecnologia.

### 5.1. Plataformas

- **RS001 - Desenvolvimento Multiplataforma:** O aplicativo deve ser desenvolvido para ser compatível com iOS e Android.
    
- **RS002 - Linguagens de Programação:** A serem definidas pela equipe de desenvolvimento (e.g., React Native, Flutter, Swift/Kotlin nativo).
    

### 5.2. Integrações

- **RS003 - Gateway de Pagamento:** O sistema deve integrar-se com um gateway de pagamento (e.g., Stripe, PagSeguro, Mercado Pago) para processar pagamentos com cartão e Pix.
    
- **RS004 - Autenticação Social:** O sistema deve integrar-se com a API de autenticação do Google para login social.
    
- **RS005 - Sistema de Gerenciamento do Bar:** O aplicativo pode precisar de integração com um sistema de gerenciamento interno do bar para atualização de cardápio, fila de karaokê e comandas (a ser definido em fases futuras).
    
- **RS006 - Leitura de QR Code:** O aplicativo deve utilizar a câmera do dispositivo para ler QR Codes.