FROM python:3.8.1

WORKDIR /app

COPY Pip* ./

RUN pip install pipenv

RUN pipenv install

COPY . .

RUN pipenv run python manage.py migrate

RUN chmod +x scripts/boostrap.sh


EXPOSE 8000

CMD ["bash", "-c", "scripts/boostrap.sh"]