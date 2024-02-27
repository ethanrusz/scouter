import streamlit as st
import database as db


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


def main():
    st.set_page_config("Lethal Company Scouter", "🛰️")

    moon_name = st.selectbox(
        "Moon",
        db.get_moon_list(),
        placeholder="Moon! Pick a moon!",
        help="Pick your current moon.",
    )
    moon_id = db.get_moon_id_by_name(moon_name)
    run = Run(db.get_moon_by_id(moon_id))

    st.markdown(f"## {run.moon.name} ({run.moon.tier})")

    st.info(f"Risk: {run.moon.risk_level} | Min scrap: {run.moon.min_scrap} "
            f"| Max scrap: {run.moon.max_scrap} | Default layout: {run.moon.default_layout}")

    # Begin column layout
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("### Outside")

    with right_column:
        st.markdown("### Inside")


if __name__ == "__main__":
    main()
