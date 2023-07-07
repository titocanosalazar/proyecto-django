# proyecto-django

Pasos Para Instalar El Proyecto De Backend

Pasos previos
Tener instalado PyCharm para facilitar las tareas y creación de Django
Tener instalado PostgreSQL


Paso 1
Abrir PyCharm, presionar en new project, dejar las opciones que ya vienen por defecto y presionar en el botón de create.


Paso 2
Cuanto ya tenga el entorno virtual, puede clonar el repositorio que está en GitHub.


https://github.com/titocanosalazar/proyecto-django.git


Paso 3
Así debería tener sus carpetas
.idea
sap
venv



![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/a7677ad3-c997-414a-8dd3-b29797bb534b)




Paso 4
Abrir PostgreSQL y crear una base de datos que se llame sap_db


Paso 5
En la terminal de PyCharm colocar los siguiente comandos:
python manage.py showmigrations
python manage.py migrate
python manage.py sqlmigrate personas 0001
Que servirá para migrar la base de datos del proyecto a PostgreSQL


Paso 6
Para ver que todo funciona de manera correcta puede usar el siguiente comando:
python manage.py runserver
Adjunto capturas:





![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/1cac4d74-d3e3-44ca-982c-fcc4c9f07165)




![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/9f457bf0-869c-4fcd-b8f1-2f9bc8d53cf6)



![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/ecaf51ce-2f88-42e9-b40b-49bc524d1d62)



![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/eaad914e-2fa8-40cf-9ced-3151aaf727e0)






Paso 7
Para crear el super usuario utilice el siguiente comando:
python manage.py createsuperuser



![image](https://github.com/titocanosalazar/proyecto-django/assets/111630034/a5c8b773-b2b7-41a5-b0e3-b8a0a40e69cd)


