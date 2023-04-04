<!---
Migracion de la base de datos a postgresql
-->


$ export FLASK_APP=run.py
$ export FLASK_DEBUG=1


$ flask shell
>>> db.drop_all()
>>> db.create_all()

>>> from WebApp.models import User, Role, HistoricFarmland, SoilFarmland, Unit, Farmland, Crop

>>> role_1 = Role(description = 'Admin')
>>> role_2 = Role(description = 'User')
>>> role_3 = Role(description = 'Ingeniero')
>>> db.session.add(role_1)
>>> db.session.add(role_2)
>>> db.session.add(role_3)
>>> db.session.commit()

>>> crop_1 = Crop(description = 'Soja')
>>> crop_2 = Crop(description = 'Maiz')
>>> crop_3 = Crop(description = 'Trigo')
>>> crop_4 = Crop(description = 'Espinaca')
>>> db.session.add(crop_1)
>>> db.session.add(crop_2)
>>> db.session.add(crop_3)
>>> db.session.add(crop_4)
>>> db.session.commit()

>>> unit_1 = Unit(description = 'ppm')
>>> unit_2 = Unit(description = 'mg/dm3')
>>> unit_3 = Unit(description = 'cmolc/dm3')
>>> db.session.add(unit_1)
>>> db.session.add(unit_2)
>>> db.session.add(unit_3)
>>> db.session.commit()


<!---
Migración para una nueva base de datos
-->



$ flask db init
Creating directory C:\Users\Documents\Python Scripts\Web\migrations ...  done
Creating directory C:\Users\Documents\Python Scripts\Web\migrations\versions ...  done
Generating C:\Users\Documents\Python Scripts\Web\migrations\alembic.ini ...  done
Generating C:\Users\Documents\Python Scripts\Web\migrations\env.py ...  done
Generating C:\Users\Documents\Python Scripts\Web\migrations\README ...  done
Generating C:\Users\Documents\Python Scripts\Web\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\Users\\Documents\\Python Scripts\\Web\\migrations\\alembic.ini' before proceeding.


$ flask db migrate -m "initial migration"

<!---
Si el siguiente mensaje es generado, el script de migración no fue creada
-->

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.env] No changes in schema detected.

<!---
Entonce ejecutar la función migrate de esta forma
-->
$ DATABASE_URL=sqlite:/// flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'crops'
INFO  [alembic.autogenerate.compare] Detected added table 'roles'
INFO  [alembic.autogenerate.compare] Detected added table 'units'
INFO  [alembic.autogenerate.compare] Detected added table 'farmlands'
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added table 'historicfarmlands'
INFO  [alembic.autogenerate.compare] Detected added table 'soilfarmlands'
Generating C:\Users\Documents\Python Scripts\Web\migrations\versions\3e4dc3d3c50f_.py ...  done


<!---
Actualiza los datos y tablas de sqlite a postgres
-->
$ export DATABASE_URL="postgresql://[user]:[password]@localhost:[port]/[db_name]"
$ flask db upgrade

<!---https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application -->

<!---
Para ejecutar el proyecto en un servidor WSGI: En Linux
-->
gunicorn --bind 0.0.0.0:5000 run:app

<!---
Para ejecutar el proyecto en un servidor WSGI: En Windows
-->
waitress-serve --host 127.0.0.1 run:app
waitress-serve --port=8080 run:app
waitress-serve --port 8080 --call "app:create_app"
waitress-serve run:app
<!-- http://localhost:8080/login -->