# RRBEC - Gestão de Bares e Restaurantes

## Sobre o Projeto
Este projeto é uma aplicação web desenvolvida em Django com o objetivo de explorar as funcionalidades e recursos desse framework. A aplicação visa simular um sistema de gestão para bares e restaurantes, abrangendo desde o cadastro de produtos e clientes até a geração de relatórios de vendas.

## Requisitos Funcionais

### Módulo de Produtos
* [x] Cadastrar novos produtos.
* [ ] Editar informações de produtos existentes.
* [ ] Ativar/Desativar produtos.
* [ ] Pesquisar produtos por nome.
* [ ] Gerenciar o estoque de cada produto.

### Módulo de Comandas
* [ ] Abrir nova comanda(inserindo nome, associando ou não a mesa).
* [ ] Editar informações da comanda.
* [ ] Adicionar produtos na comanda.
* [ ] Imprimir cupom de pagamento.
* [ ] Imprimir fichas dos produtos.
* [ ] Pagamento e fechamento da comanda.

### Módulo de Mesa
* [x] Gerenciar mesas (ocupação, reserva).
* [x] Associar pedidos e comandas a mesas.
* [ ] Dividir contas.

### Módulo de Clientes
* [ ] Cadastrar novos clientes (nome, endereço, telefone, email).
* [ ] Editar informações de clientes existentes.
* [ ] Excluir clientes.
* [ ] Consultar o histórico de pedidos de um cliente.

### Módulo de Pedidos
* [ ] Realizar novos pedidos (produtos, quantidade, cliente).
* [ ] Editar pedidos (adicionar/remover itens, alterar quantidade).
* [ ] Cancelar pedidos.
* [ ] Consultar o status de um pedido (em aberto, em preparo, entregue).
* [ ] Gerar nota fiscal para pedidos finalizados.

### Módulo de Funcionários
* [ ] Cadastrar novos funcionários (nome, cargo, salário, data de admissão).
* [ ] Editar informações de funcionários existentes.
* [ ] Excluir funcionários.
* [ ] Gerenciar as permissões de cada funcionário (acesso a módulos, funções).

### Módulo de Relatórios
* [ ] Gerar relatório de vendas por período (diário, semanal, mensal).
* [ ] Gerar relatório de estoque (produtos em falta, produtos com alta rotatividade).
* [ ] Gerar relatório de clientes (mais ativos, menos ativos).
* [ ] Gerar relatório de funcionários (horas trabalhadas, faltas).

### Módulo de Pagamentos
* [ ] Integrar com gateways de pagamento (cartão de crédito, débito, dinheiro).
* [x] Gerenciar formas de pagamento.
* [ ] Emitir notas fiscais eletrônicas.


### Módulo de Delivery (opcional para restaurantes)
* [ ] Cadastrar entregadores.
* [ ] Gerenciar rotas de entrega.
* [ ] Acompanhar pedidos em tempo real.

### Módulo de Sistema
* [ ] Gerenciar usuários do sistema (login, senha, permissões).
* [ ] Realizar backups do sistema.

## Tecnologias Utilizadas
* **Django:** Framework Python para desenvolvimento web.
* **Python:** Linguagem de programação principal do projeto.
* **HTML:** Linguagem de marcação para disponibilizar os elementos na pagina.
* **HTMX:** Biblioteca para deixar a pagina mais dinâmica, reduzindo a necessidade do js.
* **CSS:** Linguagem para estilizar a interface do usuário.
* **JavaScript:** Linguagem que executa a lógica da pagina.

## Como Executar o Projeto
1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/Pindoba/RRBEC.git
2. **Criar um ambiente virtual:**
   ```bash
    python -m venv [nome da sua preferencia]
    source venv/bin/activate
3. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Executar as migrations:**
   ```bash
   python manage.py migrate
5. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
