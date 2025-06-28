# interactive_plotly.py
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load wind dataset
df = pldata.wind(return_type='pandas')

# Display for validation
print(df.head(10))
print(df.tail(10))

# Clean strength column
df["strength"] = df["strength"].str.replace("[^0-9.]", "", regex=True).astype(float)

# Interactive scatter plot
fig = px.scatter(df, x="strength", y="frequency", color="direction", title="Wind Strength vs Frequency")
fig.write_html("wind.html")
fig.show()
