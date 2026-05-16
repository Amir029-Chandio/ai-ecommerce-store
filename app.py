import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI E-Commerce Store", layout="wide")

data = {
    "Product": ["Smart Watch", "Headphones", "Laptop Stand", "USB Hub", "Gaming Mouse"],
    "Category": ["Electronics", "Audio", "Accessories", "Accessories", "Gaming"],
    "Price": [120, 80, 45, 30, 60],
    "Sales": [500, 800, 300, 600, 900],
    "Rating": [4.5, 4.2, 4.0, 3.8, 4.6]
}

df = pd.DataFrame(data)

st.title("🛒 AI E-Commerce SaaS Store")

search = st.text_input("🔍 Search Product")

if search:
    st.dataframe(df[df["Product"].str.lower().str.contains(search.lower())])

st.subheader("🧠 AI Recommendation System")
df["Score"] = df["Price"] * df["Sales"] * df["Rating"]
st.dataframe(df.sort_values("Score", ascending=False))

st.subheader("📊 Sales Chart")
st.bar_chart(df.set_index("Product")["Sales"])