<h1 align="center">
    Flights Management App
</h1>

A Django App for managing flights and ticket reservations, with CRUD operations. Project for the third-semester course "Database" (ST0246) taught at EAFIT University by prof Marta Tabares.

## Motivation

The main aim of this project was to apply all the concepts learned in the course, such as relational algebra, SQL, NoSQL and Django. 

Also, creating an app with the Model-View-Controller (MVC) architecture.

## Documentation

**Note:** This project was implemented on SQL and NoSQL databases. You can find the NoSQL version [here](https://github.com/NicoHurtado/Flight_Management)

The documentation for this project can be found [here](https://drive.google.com/drive/folders/19CI_E6QT7CTlOjUZLbPekc22r53T0dgP?usp=sharing). It contains the following:

- Data creation process on MySQL and MongoDB.

- Script used to define and create the model of the database on MySQL Workbench.

- EER diagram of the database.

- Register created on MongoDB.

- A document explaining the development process of the project during the semester.

## Install and Run

1. Clone the repository

```bash
git clone git@github.com:alejoriosm04/flights-management-app.git
```

2. Go to the project directory

```bash
cd flights-management-app
```

3. Create a virtual environment

```bash
python -m venv venv
```

4. Activate the virtual environment

```bash
source venv/bin/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create a .env file and add your database credentials, otherwise the app won't work. *Also, you can uncomment the lines 98-103 on settings.py and comment the lines 83-95 to use SQLite3 (Maybe you will have to build again the Django models).*

```bash
touch .env
```

7. Migrate the database

```bash
python manage.py migrate
```

8. Create a superuser

```bash
python manage.py createsuperuser
```

9. Run the server

```bash
python manage.py runserver
```

10. Go to http://localhost:8000/admin/ and login with the superuser credentials.

## Screenshots

<div align="center">
  <img src='https://i.imgur.com/xjdfUln.png' height='280px'/>
  <img src='https://i.imgur.com/BPkBoZR.png' height='280px'/>
  <img src='https://imgur.com/jEa8qsV.png' height='280px'/>
</div>

## Authors

[Alejandro Ríos](https://github.com/alejoriosm04) and [Nicolás Hurtado](https://github.com/NicoHurtado) developed this project during the semester.

We thank our professor Marta Tabares for her guidance and support during the development of this project.
