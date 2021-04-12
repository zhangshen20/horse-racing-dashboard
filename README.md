# horse-racing-dashboard

## Purpose

This solution will horse racing dashboard. Information included are
- Jockey
- Runner History - Finishing Position, Margin, Starting Odds

## Installation

- Download the source by _git clone url_
- Deploy the application to a website provider.

## Deployment Steps (heroku)

- mkdir web_app
- cp -R data myapp myapp.py wrangling_scripts web_app/.
- python -m venv --without-pip horseracing
- source horseracing/bin/activate
- curl https://bootstrap.pypa.io/get-pip.py | python
- deactivate
- source horseracing/bin/activate
- which pip
- pip install --upgrade pip
- pip install flask pandas plotly gunicorn
- curl https://cli-assets.heroku.com/install-ubuntu.sh | sh https://devcenter.heroku.com/articles/heroku-cli#standalone-installation 
- heroku --version
- heroku login --interactive
- cd web_app/
- touch Procfile and then open the file to add 'web gunicorn worldbank:app'
- pip freeze > requirements.txt
- git init
- git add .
- git commit -m "first commit"
- heroku create horse-racing-dashboard
- git remote -v
- git push heroku master

## Note

This dashboard is still developing.
