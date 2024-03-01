import streamlit as st
import database as db


class Run:
    def __init__(self, moon: db.Moon):
        self.moon: db.Moon = moon
        self.inside_power: int = moon.inside_max_power
        self.outside_power: int = moon.outside_max_power


def main():
    st.set_page_config("Lethal Company Scouter", "🛰️")

    st.markdown("# :red[Lethal Company] Scouter")
    st.markdown(":rainbow[What does the scouter say about this moon's power level?]")

    moon_name = st.selectbox(
        "Moon",
        db.get_moon_list(),
        placeholder="Moon! Pick a moon!",
        help="Pick your current moon.",
    )
    moon_id: int = db.get_moon_id_by_name(moon_name)
    run: Run = Run(db.get_moon_by_id(moon_id))

    st.markdown(f"## {run.moon.name} ({run.moon.tier})")

    st.write(run)
    st.write(run.moon)

    # Begin column layout
    creatures = db.get_spawnable_inside_creature_ids(run.moon.moon_id)
    for creature in creatures:
        st.write(db.get_creature_by_id(creature))

    st.markdown('## Scrap Lookup')

    scrap_name = st.selectbox(
        'Scrap',
        db.get_scrap_list(),
        placeholder='Select a scrap name!'
    )
    scrap_id: int = db.get_scrap_id_by_name(scrap_name)
    scrap: db.Scrap = db.get_scrap_by_id(scrap_id)

    st.write(scrap)


if __name__ == "__main__":
    main()
