import sqlite3
from sqlite3 import Connection

import click
from flask import Flask, current_app, g


def get_db() -> Connection:
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None) -> None:
    db: Connection = g.pop("db", None)

    if db is not None:
        db.close()


def init_db() -> None:
    db = get_db()

    with current_app.open_resource("schema.sql", "r") as f:
        db.executescript(f.read())


def drop_db() -> None:
    db = get_db()

    # Disable foreign key checks
    db.execute('PRAGMA foreign_keys = OFF')

    # Get All the Tables
    tables = db.execute(
        'SELECT name' 
        ' FROM sqlite_master' 
        ' WHERE type=?',
        ('table',),
    ).fetchall()
    
    # Drop every table 
    for table in tables:
        table_name = table[0]
        if table_name == 'sqlite_sequence':             #? Skip this table
            continue
        
        db.execute(f"DROP TABLE IF EXISTS {table[0]}")
    
    # Commit changes and re-enable foreign key checks
    db.commit()
    db.execute('PRAGMA foreign_keys = ON')


def insert_fake_data() -> None:
    db = get_db()
    
    # Disable foreign key checks
    db.execute('PRAGMA foreign_keys = OFF')

    with current_app.open_resource("fake_data.sql", "r") as f:
        db.executescript(f.read())
    
    # Commit changes and re-enable foreign key checks
    db.commit()
    db.execute('PRAGMA foreign_keys = ON')

#? COMMAND to interact with Database
@click.command("init-db")
def init_db_command() -> None:
    # Create new tables
    init_db()
    click.echo("Initialized the database.")


@click.command("drop-db")
def drop_db_command() -> None:
    # Clear the existing data
    drop_db()
    click.echo("Dropped all the tables in the database.")


@click.command("insert-db")
def insert_fake_data_command() -> None:
    # Insert the fake data into database
    insert_fake_data()
    click.echo("Inserted fake data into the database.")


@click.command("reset-db")
def reset_db_command() -> None:
    # Drop the database
    drop_db()
    
    # Init the database
    init_db()
    
    # Insert Fake data
    insert_fake_data()
    click.echo("Reset the database to the initial phase.")

def init_app(app: Flask) -> None:
    app.app_context().push()
    
    # Add A new command that can be called with the `flask` command
    app.cli.add_command(init_db_command)
    app.cli.add_command(drop_db_command)
    app.cli.add_command(insert_fake_data_command)
    
    app.cli.add_command(reset_db_command)
    
    # Close the Database (If Needed)
    close_db()