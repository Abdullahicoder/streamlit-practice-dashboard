import streamlit as st
import pandas as pd
import numpy as np

# --- Dashboard Title ---
st.title("Simple Practice Dashboard 📊")

st.write("Welcome! This is a simple Streamlit dashboard to practice data visualization.")

# --- Create Sample Data ---
np.random.seed(42)  # for reproducibility
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Score": np.random.randint(50, 100, 5),
    "Risk": np.random.rand(5)
})

# --- Show Data ---
st.subheader("Data Table")
st.dataframe(data)

# --- Chart 1: Bar Chart ---
st.subheader("Scores by Category")
st.bar_chart(data.set_index("Category")["Score"])

# --- Chart 2: Line Chart ---
st.subheader("Risk Line Chart")
st.line_chart(data.set_index("Category")["Risk"])

# --- User Interaction ---
st.subheader("Try it Yourself")
choice = st.selectbox("Pick a category:", data["Category"])
row = data[data["Category"] == choice]

st.write(f"You selected **{choice}**:")
st.write(row)
