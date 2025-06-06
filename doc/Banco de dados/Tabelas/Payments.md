| Atributo    | Tipo          | Modificadores                                    |
| ----------- | ------------- | ------------------------------------------------ |
| id          | AutoField     | primary_key=True                                 |
| value       | DecimalField  | max_digits=10, decimal_places=2                  |
| type_pay    | ForeignKey    | on_delete=models.PROTECT ([[TypePay]])           |
| comanda     | ForeignKey    | on_delete=models.PROTECT ([[Comanda]])           |
| client      | ForeignKey    | null=True, on_delete=models.PROTECT ([[Client]]) |
| description | CharField     | max_length=255                                   |
| datetime    | DateTimeField | auto_now_add=True                                |


A classe `Payments` é um modelo Django que representa os pagamentos realizados no sistema.

**Atributos:**

*   `id`: Campo de identificação único para cada pagamento. É um `AutoField`, o que significa que é um campo que se incrementa automaticamente, definido como chave primária (`primary_key=True`).
*   `value`: Campo que armazena o valor do pagamento. É um `DecimalField` com um máximo de 10 dígitos, sendo 2 casas decimais (`max_digits=10, decimal_places=2`).
*   `type_pay`: Campo que armazena o tipo de pagamento. É um `ForeignKey` que se relaciona com o modelo [[TypePay]]. Quando um tipo de pagamento é excluído, o campo `type_pay` é protegido, impedindo a exclusão do tipo de pagamento se houver pagamentos associados a ele (`on_delete=models.PROTECT (TypePay)`).
*   `comanda`: Campo que armazena a comanda relacionada ao pagamento. É um `ForeignKey` que se relaciona com o modelo [[Comanda]]. Quando uma comanda é excluída, o campo `comanda` é protegido, impedindo a exclusão da comanda se houver pagamentos associados a ela (`on_delete=models.PROTECT (Comanda)`).
*   `client`: Campo que armazena o cliente relacionado ao pagamento. É um `ForeignKey` que se relaciona com o modelo [[Client]]. Pode ser nulo e, quando um cliente é excluído, o campo `client` é protegido, definindo o campo como `NULL` (`null=True, on_delete=models.PROTECT (Client)`).
*   `description`: Campo que armazena uma descrição do pagamento. É um `CharField` com um comprimento máximo de 255 caracteres (`max_length=255`).
*   `datetime`: Campo que armazena a data e hora em que o pagamento foi realizado. O valor é definido automaticamente ao criar o pagamento (`auto_now_add=True`).