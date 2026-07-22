import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Peak Hour Demand Dashboard", layout="wide")

st.title("Peak Hour Forecasting Dashboard")
st.caption("Hampshire Bus Network — Go-Ahead / Go South Coast (BODS data)")

# Load exported data
lr_df = pd.read_csv("lr_predictions.csv")
rf_df = pd.read_csv("rf_predictions.csv")
gbt_df = pd.read_csv("gbt_predictions.csv")
metrics_df = pd.read_csv("model_metrics.csv")
headway_df = pd.read_csv("headway_summary.csv")

# --- Model comparison table ---
st.header("Model Comparison")
st.dataframe(metrics_df, use_container_width=True)

# --- Actual vs Predicted chart, model selector ---
st.header("Actual vs Predicted Demand")

model_choice = st.selectbox("Select model", ["Gradient Boosted Trees", "Random Forest", "Linear Regression"])

if model_choice == "Gradient Boosted Trees":
    plot_df = gbt_df
elif model_choice == "Random Forest":
    plot_df = rf_df
else:
    plot_df = lr_df

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(plot_df["demand"], plot_df["prediction"], alpha=0.6)
max_val = plot_df["demand"].max()
ax.plot([0, max_val], [0, max_val], "r--", lw=2)
ax.set_xlabel("Actual Demand")
ax.set_ylabel("Predicted Demand")
ax.set_title(f"{model_choice}: Actual vs Predicted")
st.pyplot(fig)

# --- Route filter ---
st.header("Explore by Route")
routes = sorted(plot_df["route_number"].astype(str).unique())
selected_route = st.selectbox("Select a route", routes)

route_data = plot_df[plot_df["route_number"].astype(str) == selected_route]
st.dataframe(route_data, use_container_width=True)

# --- Headway regularity table ---
st.header("Headway Regularity by Route")
st.caption("Lower % = more consistent service intervals")
st.dataframe(
    headway_df.sort_values("headway_regularity_pct").head(20),
    use_container_width=True
)