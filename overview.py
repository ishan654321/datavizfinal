import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
#There will be overview related viz.
def overview():
    html_files = {
    "Dataset Overview": "weather_events_dashboard.html",
    "Weather Timeline": "weather_animation.html",
    "Foggy Days": "city_fog_percent (1).html",
    "Rainy Days": "city_rain_percent (1).html",
    "Weather Clusters": "weather_cluster_distribution.html"
    # add more as needed…
    }

    for section, path in html_files.items():
        st.header(section)
        html = Path(path).read_text(encoding="utf-8")
        components.html(html, height=800, scrolling=True)
    st.header('Values in Cluster')
    st.image('Screenshot 2025-04-28 213043.png')