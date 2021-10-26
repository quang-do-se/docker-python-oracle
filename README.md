
# Run with Docker

## Run

``` shell
docker build --no-cache --progress=plain -t python-oracle -f Dockerfiles/python.Dockerfile .

docker container run -d \
  -v $(pwd)/python:/scripts \
  -v /usr/local/adm/config/tomcat/oracle_wallets:/usr/local/adm/config/tomcat/oracle_wallets:ro \
  --name python-oracle \
  python-oracle

docker exec -it python-oracle /bin/bash

python /scripts/test-oracle-connection.py --url="<user>/<password>@<tns-name>"
```
## Clean up

``` shell
docker stop python-oracle

docker rm python-oracle
```

---

# Run with Docker Compose

## Run

- Note: you can run `cp .env-template .env`, store db connection string in .env, retrieve it using ${DB_URL}

``` shell
docker-compose up -d --build
```

``` shell

docker exec -it python-oracle /bin/bash

python /scripts/test-oracle-connection.py --url="${DB_URL}"

```

OR

``` shell
docker exec -it python-oracle sh -c 'python /scripts/test-oracle-connection.py --url="${DB_URL}"'

```
## Clean up

``` shell
docker-compose down
```
