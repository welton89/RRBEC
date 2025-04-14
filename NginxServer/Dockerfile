FROM nginx:latest

# Remover a configuração padrão
RUN rm /etc/nginx/conf.d/default.conf

# Copiar sua configuração personalizada
COPY nginx.conf /etc/nginx/conf.d/