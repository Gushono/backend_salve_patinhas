# 
FROM python:3.10.3-slim

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app.py .
COPY ./alembic.ini .
COPY ./alembic /code/alembic
COPY ./src /code/src
COPY ./server.py .

#
EXPOSE 8081
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]