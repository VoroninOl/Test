import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas


def setting_maker(fig):
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)


years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
pc_profit_list = [26.122, 29.07, 30.528, 31.654, 31.95, 32.859, 33.096, 33.418, 34.839]
mob_profit_list = [12.708, 17.595, 24.592, 31.654, 42.6, 55.982, 70.329, 82.026, 94.563]
con_profit_list = [31.77, 29.835, 29.68, 29.792, 31.95, 32.859, 34.475, 36.456, 38.157]
pc_profit = {'Profit $Bn' : pc_profit_list , 'Year' : years}
mob_profit = {'Profit $Bn' : mob_profit_list, 'Year' : years}
con_profit = {'Profit $Bn' : con_profit_list, 'Year' : years}

pc_profit_df = pandas.DataFrame(data=pc_profit)
mob_profit_df = pandas.DataFrame(data=mob_profit)
con_profit_df = pandas.DataFrame(data=con_profit)

fig_pc = px.bar(pc_profit_df, x='Year', y='Profit $Bn', height=400, title="Profit of PC Games")
fig_mob = px.bar(mob_profit_df, x='Year', y='Profit $Bn', height=400, title="Profit of Mobile Games")
fig_con = px.bar(con_profit_df, x='Year', y='Profit $Bn', height=400, title="Profit of Console Games")

setting_maker(fig_pc)
setting_maker(fig_mob)
setting_maker(fig_con)

page2 = html.Div(
    [
        html.H2("Profit of Games"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig_pc),
                        style={"height": "400px", "border-style": "solid"},
                    ),
                    md=6,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(figure=fig_mob),
                        style={"height": "400px", "border-style": "solid"},
                    ),
                    md=6,
                ),
            ],
            no_gutters=True,
        ),
        html.Br(),
        html.H2(""),
        html.H2(""),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(

                        dcc.Graph(figure=fig_con),
                        style={"height": "400px", "border-style": "solid", "margin-top": "40px"},
                    ),

                ),

            ],
            no_gutters=True,
        ),
    ]
)

def get_page2():
    return page2


