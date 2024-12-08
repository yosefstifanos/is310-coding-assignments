import requests
import apikey
import os

# the_one_api_key = apikey.load('THE_ONE_API_KEY')
# authorization_headers = {"Authorization" : 'Bearer ' + the_one_api_key }

# url = 'https://the-one-api.dev/v2/character'
# response = requests.get(url, headers=authorization_headers)
# print(response.json().keys())


europeana_api_key = apikey.load("EUROPEANA_API_KEY")
os.environ["EUROPEANA_API_KEY"] = europeana_api_key

import pyeuropeana.apis as apis
import pyeuropeana.utils as utils

# use this function to search our collections
result = apis.search(
   query = '*',
   qf = '(skos_concept:"http://data.europeana.eu/concept/base/48" AND TYPE:IMAGE)',
   reusability = 'open AND permission',
   media = True,
   thumbnail = True,
   landingpage = True,
   colourpalette = '#0000FF',
   theme = 'photography',
   sort = 'europeana_id',
   profile = 'rich',
   rows = 1000,
   ) # this gives you full response metadata along with cultural heritage object metadata

   # use this utility function to transform a subset of the cultural heritage object metadata
   # into a readable Pandas DataFrame
dataframe = utils.search2df(result)