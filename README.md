# RRBEC - Gestão de Bares e Restaurantes

## Sobre o Projeto
Este projeto é uma aplicação web desenvolvida em Django com o objetivo de explorar as funcionalidades e recursos desse framework. A aplicação visa simular um sistema de gestão para bares e restaurantes, abrangendo desde o cadastro de produtos e clientes até a geração de relatórios de vendas.

## Requisitos Funcionais

### Módulo de Produtos
* [x] Cadastrar novos produtos.
* [x] Editar informações de produtos existentes.
* [x] Ativar/Desativar produtos.
* [x] Pesquisar produtos por nome.
* [ ] Gerenciar o estoque de cada produto.

### Módulo de Comandas
* [x] Abrir nova comanda(inserindo nome, associando ou não a mesa).
* [x] Editar informações da comanda.
* [x] Adicionar produtos na comanda.
* [x] Remover produtos da comanda.
* [x] Imprimir cupom de pagamento.
* [x] Imprimir fichas dos produtos.
* [x] Fechamento da comanda.
* [x] Receber pagamento

### Módulo de Mesa
* [ ] Gerenciar mesas (ocupação, reserva).
* [x] Associar pedidos e comandas a mesas.
* [ ] Dividir contas.

### Módulo de Clientes
* [ ] Cadastrar novos clientes (nome, endereço, telefone, email).
* [ ] Editar informações de clientes existentes.
* [ ] Excluir clientes.
* [ ] Consultar o histórico de pedidos de um cliente.

### Módulo de Guarita
* [x] Adicionar produtos, quantidade.
* [x] Pesquisa produto reativa.
* [x] Exibição de produtos em ordem de maior saida.
* [x] Excluir produtos.
* [x] Impressão de fichas de consumo.
* [x] Atalhos do teclado para maior agilidade.
* [x] Calculo de troco do pagamento.

### Módulo de Funcionários
* [X] Cadastrar novos funcionários.
* [x] Editar informações de funcionários existentes.
* [x] Excluir funcionários.
* [X] Gerenciar as permissões de cada funcionário (acesso a módulos, funções).

### Módulo de Relatórios
* [ ] Gerar relatório de vendas por período (diário, semanal, mensal).
* [ ] Gerar relatório de estoque (produtos em falta, produtos com alta rotatividade).
* [ ] Gerar relatório de clientes (mais ativos, menos ativos).
* [ ] Gerar relatório de funcionários (horas trabalhadas, faltas).

### Módulo de Pagamentos
* [ ] Integrar com gateways de pagamento (cartão de crédito, débito, PIX).
* [x] Gerenciar formas de pagamento.
* [ ] Emitir notas fiscais eletrônicas.


### Módulo de Delivery (opcional para restaurantes)
* [ ] Cadastrar entregadores.
* [ ] Gerenciar rotas de entrega.
* [ ] Acompanhar pedidos em tempo real.

### Módulo de Sistema
* [x] Gerenciar usuários do sistema (login, senha, permissões).
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
