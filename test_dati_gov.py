"""
Test del servizio Open Data del sito http://www.dati.gov.it
scritto da Gabriele Guizzardi
presso Contamination Lab - Univpm
durante hack.developers.italia.it 
"""
import urllib
import json
import timeit


def pp_json(json_thing, sort=True, indents=4):

    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return ""

start = timeit.default_timer()
url = 'http://www.dati.gov.it/api/3/action/package_show?id=personale-provinciale-rapporto-lavoro-non-tempo-indeterminato'
result = json.load(urllib.urlopen(url))
print pp_json(result)

item_dict = json.load(urllib.urlopen(url))
print "Numero di resources: " + str(len(item_dict['result']['resources']))

stop = timeit.default_timer()

print "Tempo: " + str(stop - start)
