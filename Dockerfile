FROM python:3

RUN git clone https://github.com/welton89/RRBEC.git
RUN cd RRBEC

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/gestaoRaul
RUN python gestaoRaul/manage.py collectstatic --noinput

# RUN python gestaoRaul/manage.py migrate --noinput



CMD [ "gunicorn",  "-w", "4", "--timeout", "15", "gestaoRaul.wsgi:application", "--bind", "0.0.0.0:8000" ]
  