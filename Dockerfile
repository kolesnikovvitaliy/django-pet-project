FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV app_port 8000
WORKDIR /code
RUN apk --update --upgrade --no-cache add fontconfig ttf-freefont font-noto terminus-font \ 
   && fc-cache -f \ 
   && fc-list | sort
RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

EXPOSE ${app_port}  
ENTRYPOINT ["/code/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=django_pet_project.settings"]
