# Quriosity-Round_1
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

### Cloning Steps

1. Clone github repo

	`git clone https://github.com/Shivam-316/Quriosity-Round_1.git`

2. Create virtual eniviroment (*I am using pipenv here*) & install all dependencies.

	`pipenv shell`

	`pipenv install -r requirements.txt`

3. Create migration files for **Quiz** & **User** Model.

	`python manage.py makemigrations quiz userProfile`

	`python manage.py migrate`

4. Run server.

	`python manage.py runserver`

Note: Signup Page is to be linked manually.
