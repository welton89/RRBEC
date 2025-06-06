| Atributo | Tipo      | Modificadores    |
| -------- | --------- | ---------------- |
| id       | AutoField | primary_key=True |
| name     | CharField | max_length=255   |


**Modelo: `Category`**

Este modelo representa uma categoria de produto. Cada categoria possui os seguintes atributos:

*   `id`: Um identificador único para cada categoria (chave primária). Este campo é preenchido automaticamente.
*   `name`: O nome da categoria (texto curto, máximo de 255 caracteres).

**Relacionamento:**

Os modelos `Product` e `Category` estão relacionados por meio de uma chave estrangeira. Cada produto pertence a uma categoria, e uma categoria pode ter vários produtos associados a ela.