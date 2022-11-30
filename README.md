# backend_salve_patinhas
Tcc using python and fastapi


# Running the server on docker

```
docker run --name postgresql -e POSTGRESQL_USERNAME=postgres -e ALLOW_EMPTY_PASSWORD=yes -p 5432:5432 bitnami/postgresql:latest
docker-compose up
```

# Running tests 
    
    ```
    docker-run --name postgresql -e POSTGRESQL_USERNAME=postgres -e ALLOW_EMPTY_PASSWORD=yes -p 5432:5432 bitnami/postgresql:latest
    ```
# To contribute commiting...

## generate a venv
virtualenv venv

## install requirements
pip install -r requirements.txt

## install pre-commit
pre-commit install

enjoy
