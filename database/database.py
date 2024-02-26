import os
import sqlite3


def get_connection() -> sqlite3.Connection:
    if os.getenv("DATABASE_FILE"):
        return sqlite3.connect(os.getenv("DATABASE_FILE"))
    else:
        return sqlite3.connect("./scouter.db")


def get_moon_list() -> list[str] | None:
    with get_connection() as connection:
        cursor = connection.cursor()
        moons = cursor.execute(
            "select moon_name from moon order by moon_id"
        )

    if moons:
        moons = [moon[0] for moon in moons]
        return moons
    else:
        return None
