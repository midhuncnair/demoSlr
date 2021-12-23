"""
Note:
    $ --> means terminal/ command prompt
    # means comment
    plain line is output for the command executed in the terminal
"""

(envSLR) [...] $ pip --version
pip 21.0.1 from .../demo_slr/envSLR/lib/python3.5/site-packages/pip (python 3.5)

# make sure the python path is from the virual environment that was created (or conda environment
# if you are using conda-prompt)

(envSLR) [...] $pip install -r requirements.txt
# the above command will install all the python dependancies needed for this demo_slr application
# make sure this was successfull; if it says file not found for requirements.txt; then make sure
# you are in outermost demo_slr folder.

