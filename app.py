import streamlit as st
import database as db


class Run:
    def __init__(self, moon):
        self.moon = moon
        self.inside_power = moon.inside_max_power
        self.outside_power = moon.outside_max_power


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
    moon_id = db.get_moon_id_by_name(moon_name)
    run = Run(db.get_moon_by_id(moon_id))

    st.markdown(f"## {run.moon.name} ({run.moon.tier})")

    st.write(run)
    st.write(run.moon)

    # Begin column layout
    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown("### Outside")

    with right_column:
        st.markdown("### Inside")

    st.markdown('## Scrap Lookup')

    scrap_name = st.selectbox(
        'Scrap',
        db.get_scrap_list(),
        placeholder='Select a scrap name!'
    )
    scrap_id = db.get_scrap_id_by_name(scrap_name)
    scrap = db.get_scrap_by_id(scrap_id)

    st.write(scrap)


if __name__ == "__main__":
    main()
