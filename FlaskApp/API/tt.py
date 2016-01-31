import json
import string
import time
import wikipedia
import heapq
import api_key
import random

from rosette.api import API, DocumentParameters, MorphologyOutput, NameMatchingParameters

user_key = api_key.user_key
ros_url = api_key.ros_url


def run(input, key=user_key, alt_url=ros_url):
    api = API(user_key=key, service_url=alt_url)
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


# for converting thesaurus, does not need to be run
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
        i += 1
        line = f.readline()
    f.close()
    f2.close()


# convert_file()

def find_similar(key_word, key=user_key, alt_url=ros_url):
    api = API(user_key=key, service_url=alt_url)
    if len(key_word.split()) > 1:
        key_word = "_".join(key_word.split())
    params = DocumentParameters()
    params["content"] = key_word
    params["language"] = "eng"
    json_obj = json.loads(json.dumps(api.morphology(params, MorphologyOutput.LEMMAS),
                                     indent=2, ensure_ascii=False))
    return search_for(json_obj['lemmas'][0]['lemma'])


def parse_with_queue(json_obj, key_word):
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


def search_for(name, key=user_key, alt_url=ros_url):
    f = open('/var/www/FlaskApp/pecan/FlaskApp/API/out.txt', 'r')
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
    else:
        f.close()
        line.replace(name, "")
    line = line.split(",");
    random.shuffle(line)
    return line[:4]


#print(find_similar("deepsea"))


def proper_noun(key_word, key=user_key, alt_url=ros_url):
    api = API(user_key=key, service_url=alt_url)
    params = DocumentParameters()
    params["content"] = key_word
    params["language"] = "eng"
    api = api.morphology(params, MorphologyOutput.PARTS_OF_SPEECH)
    return "PROP" in str(json.loads(json.dumps(api, indent=2, ensure_ascii=False)))


# print(proper_noun("Jianqial Liu"))
# ->True

def proper_key_words(key_word, key=user_key, alt_url=ros_url):
    # Create an API instance
    api = API(user_key=key, service_url=alt_url)

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
    return parse_with_queue(json_obj, key_word)


    # print(str(proper_key_words("Barrack Obama")))
    # ->['president', 'U.S.', "American', 'United States']

def look_up(key_word, key=user_key, alt_url=ros_url):
    if proper_noun(key_word):
        return proper_key_words(key_word);
    else:
        return find_similar(key_word)
