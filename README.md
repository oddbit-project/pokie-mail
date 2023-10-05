# Welcome to Pokie-mail


Transactional email support for Pokie

# Features

The pokie-mail package implements a simple templating system for emails, as well as a job queue to send them. The templating
system supports multiple locales per template, and has the notion of channel - allowing it to be used for other
purposes such as push notifications.

The provided worker will attempt to send upto 10k emails per batch from the queue, using the configured [rick_mailer](https://github.com/oddbit-project/rick-mailer) 
sink for channel 0 submissions.

Other channel submissions (such as site notifications and push notifications) need to be implemented with their specific
behaviour.

# Templates

The module supports both embedded html templates and text templates, as well as a list of placeholders and default values.
Application templates can either be imported directly via SQL or using Pokie's fixture mechanism.




# Running tests

Running tests require a PostgreSQL database server with access credentials that can run CREATE DATABASE/DROP DATABASE 
commands. The test database is created automatically.

## running with pytest

Install required dependencies:

```shell
$ pip3 install -r requirements-dev.txt
```

Define the appropriate environment variables to access the database, and run pytest (optionally with code coverage):
```shell
$ TEST_DB_HOST='localhost' TEST_DB_USER='db_user' TEST_DB_PASSWORD='db_password' python3 main.py pytest [-cov=pokie_mail]
```

## running with tox

Edit tox.ini and set the appropriate database credentials, then just run tox with the desired environment, eg:  

```shell
$ tox -e py310
```

