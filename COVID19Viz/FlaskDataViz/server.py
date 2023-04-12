import pandas as pd
from flask import Flask, render_template, request
from definitions import months, states, years, year_dict

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html',
                           message="Hello World!",
                           years=years, months=months,
                           states=states)

@app.route('/mapviz', methods=['GET'])
def mapViz():
    year = request.args.get('years')
    month = request.args.get('months')

    monthnum = year_dict[month]
    monthnum = f"{int(monthnum):02d}"

    return render_template('mapviz.html',
                           year=year, month=month,
                           years=years, monthnum=monthnum,
                           months=months, states=states)

@app.route('/lineviz', methods=['GET'])
def lineViz():
    stateChosen = request.args.get('states')
    print(f"You selected {stateChosen}.")

    return render_template('lineviz.html',
                           stateChosen=stateChosen, states=states,
                           years=years, months=months)

if __name__ == '__main__':
    app.run(port=5050, debug=True)