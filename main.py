import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

app = Dash(__name__, external_stylesheets=['styles.css'])
colors = {
    'background': '#111111',
    'text': '#73B449'
}
app.css.config.serve_locally = True
app.title = 'TreeDatalize'

df = (
    pd.read_csv('iTreePlantingSclean.csv')
)

species_options = [{'label': species, 'value': species} for species in df['Species']]

species_images = {
    'Canary island pine(Pinus canariensis)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Young_cone.JPG/317px-Young_cone.JPG',
    'Blue atlas cedar(Cedrus atlantica v. glauca)': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Cedrus_atlantica.jpg',
    'Incense cedar(Calocedrus decurrens)': 'https://en.wikipedia.org/wiki/File:Calocedrus_decurrens_Yosemite_NP.jpg',
    'Aleppo pine(Pinus halepensis)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Pinus-halepensis-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Outeniqua yellowwood(Afrocarpus falcatus)': 'https://en.wikipedia.org/wiki/File:Southafrica428yellowwood.jpg',
    'Bronze loquat(Eriobotrya deflexa)': 'https://en.wikipedia.org/wiki/File:Eriobotryadeflexa.jpg',
    'Loquat tree(Eriobotrya japonica)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Loquat-0.jpg/440px-Loquat-0.jpg',
    'Carob(Ceratonia siliqua)': 'https://images.fineartamerica.com/images-medium-large-5/carob-tree-ceratonia-siliqua-seed-pods-photostock-israelscience-photo-library.jpg',
    'Deodar cedar(Cedrus deodara)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/20130903Cedrus_deodara2.jpg/2560px-20130903Cedrus_deodara2.jpg',
    'Cork oak(Quercus suber)': 'https://en.wikipedia.org/wiki/File:Cork_oak_(28864190188).jpg',
    'Bay laurel(Laurus nobilis)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Laurus_nobilis_111.JPG/320px-Laurus_nobilis_111.JPG',
    'Purple blow maple(Acer truncatum)': 'https://en.wikipedia.org/wiki/File:Acer_truncatum_Leaf.jpg',
    'Washington hawthorn(Crataegus phaenopyrum)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Crataegus_phaenopyrum_HRM.jpg/440px-Crataegus_phaenopyrum_HRM.jpg',
    'Wilga; australian willow(Geijera parviflora)': 'https://en.wikipedia.org/wiki/File:Geijera_parviflora_4.jpg',
    'California peppertree(Schinus molle)': 'https://en.wikipedia.org/wiki/File:Schinus_Molle.jpg',
    'Japanese flower crabapple(Malus floribunda)': 'https://en.wikipedia.org/wiki/File:Malus_floribunda_(Japanese_crabapple).jpg',
    'Goldenrain tree(Koelreuteria paniculata)': 'https://en.wikipedia.org/wiki/File:(MHNT)_Koelreuteria_paniculata_-Leaves_and_inflorescences_-_Palais_Niel.jpg',
    'Southern magnolia(Magnolia grandiflora)': 'https://en.wikipedia.org/wiki/File:Magnolia_flower_Duke_campus.jpg',
    'Italian stone pine(Pinus pinea)': 'https://en.wikipedia.org/wiki/File:Pinus_pinea_Wellington_Botanic_Gardens.jpg',
    'Hedge maple(Acer campestre)': 'https://en.wikipedia.org/wiki/File:Acer_campestre_in_Appennino2.jpg',
    'Persian ironwood(Parrotia persica)': 'https://en.wikipedia.org/wiki/File:Morlanwelz_Mariemont_JPG22a.jpg',
    'Eastern hophornbeam(Ostrya virginiana)': 'https://en.wikipedia.org/wiki/File:Ostrya_virginiana_2.jpg',
    'Bur oak(Quercus macrocarpa)': 'https://en.wikipedia.org/wiki/File:Big_Tree_with_spring_picnic.jpg',
    'Chinese pistache(Pistacia chinensis)': 'https://en.wikipedia.org/wiki/File:Pistacia_chinensis.jpg',
    'Austrian pine(Pinus nigra)': 'https://en.wikipedia.org/wiki/File:Forest_in_Bulgaria_near_Dundukovo_dam.jpg',
    'California sycamore(Platanus racemosa)': 'https://en.wikipedia.org/wiki/File:J20160926-0053%E2%80%94Platanus_racemosa%E2%80%94RPBG_(29346126813).jpg',
    'Ponderosa pine(Pinus ponderosa)': 'https://en.wikipedia.org/wiki/File:Pinus_ponderosa_15932.JPG',
    'Blue oak(Quercus douglasii)': 'https://en.wikipedia.org/wiki/File:Large_Blue_Oak.jpg',
    'Red maple(Acer rubrum)': 'https://en.wikipedia.org/wiki/File:2014-10-30_11_09_40_Red_Maple_during_autumn_on_Lower_Ferry_Road_in_Ewing,_New_Jersey.JPG',
    'Marina arbutus(Arbutus v. marina)': 'https://waterwisegardenplanner.org/wp-content/uploads/2016/12/24110200/Arbutus-Marina-4-of-7.jpg',
    'Eastern redbud(Cercis canadensis)': 'https://en.wikipedia.org/wiki/File:RedbudOhio02.jpg',
    'Interior live oak(Quercus wislizeni)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/05/Quercus-wislizenii-5-scaled.jpeg?fit=668%2C1024&ssl=1',
    'Chinese flame tree(Koelreuteria bipinnata)': 'https://en.wikipedia.org/wiki/File:PikiWiki_Israel_5534_koelreuteria_bippnata.jpg',
    'Kentucky coffeetree(Gymnocladus dioicus)': 'https://en.wikipedia.org/wiki/File:Gymnocladus_dioicus.JPG',
    'Chinese fringe tree(Chionanthus retusus)': 'https://en.wikipedia.org/wiki/File:Chionanthus_retusus3.jpg',
    'Afghan pine(Pinus eldarica)': 'https://en.wikipedia.org/wiki/File:Pinus_brutia(03).jpg',
    'Littleleaf linden(Tilia cordata)': 'https://en.wikipedia.org/wiki/File:Tilia-cordata2.JPG',
    'Baldcypress(Taxodium distichum)': 'https://en.wikipedia.org/wiki/File:Taxodium_distichum_NRCSMS01010.jpg',
    'European hornbeam(Carpinus betulus)': 'https://en.wikipedia.org/wiki/File:Carpinus_betulus_-_Hunsr%C3%BCck_001.jpg',
    'Kurrajong(Brachychiton populneus)': 'https://en.wikipedia.org/wiki/File:Brachychiton_populneus_tree.jpg',
    'Jeffrey pine(Pinus jeffreyi)': 'https://en.wikipedia.org/wiki/File:Mature_Jeffrey_Pine.JPG',
    'Japanese zelkova(Zelkova serrata)': 'https://en.wikipedia.org/wiki/File:Zelkova_serrata_Noma_keyaki01.jpg',
    'Buckley oak(Quercus buckleyi)': 'https://cdn.shopify.com/s/files/1/0514/8809/6429/products/QuercusBuckleyi60.jpg?v=1659238420&width=990',
    'California laurel(Umbellularia californica)': 'https://en.wikipedia.org/wiki/File:Umbellularia_californica_02.jpg',
    'Black tupelo(Nyssa sylvatica)': 'https://en.wikipedia.org/wiki/File:Nyssa_sylvatica_v_sylvatica.jpg',
    'Oregon ash(Fraxinus latifolia)': 'https://en.wikipedia.org/wiki/File:Fraxinus_latifolia_JPG1A.jpg',
    'London plane(Platanus x acerifolia)': 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Platanus-acerfolia--josh-s-jackson--CC-BY-NC.jpg',
    'Shoestring acacia(Acacia stenophylla)': 'https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTjIZtZGTR_v_eG-ssLqAJv4cB0ALGqLup5IMNhg5XI1DdE-2SQ1tgfY3EXYAubN2tGBKkIHYej8nKOnaI',
    'Chestnut-leaved oak(Quercus castaneifolia)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Quercus_castaneifolia2_kew.jpg/440px-Quercus_castaneifolia2_kew.jpg',
    'Northern red oak(Quercus rubra)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Quercus_rubra_%40_Tortworth_Court.jpg/440px-Quercus_rubra_%40_Tortworth_Court.jpg',
    'Shumard oak(Quercus shumardii)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/EncinoRojo.jpg/440px-EncinoRojo.jpg',
    'European hackberry(Celtis australis)': 'https://sactree.org/wp-content/uploads/2021/03/Celtis-australis-European-hackberry-canopy-SelecTree.jpg',
    'California white oak(Quercus lobata)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Quercus_lobata_early_spring.jpg/440px-Quercus_lobata_early_spring.jpg',
    'Japanese black pine(Pinus thunbergii)': 'https://en.wikipedia.org/wiki/File:Pinus_thunbergii_Matsushima.jpg',
    'Common fig(Ficus carica)': 'https://en.wikipedia.org/wiki/File:Ficus-carica.jpg'
}


