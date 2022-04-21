def null_heatmap(dataframe):
    '''Creates a heatmap highlighting null values in a dataframe '''
    import plotly.express as px
    
    fig = px.imshow(dataframe.isnull(), width=800, height=600)
    fig.update(layout_coloraxis_showscale=False)
    fig.update_xaxes(tickangle=90)
    fig.update_yaxes(showticklabels=False)
    
    return fig



def show_box(dataframe):
    '''Return a box-and-whiskers diagram of selected data'''
    import plotly.graph_objects as go
    
    fig = go.Figure()

    for col in dataframe:
        fig.add_trace(go.Box(x=dataframe[col].values,
                             name=dataframe[col].name))

    fig.update_layout(title="",autosize=False, 
                      width=800,height=800, showlegend=False)

    return fig
