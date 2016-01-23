import json
import string
import time
import rosette.api

from rosette.api import API, DocumentParameters, MorphologyOutput

def run(input, key="4a2ce33afde2071fd73b8c8f3977e4ea", altUrl='https://api.rosette.com/rest/v1/'):
    api = API(user_key=key, service_url=altUrl)
    content = ''.join(ch.lower() for ch in input if ch not in set(string.punctuation))
    params = DocumentParameters()
    params["content"] = content
    return api.morphology(params, MorphologyOutput.LEMMAS)

# conversta a list of strings into a list of its lemmas
def lemma_list(lst):
    result = run(str(lst))
    json_obj = json.loads(json.dumps(result, indent=2, ensure_ascii=False))
    lst = [dicti['lemma'] for dicti in json_obj['lemmas']]
    lst.sort()
    return lst

def convert_file():
    f = open('mthes/mobythes.aur', 'r')
    f = open('out.txt')
    line = f.readline()
    while line != "":
        time.sleep(.1)
        line = line.split(',')
        key = lemma_list(line[0:1])
        rest = lemma_list(line[1:])
        key.extend(rest)
        print(str(key))
        line = f.readline()
    f.close()
convert_file()