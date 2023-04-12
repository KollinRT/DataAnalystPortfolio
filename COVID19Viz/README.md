# Overview of Project

This visualization is carried out via the use of a Python backend with the Flask micro framework for web development and the fairly-standard HTML/CSS/JavaScript as a front end.

Purpose: To explore the visualization of time-series data for COVID-19.

## How to install and run

1. Create a virtual environment (venv) via (see ([this](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/)).
)
`python -m venv ./venv`
2. Activate the venv. On Mac this is `source venv/bin/activate` (look up how to source it on device on link for #1)
3. Install required Python packages using the requirements.txt file via the command `pip install -r requirements.txt`
4. Run `python server.py` to initiate the server.

`WorkingJournal.ipynb` and `data_parsing.py` are identical, just one in .py and one in .ipynb format.

## How to improve
- Utilization of React for the frontend and Typescript to accommodate the larger app codebase as it'd inevitably grow in complexity.
- Switch the data digestion in Python from downloading to the data to grabbing it from the API and processing it locally.