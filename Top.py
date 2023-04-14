import streamlit as st
import re

st.header("米国相場各種チャート")
st.markdown(
	'''
	米国株のティッカーを入力すると以下のチャートを見ることができます。
	1. 株価ローソク足チャート
	2. RSIチャート
	3. MACDチャート
	4. MACD売買シグナル
	5. ストキャスティクス
	6. VIXラインチャート
	7. VIXローソク足チャート
	8. WTI原油先物チャート
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
