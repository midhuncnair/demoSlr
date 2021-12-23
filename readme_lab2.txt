"""
Note:
    $ --> means terminal/ command prompt
    # means comment
    plain line is output for the command executed in the terminal
"""

(envSLR) [...] $ python local_run.py --asgi
INFO:     Started server process [94275]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
...


# goto http://127.0.0.1:8000/ in your prefered browser
# and check the output {"message":"Hello World"}
# now goto http://127.0.0.1:8000/docs to use the fast api server.
# once done with the lab2 press CTRL+C 1/2 times to stop this server.
