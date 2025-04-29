import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
def insight():
    html_files = {
    "Severe Events by Year":"extreme_weather_events_by_year.html",
    "Weather Duration Overview": "weather_duration.html",
    "Severe City Fog": "severe_city_fog_gt6.html",
    "Severe City Storm": "severe_city_storm_gt05.html"
    }

    for section, path in html_files.items():
        st.header(section)
        html = Path(path).read_text(encoding="utf-8")
        components.html(html, height=700, width=1000)