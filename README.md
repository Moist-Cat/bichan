# Instructions

1. Create python virtual environment called `env` and install dependencies listed in requirements.txt
2. Set the environment variables in env/bin/activate appending something like the following
```
export PYTHONPATH=[path_to_root]/src
export DJANGO_SECRET_KEY="django-insecure-#f^h--ptebip*s!2yf^+3ioh*-2v@m#uu2zr0ryrqpj^n9tp59"
export DJANGO_SETTINGS_MODULE="bichan.settings.dev"

export DATABASE_NAME="bichan"
export DATABASE_USER="bichan"
export DATABASE_PASSWORD="bichan"
export DATABASE_PORT=5432
```
3. Configure the database using the credentials set in the environment
4. Run `./bichan migrate`
5. Run `./bichan runserver`
6. If everything is working, create a superuser
7. Login at http://127.0.0.1:8000/fgsgf/
8. Add an user (or yourself) to a group called either "CEO" or "ECON"
9. Go to http://127.0.0.1:8000/view to visualize the data

# To load data
1. Convert the xls file to csv.
2. Name it in.csv
3. Run `python parse.py`
4. Make sure you are inside the environment and run `python load.py`
