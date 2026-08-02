
import streamlit as st
import pandas as pd
import sys

sys.path.append("/content/drive/MyDrive/GeoShield_Project")

import config
from pipeline.loader import load_dataset

st.set_page_config(
    page_title="GeoShield",
    page_icon="🌍",
    layout="wide"
)

df = load_dataset("drought", config.DATA)

st.title("🌍 GeoShield")

st.caption("National Geospatial Intelligence Platform")
