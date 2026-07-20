# -*- coding: utf-8 -*-
"""
AICodingEditor Streamlit infinite Sin / Cos monitor
---------------------------------------------------
- x loops continuously: 0, 1, ..., 359, 0, ...
- One new sample is created every 0.2 seconds.
- y1 = sin(x), y2 = cos(x), where x is in degrees.
- Stop methods:
  1. Click Stop in the Streamlit page.
  2. Press ESC in the Streamlit page (Stop button shortcut).
  3. Press Ctrl+C in CMD / Terminal.
  4. In AICodingEditor, click the Stop button to end the Streamlit server.

Each sample prints one AICE_VAR line, so AICodingEditor's Live Variable Monitor
can save each row independently and draw the continuous time waveform.
"""

import math
from datetime import datetime

import pandas as pd
import streamlit as st

SAMPLE_INTERVAL_SECONDS = 0.2


def initialize_session_state() -> None:
    """Create persistent data storage for the current Streamlit browser session."""
    defaults = {
        "streaming": True,            # Start immediately when the app opens.
        "sample_index": 0,
        "records": [],
        "started_at": datetime.now(),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def start_streaming() -> None:
    """Resume sampling without deleting existing history."""
    st.session_state.streaming = True


def stop_streaming() -> None:
    """Stop automatic sampling; existing data remains visible and downloadable."""
    st.session_state.streaming = False


def reset_history() -> None:
    """Clear all current browser-session samples and restart x from zero."""
    st.session_state.sample_index = 0
    st.session_state.records = []
    st.session_state.started_at = datetime.now()


def append_one_sample() -> None:
    """Append exactly one independent sample row."""
    sample = st.session_state.sample_index
    x_degree = sample % 360
    time_s = sample * SAMPLE_INTERVAL_SECONDS

    y1_sin = math.sin(math.radians(x_degree))
    y2_cos = math.cos(math.radians(x_degree))

    record = {
        "sample": sample,
        "time_s": round(time_s, 3),
        "x_degree": x_degree,
        "y1_sin": round(y1_sin, 6),
        "y2_cos": round(y2_cos, 6),
    }
    st.session_state.records.append(record)
    st.session_state.sample_index += 1

    # AICodingEditor V0.1.27+ captures this as one independent row:
    # sample, time_s, x_degree, y1_sin, y2_cos are separate columns.
    print(
        "AICE_VAR "
        f"sample={record['sample']} "
        f"time_s={record['time_s']:.3f} "
        f"x_degree={record['x_degree']} "
        f"y1_sin={record['y1_sin']:.6f} "
        f"y2_cos={record['y2_cos']:.6f}",
        flush=True,
    )


def records_dataframe() -> pd.DataFrame:
    """Return all samples without discarding earlier periods."""
    columns = ["sample", "time_s", "x_degree", "y1_sin", "y2_cos"]
    return pd.DataFrame(st.session_state.records, columns=columns)


initialize_session_state()

st.set_page_config(page_title="Infinite Sin / Cos Monitor", layout="wide")
st.title("Infinite Sin / Cos Monitor")
st.caption(
    "x continuously cycles from 0 to 359 degrees. "
    "A new independent sample is generated every 0.2 seconds."
)

control_left, control_middle, control_right, status_column = st.columns([1, 1, 1, 2])

with control_left:
    st.button(
        "Start / Resume",
        on_click=start_streaming,
        disabled=st.session_state.streaming,
        use_container_width=True,
        type="primary",
    )

with control_middle:
    # ESC is a native Streamlit keyboard shortcut for this button.
    st.button(
        "Stop (Esc)",
        on_click=stop_streaming,
        disabled=not st.session_state.streaming,
        use_container_width=True,
        shortcut="Esc",
    )

with control_right:
    st.button(
        "Reset History",
        on_click=reset_history,
        use_container_width=True,
    )

with status_column:
    state = "RUNNING" if st.session_state.streaming else "STOPPED"
    st.metric("Status", state)
    st.caption(
        "Ctrl+C ends the Streamlit server in CMD / Terminal. "
        "AICodingEditor's Stop button also stops the server."
    )

run_every = SAMPLE_INTERVAL_SECONDS if st.session_state.streaming else None


@st.fragment(run_every=run_every)
def render_live_monitor() -> None:
    """
    Streamlit reruns this fragment every 0.2 seconds while streaming is enabled.
    Every rerun appends one new row and preserves all earlier rows.
    """
    if st.session_state.streaming:
        append_one_sample()

    df = records_dataframe()

    if df.empty:
        st.info("No samples yet. Click Start / Resume to begin.")
        return

    st.line_chart(
        df,
        x="time_s",
        y=["y1_sin", "y2_cos"],
        height=430,
    )

    latest = df.iloc[-1]
    metric_1, metric_2, metric_3, metric_4 = st.columns(4)
    metric_1.metric("Samples", f"{len(df):,}")
    metric_2.metric("Latest x (degree)", int(latest["x_degree"]))
    metric_3.metric("Latest sin(x)", f"{latest['y1_sin']:.6f}")
    metric_4.metric("Latest cos(x)", f"{latest['y2_cos']:.6f}")

    st.caption(
        "The chart uses continuous elapsed time (time_s) on the X-axis. "
        "The longer the program runs, the longer the chart becomes."
    )
    st.dataframe(df, use_container_width=True, height=260)

    csv_data = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "Download all samples as CSV",
        data=csv_data,
        file_name="infinite_sin_cos_samples.csv",
        mime="text/csv",
        use_container_width=False,
    )


render_live_monitor()
