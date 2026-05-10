import streamlit as st
import plotly.graph_objects as go
from services.data_service import get_stock_data, get_market_metrics
from services.sentiment_service import get_news_sentiment

st.set_page_config(layout="wide")
st.title("Market Insights Dashboard")

ticker = st.sidebar.text_input("Enter Ticker", value="AAPL")

if st.sidebar.button("Analyze"):
    # Fetch Data
    with st.spinner('Loading...'):
        df = get_stock_data(ticker)
        sentiment = get_news_sentiment(ticker)
        metrics = get_market_metrics(ticker)

    # Dashboard Layout
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(f"{ticker} Performance")
        fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Sentiment Analysis")
        st.metric("Overall Sentiment", sentiment['sentiment'], delta=sentiment['score'])
        for headline in sentiment['headlines']:
            st.write(f"- {headline}")

    st.write("Market Overview:", metrics.get('summaryProfile', 'N/A'))
