FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python gestaoRaul/manage.py collectstatic --noinput

WORKDIR /app/gestaoRaul



CMD [ "gunicorn", "gestaoRaul.wsgi:application", "--bind", "0.0.0.0:8000" ]
  