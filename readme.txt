$ cd demo_slr
# outermost demo_slr folder

$ ls
Procfile    asgi.py    demo_slr    envSLR    local_run.py    readme.txt
request_flask.py    requirements.txt    wsgi.py

$ python3 --version
Python 3.5.2
# or greater

$ python3 -m venv envSLR

$ source ./envSLR/bin/activate

(envSLR) ... $ which python
.../demo_slr/envSLR/bin/python

(envSLR) ... $ which pip
.../demo_slr/envSLR/bin/pip

(envSLR) ... $ pip install -r requirements.txt
# installation successfull

(envSLR) ... $ python local_run.py
 * Serving Flask app 'demo_slr.app_flask' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
...

# goto http://127.0.0.1:5000/