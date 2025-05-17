FROM python:3.12.6-slim
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --without dev

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]
