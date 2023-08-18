import streamlit as st
import re

st.header("米国相場各種チャート簡易版")
st.markdown(
	'''
	米国株のティッカーを入力すると以下のチャートを見ることができます。
	- 株価ローソク足チャート
	
	VIXのチャートを見ることができます。
	- VIXラインチャート
	- VIXローソク足チャート
	
	WTI原油先物のチャートを見ることができます。
	- WTI原油先物チャート
	'''
)

rep = r"^[a-zA-Z]{1,5}$"
ticker = ""

if "ticker" not in st.session_state:
	st.session_state.ticker = ""

ticker = st.text_input("ティッカー", max_chars=5)

if re.match(rep, ticker):
	st.session_state.ticker = ticker #値の更新
	st.subheader(f"{ticker.upper()}の各種チャートを表示します")
else:
	st.write("ティッカーを入力してください")
