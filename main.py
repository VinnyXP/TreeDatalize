import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

app = Dash(__name__, external_stylesheets=['styles.css'])
app.css.config.serve_locally = True
app.title = 'TreeDatalize'

df = (
    pd.read_csv('iTreePlantingSclean.csv')
)

species_options = [{'label': species, 'value': species} for species in df['Species']]

app.layout = html.Div(
    children=[
    html.H1(
        children='TreeDatalize',
        style={
            'textAlign': 'center',
            'font-family': 'DM Sans'
        }
    ),
    dcc.Markdown('''
    # Cost Benefits of Each Tree

    '''),
    html.Label('Select a Species:'),
    dcc.Dropdown(
        id='species-dropdown',
        options=species_options,
        value=species_options[0]['value']  # Set default value to the first species
    ),
    html.Div(id='output-div')
])

@app.callback(
    Output('output-div', 'children'),
    Input('species-dropdown', 'value')
)
def update_output(species):
    # Retrieve the data for the selected species from your dataset
    species_data = df.loc[df['Species'] == species]

    # Create a bar chart using the CO2 Avoided and CO2 Sequestered values
    data = [
        go.Bar(
            x=['CO2 Avoided', 'CO2 Sequestered', 'Electricity Saved', 'Fuel Saved', 'Avoided Runoff', 'Avoided Value', 'Removal Value'],
            y=[species_data['CO2 Avoided ($)'].values[0], species_data['CO2 Sequestered ($)'].values[0],
               species_data['Electricity Saved ($)'].values[0], species_data['Fuel Saved ($)'].values[0],
               species_data['Avoided Runoff ($)'].values[0], species_data['Avoided Value ($)'].values[0],
               species_data['Removal Value ($)'].values[0]],
            marker=dict(color=['#0e5cf1','#356fca','#5772a8', '#6b7b94', '#a88d57', '#ca9035' ,'#f1a30e']),
            text=[f"{species_data['CO2 Avoided ($)'].values[0]} dollars",
                  f"{species_data['CO2 Sequestered ($)'].values[0]} dollars",
                  f"{species_data['Electricity Saved ($)'].values[0]} dollars",
                  f"{species_data['Fuel Saved ($)'].values[0]} dollars",
                  f"{species_data['Avoided Runoff ($)'].values[0]} dollars",
                  f"{species_data['Avoided Value ($)'].values[0]} dollars",
                  f"{species_data['Removal Value ($)'].values[0]} dollars"],
            textposition='auto'
        )
    ]

    layout = go.Layout(
        xaxis=dict(title='Category'),
        yaxis=dict(title='Dollar Value'),
        barmode='group'
    )

    # Create the bar chart figure
    fig = go.Figure(data=data, layout=layout)
    
    fig.update_layout(autotypenumbers='convert types')
    fig.update_traces(width=0.8)

    # Return the chart as a Plotly graph object
    return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True)