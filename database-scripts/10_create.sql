create table if not exists moon_tier
(
    moon_tier_id int primary key,
    tier_name    text not null
);

create table if not exists risk_level
(
    risk_level_id   int primary key,
    risk_level_name text not null
);

create table if not exists layout
(
    layout_id   int primary key,
    layout_name text not null
);

create table if not exists weather
(
    weather_id   int primary key,
    weather_name text not null,
    effect       text
);

create table if not exists moon
(
    moon_id             int primary key,
    moon_name           text not null,
    risk_level_id       int  not null,
    cost                int  not null,
    default_layout_id   int  not null,
    map_size_multiplier real not null,
    min_scrap           int  not null,
    max_scrap           int  not null,
    outside_max_power   int  not null,
    inside_max_power    int  not null,
    moon_tier_id        int  not null,
    foreign key (risk_level_id)
        references risk_level (risk_level_id),
    foreign key (default_layout_id)
        references layout (layout_id),
    foreign key (moon_tier_id)
        references moon_tier (moon_tier_id)
);

create table if not exists creature_type
(
    creature_type_id int primary key,
    type_name        text not null
);

create table if not exists creature
(
    creature_id       int primary key,
    creature_name     text not null,
    creature_nickname text,
    health            int,
    power_level       int  not null,
    max_spawn         int  not null,
    stunnable         int  not null,
    stun_multiplier   real,
    door_open_speed   real,
    hostile           int  not null,
    creature_type_id  int  not null,
    favorite_moon_id  int  not null,
    foreign key (creature_type_id)
        references creature_type (creature_type_id),
    foreign key (favorite_moon_id)
        references moon (moon_id)
);

create table if not exists scrap
(
    scrap_id   int primary key,
    scrap_name text not null,
    min_value  int  not null,
    max_value  int  not null,
    weight     int  not null,
    conductive int  not null,
    two_handed int  not null
);

create table if not exists viable_weather
(
    moon_id    int not null,
    weather_id int not null,
    foreign key (moon_id)
        references moon (moon_id),
    foreign key (weather_id)
        references weather (weather_id)
);

create table if not exists spawn_chance
(
    moon_id      int  not null,
    creature_id  int  not null,
    spawn_chance real not null,
    foreign key (moon_id)
        references moon (moon_id),
    foreign key (creature_id)
        references creature (creature_id)
);
