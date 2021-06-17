import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import datetime
import numpy as np
import plotly.express as px

# START-HEATMAP-COMPONENT
np.random.seed(1)

country = ['Europe, Middle East, Africa', 'Latin America', 'North America', 'Asia-Pacific']
money = [34.7, 5.6, 39.6, 72.2]
age = ['under 18', '18-35', '36-49', '50+']
age_percent = [27, 29, 18, 26]
sex = ['Male', 'Female']
sex_percent = [59, 41]

player_age = {'%': age_percent, 'Age' : age}
player_sex = {'%': sex_percent, 'Sex' : sex}
games_profit = {'Profit $Bn' : money , 'Country' : country}
fig_profit = px.pie(games_profit, values="Profit $Bn", names="Country", title = "Statistics of 2019 year", labels="Country")
fig_age = px.pie(player_age, values="%", names="Age", title = "Age of Game Players", hole=.4)
fig_sex = px.pie(player_sex, values="%", names="Sex", title = "Sex of Game Players", hole=.4)


# END-HEATMAP-COMPONENT

# fig.update_layout(
#
# )

page1 = html.Div(
    [
        html.H2("Global Game Market"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig_profit),
                        style={"height": "450px"},
                    ),

                    md=10,
                ),
            ],
            no_gutters=True,
        ),
        html.Br(),
        html.H4("Statistics of Players"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig_age),
                        style={"height": "450px", "border-style": "solid"}
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig_sex),
                        style={"height": "450px", "border-style": "solid"},
                    ),
                    md=6,
                ),
            ],
            no_gutters=True,
        ),
    ]
)


def get_page1():
    return page1
