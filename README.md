# BioinformaticianTechnicalAssignment

### Running The Application Locally

Change the directory to DB-Docker:

```
cd SQL-Docker
```

ّIn this folder, you will find a Dockerfile used for creating the mysql image. execute the file by running the command below and wait until the build is complete:

```
docker build --tag mysql_db .
```

Then move back to the main directory and run the command below to execute the Dockerfile which is used to build the application image:
```
docker build --tag bio-ta .
```

After building is finished, run the command below to run the application:

```
docker-compose up
```

### Migrations

Once application is running, open a new terminal window and run the command below to create the default Django ORM models:

```
docker exec -it django_container python manage.py makemigrations
docker exec -it django_container python manage.py migrate
```

ُTo create an admin, run the command below:
```
docker exec -it django_container python manage.py createsuperuser
```
Then follow the instructions to set the credentials.


## Populating Data

To populate data, you can either use the ``` diff populateData() in orange ``` function function provided in the Notebook.ipynb 

