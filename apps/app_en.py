from app import latest_update_date
from template import generate_layout

##### Label text (EN) #####
labels = {
    'language0' : '...',
    'language_link0' : '/',
    'title' : 'COVID-19 Libya Dashboard',
    'subtitle' : 'Last update: ' + latest_update_date,
    'cases_label' : 'Cases',
    'deaths_label' : 'Deaths',
    'recovered_label' : 'Recovered',
    'total_cases_label' : 'Confirmed cases',
    'total_deaths_label' : 'Deaths',
    'total_hospitalisations_label': 'Hospitalisations',
    'total_testing_label' : 'Diagnostic tests',
    'footer_left' : 'Data: [Link]() / Built with [Dash](https://plotly.com/dash/) / [Github](https://github.com/Almahjoub/covid19ly)',
    'footer_right' : 'Made by Alhusein Almahjoub & Jeremy Moreau / [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)',
    'infobox' : """
    ###### Useful resources
    
    - [Link](https://)

    Text
    """,
    'confirmed_cases_y_label' : 'Confirmed cases (cumulative)',
    'confirmed_cases_label' : 'Libya',
    'deaths_fig_label' : 'Deaths',
    'deaths_y_label' : 'Deaths (cumulative)',
    'hospitalisations_y_label' : 'Hospitalisations (cumulative)',
    'hospitalisations_label' : 'Hospitalisations',
    'recovered_y_label' : 'Recovered (cumulative)',
    'testing_y_label' : 'Cases (cumulative)',
    'negative_tests_label' : 'Negative tests',
    'positive_cases_label' : 'Confirmed positive cases',
    'date_slider_label' : 'Date: ',
    'date_label' : 'Date',
    'age_label' : 'Age',
    'linear_label' : 'Linear scale',
    'log_label' : 'Log scale',
    'map_label' : 'Cases per 1000 population (Map)',
    # 'map_colourbar_labels' : {
    #                                     'date': 'Date', 
    #                                     'borough': 'Borough/City',
    #                                     'cases_per_1000': 'Cases per 1000<br>population'
    #                                     },
    # 'map_hovertemplate' : '<br>Borough/City: %{location}<br>Cases per 1000 population: %{z}',
        # 'age_total_label' : 'Distribution of total<br>cases across age groups',
    # 'age_per100000_label' : 'Distribution of cases per<br>100,000 population in age group',
    # 'age_fig_hovertemplate' : '%: %{y}',
}

layout = generate_layout(labels)
