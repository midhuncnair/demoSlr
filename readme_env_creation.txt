"""
Note:
    $ --> means terminal/ command prompt
    # means comment
    plain line is output for the command executed in the terminal

    *nix --> mac, linux systems or any unix based systems
"""

# use powershell for windows
# use any standard terminal for *nix based system


# check if python3 is available
$ python3 --version
Python 3.5.2
# or greater

# (only for windows) if above command throws error try the below command
$ py -3 --version
Python 3.5.2
# or greater
# use ``py -3`` instead of python3 in all the below commands until you activate the
# virtual environment only if this command was successfull and the previous one was not.
# IMPORTANT: once the virtual environment is active/activated use ``python`` and not ``py -3``.

# if [both of the above (in windows)] command is throwing error; then you need to install python3
# or add the installed python3 to your environment variable.


# once you verify that the python is available; make sure you are in the project dir ``demo_slr``
# use ``cd`` command to reach ``demo_slr``.
$ ls
Procfile    asgi.py    demo_slr_app    local_run.py
request_flask.py    requirements.txt    wsgi.py

# there may be other files but the above mentioned will definitely be there if you are at right place.


$ python3 -m venv envSLR
# the above command will create an python virtual environment named ``envSLR``;
# use ``py -3`` inplace off ``python3`` (only for windows) as needed for the above command.

# in *nix system
$ source ./envSLR/bin/activate
# the above will activate the virtual env in *nix based system; if in windows follow next command.

# in windows:
$ cd ./envSLR/Scripts/ && activate && cd ../..
# the above will activate the virtual env in windows system;

# Once your env is active; the ``$`` at the start of the terminal will change to ``(envSLR) [...] $``
# [...] represents path in your system which is optional.
# but the line will start with ``(envSLR)`` and ends with ``$``

# at any given point if you need to come out of the virtual environment type ``deactivate``
# eg:
(envSLR) [...] $ deactivate
$

# the above statement will deactivate the virtual env. however we need to be in virtual environment
#   so dont deactivate unless necessary.

