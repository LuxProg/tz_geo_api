FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade && apt-get autoremove && apt-get autoclean && apt-get install -y sqlite3

RUN mkdir web_apps_maps
COPY ../web_app_maps/
COPY roads.sqlite /web_app_maps/roads.sqlite
WORKDIR /web_apps_maps

RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]