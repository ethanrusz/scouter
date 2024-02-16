import streamlit as st


class Moon:
    def __init__(self, name, tier, inside_max_power, outside_max_power):
        self.name = name
        self.tier = tier
        self.inside_max_power = inside_max_power
        self.outside_max_power = outside_max_power


class Creature:
    def __init__(self, name, nickname, power, max_spawns, hits_to_kill):
        self.name = name
        self.nickname = nickname
        self.power = power
        self.max_spawns = max_spawns
        self.hits_to_kill = hits_to_kill


class Run:
    def __init__(self, moon):
        self.moon = moon
        self.inside_power = moon.inside_max_power
        self.outside_power = moon.outside_max_power


def find_spawnlist(remaining_power: int, creatures: list[Creature]) -> list[str]:
    """
    Given a run, return all possible spwns for location.

    :param remaining_power: The remaining power in the current location.
    :return: A list of all creatures that may still spawn.
    """
    return sorted(
        [creature.name for creature in creatures if creature.power <= remaining_power]
    )


def main():
    st.set_page_config("Lethal Company Scouter", "🛰️")

    moons = [
        # Tier 1
        Moon("Experimentation", 1, 4, 8),
        Moon("Assurance", 1, 6, 8),
        Moon("Vow", 1, 7, 6),
        # Tier 2
        Moon("Offense", 2, 12, 12),
        Moon("March", 2, 14, 12),
        # Tier 3
        Moon("Rend", 3, 10, 6),
        Moon("Dine", 3, 15, 6),
        Moon("Titan", 3, 18, 7),
    ]

    outside_creatures = [
        Creature("Baboon Hawk", None, 1, 15, 6),
        Creature("Circuit Bees", None, 1, 6, None),
        Creature("Eyeless Dog", None, 2, 8, 12),
        Creature("Forest Keeper", "Giant", 3, 3, None),
        Creature("Earth Leviathan", "Worm", 2, 3, None),
        # Hybrid
        Creature("Outside Ghost Girl ", None, 2, 1, None),
        Creature("Outside Masked", None, 1, 10, 4),
    ]

    inside_creatures = [
        Creature("Bracken", "Freddy Fazbear", 3, 1, 6),
        Creature("Bunker Spider", None, 3, 1, 6),
        Creature("Coil Head", None, 1, 5, None),
        Creature("Hoarding Bug", "Yippee Bug", 1, 8, 3),
        Creature("Hygrodere", "Goo", 1, 2, None),
        Creature("Jester", None, 3, 1, None),
        Creature("Nutcracker", None, 1, 10, 5),
        Creature("Snare Flea", "Head. Bug.", 1, 4, 3),
        Creature("Spore Lizard", None, 1, 2, None),
        Creature("Thumper", None, 2, 4, 4),
        # Hybrid
        Creature("Inside Ghost Girl", None, 2, 1, None),
        Creature("Inside Masked", None, 1, 10, 4),
    ]

    st.markdown("# :red[Lethal Company] Scouter")
    st.markdown(":rainbow[What does the scouter say about this moon's power level?]")

    moon = st.selectbox(
        "Moon",
        sorted(m.name for m in moons),
        placeholder="Moon! Pick a moon!",
        help="Pick your current moon.",
    )

    run = Run(next(m for m in moons if m.name is moon))

    st.markdown(f"## {run.moon.name} (Tier {run.moon.tier})")

    # Begin column layout
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("### Outside")

        with st.form("outside"):
            for creature in outside_creatures:
                moon_max = min(
                    creature.max_spawns, run.moon.outside_max_power // creature.power
                )
                if moon_max > 0:
                    st.slider(
                        creature.name,
                        0,
                        moon_max,
                        key=creature.name,
                        help=creature.nickname,
                    )
                else:
                    st.slider(
                        creature.name,
                        0,
                        1,
                        key=creature.name,
                        help=creature.nickname,
                        disabled=True,
                    )

                run.outside_power = run.outside_power - st.session_state[creature.name]

            outside_submit = st.form_submit_button("Calculate")
            if outside_submit:
                st.info(f"Maximum power: {run.moon.outside_max_power}")
                if run.outside_power >= 0:
                    st.warning(f"🌳 Outside power remaining: {run.outside_power}")
                    st.write(find_spawnlist(run.outside_power, outside_creatures))
                else:
                    st.error(
                        f"Power level exceedes maximum possible for {run.moon.name}."
                    )

    with right_column:
        st.markdown("### Inside")

        with st.form("inside"):
            for creature in inside_creatures:
                moon_max = min(
                    creature.max_spawns, run.moon.inside_max_power // creature.power
                )
                if moon_max > 0:
                    st.slider(
                        creature.name,
                        0,
                        moon_max,
                        key=creature.name,
                        help=creature.nickname,
                    )
                else:
                    st.slider(
                        creature.name,
                        0,
                        1,
                        key=creature.name,
                        help=creature.nickname,
                        disabled=True,
                    )

                run.inside_power = run.inside_power - st.session_state[creature.name]

            inside_submit = st.form_submit_button("Calculate")
            if inside_submit:
                st.info(f"Maximum power: {run.moon.inside_max_power}")
                if run.inside_power >= 0:
                    st.warning(f"🏭 Inside power remaining: {run.inside_power}")
                    st.write(find_spawnlist(run.inside_power, inside_creatures))
                else:
                    st.error(
                        f"Power level exceedes maximum possible for {run.moon.name}."
                    )


if __name__ == "__main__":
    main()
