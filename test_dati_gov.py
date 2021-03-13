"""
Test del servizio Open Data del sito http://www.dati.gov.it
scritto da Gabriele Guizzardi
presso Contamination Lab - Univpm
durante hack.developers.italia.it 
"""

import requests
import json


API_BASE = 'http://www.dati.gov.it/api/3'
API_PACKAGE_SHOW = 'action/package_show'

def get_resources_by_id(id):
    url = f'{API_BASE}/{API_PACKAGE_SHOW}?id={id}'
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Resource not found!")


resources = get_resources_by_id('19dfee8a-60c3-4718-ad62-199735f7a16b')
print (json.dumps(resources, indent=4, sort_keys=True))
print ("Numero di resources: " + str(len(resources['result']['resources'])))
