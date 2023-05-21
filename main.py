
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

app = Dash(__name__, external_stylesheets=['styles.css'])
colors = {
    'text': '#73B449'
}
app.css.config.serve_locally = True
app.title = 'TreeDatalize'

#Reading the csv
df = (
    pd.read_csv('iTreePlantingSclean.csv')
)
species_options = [{'label': species, 'value': species} for species in df['Species']]

#Map of tree types to their images
species_images = {
    'Canary island pine(Pinus canariensis)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Young_cone.JPG/317px-Young_cone.JPG',
    'Blue atlas cedar(Cedrus atlantica v. glauca)': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Cedrus_atlantica.jpg',
    'Incense cedar(Calocedrus decurrens)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Calocedrus-decurrens-Incense-cedar.jpg?fit=252%2C300&ssl=1',
    'Aleppo pine(Pinus halepensis)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Pinus-halepensis-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Outeniqua yellowwood(Afrocarpus falcatus)': '//upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Southafrica428yellowwood.jpg/220px-Southafrica428yellowwood.jpg',
    'Bronze loquat(Eriobotrya deflexa)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Eriobotrya-deflexa-Bronze-loquat.jpg?fit=252%2C300&ssl=1',
    'Loquat tree(Eriobotrya japonica)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Loquat-0.jpg/440px-Loquat-0.jpg',
    'Carob(Ceratonia siliqua)': 'https://images.fineartamerica.com/images-medium-large-5/carob-tree-ceratonia-siliqua-seed-pods-photostock-israelscience-photo-library.jpg',
    'Deodar cedar(Cedrus deodara)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/20130903Cedrus_deodara2.jpg/2560px-20130903Cedrus_deodara2.jpg',
    'Cork oak(Quercus suber)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Quercus-suber-Cork-oak-SelecTree-e1636583698665.jpeg?fit=252%2C300&ssl=1',
    'Bay laurel(Laurus nobilis)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Laurus_nobilis_111.JPG/320px-Laurus_nobilis_111.JPG',
    'Purple blow maple(Acer truncatum)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Acer-truncatum-Shantung-maple-leaves-fall-color.jpg?fit=252%2C300&ssl=1',
    'Washington hawthorn(Crataegus phaenopyrum)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Crataegus_phaenopyrum_HRM.jpg/440px-Crataegus_phaenopyrum_HRM.jpg',
    'Wilga; australian willow(Geijera parviflora)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Geijera-parviflora-Australian-willow.jpg?fit=252%2C300&ssl=1',
    'California peppertree(Schinus molle)': 'https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcT_d99zrMeZHJOAGNUoFzLiDINGxLsRih7_CbBK--JUJINutws13Az-0acY1VLIDARSYL66qGueALwgnws',
    'Japanese flower crabapple(Malus floribunda)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Malus-floribunda-Japanese-crabapple-flowers.jpg?fit=252%2C300&ssl=1',
    'Goldenrain tree(Koelreuteria paniculata)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Koelreuteria-paniculata-Goldenrain-tree-flowers.jpg?fit=252%2C300&ssl=1',
    'Southern magnolia(Magnolia grandiflora)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Magnolia-grandiflora-Little-Gem-Little-Gem-magnolia-flower.jpg?fit=252%2C300&ssl=1',
    'Italian stone pine(Pinus pinea)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Pinus-pinea-Italian-stone-pine-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Hedge maple(Acer campestre)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Acer-campestre-Hedge-maple.jpg?fit=252%2C300&ssl=1',
    'Persian ironwood(Parrotia persica)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Parrotia-persica-Persian-ironwood-flowers-OSU.jpg?fit=252%2C300&ssl=1',
    'Eastern hophornbeam(Ostrya virginiana)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Ostrya-virginiana-OSU.jpg?fit=252%2C300&ssl=1',
    'Bur oak(Quercus macrocarpa)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/12/Quercus-macrocarpa-bur-oak-acorns-SelecTree-1.jpg?fit=252%2C300&ssl=1',
    'Chinese pistache(Pistacia chinensis)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Pistacia-chinensis-Chinese-pistache-fall-color-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Austrian pine(Pinus nigra)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Pinus-nigra-cone-SelecTree.jpg?fit=252%2C300&ssl=1',
    'California sycamore(Platanus racemosa)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/12/Platanus-racemosa-California-sycamore-2.jpg?fit=252%2C300&ssl=1',
    'Ponderosa pine(Pinus ponderosa)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Pinus-ponderosa-Ponderosa-pinecone-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Blue oak(Quercus douglasii)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Quercus-douglasii-1.jpg?fit=1815%2C2164&ssl=1',
    'Red maple(Acer rubrum)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Acer-rubrum-red-maple-1-1.jpg?fit=252%2C300&ssl=1',
    'Marina arbutus(Arbutus v. marina)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Arbutus-unedo-Marina-Strawberry-tree-leaves-and-flowers-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Eastern redbud(Cercis canadensis)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Cercis-canadensis-Eastern-redbud-6.jpg?fit=252%2C300&ssl=1',
    'Interior live oak(Quercus wislizeni)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/05/Quercus-wislizenii-5-scaled.jpeg?fit=668%2C1024&ssl=1',
    'Chinese flame tree(Koelreuteria bipinnata)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Koelreuteria-bipinnata-Chinese-flame-tree.jpg?fit=768%2C916&ssl=1',
    'Kentucky coffeetree(Gymnocladus dioicus)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Gymnocladus-dioica-Kentucky-coffeetree-young-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Chinese fringe tree(Chionanthus retusus)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Chionanthus-retusus-Chinese-fringe-tree-flowers.jpg?fit=252%2C300&ssl=1',
    'Afghan pine(Pinus eldarica)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/Pinus-eldarica-cones-SelecTre.jpg?fit=252%2C300&ssl=1',
    'Littleleaf linden(Tilia cordata)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Tilia-cordata-Little-leaf-linden.jpg?fit=252%2C300&ssl=1',
    'Baldcypress(Taxodium distichum)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2022/01/Taxodium-distichum-Bald-cypress-bark.jpg?fit=252%2C300&ssl=1',
    'European hornbeam(Carpinus betulus)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Carpinus-betulus-Fastigiata-European-hornbeam.jpg?fit=252%2C300&ssl=1',
    'Kurrajong(Brachychiton populneus)': 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQH4ov3BC-VZhHsz7eJmSJysMAfMKZSVl3uzUjgfsWVdwfu3AyI78q_tFbAiHZh1pgBtsLKDNOojSVNPNI',
    'Jeffrey pine(Pinus jeffreyi)': 'https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcRNQ_cLJK8E_inb1t9yCj-v42VODRrp0Hjzs3wPLFFNnZflX1TfFBi9BcL8c_BYkKD4dNWj_sxAbgv5Aug',
    'Japanese zelkova(Zelkova serrata)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Zelkova-serrata-Sawleaf-zelkova.jpg?fit=252%2C300&ssl=1',
    'Buckley oak(Quercus buckleyi)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Quercus-buckleyi-Texas-red-oak-leaves.jpg?fit=252%2C300&ssl=1',
    'California laurel(Umbellularia californica)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Umbellularia-californica-California-bay-laurel-leaves-SelecTree.jpg?fit=252%2C300&ssl=1',
    'Black tupelo(Nyssa sylvatica)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Nyssa-sylvatica-Tupelo-fall-color.jpg?fit=252%2C300&ssl=1',
    'Oregon ash(Fraxinus latifolia)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2021/03/Fraxinus-latifolia-Oregon-ash-fall-color-SelecTree.jpg?fit=252%2C300&ssl=1',
    'London plane(Platanus x acerifolia)': 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Platanus-acerfolia--josh-s-jackson--CC-BY-NC.jpg',
    'Shoestring acacia(Acacia stenophylla)': 'https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTjIZtZGTR_v_eG-ssLqAJv4cB0ALGqLup5IMNhg5XI1DdE-2SQ1tgfY3EXYAubN2tGBKkIHYej8nKOnaI',
    'Chestnut-leaved oak(Quercus castaneifolia)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Quercus_castaneifolia2_kew.jpg/440px-Quercus_castaneifolia2_kew.jpg',
    'Northern red oak(Quercus rubra)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Quercus_rubra_%40_Tortworth_Court.jpg/440px-Quercus_rubra_%40_Tortworth_Court.jpg',
    'Shumard oak(Quercus shumardii)': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/EncinoRojo.jpg/440px-EncinoRojo.jpg',
    'European hackberry(Celtis australis)': 'https://sactree.org/wp-content/uploads/2021/03/Celtis-australis-European-hackberry-canopy-SelecTree.jpg',
    'California white oak(Quercus lobata)': 'https://i0.wp.com/sactree.org/wp-content/uploads/2020/04/valley-oak-PFS.jpg?fit=252%2C300&ssl=1',
    'Japanese black pine(Pinus thunbergii)': 'https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcT-DDRcHhJK-ZwtThlZwOiG2t1-a1c9b7Sc5J-sL-II6JxmZjfFdT9SQcR1jRWVr3pCM4N6HkGEmCwJxK0',
    'Common fig(Ficus carica)': 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Ficus_carica_fruit_b_ICYrKNqDYB9v.jpeg'
}

#Format the structure of the page
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
                    style={'flex': '0.5', 'width': '400px', 'height': '400px', 'overflow': 'hidden', 'justify-content': 'center', 'align-items': 'center'}
                )
            ],
            style={"display": "flex", 'justify-content': 'center'}
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