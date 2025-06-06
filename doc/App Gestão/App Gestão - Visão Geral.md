# Aplicativo de Gestão do Bar - Visão Geral

O **Aplicativo de Gestão do Bar** é uma plataforma web centralizada, desenvolvida em Django/Python, destinada a administradores e gerentes do bar. Ele atua como o cérebro da operação, integrando e gerenciando todas as funcionalidades dos aplicativos mobile (BarApp e GarçomApp), além de introduzir capacidades essenciais de gestão empresarial.

## Propósito

O principal objetivo deste aplicativo é proporcionar um controle abrangente e eficiente sobre todas as áreas do negócio, desde a operação diária até a análise estratégica e financeira. Ele visa otimizar processos, reduzir erros e fornecer insights valiosos para a tomada de decisões.

## Principais Funcionalidades:

- **Gestão de Usuários:** Gerenciamento completo de clientes (do BarApp) e garçons (do GarçomApp), incluindo cadastro, edição e permissões.
    
- **Gestão de Cardápio e Produtos:** Cadastro, edição, exclusão e controle de disponibilidade de todos os itens do cardápio.
    
- **Gestão de Tickets e Eventos:** Visualização detalhada das vendas de tickets e ingressos, além do gerenciamento completo de eventos (cadastro, edição, exclusão).
    
- **Gestão da Fila do Karaokê:** Controle administrativo da fila, permitindo adicionar, editar, remover e reordenar participantes.
    
- **Gestão de Comandas:** Visão geral e gerenciamento detalhado de todas as comandas abertas, aguardando pagamento, pagas e fechadas.
    
- **Gestão de Funcionários:** Cadastro, manutenção de dados, cargos e controle de acesso para toda a equipe do bar.
    
- **Gestão de Pagamentos de Salário:** Registro de pagamentos, cálculo de holerites e histórico de salários.
    
- **Gestão de Estoque e Mercadorias:** Registro de entradas de produtos, atualização automática de estoque, visualização do inventário atual e alertas de estoque baixo.
    
- **Dashboards e Relatórios:** Painéis visuais e relatórios detalhados sobre vendas, lucratividade, desempenho de funcionários, estoque e finanças, permitindo análises estratégicas.
    

## Integração com os Outros Aplicativos:

Este aplicativo de gestão é o backend central para o **BarApp (cliente)** e o **GarçomApp (interno)**. Todas as informações de cardápio, tickets, ingressos, comandas, fila do karaokê e notificações são gerenciadas aqui e sincronizadas em tempo real com os aplicativos mobile, garantindo uma operação coesa e eficiente.

## Documentos Relacionados:

Para mais detalhes sobre o Aplicativo de Gestão do Bar, consulte os seguintes documentos:

- [[Requisitos - Aplicativo de Gestão]]
    
- [[Casos de Uso - Aplicativo de Gestão]]
    
- [[Histórias de Usuário - Aplicativo de Gestão]]
    
- [[Modelagem de Banco de Dados]]
    
- [[Visão Geral do Projeto]]