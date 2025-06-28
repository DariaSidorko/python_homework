# myapp.py
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

# Load data
df = pldata.gapminder()

# Unique countries
countries = df['country'].unique()

# App setup
app = Dash(__name__)
server = app.server  # for Render deployment

app.layout = html.Div([
    html.H1("GDP per Capita Over Time"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": c, "value": c} for c in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

@app.callback(
    Output("gdp-growth", "figure"),
    Input("country-dropdown", "value")
)
def update_graph(country):
    filtered = df[df["country"] == country]
    fig = px.line(filtered, x="year", y="gdpPercap", title=f"GDP per Capita Over Time for {country}")
    return fig

if __name__ == "__main__":
    app.run(debug=True)
