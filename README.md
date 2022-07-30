# backend_salve_patinhas
Tcc using python and fastapi


# Running the server on docker

```
docker build . -t backend_salve_patinhas
docker run -p 8081:8081 --name backend_salve_patinhas -d backend_salve_patinhas

```

# To contribute commiting...

## generate a venv
virtualenv venv

## install requirements
pip install -r requirements.txt

## install pre-commit
pre-commit install

enjoy
