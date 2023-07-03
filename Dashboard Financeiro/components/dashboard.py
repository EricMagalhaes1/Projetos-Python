from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from app import app
import pdb

card_icon = {
    "color":"white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto"
}


#============ Layout ============#
layout = dbc.Col([
        dbc.Row([
            dbc.Col([

                # Saldo
                dbc.CardGroup([
                    dbc.Card([
                        html.Legend("Saldo"),
                        html.H5("R$ 5400", id='p-saldo-dashboard',style='')
                    ],style={'padding-left':'20px', 'padding-top':'10px'}),
                    dbc.Card(
                        html.Div(className='fa fa-university',style=card_icon),
                        color='warning',
                        style={'maxWidth':75, 'height': 100,'margin-left':'-10px'},
                    )])

                ],width=4),
                # Receita

                dbc.Col([
                    dbc.CardGroup([
                            dbc.Card([
                                    html.Legend("Receita"),
                                    html.H5("R$ -", id="p-receita-dashboards"),
                            ], style={"padding-left": "20px", "padding-top": "10px"}),
                            dbc.Card(
                                html.Div(className="fa fa-smile-o", style=card_icon),
                                color="success",
                                style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                            )])
                    ], width=4),

                    # Despesa
                dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend("Despesas"),
                            html.H5("R$ -", id="p-despesa-dashboards"),
                        ], style={"padding-left": "20px", "padding-top": "10px"}),
                        dbc.Card(
                            html.Div(className="fa fa-meh-o", style=card_icon),
                            color="danger",
                            style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                    )])
                ], width=4),
        ], style={"margin": "10px"}),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    html.Legend('Filtrar Lançamentos', className="card-title"),
                    html.Label("Categoria das Receitas"),
                    html.Div(
                        dcc.Dropdown(
                            id="dropdown-receita",
                            clearable=False,
                            style={"width": "100%"},
                            persistence=True,
                            persistence_type="session",
                            multi=True
                            ),
                    ),
                    html.Label("Categoria das Despesas"),
                    #html.Div(
                    #    dcc.Dropdown(
                    #        id="dropdown-despesa",
                    #        clearable=False,
                    #        style={"width": "100%"},
                    #        persistence=True,
                    #        persistence_type="session",
                    #       ),
                    # )
                ])
            ])
        ])
])
