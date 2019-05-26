import dash
import dash_core_components as dcc
import dash_html_components as html
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


r = requests.get('https://api.osf.io/v2/providers/preprints/africarxiv/preprints/?format=json')
dict = r.json()
# store the Api in a dictionary

x = list()
x.insert(0, dict["data"][0]["attributes"]["date_published"][:7])
y = list()
y.insert(0, 1)
# those lists will contain the date (yyyy-mm) and number_of_preprints)

flag = 0

while True:

    for j in range(1, len(dict["data"])):
        date = dict["data"][j]["attributes"]["date_published"][:7]

        if date == x[0]:
            y[0] += 1

        else:
            x.insert(0, date)
            y.insert(0, 1)

    if flag == 1:
        break
    else:
        r = requests.get(dict["links"]["next"])
        dict = r.json()
        if (dict["links"]["next"] == None):
            flag = 1


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children="Data Vizualisation :",
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children="Nombre d'articles publies par mois :", style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'bar', 'name': 'SF'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)