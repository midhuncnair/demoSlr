#! /usr/bin/env python3
"""
"""

import sys

import uvicorn

from demo_slr_app import app_fast, app_flask


if __name__ == "__main__":
    argv = sys.argv
    print("Input args = ", argv)
    if '--asgi' in argv:
        uvicorn.run(app_fast, host='127.0.0.1', port=8000)
    else:
        app_flask.run(debug=True)
