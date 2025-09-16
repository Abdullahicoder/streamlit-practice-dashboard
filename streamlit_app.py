import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import kagglehub  # to fetch the dataset

# --- Title & Intro ---
st.title("Iris Dataset Report 🌸")
st.markdown("""
This report explores the **Iris dataset** using interactive visualizations.  
We summarize the dataset, provide descriptive statistics, and show comparisons between species.
""")

# --- Load Data with KaggleHub ---
@st.cache_data
def load_data():
    path = kagglehub.dataset_download("uciml/iris")
    csv_path = f"{path}/Iris.csv"
    return pd.read_csv(csv_path)

df = load_data()

# --- Section 1: Data Overview ---
st.header("1. Dataset Overview")
st.write("Here’s a preview of the dataset:")
st.dataframe(df.head())

# --- Section 2: Summary Statistics ---
st.header("2. Summary Statistics")
st.write("Descriptive statistics for all numerical features:")
st.write(df.describe())

# --- Section 3: Species Filter ---
st.header("3. Filter by Species")
species = st.selectbox("Select species:", df["Species"].unique())
filtered = df[df["Species"] == species]
st.write(f"Showing data for **{species}**:")
st.dataframe(filtered)

# --- Section 4: Visualizations ---
st.header("4. Visualizations")

# Plot 1: Sepal Length vs Sepal Width
st.subheader("4.1 Sepal Length vs Sepal Width")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm", hue="Species", ax=ax1)
st.pyplot(fig1)

# Plot 2: Petal Length vs Petal Width
st.subheader("4.2 Petal Length vs Petal Width")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=df, x="PetalLengthCm", y="PetalWidthCm", hue="Species", ax=ax2)
st.pyplot(fig2)

# Plot 3: Distribution of Sepal Length
st.subheader("4.3 Distribution of Sepal Length")
fig3, ax3 = plt.subplots()
sns.histplot(df, x="SepalLengthCm", hue="Species", multiple="stack", kde=True, ax=ax3)
st.pyplot(fig3)

# Plot 4: Boxplot of Petal Length by Species
st.subheader("4.4 Petal Length by Species")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df, x="Species", y="PetalLengthCm", ax=ax4)
st.pyplot(fig4)

# --- Section 5: Conclusion ---
st.header("5. Conclusion")
st.markdown("""
- **Setosa** flowers tend to have smaller petals and sepals.  
- **Virginica** generally has the largest measurements.  
- Petal dimensions show the clearest separation between species.
""")
