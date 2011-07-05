# sets up virtual environments for both test projects

cd `dirname $0`

# django 1.2
cd django_1-2/
virtualenv --no-site-packages venv
venv/bin/pip install -r requirements.txt

cd ../

# django 1.3
cd django_1-3/
virtualenv --no-site-packages venv
venv/bin/pip install -r requirements.txt
