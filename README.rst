django-db-geventpool
====================

Another DB pool using gevent for PostgreSQL DB.

*Need Django 1.5.x or Django 1.6.x*


Patch psycopg2
--------------

Before using the pool, psycopg2 must be patched with psycogreen, if you are using `gunicorn webserver <http://www.gunicorn.org/>`_,
a good place is the `post_fork()` function at the config file

.. code:: python

   from psycogreen.gevent import patch_psycopg
   
   def post_fork(server, worker):
       patch_psycopg()
       worker.log_info("Made Psycopg2 Green")
       
       
Settings
---------


  * Set `ENGINE` in your database settings to: *'django_db_geventpool.backends.postgresql_psycopg2'*
  * Add `MAX_CONNS` to `OPTIONS` to set the maximun number of connections allowed to database (default=4)
  * If using django 1.6 or newer, add `CONN_MAX_AGE: 0` to settings to disable default django persistent connection feature.

.. code:: python

    # for django 1.5.x
    DATABASES = {
        'default': {
            'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
            'NAME': 'db',           # Or path to database file if using sqlite3.
            'USER': 'postgres',                      # Not used with sqlite3.
            'PASSWORD': 'postgres',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            'OPTIONS': {
                'MAX_CONNS': 20
            }
        }
    }

    # for django 1.6 and newer version, CONN_MAX_AGE must be set to 0, or connections will never go back to the pool
    DATABASES = {
        'default': {
            'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
            'NAME': 'db',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '',
            'PORT': '',
            'ATOMIC_REQUESTS': False,
            'AUTOCOMMIT': True,
            'CONN_MAX_AGE': 0,
            'OPTIONS': {
                'MAX_CONNS': 20
            }
        }
    }


Other pools
------------

* `django-db-pool <https://github.com/gmcguire/django-db-pool>`_
* `django-postgresql <https://github.com/kennethreitz/django-postgrespool>`_
