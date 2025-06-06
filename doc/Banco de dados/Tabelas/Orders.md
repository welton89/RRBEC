| Atributo       | Tipo          | Modificadores                                             |
| -------------- | ------------- | --------------------------------------------------------- |
| id             | AutoField     | primary_key=True                                          |
| productComanda | ForeignKey    | on_delete=models.SET_NULL ([[ProductComanda]]), null=True |
| id_product     | ForeignKey    | on_delete=models.CASCADE ([[Product]])                    |
| id_comanda     | ForeignKey    | on_delete=models.CASCADE ([[Comanda]])                    |
| obs            | TextField     | blank=True, null=True                                     |
| queue          | DateTimeField | auto_now_add=True                                         |
| preparing      | DateTimeField | null=True, blank=True                                     |
| finished       | DateTimeField | null=True, blank=True                                     |
| delivered      | DateTimeField | null=True, blank=True                                     |
| canceled       | DateTimeField | null=True, blank=True                                     |

**Modelo: `Orders`**

A classe apresentada no arquivo [[Orders]] representa um modelo para rastrear o status de um pedido ao longo do tempo.

**Atributos:**

*   `id`: Um identificador único para cada atualização de status do pedido (chave primária).
*   `productComanda`: Uma chave estrangeira que referencia o modelo [[ProductComanda]]. Se o `ProductComanda` for excluído, este campo será definido como `NULL`.
*   `id_product`: Uma chave estrangeira que referencia o modelo [[Product]]. Se o produto for excluído, o `ProductComanda` e, portanto, este pedido serão excluídos.
*   `id_comanda`: Uma chave estrangeira que referencia o modelo [[Comanda]]. Se a comanda for excluída, este pedido será excluído.
*   `obs`: Campo de texto para observações sobre o pedido.
*   `queue`: Data e hora em que o pedido foi colocado na fila.
*   `preparing`: Data e hora em que o pedido começou a ser preparado.
*   `finished`: Data e hora em que o pedido foi finalizado.
*   `delivered`: Data e hora em que o pedido foi entregue.
*   `canceled`: Data e hora se  o pedido for cancelado. Campo pode ser nulo

**Relacionamentos:**

*   `Orders` possui um relacionamento ForeignKey com [[ProductComanda]].
*   `Orders` possui um relacionamento ForeignKey com [[Product]].
*   `Orders` possui um relacionamento ForeignKey com [[Comanda]].

**Uso:**

Este modelo permite rastrear o progresso de um pedido desde o momento em que é colocado na fila até a entrega ou cancelamento. Ele fornece informações valiosas para análise de tempo de preparo, gargalos no processo e eficiência da equipe.

