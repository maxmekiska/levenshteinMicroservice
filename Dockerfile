FROM python:3.8-alpine
COPY . /app
WORKDIR /app
RUN pip install .
EXPOSE 5000
CMD [ "python", "service/app/endpoints.py" ]