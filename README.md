# 米国株個別銘柄各種チャート

## 紹介動画

[![](http://img.youtube.com/vi/rmCL18Jp-9I/0.jpg)](https://www.youtube.com/watch?v=rmCL18Jp-9I)

## 米国株のティッカーを入力すると以下のチャートを見ることができます。

1. 株価ローソク足チャート
2. RSIチャート
3. MACDチャート
4. MACD売買シグナル
5. ストキャスティクス
6. VIXラインチャート
7. VIXローソク足チャート
8. WTI原油先物チャート

## 技術スタック
- Python
- Streamlit
- Plotly

## 使用手順

### Python 仮想環境を作成

以下のコマンドを実行して仮想環境を作成します。

```bash
python3 -m venv .venv
```

### Python 仮想環境を起動

以下のコマンドを実行して仮想環境を起動します。

```bash
# shell zsh
source .venv/bin/activate

# shell fish
source .venv/bin/activate.fish
```

### Python 仮想環境にパッケージをインストール

以下のコマンドを実行して`requirements.txt`にリストされているすべてのパッケージが仮想環境にインストールします。

```bash
pip3 install -r requirements.txt
```

### 起動

以下のコマンドを実行してアプリを起動します。

```bash
streamlit run Top.py
```
