import streamlit as st


class Moon:
    def __init__(self, name, tier, inside_max_power, outside_max_power):
        self.name = name
        self.tier = tier
        self.inside_max_power = inside_max_power
        self.outside_max_power = outside_max_power


class Creature:
    def __init__(self, name, power, max_spawns, hits_to_kill):
        self.name = name
        self.power = power
        self.max_spawns = max_spawns
        self.hits_to_kill = hits_to_kill


class Run:
    def __init__(self, moon):
        self.moon = moon


def main():
    st.set_page_config('Scouter', '🔎')

    moons = [
        # Tier 1
        Moon('Experimentation', 1, 4, 8),
        Moon('Assurance', 1, 6, 8),
        Moon('Vow', 1, 7, 6),
        # Tier 2
        Moon('Offense', 2, 12, 12),
        Moon('March', 2, 14, 12),
        # Tier 3
        Moon('Rend', 3, 10, 6),
        Moon('Dine', 3, 15, 6),
        Moon('Titan', 3, 18, 7),
    ]

    outside_creatures = [
        Creature('Baboon Hawk', 1, 15, 6),
        Creature('Circuit Bees', 1, 6, None),
        Creature('Eyeless Dog', 2, 8, 12),
        Creature('Forest Keeper', 3, 3, None),
        Creature('Earth Leviathan', 2, 3, None),
        # Hybrid
        Creature('Outside Ghost Girl ', 2, 1, None),
        Creature('Outside Masked', 10, 10, 4),
    ]

    inside_creatures = [
        Creature('Bracken', 3, 1, 6),
        Creature('Bunker Spider', 3, 1, 6),
        Creature('Coil Head', 1, 5, None),
        Creature('Hoarding Bug', 1, 8, 3),
        Creature('Hygrodere', 1, 2, None),
        Creature('Jester', 3, 1, None),
        Creature('Nutcracker', 1, 10, 5),
        Creature('Snare Flea', 1, 4, 3),
        Creature('Spore Lizard', 1, 2, None),
        Creature('Thumper', 2, 4, 4),
        # Hybrid
        Creature('Inside Ghost Girl', 2, 1, None),
        Creature('Inside Masked', 10, 10, 4),
    ]

    st.markdown('# :red[Lethal Company] Scouter')
    st.markdown(":rainbow[What does the scouter say about this moon's power level?]")

    moon = st.selectbox('Moon', sorted(m.name for m in moons),
                        placeholder='Moon! Pick a moon!',
                        help='Pick your current moon.')
    run = Run(next(m for m in moons if m.name is moon))

    st.markdown(f"## {run.moon.name} (Tier {run.moon.tier})")
    column_1, column_2 = st.columns(2)

    with column_1:
        st.markdown('### Outside')
        st.info(f"Maximum power: {run.moon.outside_max_power}")

        for outside_creature in outside_creatures:
            st.slider(outside_creature.name, 0, outside_creature.max_spawns)

    with column_2:
        st.markdown('### Inside')
        st.info(f"Maximum power: {run.moon.inside_max_power}")

        for inside_creature in inside_creatures:
            st.slider(inside_creature.name, 0, inside_creature.max_spawns)


# https://docs.streamlit.io/library/api-reference/session-state


if __name__ == '__main__':
    main()
