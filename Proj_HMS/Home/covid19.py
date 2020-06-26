import json
from urllib.request import urlopen

with urlopen("https://api.rootnet.in/covid19-in/stats/latest") as response:
    source = response.read()

datal = json.loads(source)

total_case = datal['data']['summary']['total']
dis = datal['data']['summary']['discharged']
death = datal['data']['summary']['deaths']
ls= datal['lastRefreshed']


def findstate(state):
    dat = dict()
    for reg in datal['data']['regional']:
        if(reg['loc']== str(state)):
            dat['rt'] = reg["totalConfirmed"]
            dat['de'] = reg['deaths']
            dat['di'] = reg['discharged']


    return dat
            
