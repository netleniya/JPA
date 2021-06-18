import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px

from dash.dependencies import Input, Output
from metrics import metrix

app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Lulu Shop LightHouse Performance Metrics', style = {'textAlign':'center','marginTop':40,'marginBottom':40}),

        dcc.Dropdown( id = 'dropdown',
        options = [
            {'label':'First Contentful Paint', 'value': metrix[0]},
            {'label':'Speed Index', 'value': metrix[1]},
            {'label':'Time to Interactive', 'value': metrix[2]},
            {'label':'Total Blocking Time', 'value': metrix[3]},
            {'label':'Largest Contentful Paint', 'value': metrix[4]},
            {'label':'Cumulative Layout Shift', 'value': metrix[5]}
        ],
        placeholder='Select metric',
        value = ''
        ),
        dcc.Graph(id = 'my-gauge'),

    html.Div(['a petro impleta die xvii junii ad mmxxi'], style={'textAlign':'center', 'color':'blue','fontsize':20})
    
    
    ])
    

@app.callback(Output(component_id='my-gauge', component_property= 'figure'),
              [Input(component_id='dropdown', component_property= 'value')])


def gauge_graphs(value):
    '''Accepts dictionary as input and graphs Average and 75th percentile metrics'''
    
    import plotly.graph_objects as go
    fig = go.Figure()
    
    fig.update_layout(title = value['title'])
    
    fig.add_trace(go.Indicator(
        title = {'text': value['mean_id']},
        value = value['mean'],
        delta = {'reference': value['delta']},
        gauge = {
            'axis': {'range': value['range']},
            'bar': {'color': "darkblue"},
            'steps': value['steps'],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value['thresh']
            }
        },
        domain = {'row': 0, 'column': 0}))
    
    fig.add_trace(go.Indicator(
        title = {'text': value['tris_id']},
        value = value['tris'],
        delta = {'reference': value['delta']},
        gauge = {
            'axis': {'range': value['range']},
            'bar': {'color': "darkblue"},
            'steps': value['steps'],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': value['thresh']
            }
        },
        domain = {'row': 0, 'column': 1}))
    
    fig.update_layout(
    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{'mode' : "number+delta+gauge",}]}})

    return fig


if __name__ == '__main__': 
    app.run_server()