from datetime import date

import plotly.graph_objs as go
import streamlit as st

from datas.holidays import data
from packages.yahoo.VIXData import VIXDataFromDD

st.set_page_config(page_title="VIXローソク足チャート", layout="wide")

period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())

fill_on = st.sidebar.checkbox("ボリンジャーバンド背景色ON")
if fill_on:
    fill_on = "tonexty"
else:
    fill_on = None

df = VIXDataFromDD(period, end_day)
fig = go.Figure()
fig.add_trace(
    go.Candlestick(
        name="price",
        x=df.index,
        open=df.Open,
        high=df.High,
        low=df.Low,
        close=df.Close,
        increasing_line_color="darkgreen",
        decreasing_line_color="red",
    )
)
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
    title="VIXローソク足チャート",
    yaxis_title="VIX",
    font_size=20,
)
fig.update_xaxes(
    rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=data)]  # hide weekends
)

st.plotly_chart(fig, use_container_width=True)
