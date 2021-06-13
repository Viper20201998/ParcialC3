# ParcialC3
aplicacion en django

paso 1: sudo git clone https://github.com/Viper20201998/ParcialC3.git

paso 2: cd ParcialC3/

paso 3: docker-compose up

paso 4: sudo docker-compose run parcial_app python locallibrary/manage.py migrate

paso 5: sudo docker-compose run parcial_app python locallibrary/manage.py makemigrations

paso 6: sudo docker-compose run parcial_app python locallibrary/manage.py createsuperuser
ingresar un nombre de usuario
ingresar un correo electronico
ingresar la contraseña que desee

paso 7: sudo docker-compose run parcial_app python locallibrary/manage.py collectstatic

acceder al navegador ingresar url
paso 8: http://localhost:8000/admin
