# Documentação do Projeto RRBEC (Gestão Raul)

Esta documentação fornece uma visão geral técnica e funcional do sistema **Gestão Raul**, abrangendo sua estrutura, regras de negócio, modelagem de banco de dados, APIs e mecanismos de autenticação.

---

## 1. Estrutura do Projeto

O projeto é baseado no framework **Django** (Python) e segue o padrão de arquitetura de aplicações modulares.

### Diretórios Principais
- `gestaoRaul/`: Configurações centrais do Django (settings, urls, wsgi).
- `products/`: Gestão de produtos, categorias e unidades de medida.
- `clients/`: Cadastro de clientes e controle de débitos ("Fiados").
- `mesas/`: Gestão das mesas físicas do estabelecimento.
- `comandas/`: Núcleo do sistema. Gerencia o consumo, estoque e fluxo de vendas.
- `orders/`: Controle da fila de produção (cozinha/bar).
- `payments/`: Registros de pagamentos e cálculos de taxas.
- `typePay/`: Tipos de pagamentos aceitos (Crédito, Débito, Pix, Fiado, etc.).
- `login/`: Lógica de autenticação e customização de tokens JWT.
- `templates/`: Arquivos HTML para a interface web (utiliza Vanilla CSS e JS).
- `media/`: Armazenamento de imagens de produtos.

---

## 2. Regras de Negócio

O sistema foi projetado para gerenciar o fluxo operacional de um restaurante/bar de ponta a ponta.

### Fluxo de Comanda e Vendas
1.  **Abertura**: Uma comanda é vinculada a uma mesa e, opcionalmente, a um cliente. O status inicial é `OPEN`.
2.  **Lançamento de Itens**: Ao adicionar um produto a uma comanda, o sistema automaticamente:
    - Deduz a quantidade do produto do estoque.
    - Se o produto for composto (combo/receita), deduz os componentes individuais.
    - Se o produto tiver a flag `cuisine=True`, gera um pedido (`Order`) na fila da cozinha.
3.  **Gestão de Estoque**: Todas as entradas e saídas são registradas na tabela de `StockMovement` para auditoria.
4.  **Fechamento**: Ao realizar o pagamento (total ou parcial), a comanda pode ser encerrada (`CLOSED`).
5.  **Taxa de Serviço**: O sistema calcula automaticamente uma taxa de 10% sobre o consumo total.

### Fila de Produção (Cozinha)
Os pedidos passam por estados cronometrados:
- `Queue` (Em espera) -> `Preparing` (Preparando) -> `Finished` (Pronto) -> `Delivered` (Entregue).
- Também é possível cancelar um pedido, o que gera um estorno automático para o estoque.

### Sistema de "Fiado" (Débitos de Clientes)
- Clientes podem ter comandas marcadas com o tipo de pagamento "FIADO".
- O sistema mantém um registro do débito acumulado do cliente.
- Existem endpoints específicos para listar e quitar múltiplos débitos de uma vez.

---

## 3. Modelagem do Banco de Dados

O banco de dados utiliza a seguinte estrutura relacional (simplificada):

### Principais Entidades
- **Mesa**: `id`, `name`, `active`.
- **Client**: `id`, `name`, `debt`, `contact`, `active`.
- **Product**: `id`, `name`, `price`, `quantity`, `category_id`, `cuisine` (boolean), `active`.
- **ProductComponent**: (Tabela intermediária de composição) Liga um `Product` a outros `Products` com uma `quantity_required`.
- **Comanda**: `id`, `mesa_id`, `client_id`, `user_id`, `status` (OPEN/CLOSED/FIADO), `dt_open`, `dt_close`.
- **ProductComanda**: `id`, `comanda_id`, `product_id`, `data_time`, `applicant`.
- **Order (Pedido)**: `id`, `productComanda_id`, `obs`, `queue`, `preparing`, `finished`, `delivered`, `canceled`.
- **Payments**: `id`, `comanda_id`, `type_pay_id`, `value`, `client_id`, `datetime`.

---

## 4. API e Autenticação

A API é construída com **Django REST Framework (DRF)** e segue os princípios REST.

### Autenticação
O sistema utiliza **JWT (JSON Web Token)** para proteger os endpoints.

1.  **Obter Token**: `POST /api/v1/token/`
    - Body: `{"username": "...", "password": "..."}`
    - Retorno: `access` e `refresh` tokens, além de dados do usuário (ID, nome, grupos).
2.  **Atualizar Token**: `POST /api/v1/token/refresh/`
    - Body: `{"refresh": "..."}`
3.  **Uso**: Deve-se enviar o token no cabeçalho: `Authorization: Bearer <seu_token>`.

### Endpoints Principais (`/api/v1/`)

| Endpoint | Método | Descrição |
| :--- | :--- | :--- |
| `comandas/` | GET/POST | Lista ou cria novas comandas. |
| `comandas/{id}/pagar/` | POST | Registra pagamento e fecha a comanda. |
| `comandas/{id}/apagar/` | POST | Limpa todos os itens e fecha a comanda (estorna estoque). |
| `items-comanda/` | POST/DELETE | Adiciona ou remove itens de uma comanda individualmente. |
| `orders/` | GET/PATCH | Lista pedidos da cozinha ou edita observações. |
| `orders/{id}/preparing/` | POST | Inicia o preparo do pedido. |
| `orders/{id}/finish/` | POST | Marca como pronto para entrega. |
| `clients/{id}/fiados/` | GET | Lista todas as comandas pendentes (fiado) de um cliente. |
| `clients/pagar_fiados/`| POST | Quita uma lista de IDs de comandas fiadas. |
| `products/` | GET | Lista produtos ativos e estoque. |

### Lógica de Negócio Integrada na API
- **POST `items-comanda/`**: Ao postar um item, a API automaticamente executa `StockMovement.subTransactionStock` e cria um `Order` se necessário.
- **DELETE `items-comanda/{id}/`**: Ao deletar, a API executa `StockMovement.sumTransactionStock` para devolver o item ao estoque.

---

## 5. Tecnologias Utilizadas
- **Backend**: Django 5.1, Django REST Framework, SimpleJWT.
- **Frontend**: HTML5, Vanilla CSS, JavaScript.
- **Service Worker**: Configurado para suporte a PWA (Progressive Web App).
- **Banco de Dados**: SQLite (Desenvolvimento) / PostgreSQL ou MySQL (Produção).
- **Middleware**: WhiteNoise (arquivos estáticos), CORS Headers.

---
*Atualizado em: 24 de Março de 2026*
