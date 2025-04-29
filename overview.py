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
    st.header('Problems in Overview:')
    st.markdown('''- It was a huge amount of data and to deal with it was big challenge.
- Colab, Kaggle, Jupyter notebook was not helpful when we tried to load 8.6 millions of rows with 1.1 GB size of csv file into data frame. 
The visualizations were taking even longer time to generate.
- The dataset lacks the event descriptions like hurricane or storm passing area and how affected the area was.
- The dataset is also between limited years 2016 to 2022 which could be insufficient to predict climate change or any such changes.
''')
