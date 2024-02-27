import os
import sqlite3


class Moon:
    def __init__(self, moon_id, name, risk_level, cost, default_layout, map_size_multiplier, min_scrap, max_scrap,
                 outside_max_power, inside_max_power, tier):
        self.id = moon_id
        self.name = name
        self.risk_level = risk_level
        self.cost = cost
        self.default_layout = default_layout,
        self.map_size_multiplier = map_size_multiplier
        self.min_scrap = min_scrap
        self.max_scrap = max_scrap
        self.outside_max_power = outside_max_power
        self.inside_max_power = inside_max_power
        self.tier = tier


def get_connection() -> sqlite3.Connection:
    """Opens a connection to the SQLite3 database at the default path
     or a path provided by an environment variable if one exists.

    :return: A connection to the database as a sqlite3.Connection object
    """
    if os.getenv("DATABASE_FILE"):
        return sqlite3.connect(os.getenv("DATABASE_FILE"))
    else:
        return sqlite3.connect("./scouter.db")


def get_moon_id_by_name(moon_name: str) -> int | None:
    """Queries the database for a moon ID that matches the given name.

    :param moon_name: Moon name as a string
    :return: The moon's ID as an int or None if no moon is found
    """
    with get_connection() as connection:
        cursor = connection.cursor()
        moon_id = cursor.execute(
            "select moon_id "
            "from moon "
            "where moon_name = ? "
            "limit 1;",
            (moon_name,)
        ).fetchone()

        if moon_id:
            return moon_id[0]
        else:
            return None


def get_moon_list() -> list[str] | None:
    """Provides a list of all moon names from the database.

    :return: All moon names as a list of strings or None if no moons are found
    """
    with get_connection() as connection:
        cursor = connection.cursor()
        moons = cursor.execute(
            "select moon_name from moon order by moon_id"
        ).fetchall()

    if moons:
        moons = [moon[0] for moon in moons]
        return moons
    else:
        return None


def get_moon_by_id(moon_id: int) -> Moon | None:
    """Queries the database to create a moon object.

    :param moon_id: Moon ID as int
    :return: A moon object or None if no moon is found
    """
    with get_connection() as connection:
        connection.text_factory = str
        cursor = connection.cursor()

        query = """
        select m.moon_id,
       m.moon_name,
       rl.risk_level_name,
       m.cost,
       l.layout_name,
       m.map_size_multiplier,
       m.min_scrap,
       m.max_scrap,
       m.outside_max_power,
       m.inside_max_power,
       mt.tier_name
from moon as m
         join main.risk_level rl on rl.risk_level_id = m.risk_level_id
         join main.layout l on l.layout_id = m.default_layout_id
         join main.moon_tier mt on mt.moon_tier_id = m.moon_tier_id
where m.moon_id = ?
limit 1;"""

        moon = cursor.execute(
            query,
            (moon_id,)
        ).fetchone()

        if moon:
            return Moon(*moon)
        else:
            return None

print(get_moon_by_id(3).default_layout)