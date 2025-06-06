| Atributo | Tipo         | Modificadores                         |
| -------- | ------------ | ------------------------------------- |
| id       | AutoField    | primary_key=True                      |
| name     | CharField    | max_length=100                        |
| location | CharField    | max_length=255, null=True, blank=True |
| active   | BooleanField | default=False                         |


A classe [[Mesas]] representa uma mesa dentro do sistema. Cada mesa possui os seguintes atributos:

*   `id`: Um identificador único para cada mesa, gerado automaticamente. Este campo é a chave primária da tabela.
*   `name`: O nome da mesa. Este campo é do tipo texto, com um limite de 100 caracteres.
*   `location`: A localização da mesa. Este campo é do tipo texto, com um limite de 255 caracteres. Pode ser nulo ou vazio.
*   `active`: Um indicador booleano que indica se a mesa está ativa ou não. Por padrão, é definido como `False`.