# IMDB Clone
## A movie and celebrity info website.

there are screenshots here.

## Used technology:
Django, Django Rest Framework and Vue.js via CDN (No npm or webpack configuration is needed! It is like a usual django website.) Vue is used for visitor pages.

# Please follow the process below to install

1. Clone this repository (use `git clone ...`)

### setting up a development environment
2. start an environment with requirements
   e.g. pipenv install -r <project-folder>/requirements.txt

### migrating the already defined models and creating the super user
3. python manage.py migrate

### super user should be created before the dummy data be loaded!
4. python manage.py createsuperuser

### loading dummy data
5. python manage.py loaddata data.json

P.S: you may follow the process as the ordering defined or there may be problems with user related data

# TODOs:
1. Registration and login
2. Image upload in vue part.
3. Watchlist, favorites and rankings
4. Comments