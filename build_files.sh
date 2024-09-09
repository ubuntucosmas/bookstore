# Install Python if not already installed
apt-get update
apt-get install -y python3 python3-pip

# Install Python dependencies
pip3 install -r requirements.txt

pip freeze > requirements.txt
python manage.py collectstatic