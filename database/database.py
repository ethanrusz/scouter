import os
import sqlite3


class Creature:
    def __init__(self, creature_id: int, creature_name: str, creature_nickname: str, health: int, power_level: int,
                 max_spawn: int, stunnable: int, stun_multiplier: float or None, door_open_speed: float or None,
                 hostile: int, creature_type: str, favorite_moon: str):
        self.creature_id: int = creature_id
        self.creature_name: str = creature_name
        self.creature_nickname: str = creature_nickname
        self.health: int = health
        self.power_level: int = power_level
        self.max_spawn: int = max_spawn
        self.stunnable: bool = bool(stunnable)
        self.stun_multiplier: float = stun_multiplier
        self.door_open_speed: float or None = door_open_speed
        self.hostile: bool = bool(hostile)
        self.creature_type: str = creature_type
        self.favorite_moon: str = favorite_moon


class Moon:
    def __init__(self, moon_id: int, name: str, risk_level: str, cost: int, default_layout: str,
                 map_size_multiplier: float, min_scrap: int, max_scrap: int, outside_max_power: int,
                 inside_max_power: int, tier: str):
        self.moon_id: int = moon_id
        self.name: str = name
        self.risk_level: str = risk_level
        self.cost: int = cost
        self.default_layout: str = default_layout
        self.map_size_multiplier: float = map_size_multiplier
        self.min_scrap: int = min_scrap
        self.max_scrap: int = max_scrap
        self.outside_max_power: int = outside_max_power
        self.inside_max_power: int = inside_max_power
        self.tier: str = tier


class Scrap:
    def __init__(self, scrap_id: int, name: str, min_value: int, max_value: int, weight: int, conductive: int,
                 two_handed: int):
        self.scrap_id: int = scrap_id
        self.name: str = name
        self.min_value: int = min_value
        self.max_value: int = max_value
        self.weight: int = weight
        self.conductive: bool = bool(conductive)
        self.two_handed: bool = bool(two_handed)


def get_connection() -> sqlite3.Connection:
    """Opens a connection to the SQLite3 database at the default path
     or a path provided by an environment variable if one exists.

    :return: A connection to the database as a sqlite3.Connection object
    """
    if os.getenv("DATABASE_FILE"):
        return sqlite3.connect(os.getenv("DATABASE_FILE"))
    else:
        return sqlite3.connect("./scouter.db")


def get_creature_by_id(creature_id: int) -> Creature or None:
    with get_connection() as connection:
        cursor = connection.cursor()

        query = """
        select c.creature_id,
       c.creature_name,
       c.creature_nickname,
       c.health,
       c.power_level,
       c.max_spawn,
       c.stunnable,
       c.stun_multiplier,
       c.door_open_speed,
       c.hostile,
       ct.type_name,
       m.moon_name
from creature as c
         join main.creature_type ct on c.creature_type_id = ct.creature_type_id
         join main.moon m on c.favorite_moon_id = m.moon_id
where creature_id = ?
limit 1;
"""

        creature = cursor.execute(
            query,
            (creature_id,)
        ).fetchone()

        if creature:
            return Creature(*creature)
        else:
            return None


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
        moon_names = cursor.execute(
            "select moon_name "
            "from moon "
            "order by moon_id;"
        ).fetchall()

    if moon_names:
        return [moon[0] for moon in moon_names]
    else:
        return None


def get_moon_by_id(moon_id: int) -> Moon | None:
    """Queries the database to create a moon object.

    :param moon_id: Moon ID as int
    :return: A moon object or None if no moon is found
    """
    with get_connection() as connection:
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
limit 1;
"""

        moon = cursor.execute(
            query,
            (moon_id,)
        ).fetchone()

        if moon:
            return Moon(*moon)
        else:
            return None


def get_scrap_list() -> list[str] | None:
    """Provides a list of all scrap names from the database.

    :return: All scrap names as a list of strings or None if no scrap is found
    """
    with get_connection() as connection:
        cursor = connection.cursor()
        scrap_names = cursor.execute(
            "select scrap_name from scrap order by scrap_id"
        )

        if scrap_names:
            scrap_names = [scrap[0] for scrap in scrap_names]
            return scrap_names
        else:
            return None


def get_scrap_id_by_name(scrap_name: str) -> int | None:
    """Queries the database for a scrap ID that matches the given name.

    :param scrap_name: Moon name as a string
    :return: The scrap's ID as an int or None if no scrap is found
    """
    with get_connection() as connection:
        cursor = connection.cursor()
        scrap_id = cursor.execute(
            "select scrap_id "
            "from scrap "
            "where scrap_name = ? "
            "order by scrap_name "
            "limit 1;",
            (scrap_name,)
        ).fetchone()

        if scrap_id:
            return scrap_id[0]
        else:
            return None


def get_scrap_by_id(scrap_id: int) -> Scrap | None:
    with get_connection() as connection:
        cursor = connection.cursor()

        query = """
        select s.scrap_id,
       s.scrap_name,
       s.min_value,
       s.max_value,
       s.weight,
       s.conductive,
       s.two_handed
from scrap as s
where scrap_id = ?
limit 1;
"""
        scrap = cursor.execute(
            query,
            (scrap_id,)
        ).fetchone()

        if scrap:
            return Scrap(*scrap)
        else:
            return None


def get_spawnable_inside_creature_ids(moon_id: int) -> list[int] | None:
    with get_connection() as connection:
        cursor = connection.cursor()

        query = """
        select c.creature_id as Creature
from spawn_chance as s
         join main.creature c on s.creature_id = c.creature_id
         join main.moon m on m.moon_id = s.moon_id
         join main.creature_type ct on ct.creature_type_id = c.creature_type_id
where s.moon_id like ?
  and (ct.type_name = 'Inside' or 'Hybrid')
  and s.spawn_chance > 0
order by s.spawn_chance desc;
"""
        creature_ids = cursor.execute(
            query,
            (moon_id,)
        ).fetchall()

        if creature_ids:
            return [creature_id[0] for creature_id in creature_ids]
        else:
            return None
