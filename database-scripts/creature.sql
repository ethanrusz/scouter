insert into main.creature (creature_id, creature_name, creature_nickname, health, power_level, max_spawn, stunnable, stun_multiplier, door_open_speed, hostile, creature_type_id, favorite_moon_id)
values  (1, 'Snare Flea', 'Head Bug', 2, 1, 4, 1, 3, 4.35, 1, 2, 2),
        (2, 'Bunker Spider', null, 5, 3, 1, 1, 1, 6.67, 1, 2, 1),
        (3, 'Hoarding Bug', 'Yippee Bug', 2, 1, 8, 1, 0.5, 0.67, 1, 2, 2),
        (4, 'Bracken', 'Flower Man', 3, 3, 1, 1, 0.25, 0.8, 1, 2, 3),
        (5, 'Thumper', null, 4, 3, 4, 1, 1, 3.33, 1, 2, 4),
        (6, 'Hygrodere', 'Goo', null, 1, 2, 1, 4, 0, 1, 2, 4),
        (7, 'Ghost Girl', null, null, 2, 1, 0, null, 0.25, 1, 3, 6),
        (8, 'Spore Lizard', null, null, 1, 2, 1, 0.6, 3.33, 1, 2, 1),
        (9, 'Nutcracker', null, 5, 1, 10, 1, 0.5, 0.5, 1, 2, 6),
        (10, 'Coil-Head', null, null, 1, 5, 1, 3.25, 16.67, 1, 2, 4),
        (11, 'Jester', null, null, 3, 1, 1, 0.6, 2, 1, 2, 6),
        (12, 'Masked', 'Mimic', 4, 1, 10, 1, 0.75, 0.25, 1, 3, 6),
        (13, 'Eyeless Dog', null, 12, 2, 8, 1, 0.7, null, 1, 1, 8),
        (14, 'Forest Keeper', 'Giant', null, 3, 3, 1, 1.2, null, 1, 1, 3),
        (15, 'Earth Leviathan', 'Worm', null, 2, 3, 0, null, null, 1, 1, 2),
        (16, 'Baboon Hawk', null, 6, 1, 15, 1, 0.4, null, 1, 1, 5),
        (17, 'Circuit Bees', null, null, 1, 6, 0, null, null, 1, 1, 5),
        (18, 'Manticoil', null, 2, 1, 16, 1, 1.1, null, 0, 1, 4),
        (19, 'Roaming Locusts', null, null, 1, 16, 0, null, null, 0, 1, 1);