app.layout = html.Div(
    children=[
    html.H1(
        children='TreeDatalize',
        style={
            'textAlign': 'center',
            'font-family': 'DM Sans',
            'color': colors['text']
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
    html.Div(
            children=[
                html.Div(id='output-div-bar', style={'flex': '1'}),
                html.Div(
                    id='output-div-image',
                    style={'flex': '1', 'width': '400px', 'height': '400px', 'overflow': 'hidden', 'justify-content': 'center', 'align-items': 'center'}
                )
            ],
            style={"display": "flex"}
        ),
    dcc.Markdown('''
    # Tree Biomass vs. Electricity Saved
    '''),
    html.Div(id='output-div-scatter')
])

@app.callback(
    Output('output-div-bar', 'children'),
    Input('species-dropdown', 'value')
)
def update_output_bar(species):
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


@app.callback(
    Output('output-div-image', 'children'),
    Input('species-dropdown', 'value')
)
def update_output_image(species):
    image_url = species_images.get(species, '')
    image_component = html.Img(src=image_url, style={'width': '400px'})
    return image_component


@app.callback(
    Output('output-div-scatter', 'children'),
    Input('species-dropdown', 'value')
)

def update_output_scatter(species):
    # Retrieve the data for the selected species from your dataset

    # Create a scatter plot using tree biomass and electricity saved
    scatter_data = []
    for i, row in df.iloc[:-1].iterrows():
        def colors(num):
            if num < 3000:
                return '#ca35a6'
            elif num >= 3000 and num < 6000:
                return '#a6ca35'
            else:
                return '#35a6ca'
        # Remove commas and convert to float
        number_float = float(row['Electricity Saved (kWh)'].replace(",", ""))
        scatter_data.append(
            go.Scatter(
                x=[row['Tree Biomass (short ton)']],
                y=[row['Electricity Saved (kWh)']],
                mode='markers',
                marker=dict(
                    size=10,
                    color=colors(number_float)
                ),
                text=row['Species'],
                name=row['Species']  # Add species name as a trace name
            )
        )

    layout = go.Layout(
        xaxis=dict(title='Tree Biomass (short ton)'),
        yaxis=dict(title='Electricity Saved (kWh)'),
        hovermode='closest',
    )

    # Create the scatter plot figure
    fig = go.Figure(data=scatter_data, layout=layout)
    fig.update_layout(autotypenumbers='convert types')

    # Return the chart as a Plotly graph object
    return dcc.Graph(figure=fig)


if __name__ == '__main__':
    app.run_server(debug=True)