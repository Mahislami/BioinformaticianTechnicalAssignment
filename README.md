# BioinformaticianTechnicalAssignment

# Running the app locally

Change the directory to DB-Docker, in this folder, you will find a Dockerfile used for creating the mysql image. execute the file by running the command below and wait until the build is complete:

```
cd SQL-Docker
docker build --tag mysql_db .
```
Then move back to the main directory and run the command below to execute the Dockerfile:
```
docker build --tag bio-ta .
```

Once building is finished, run the command below to run the applicarion:

```
docker-compose up
```