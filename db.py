import pymysql

import click
from flask import current_app
from flask import g


def get_db():
   
   # Connect to the database
    if "db" not in g:
        g.db = pymysql.connect(host='39.101.185.8',
                                    user='appcmdb',
                                    password='Zh@1024*',
                                    database='appcma',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    
    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()


@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    #app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
