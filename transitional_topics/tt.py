import json
import string
import time
import wikipedia
import heapq
import rosette.api

from rosette.api import API, DocumentParameters, MorphologyOutput, NameMatchingParameters

user_key = "7633a1fc4dab2a460ec878d2f42b1972"
ros_url = 'https://api.rosette.com/rest/v1/'

def run(input, key=user_key, altUrl=ros_url):
    api = API(user_key=key, service_url=altUrl)
    content = ''.join(ch.lower() for ch in input if ch not in set(string.punctuation))
    params = DocumentParameters()
    params["content"] = content
    params["language"] = "eng"
    return api.morphology(params, MorphologyOutput.LEMMAS)


# converts a a list of strings into a list of its lemmas
def lemma_list(lst):
    result = run(str(lst))
    json_obj = json.loads(json.dumps(result, indent=2, ensure_ascii=False))
    lst = [dicti['lemma'] for dicti in json_obj['lemmas']]
    lst.sort()
    return lst


def convert_file():
    f = open('mthes/mobythes.aur', 'r')
    f2 = open('out2.txt', 'w')
    line = f.readline()
    i = 1
    while line != "":
        time.sleep(.1)
        line = line.split(',')
        key = lemma_list(line[0:1])
        rest = lemma_list(line[1:])
        key.extend(rest)
        f2.write(",".join(key) + "\n")
        print(i)
        i+=1
        line = f.readline()
    f.close()
    f2.close()

#convert_file()

def find_similar(key_word, key=user_key, altUrl=ros_url):
    api = API(user_key=key, service_url=altUrl)
    if len(key_word.split()) > 1:
        key_word = "_".join(key_word.split())
    params = DocumentParameters()
    params["content"] = key_word
    params["language"] = "eng"
    json_obj = json.loads(json.dumps(api.morphology(params, MorphologyOutput.LEMMAS),
                                   indent=2, ensure_ascii=False))
    return search_for(json_obj['lemmas'][0]['lemma'])


def search_for(name: string):
    f = open('out.txt', 'r')
    line = f.readline()
    while not (line == "" or line.split(",")[0] == name):
        line = f.readline()
    if line == "":
        f.seek(0)
        line = f.readline()
        while not (line == "" or name in line):
            line = f.readline()
        if line == "":
            f.close()
            return "No keyword found"

        else:
            line.replace(name, "")
            f.close()
            return line
    else:
        f.close()
        line.replace(name, "");
        return line

#print(find_similar("down"))

def proper_noun(key_word, key=user_key, altUrl=ros_url):
     api = API(user_key=key, service_url=altUrl)
     params = DocumentParameters()
     params["content"] = key_word
     params["language"] = "eng"
     api = api.morphology(params, MorphologyOutput.PARTS_OF_SPEECH)
     return "PROP" in str(json.loads(json.dumps(api, indent=2, ensure_ascii=False)))

#print(proper_noun("Jianqial Liu"))

def proper_key_words(key_word, key=user_key, altUrl=ros_url):
    # Create an API instance
    api = API(user_key=key, service_url=altUrl)

    params = NameMatchingParameters()
    params['name1'] = key_word
    max = ['error', 0]
    for x in wikipedia.search(key_word):
        params["name2"] = x
        val = json.loads(json.dumps(api.matched_name(params), indent=2,
                                    ensure_ascii=False))['result']['score'] > max[1]
        if val > max[1]:
            max = [x, val]
    params = DocumentParameters()
    params['content'] = wikipedia.summary(max[0])
    json_obj = json.loads(json.dumps(api.entities(params), indent=2, ensure_ascii=False,
                                 sort_keys=True))
    queue = []
    for x in json_obj['entities']:
        if x['normalized'] in key_word:
            continue
        confidence = int(x['confidence'])
        if len(queue) < 4:
            heapq.heappush(queue, (confidence, x['normalized']))
        elif queue[0][0] > confidence:
            heapq.heappushpop(queue, (confidence, x['normalized']))
    return [x[1] for x in queue]


print(str(proper_key_words("Barrack Obama")))