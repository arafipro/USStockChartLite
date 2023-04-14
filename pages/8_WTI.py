from datetime import date

import plotly.graph_objs as go
import streamlit as st

from packages.indicators import RSI
from packages.yahoo.WTIData import WTIDataFromDD

st.set_page_config(page_title="WTI", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())

df = WTIDataFromDD(period, end_day)

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df.Close))
fig.add_vrect(
    x0=vrect_x0,
    x1=vrect_x1,
    fillcolor="#333333",
    opacity=0.1,
    layer="below",
    line_width=0,
)
fig.update_layout(
    xaxis_rangeslider_visible=False,
    width=1200,
    height=800,
    title="WTI",
    yaxis_title="WTI",
    font_size=20,
)

st.plotly_chart(fig, use_container_width=True)
