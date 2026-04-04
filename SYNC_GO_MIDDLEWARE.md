# Guia de Sincronização: Django <-> Middleware Go

Este documento descreve o funcionamento do sistema de **ChangeLog** implementado no Django para permitir que o middleware em Go mantenha uma cópia local (local-first) dos dados de forma eficiente.

## 1. Funcionamento Técnico

### Rastreamento de Mudanças (Django Signals)
Foi criada uma aplicação chamada `sync` que utiliza **Django Signals**. Sempre que um dos modelos abaixo é criado, editado ou excluído, uma entrada é gerada automaticamente na tabela `ChangeLog`:

- `Product`
- `Comanda`
- `ProductComanda`
- `Order`
- `Client`
- `Categories`
- `Mesa`
- `Payments`

### Tabela de Log (`ChangeLog`)
Cada registro no log contém:
- `id`: Identificador sequencial da mudança.
- `model_name`: Nome do modelo (ex: "Product").
- `object_id`: ID do objeto que mudou.
- `action`: "SAVE" (para criação/edição) ou "DELETE".
- `timestamp`: Quando a mudança ocorreu.

## 2. API de Sincronização

O middleware Go deve consumir o seguinte endpoint:

**Endpoint:** `GET /api/v1/sync/`

### Parâmetros:
- `since_id` (opcional): Retorna apenas mudanças com ID maior que este valor.

### Exemplo de Fluxo no Go:

1.  **Estado Inicial**: O Go armazena o `last_sync_id` (começando em 0).
2.  **Polling**: De tempos em tempos (ex: a cada 5 segundos), o Go chama:
    `GET http://seu-servidor/api/v1/sync/?since_id=100` (supondo que o último ID processado foi 100).
3.  **Processamento**:
    - O Django retorna uma lista de mudanças (ex: IDs 101, 102, 103).
    - Para cada mudança `SAVE` no log, o Go deve fazer um `GET` no endpoint específico do modelo para buscar os dados atualizados:
      - Se `model_name == "Product"`, buscar em `GET /api/v1/products/{object_id}/`.
    - Para cada mudança `DELETE`, o Go deve remover o item correspondente do seu banco de dados local.
4.  **Atualização**: O Go atualiza seu `last_sync_id` para o maior ID recebido (neste caso, 103).

## 3. Vantagens
- **Performance**: O Go não precisa baixar todos os produtos/pedidos toda vez. Ele só baixa o que realmente mudou.
- **Detecção de Deleção**: O sistema informa explicitamente o que foi apagado no Django.
- **Resiliência**: Se a conexão cair, ao reconectar, o Go apenas retoma a partir do último ID que ele conhece, garantindo que nenhuma mudança seja perdida.

---
*Configurado em: 28 de Março de 2026*
