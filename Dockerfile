FROM tiangolo/uwsgi-nginx-flask:python3.10
RUN pip install requests
COPY ./app /app
