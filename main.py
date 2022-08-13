# -*- coding: utf-8 -*-
"""
Description
"""

__version__ = '0.1'
__author__ = 'Utkarsh Srivastava'

import logging

from dash import dcc
import plotly.express as px
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go

from app.services.dash.application import app
from app.services.data_loader import DataLoaderService

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

server = app.server
data_loader_service = DataLoaderService()

sheet_names = data_loader_service.load_sheet_names()

app.layout = html.Div([
    html.H1("Temp App name"),
    dbc.Row([
        dbc.Col([
            html.Div([
            dbc.RadioItems(
                id="radios",
                inline=True,
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-dark",
                labelCheckedClassName="active",
                style={"width": "300px", "align": "left", "display": "inline-block", "padding": "4px", "margin": "12px",
                       "margin-left": "5px", "margin-right": "5px","margin-top": "5px", "margin-bottom": "5px"},
                options=[
                    {"label": sheet_names[i-1], "value": i} for i in range(1, len(sheet_names) + 1)
                ],
                value=1
            )
        ], className="radio-group")
    ], width=3),
    dbc.Col([
            html.Div(id="page-content")])
        ], align="left")
])


@app.callback(
    Output("page-content", "children"),
    Input("radios", "value"),
    State("page-content", "children")
)
def render_content(sel_graph, curr_graph):
    print(sel_graph)
    if sel_graph == None or sel_graph == 0:
        raise PreventUpdate()
    else:
        if sel_graph == 1:
            return pcg_mf_pop()
        elif sel_graph == 2:
            return pcg_stats_16()
        elif sel_graph == 3:
            return pcgmem_agents16()
        elif sel_graph == 4:
            return agentscomp_16()
        elif sel_graph == 5:
            return comm_pcgmem16()
        elif sel_graph == 6:
            return ppastors16()
        elif sel_graph == 7:
            return pcg_ghana_16()
        elif sel_graph == 8:
            return chythatd16()
        elif sel_graph == 9:
            return pcggrowth_16_15()
        elif sel_graph == 10:
            return adtnonadt_16()
        elif sel_graph == 11:
            return ann_trd_child_16()
        elif sel_graph == 12:
            return ann_trd_jy_16()
        elif sel_graph == 13:
            return ann_trd_ypg_16()
        elif sel_graph == 14:
            return ann_trd_yaf_16()
        elif sel_graph == 15:
            return ann_trd_adlt_16()
        elif sel_graph == 16:
            return ann_stats_01_16()
        elif sel_graph == 17:
            return ann_trend_01_16()

def pcg_mf_pop():
    data = data_loader_service.pcg_mf_pop()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="pcg_mf_pop_piechart", figure=px.pie(
                data, values='pop', names='index')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )


def pcg_stats_16():
    data = data_loader_service.pcg_stats_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="pcg_stats16_piechart", figure=px.pie(
                data, values='Pop for 2015', names='Presbytery')
        , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def pcgmem_agents16():
    data = data_loader_service.pcg_mem_agents_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="pcg_mem_agents_piechart", figure=px.pie(
                data, values='pop', names='index')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def agentscomp_16():
    data = data_loader_service.agents_comp_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="agentscomp_16_piechart", figure=px.pie(
                data, values='Pop', names='Agents')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def comm_pcgmem16():
    data = data_loader_service.comm_pcgmem_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="comm_pcgmem_16_piechart", figure=px.pie(
                data, values='pop', names='index')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def ppastors16():
    data = data_loader_service.ppastors_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ppastors16_piechart", figure=px.pie(
                data, values='No. of Ministers ', names='Presbytery')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def pcg_ghana_16():
    data = data_loader_service.pcg_ghana_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="pcg_ghana_16_piechart", figure=px.pie(
                data, values='pop', names='index')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def chythatd16():
    data = data_loader_service.chythatd16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="chythatd16_piechart", figure=px.pie(
                data, values='Pop', names='Group')
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def pcggrowth_16_15():
    data = data_loader_service.pcg_growth_16_15()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Presbytery"],
            y=data["Tot For 2016"],
            name="2016",
            marker_color='rgb(55, 83, 109)'
        )
    )
    fig.add_trace(
        go.Bar(
            x=data["Presbytery"],
            y=data["Tot For 2015"],
            name="2015",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.update_layout(
        title="PCG Presbytery Growth Chart - 2016 and 2015",
        yaxis=dict(
            title="Population"
        ),
        barmode="group",
        bargap=0.15,
        bargroupgap=0.1,
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="pcggrowth_16_15_bar", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def adtnonadt_16():
    data = data_loader_service.adtnonadt_16()
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="adtnonadt_16_piechart", figure=px.pie(
                data, values='Pop', names='Class', title="Ratio of Adults to Non-Adults within PCG - 2016 ")
            , style={'width': '90vh', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ]
    )

def ann_trd_child_16():
    data = data_loader_service.ann_trd_child_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG Children Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trd_child_16_bar_line", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
])

def ann_trd_jy_16():
    data = data_loader_service.ann_trd_jy_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG JY Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trd_jy_16_bar_line", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
])

def ann_trd_ypg_16():
    data = data_loader_service.ann_trd_ypg_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG YPG Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trd_ypg_16_barline", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
])

def ann_trd_yaf_16():
    data = data_loader_service.ann_trd_yaf_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG YAF Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trd_yaf_16_barline", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
])

def ann_trd_adlt_16():
    data = data_loader_service.ann_trd_adlt_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG Adult Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trd_adlt_16_barline", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ])

def ann_stats_01_16():
    data = data_loader_service.ann_stats_01_16()
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Year"],
            y=data["Population"],
            name="Year",
            marker_color='rgb(26, 118, 255)'
        )
    )
    fig.add_trace(
        go.Scatter(name="Linear best fit line",
                   x=data["Year"], y=data["bestfit"], mode="lines")
    )
    fig.update_layout(
        title="PCG Annual Trend Chart - 2002 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_stats_01_16_barline", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ])

def ann_trend_01_16():
    data = data_loader_service.ann_trd_adlt_16()
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=data["Year"], y=data["Population"], mode="lines+markers+text", text=data["Population"], textposition="top center")
    )
    fig.update_layout(
        title="Trend of PCG Annual Growth - 2001 to 2016",
        yaxis=dict(
            title="Population"
        ),
        width=400
    )
    return html.Div([dbc.Spinner(children=[
        dcc.Graph(
            id="ann_trend_01_16_line", figure=fig
            , style={'width': '120h', 'height': '90vh'}
        )
    ], size="lg", color="primary", type="border")
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
