# horse-racing-dashboard

## Purpose

This solution will horse racing dashboard. Information included are
- Jockey
- Runner History - Finishing Position, Margin, Starting Odds

## Installation

- Download the source by _https://github.com/zhangshen20/horse-racing-dashboard.git_
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
- pip install flask pandas plotly gunicorn requests
- curl https://cli-assets.heroku.com/install-ubuntu.sh | sh https://devcenter.heroku.com/articles/heroku-cli#standalone-installation 
- heroku --version
- heroku login --interactive
- cd web_app/
- touch Procfile and then open the file to add 'web gunicorn myapp:app'
- remove 'app.run(host='0.0.0.0', port=3001, debug=True)' from myapp.py
- pip freeze > requirements.txt
- git init
- git add .
- git commit -m "first commit"
- heroku create horse-racing-dashboard
- git remote -v
- git push heroku master

## Web hosted on heroku

https://horse-racing-dashboard.herokuapp.com/

## Note

This dashboard is still being developed.
