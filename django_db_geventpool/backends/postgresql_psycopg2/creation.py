# coding=utf-8

import django

from django.db.backends.postgresql_psycopg2.creation import DatabaseCreation as OriginalDatabaseCreation


class DatabaseCreationMixin16(object):
    def _create_test_db(self, verbosity, autoclobber):
        self.connection.closeall()
        return super(DatabaseCreationMixin16, self)._create_test_db(verbosity, autoclobber)

    def _destroy_test_db(self, test_database_name, verbosity):
        self.connection.closeall()
        return super(DatabaseCreationMixin16, self)._destroy_test_db(test_database_name, verbosity)


class DatabaseCreationMixin17(object):
    def _create_test_db(self, verbosity, autoclobber):
        self.connection.closeall()
        return super(DatabaseCreationMixin17, self)._create_test_db(verbosity, autoclobber)

    def _destroy_test_db(self, test_database_name, verbosity):
        self.connection.closeall()
        return super(DatabaseCreationMixin17, self)._destroy_test_db(test_database_name, verbosity)


class DatabaseCreationMixin18(object):
    """
    As per Django 1.8 create_test_db needs extra parameter keepdb.
    Without this param './manage.py test' arise error
    """
    def _create_test_db(self, verbosity, autoclobber, keepdb):
        self.connection.closeall()
        return super(DatabaseCreationMixin18, self)._create_test_db(verbosity, autoclobber, keepdb)

    def _destroy_test_db(self, test_database_name, verbosity):
        self.connection.closeall()
        return super(DatabaseCreationMixin18, self)._destroy_test_db(test_database_name, verbosity)


if django.VERSION >= (1, 8):
    class DatabaseCreationMixin(DatabaseCreationMixin18):
        pass
elif (django.VERSION >= (1, 7)) and (django.VERSION < (1, 8)):
    class DatabaseCreationMixin(DatabaseCreationMixin17):
        pass
else:
    class DatabaseCreationMixin(DatabaseCreationMixin16):
        pass


class DatabaseCreation(DatabaseCreationMixin, OriginalDatabaseCreation):
    pass
