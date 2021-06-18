first_contentful = {'title':'First Contentful Paint (10%)', 
               'mean_id': 'Average', 'mean':1.5,
               'tris_id': '75th Percentile', 'tris':1.9,
               'delta':1.8, 'range':[None, 5.0],
               'steps':[{'range':[0.0, 1.8], 'color':"limegreen"},
                        {'range':[1.8, 3.0], 'color':"gold"},
                        {'range':[3.0, 5.0], 'color':"red"}],
               'thresh': 1.8
              }

speed_index = {'title':'Speed Index (10%)', 
               'mean_id': 'Average', 'mean':4.2,
               'tris_id': '75th Percentile', 'tris':5.7,
               'delta':3.4, 'range':[None, 8.5],
               'steps':[{'range':[0.0, 3.4], 'color':"limegreen"},
                        {'range':[3.4, 5.8], 'color':"gold"},
                        {'range':[5.8, 8.5], 'color':"red"}],
               'thresh': 3.4
              }


time_to_inter = {'title':'Time to Interactive (10%)', 
               'mean_id': 'Average', 'mean':8.0,
               'tris_id': '75th Percentile', 'tris':9.2,
               'delta':3.8, 'range':[None, 14.0],
               'steps':[{'range':[0.0, 3.8], 'color':"limegreen"},
                        {'range':[3.8, 7.3], 'color':"gold"},
                        {'range':[7.3, 14.0], 'color':"red"}],
               'thresh': 3.8
              }


total_blocking_time = {'title':'Total Blocking Time (30%)', 
               'mean_id': 'Average', 'mean':1.6,
               'tris_id': '75th Percentile', 'tris':1.8,
               'delta':2.0, 'range':[None, 8.5],
               'steps':[{'range':[0.0, 2.0], 'color':"limegreen"},
                        {'range':[2.0, 6.0], 'color':"gold"},
                        {'range':[6.0, 8.5], 'color':"red"}],
               'thresh': 2.0
              }


largest_contentful = {'title':'Largest Contentful Paint (25%)', 
               'mean_id': 'Average', 'mean':4.2,
               'tris_id': '75th Percentile', 'tris':5.7,
               'delta':2.5, 'range':[None, 8.0],
               'steps':[{'range':[0.0, 2.5], 'color':"limegreen"},
                        {'range':[2.5, 4.0], 'color':"gold"},
                        {'range':[4.0, 8.0], 'color':"red"}],
               'thresh': 2.5
              }


cumulative_layout = {'title':'Cumulative Layout Shift (15%)', 
               'mean_id': 'Average', 'mean':0.03,
               'tris_id': '75th Percentile', 'tris':0.06,
               'delta':0.1, 'range':[None, 1.25],
               'steps':[{'range':[0.00, 0.10], 'color':"limegreen"},
                        {'range':[0.10, 0.25], 'color':"gold"},
                        {'range':[0.25, 1.25], 'color':"red"}],
               'thresh': 0.1
              }


def gauge_graphs(metric):
    '''Accepts dictionary as input and graphs Average and 75th percentile metrics'''
    
    import plotly.graph_objects as go
    fig = go.Figure()
    
    fig.update_layout(title = metric['title'])
    
    fig.add_trace(go.Indicator(
        title = {'text': metric['mean_id']},
        value = metric['mean'],
        delta = {'reference': metric['delta']},
        gauge = {
            'axis': {'range': metric['range']},
            'bar': {'color': "darkblue"},
            'steps': metric['steps'],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': metric['thresh']
            }
        },
        domain = {'row': 0, 'column': 0}))
    
    fig.add_trace(go.Indicator(
        title = {'text': metric['tris_id']},
        value = metric['tris'],
        delta = {'reference': metric['delta']},
        gauge = {
            'axis': {'range': metric['range']},
            'bar': {'color': "darkblue"},
            'steps': metric['steps'],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': metric['thresh']
            }
        },
        domain = {'row': 0, 'column': 1}))
    
    fig.update_layout(
    grid = {'rows': 1, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{'mode' : "number+delta+gauge",}]}})
    
    fig.show()


metrix = [first_contentful, speed_index, time_to_inter, total_blocking_time,
          largest_contentful, cumulative_layout]
