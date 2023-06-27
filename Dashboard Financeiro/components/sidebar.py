import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


#============ Layout ============#

layout = dbc.Col([
            html.H1("My Budget", className="primary-text"),
            html.P("By Eric", className="info-text"),
            html.Hr(),

#====== Selecao de perfil ======#
            dbc.Button(id='button-avatar',
                children=[html.Img(src='/assets/img_hom.png',id='avatar_change', alt='Avatar', className='perfil_avatar'),
            ], style={'background-color':'transparent', 'border-color':'transparent'}),




#====== Secao Novo ======#

            dbc.Row({

                dbc.Col([
                    dbc.Button(color='success', id='open_receita',
                               children=['+ Receita'])
                ], width=6),
                dbc.Col([
                    dbc.Button(color='danger', id='open_dispesa',
                               children=['- Despesa'])
                ], width=6)
            })

])
