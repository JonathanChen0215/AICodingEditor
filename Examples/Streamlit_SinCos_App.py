# -*- coding: utf-8 -*-
"""AICodingEditor V0.1.33 Streamlit package auto-install test.
Open this saved Python file and click Streamlit.
When Streamlit or pandas are missing, AICodingEditor automatically runs:
    uv pip install streamlit pandas
in the selected Python / uv environment, then starts this page.
"""

import math
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Sin / Cos Monitor", layout="wide")
st.title("Sin / Cos Streamlit Test")
st.caption("AICodingEditor V0.1.33 can automatically prepare uv, Streamlit and pandas.")

interval_ms = st.slider("Sample interval (ms)", 50, 1000, 200, 50)
cycles = st.slider("Cycles", 1, 10, 2)

samples = list(range(0, 360 * cycles))
time_s = [x * (interval_ms / 1000.0) for x in samples]
df = pd.DataFrame({
    "time_s": time_s,
    "x_degree": [x % 360 for x in samples],
    "y1_sin": [math.sin(math.radians(x)) for x in samples],
    "y2_cos": [math.cos(math.radians(x)) for x in samples],
})

st.line_chart(df, x="time_s", y=["y1_sin", "y2_cos"], height=420)
st.dataframe(df, use_container_width=True, height=260)
st.download_button("Download CSV", df.to_csv(index=False).encode("utf-8"),
                   "sin_cos_samples.csv", "text/csv")
