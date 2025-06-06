| Atributo | Tipo      | Modificadores    |
| -------- | --------- | ---------------- |
| id       | AutoField | primary_key=True |
| name     | CharField | max_length=255   |


A classe [[TypePay]] (TipoPagamento) é um modelo Django que representa as formas de pagamento aceitas no sistema.

*   **`id`**: Campo de identificação único para cada forma de pagamento. É um `AutoField`, o que significa que é um campo que se incrementa automaticamente, definido como chave primária (`primary_key=True`).
*   **`name`**: Campo que armazena o nome da forma de pagamento (ex: "Cartão de Crédito", "Boleto Bancário", "Pix"). É um `CharField` com um comprimento máximo de 255 caracteres (`max_length=255`).