import re
from datetime import date

import plotly.graph_objs as go
import streamlit as st

from datas.holidays import data
from packages.yahoo.StockHistoricalData import stockDataFromDD

st.set_page_config(page_title="米国株価チャート", layout="wide")

rep = r"^[a-zA-Z]{1,5}$"

if "ticker" not in st.session_state:
    st.session_state.ticker = ""

if "lines" not in st.session_state:
    st.session_state.lines = []

ticker = st.session_state.ticker
period = st.sidebar.slider("チャートの期間", min_value=1, max_value=5, value=3)
line = st.sidebar.text_input("トレンドライン")
st.session_state.lines.append(line)
print(st.session_state.lines)
if st.sidebar.button("トレンドラインリセット"):
    st.session_state.lines = []
end_day = st.sidebar.date_input("チャートの最終日", date.today())
vrect_x0 = st.sidebar.date_input("強調表示開始日", date.today())
vrect_x1 = st.sidebar.date_input("強調表示終了日", date.today())

fill_on = st.sidebar.checkbox("ボリンジャーバンド背景色ON")
if fill_on:
    fill_on = "tonexty"
else:
    fill_on = None

if re.match(rep, ticker):
    df = stockDataFromDD(ticker, period, end_day)

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
    for line in st.session_state.lines:
        fig.add_hline(y=line, line_width=0.8)
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
        title=f"{ticker.upper()} - 米国株価チャート",
        yaxis_title="USD ($)",
        font_size=20,
    )
    fig.update_xaxes(
        rangebreaks=[dict(bounds=["sat", "mon"]), dict(values=data)]  # hide weekends
    )

    st.plotly_chart(fig, use_container_width=True)
elif ticker == "":
    st.info("トップページでティッカーを入力してください")
