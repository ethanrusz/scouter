create table creature_type
(
    creature_type_id int
        primary key,
    type_name        text not null
);

create table layout
(
    layout_id   int
        primary key,
    layout_name text not null
);

create table moon_tier
(
    moon_tier_id int
        primary key,
    tier_name    text not null
);

create table risk_level
(
    risk_level_id   int
        primary key,
    risk_level_name text not null
);

create table moon
(
    moon_id             int
        primary key,
    moon_name           text not null,
    risk_level_id       int  not null
        references risk_level,
    cost                int  not null,
    default_layout_id   int  not null
        references layout,
    map_size_multiplier real not null,
    min_scrap           int  not null,
    max_scrap           int  not null,
    outside_max_power   int  not null,
    inside_max_power    int  not null,
    moon_tier_id        int  not null
        references moon_tier
);

create table creature
(
    creature_id       int
        primary key,
    creature_name     text not null,
    creature_nickname text,
    health            int,
    power_level       int  not null,
    max_spawn         int  not null,
    stunnable         int  not null,
    stun_multiplier   real,
    door_open_speed   real,
    hostile           int  not null,
    creature_type_id  int  not null
        references creature_type,
    favorite_moon_id  int  not null
        references moon
);

create table scrap
(
    scrap_id   int
        primary key,
    scrap_name text not null,
    min_value  int  not null,
    max_value  int  not null,
    weight     int  not null,
    conductive int  not null,
    two_handed int  not null
);

create table spawn_chance
(
    moon_id      int  not null
        references moon,
    creature_id  int  not null
        references creature,
    spawn_chance real not null
);

create table weather
(
    weather_id   int
        primary key,
    weather_name text not null,
    effect       text
);

create table viable_weather
(
    moon_id    int not null
        references moon,
    weather_id int not null
        references weather
);


