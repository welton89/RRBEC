
| Atributo | Tipo          | Modificadores                                                 |
| -------- | ------------- | ------------------------------------------------------------- |
| id       | AutoField     | primary_key=True                                              |
| mesa     | ForeignKey    | on_delete=models.CASCADE ([[Mesas]])                          |
| user     | ForeignKey    | on_delete=models.CASCADE ([[Projeto_RRBEC/Banco de dados/Tabelas/Users]]), null=False, blank=True  |
| type_pay | ForeignKey    | on_delete=models.SET_NULL (TypePay), null=True                |
| dt_open  | DateTimeField | auto_now_add=True                                             |
| dt_close | DateTimeField | null=True, blank=True                                         |
| client   | ForeignKey    | on_delete=models.SET_NULL ([[Client]]), null=True, blank=True |
| name     | CharField     | max_length=255                                                |
| status   | CharField     | max_length=255, default="OPEN"                                |


A classe [[Comanda]] representa um pedido ou conta em um restaurante. Ela contém informações sobre a mesa em que o pedido foi feito, o usuário (garçom) responsável, a forma de pagamento, horários de abertura e fechamento, o cliente associado (se houver), um nome para a comanda e seu status.

**Atributos:**

*   `id`: Identificador único da comanda (chave primária).
*   `mesa`: Mesa à qual a comanda está associada (chave estrangeira para a classe [[Mesas]]). Se a mesa for excluída, a comanda também será excluída (on\_delete=models.CASCADE).
*   `user`: Usuário (garçom) que abriu a comanda (chave estrangeira para a classe [[Projeto_RRBEC/Banco de dados/Tabelas/Users]]). Se o usuário for excluído, a comanda também será excluída (on\_delete=models.CASCADE). Pode ser nulo e em branco.
*   `type_pay`: Forma de pagamento utilizada na comanda (chave estrangeira para a classe TypePay ). Se a forma de pagamento for excluída, o campo `type_pay` da comanda será definido como `NULL` (on_delete=models.SET_NULL).
*   `dt_open`: Data e hora em que a comanda foi aberta. O valor é definido automaticamente ao criar a comanda (auto\_now\_add=True).
*   `dt_close`: Data e hora em que a comanda foi fechada. Pode ser nulo e em branco.
*   `client`: Cliente associado à comanda (chave estrangeira para a classe [[Client]]). Se o cliente for excluído, o campo `client` da comanda será definido como `NULL` (on\_delete=models.SET\_NULL). Pode ser nulo e em branco.
*   `name`: Nome da comanda (por exemplo, "Comanda da Mesa 5").
*   `status`: Status da comanda (por exemplo, "ABERTA", "FECHADA"). O valor padrão é "OPEN".