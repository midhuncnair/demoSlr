#! /usr/bin/env python3
"""
"""


import os

from . import slr_model  # this will make sure the model generated and pickle file is saved to disk
from .app_flask import app as app_flask
from .app_fast import app as app_fast
