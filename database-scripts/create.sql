create table creature_type
(
    creature_type_id int,
    type_name        text not null,
    primary key (creature_type_id)
);

create table layout
(
    layout_id   int,
    layout_name text not null,
    primary key (layout_id)
);

create table moon_tier
(
    moon_tier_id int,
    tier_name    text not null,
    primary key (moon_tier_id)
);

create table risk_level
(
    risk_level_id   int,
    risk_level_name text not null,
    primary key (risk_level_id)
);

create table moon
(
    moon_id             int,
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
    primary key (moon_id),
    foreign key (risk_level_id) references risk_level,
    foreign key (default_layout_id) references layout,
    foreign key (moon_tier_id) references moon_tier
);

create table creature
(
    creature_id       int,
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
    primary key (creature_id),
    foreign key (creature_type_id) references creature_type,
    foreign key (favorite_moon_id) references moon
);

create table scrap
(
    scrap_id   int,
    scrap_name text not null,
    min_value  int  not null,
    max_value  int  not null,
    weight     int  not null,
    conductive int  not null,
    two_handed int  not null,
    primary key (scrap_id)
);

create table spawn_chance
(
    moon_id      int  not null,
    creature_id  int  not null,
    spawn_chance real not null,
    foreign key (moon_id) references moon,
    foreign key (creature_id) references creature
);

create table weather
(
    weather_id   int,
    weather_name text not null,
    effect       text,
    primary key (weather_id)
);

create table viable_weather
(
    moon_id    int not null,
    weather_id int not null,
    foreign key (moon_id) references moon,
    foreign key (weather_id) references weather
);


