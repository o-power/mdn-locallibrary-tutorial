## Setting up a development environment

Virtual Environment
venv for Python 3 or virtualenv for Python 2.
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
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