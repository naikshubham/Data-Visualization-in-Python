import dash # main library
import dash_core_components as dcc # contains diff building blocks

app = dash.Dash() # create app object
app.layout = dcc.Graph(id='example-graph', figure='bar_fig')
# create app layout

if __name__ == '__main__':
    app.run_server(debug=True)

