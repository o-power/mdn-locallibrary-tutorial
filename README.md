<h1 id="title">Dashing Data</h1>

1. [Introduction](#introduction)
2. [Deployment](#deployment)
3. [Credits](#credits)

<h2 id="introduction">Introduction</h2>


<h2 id="deployment">Development Environment</h2>

Virtual Environment
venv for Python 3 or virtualenv for Python 2.
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
venv is included in the Python 3 standard library and requires no additional installation.
python -m venv env
source env/Scripts/activate

(env)
pip list

python -m pip install versus pip install
They do exactly the same thing. In fact, the docs for distributing Python modules were just updated to suggest using python -m pip instead of the pip executable, because it's easier to tell which version of python is going to be used to actually run pip that way.

For a package, the contents of the __main__.py module will be executed when the module is run with -m.

pip install Django
python -m django --version

django-admin startproject locallibrary .
or
mkdir django_projects 
cd django_projects
django-admin startproject locallibrary
cd locallibrary

Run the application on a local development server
python manage.py runserver

Put SECRET_KEY in env.py file

.gitignore

Initialize, add remote, commit

Create the catalog application
python manage.py startapp catalog

Register the application by adding it to the INSTALLED_APPS list in the project settings. 

python manage.py makemigrations
python manage.py migrate

To install the command-line tool for executing SQL statements against the SQLite database.
Got to https://sqlite.org/download.html. Download the zip file containing the sqlite tools. Open the zip file and copy the executable files into the env/Scripts folder.

sqlite3 db.sqlite3
.tables (lists all tables)
.headers on
.mode column
select * from django_migrations;
.quit

To view the SQl a migration will execute:
python manage.py sqlmigrate catalog 0001

To check a migration for errors (after makemigrations but before migrate):
python manage.py check

Create a superuser account:
python manage.py createsuperuser
http://127.0.0.1:8000/admin
Redirected to http://127.0.0.1:8000/admin/login and then back to http://127.0.0.1:8000/admin.
http://127.0.0.1:8000/admin/login/?next=/admin/

Statements not used yet:
pip freeze --local > requirements.txt


<h2 id="credits">Credits</h2>

- The bulk of the code was taken directly from the MDN web docs [Django Tutorial: The Local Library website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website) [accessed 22nd July 2020].