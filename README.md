# ParcialC3
Aplicacion en django (Python)

Paso 1: sudo git clone https://github.com/Viper20201998/ParcialC3.git

Paso 2: cd ParcialC3/

Paso 3: docker-compose up

Paso 4: sudo docker-compose run parcial_app python locallibrary/manage.py makemigrations

Paso 5: sudo docker-compose run parcial_app python locallibrary/manage.py migrate

Paso 6: sudo docker-compose run parcial_app python locallibrary/manage.py createsuperuser
"Ingresar un nombre de usuario"
"Ingresar un correo electronico"
"Ingresar la contraseña que desee"

Paso 7: sudo docker-compose run parcial_app python locallibrary/manage.py collectstatic

Acceder al navegador ingresar url
Paso 8: http://localhost:8000/admin
