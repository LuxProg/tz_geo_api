FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade && apt-get autoremove && apt-get autoclean

RUN mkdir web_apps_maps
COPY ../web_app_maps/
WORKDIR /web_apps_maps

RUN pip install --upgrade pip
RUN pip install django
RUN pip install djangorestframework

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]