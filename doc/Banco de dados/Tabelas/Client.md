
| Atributo   | Tipo          | Modificadores                         |
| ---------- | ------------- | ------------------------------------- |
| id         | AutoField     | primary_key=True                      |
| name       | CharField     | max_length=255                        |
| debt       | DecimalField  | max_digits=10, decimal_places=2       |
| created_at | DateTimeField | auto_now_add=True                     |
| active     | BooleanField  | default=True                          |
| contact    | CharField     | max_length=255, null=True, blank=True |


A classe [[Client]] define um modelo de dados para representar um cliente no sistema. Ela contém os seguintes atributos:

*   **id**: Um campo AutoField que serve como chave primária, identificando unicamente cada cliente. O Django gerencia esse campo automaticamente.
*   **name**: Um campo CharField que armazena o nome do cliente, com um limite máximo de 255 caracteres.
*   **debt**: Um campo DecimalField que representa o débito do cliente. Ele permite armazenar números decimais com precisão de até 10 dígitos, com 2 casas decimais.
*   **created\_at**: Um campo DateTimeField que registra a data e hora de criação do cliente. O valor é definido automaticamente quando o cliente é criado (auto\_now\_add=True).
*   **active**: Um campo BooleanField que indica se o cliente está ativo ou não. Por padrão, o valor é True.
*   **contact**: Um campo CharField para armazenar informações de contato do cliente, como telefone ou e-mail. Pode ser nulo (null=True) e em branco (blank=True) no banco de dados.