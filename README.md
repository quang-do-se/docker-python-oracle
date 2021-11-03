
# Run with Docker

## Run

``` shell
git clone git@github.com:quang-do-se/docker-python-oracle.git

cd docker-python-oracle

docker build --no-cache --progress=plain -t python-oracle -f Dockerfiles/python.Dockerfile .

docker container run -d \
-v $(pwd)/python:/scripts \
-v /usr/local/adm/config/tomcat/oracle_wallets:<oracle-wallet-location-on-your-machine>:ro \
--name python-oracle \
python-oracle

docker exec -it python-oracle /bin/bash

python /scripts/test-oracle-connection.py --tns="<ORACLE_TNS_NAME>"
```

## Clean up

``` shell
docker stop python-oracle

docker rm python-oracle
```

---

# Run with Docker Compose

## Run


``` shell
git clone git@github.com:quang-do-se/docker-python-oracle.git

cd docker-python-oracle

docker-compose up -d --build
```

``` shell

docker exec -it python-oracle /bin/bash

python /scripts/test-oracle-connection.py --tns="<ORACLE_TNS_NAME>"

```

OR

``` shell
docker exec -it python-oracle sh -c 'python /scripts/test-oracle-connection.py --tns="<ORACLE_TNS_NAME>"

```

## Testing manually

- Run below commands in Python interpreter:

``` shell
import cx_Oracle

connection = cx_Oracle.connect(user="<your-user>", password="<your-password>", dsn="<dsn>")

cursor = connection.cursor()

cursor.execute('select sysdate from dual').fetchall()
```

## Clean up

``` shell
docker-compose down
```

## References

- Environment Variables for Oracle Instant Client: https://docs.oracle.com/en/database/oracle/oracle-database/21/lacli/environment-variables-instant-client.html#GUID-BA8FB14E-1463-4F6A-9926-4F9F696E52D0
