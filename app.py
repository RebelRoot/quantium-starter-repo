from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer"),
    html.Div("Environment successfully set up!"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'Pink Morsels'},
            ],
            'layout': {
                'title': 'Sample Sales Data'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
