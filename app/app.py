import hopsworks
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError


@st.cache
def get_data():
    project = hopsworks.login(
            host="2a5f8040-2d0d-11ed-b5c5-c151c2fe58c1.cloud.hopsworks.ai",
            project="electricity",
            api_key_value="xIGaDiwBZpXxLYRQ.SgheZwqHTZteASnO1PtPMC4HMgco2OVD6VK6xZN3sKCy96FQT27rF0JbBuFivTTA",
        )
    fs = project.get_feature_store()

    fg = fs.get_feature_group('se3_daily_predictions')
    return fg.read(online=True)
    
try:
    df = get_data()

    st.write("## SE3 Day ahead price prediction")
    st.write("")
    st.bar_chart(df, x="time", y="price")

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
