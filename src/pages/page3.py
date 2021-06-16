import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import  math
import numpy


def func(x):
    y=x*math.cos(x+numpy.log(1+x))
    return(y)


x_graf = numpy.arange(50)
y_graf = []
for i in x_graf:
    y_graf.append(func(i))
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
profit_ue = [1463.75, 1394, 1459.87, 1731.89, 1845.52, 1594.83, 2223.8]
profit_ea = [4517, 4373, 4808, 5160, 4932, 5466, 5659]



fig_profit = go.Figure()
fig_profit.add_trace(go.Scatter(x=years, y=profit_ue, mode='lines', name='Ubisoft'))
fig_profit.add_trace(go.Scatter(x=years, y=profit_ea, mode='lines', name='EA'))
fig_profit.update_layout(title='Profit of Ubisoft and EA', xaxis_title='Years', yaxis_title='Million $')

fig_graph = go.Figure(data=go.Scatter(x=x_graf, y=y_graf))
fig_graph.update_layout(title='Graph of y = x*cos(x+log(1+x))', xaxis_title='x', yaxis_title='y')

page3 = html.Div(
    [
        html.H1('Profit of Companies'),
        dbc.Row(
            [
                html.Div(
                    dcc.Graph(figure=fig_profit),
                    style={"height": "400px", "width": "850px"},
                    ),
            ]
        ),
        dbc.Row(
            [
                html.Div(
                    html.H2('Bonus Graph'),
                    style={"margin-top": "70px"}
                ),

            ]
        ),
        dbc.Row(
            [
                html.Div(
                    dcc.Graph(figure=fig_graph),
                    style={"height": "400px", "width": "800px", "margin-top": "30px"},
                    ),

            ]
        ),

    ]
)


def get_page():
    return page3
