
| Atributo         | Tipo de Dado   | Restrições/Observações                                    |
| ---------------- | -------------- | --------------------------------------------------------- |
| `id_produto`     | UUID           | PK                                                        |
| `nome`           | VARCHAR(255)   | NOT NULL                                                  |
| `descricao`      | TEXT           | NULLABLE                                                  |
| `preco`          | DECIMAL(10, 2) | NOT NULL                                                  |
| `custo_unitario` | DECIMAL(10, 2) | NULLABLE (Para cálculo de lucratividade)                  |
| `estoque_atual`  | INTEGER        | NOT NULL, DEFAULT 0                                       |
| `estoque_minimo` | INTEGER        | DEFAULT 0 (Para alertas de estoque baixo)                 |
| `url_imagem`     | VARCHAR(255)   | NULLABLE                                                  |
| `disponivel`     | BOOLEAN        | NOT NULL, DEFAULT TRUE (Indica se está no cardápio ativo) |
| `id_categoria`   | UUID           | FK para `CategoriasProduto`                               |

| Atributo    | Tipo         | Modificadores                           |
| ----------- | ------------ | --------------------------------------- |
| id          | AutoField    | primary_key=True                        |
| name        | CharField    | max_length=100                          |
| description | TextField    | null=True, blank=True                   |
| image       | ImageField   | null=True, blank=True                   |
| price       | DecimalField | max_digits=10, decimal_places=2         |
| quantity    | IntegerField | null=False, default=0                   |
| category    | ForeignKey   | on_delete=models.CASCADE ([[Category]]) |
| cuisine     | BooleanField | default=False                           |
| active      | BooleanField | default=True                            |


**Modelo: `Product`**

Este modelo representa um produto no sistema. Cada produto possui os seguintes atributos:

*   `id`: Um identificador único para cada produto (chave primária). Este campo é preenchido automaticamente.
*   `name`: O nome do produto (texto curto, máximo de 100 caracteres).
*   `description`: Uma descrição detalhada do produto (texto longo). Pode ser deixada em branco.
*   `image`: Uma imagem associada ao produto. Pode ser deixada em branco.
*   `price`: O preço do produto (valor decimal com um total de 10 dígitos, incluindo 2 casas decimais).
*   `quantity`: A quantidade disponível em estoque (número inteiro). Por padrão, é 0.
*   `category`: A categoria à qual o produto pertence. É uma chave estrangeira que se relaciona ao modelo [[Category]]. Se uma categoria for excluída, todos os produtos associados a essa categoria também serão excluídos (`on_delete=models.CASCADE`).
*   `cuisine`: Um campo booleano que indica se o produto é preparado na cozinha. O valor padrão é `False`.
*   `active`: Um campo booleano que indica se o produto está ativo e disponível para venda. O valor padrão é `True`.

**Modelo: `Category`**

Este modelo representa uma categoria de produto. Cada categoria possui os seguintes atributos:

*   `id`: Um identificador único para cada categoria (chave primária). Este campo é preenchido automaticamente.
*   `name`: O nome da categoria (texto curto, máximo de 255 caracteres).

**Relacionamento:**

Os modelos `Product` e `Category` estão relacionados por meio de uma chave estrangeira. Cada produto pertence a uma categoria, e uma categoria pode ter vários produtos associados a ela.

**Uso:**

Esses modelos são usados para definir a estrutura do banco de dados e facilitar a criação, leitura, atualização e exclusão (CRUD) de produtos e categorias no sistema. Eles são componentes essenciais para gerenciar o catálogo de produtos.
