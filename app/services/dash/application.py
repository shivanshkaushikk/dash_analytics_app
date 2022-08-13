# -*- coding: utf-8 -*-
"""
Description
"""

__version__ = '0.1'
__author__ = 'Shivansh Kaushik'

import logging
import dash
import dash_bootstrap_components as dbc

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.scripts.append_script({"external_url": ['https://code.jquery.com/jquery-3.2.1.min.js']})
server = app.server