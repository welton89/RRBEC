
| Atributo  | Tipo          | Modificadores                          |
| --------- | ------------- | -------------------------------------- |
| id        | AutoField     | primary_key=True                       |
| comanda   | ForeignKey    | on_delete=models.CASCADE ([[Comanda]]) |
| data_time | DateTimeField | auto_now_add=True                      |
| product   | ForeignKey    | on_delete=models.PROTECT ([[Product]]) |
| applicant | CharField     | max_length=255, null=True, blank=True  |



**Modelo: `ProductComanda`**

Este modelo representa um item individual dentro de um pedido (comanda). Ele atua como uma tabela de junção entre os modelos `Product` e `Comanda`, permitindo que uma comanda contenha múltiplos produtos e que um produto possa aparecer em múltiplas comandas.

**Atributos:**

*   `id`: Um identificador único para cada entrada de produto em um pedido (chave primária). Este campo é preenchido automaticamente.
*   `comanda`: Uma chave estrangeira que referencia o modelo [[Comanda]]. Define a qual comanda este produto está associado. Se a comanda relacionada for excluída, todos os `ProductComanda` associados a ela também serão excluídos (`on_delete=models.CASCADE`).
*   `data_time`: A data e hora em que o produto foi adicionado à comanda. Este campo é preenchido automaticamente no momento da criação (`auto_now_add=True`).
*   `product`: Uma chave estrangeira que referencia o modelo [[Product]]. Define qual produto está sendo incluído na comanda. Se o produto relacionado for excluído, o `ProductComanda` permanecerá, mas o produto será protegido contra exclusão (`on_delete=models.PROTECT`).
*   `applicant`: Um campo de texto (CharField) que armazena o nome de quem solicitou o produto. Pode ser nulo ou em branco.

**Relacionamentos:**

*   `ProductComanda` possui um relacionamento ForeignKey com [[Comanda]] (uma comanda pode ter vários produtos).
*   `ProductComanda` possui um relacionamento ForeignKey com [[Product]] (um produto pode estar em vários pedidos).

**Uso:**

Este modelo é crucial para rastrear quais produtos foram incluídos em cada pedido, bem como quando cada produto foi adicionado. Ele permite gerar relatórios de vendas por produto, analisar quais produtos são mais populares em determinados horários e gerenciar o estoque de forma eficiente. Através do campo `applicant` é possível saber quem solicitou o produto dentro da comanda.