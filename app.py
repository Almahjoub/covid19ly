import dash
import datetime
import json
import pathlib
import pandas as pd

app = dash.Dash(__name__, meta_tags=[{'name' : 'viewport',
                                      'content' : 'width=device-width',
                                      'description' : 'COVID-19 Libya Dashboard'
                                      }
                                    ]
                                )
app.title = 'COVID-19 Libya'
server = app.server
app.config.suppress_callback_exceptions = True

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('data').resolve()

##### load data #####
# Libya geojson
with open(DATA_PATH.joinpath('libya_shapefile.geojson'), encoding='utf-8') as shapefile:
    geojson = json.load(shapefile)

# # Montreal cases per borough
# cases = pd.read_csv(DATA_PATH.joinpath('cases.csv'), encoding='utf-8', na_values='na').dropna(axis=1, how='all')
# borough_tbc = cases[-1:]  # Nb. of cases with borough TBC
# cases_df = cases[:-1]  # Nb. of cases with known borough
# cases_long = pd.melt(cases_df, id_vars='borough',
#                     var_name='date', value_name='cases')
# cases_per1000_df = pd.read_csv(DATA_PATH.joinpath('cases_per1000.csv'), encoding='utf-8', na_values='na').dropna(axis=1, how='all')
# cases_per1000_long = pd.melt(cases_per1000_df, id_vars='borough',
#                              var_name='date', value_name='cases_per_1000')

# Libya data
data = pd.read_csv(DATA_PATH.joinpath('data_ly.csv'), encoding='utf-8', na_values='na')

# Last update date
# Display 1 day after the latest data as data from the previous day are posted
latest_date = datetime.date.fromisoformat(data['date'].iloc[-1]) + datetime.timedelta(days=1)
latest_update_date = latest_date.isoformat()

# # Mini info boxes
latest_cases = str(int(data['cases_ly'].iloc[-1]))
latest_deaths = str(int(data['deaths_ly'].iloc[-1]))
latest_hospitalisations = str(int(data['hospitalisations_ly'].iloc[-1]))
latest_recovered = str(int(data['recovered_ly'].iloc[-1]))
latest_negative_tests = str(int(data['negative_tests_ly'].iloc[-1]))
