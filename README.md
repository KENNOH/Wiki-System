# WIKI SYSTEM TEST

# Create a database in POSTGRESQL
Create a database in POSTGRESQL and input the correct env values in the .env file
This is mentioned under the .env file section
Optional: Check the connection details in settings.py for the database connection.

# Virtual environment
I recommend creating a virtual env for all the python dependencies.
	
# Install the dependencies from requirements.txt
	pip install -r requirements.txt

# Run the database migrations 
	python3 manage.py migrate


# To set up Celery for running automatic backups
To configure and celery you need first install and configure rabbitmq server
Once set up just update the credentials on the .env file
To run celery on windows open another powershell or linux terminal or a cmd tab in the project root and run the command

	celery -A wiki_system worker --pool=solo -l info


And on another terminal run the celery beat

	celery -A wiki_system beat -l info

*** Although not recommended for multiple horizontal instances, to run celery worker and beat in one command: ***
	celery -A wiki_system worker --concurrency=3 beat -l info

*** Where 3 is the number of workers determined by the cpu cores available in the server using the formula: ***
	workers = (2 * cores) + 1


# To start the server
	python3 manage.py runserver

# To create superuser
	python3 manage.py createsuperuser

# .env file
Create a .env file in the root folder of the project with the following keys along with their appropriate values

	DATABASE_NAME = 
	DATABASE_USER = 
	DATABASE_PASSWORD = 
	DATABASE_HOST = 
	DB_HOST = 
	DB_PORT = 

	REDIS_IP = 
	SECRET_KEY = 

    RABBITMQUSER =
    RABBITMQPASSWORD =
    RABBITMQVHOST = 

    AWS_ACCESS_KEY_ID =
    AWS_SECRET_ACCESS_KEY =
    AWS_STORAGE_BUCKET_NAME =
    AWS_S3_ENDPOINT_URL =
    AWS_S3_CUSTOM_DOMAIN =
	



