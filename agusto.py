import streamlit as st
import matplotlib.pyplot as plt

# Datos de ejemplo
labels = ["Severos", "Fatales"]
sizes = [3, 5]
colors = ["orange", "red"]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
ax.set_title("Casos en Argentina")

st.pyplot(fig)