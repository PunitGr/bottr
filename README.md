# bottr
Bottr Test

## Basic Setup
```
git clone git@github.com:PunitGr/bottr.git
cd bottr
sudo easy_install pip
pip install virtualenv
pip install virtualenvwrapper
source virtualenvwrapper.sh
mkvirtualenv --python=/usr/local/bin/python3 bottr
```

## Install packages
```
workon bottr
(bottr)$ pip install -r requirements.txt
```

## Start django server
Run `./manage.py runserver`
