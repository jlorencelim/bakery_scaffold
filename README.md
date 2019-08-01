# Product Scaffold 
This is a repository for a trivial challenge scaffold developed with Django contains Stripe checkout page.
### Recommended Installation
1. [Postgresql](https://www.postgresql.org/download/)
2. [Python](https://www.python.org/downloads/release/python-365/)

### Installation
1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd {{cookiecutter.project_slug}}`
3. Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
4. Run `pipenv --python 3.6`
5. Run `pipenv install`
6. Run `cp .env.example .env`
7. Update .env file `DATABASE_URL` with your `database_name`, `database_user`, `database_password`, if you use postgresql. 
    Can alternatively set it to `sqlite:////tmp/my-tmp-sqlite.db`, if you want to use sqlite for local development.


### Getting Started
1. Run `pipenv shell`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`