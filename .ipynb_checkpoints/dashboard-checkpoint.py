import dash
import dash_html_components as html 
import dash_core_components as dcc 
import plotly.graph_objects as go
import plotly.express as px

app=dash.Dash()

app.layout=html.Div([

    html.H1('Lulu Metrics', style={'color':'blue','fontsize':40,'border-style':'outset'}),

    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label':'First Contentful Paint', 'value': '1'},
            {'label':'Speed Index', 'value': '2'},
            {'label':'Time to Interactive', 'value': '3'},
            {'label':'Total Blocking Time', 'value': '4'},
            {'label':'Largest Contentful Paint', 'value': '5'},
            {'label':'Cumulative Layout Shift', 'value': '6'},
        ],
        value='1'
    ),

    html.Div(['a Petro factvs'], style={'color':'blue','fontsize':30,'border-style':'double'})
],
style={'border-style':'ridge','border-color':'blue'})

if __name__ == '__main__':
    app.run_server(port=8002,host='127.0.0.1',debug=True)