import Wolfram
import sp
import synopsis
import tt
import api_key
import json
import twitter_streaming as ts
from rosette.api import API, DocumentParameters

user_key = api_key.user_key
ros_url = api_key.ros_url

def handle_query(query):
    syn_result = synopsis.wikipedia_summary(query)
    sp_result = sp.look_up(query)
    tt_result = tt.look_up(query)
    wol_result = Wolfram.main(query)
    #   twi_result = ts.timed_process(query)

    info = {
        "syn": syn_result,
        "sp": sp_result,
        "tt": tt_result,
        "wol": wol_result,
        #        "twi": twi_result
    }
    return info


def get_synopsis(syn):
    return syn
    #return "<p>" + syn + "</syn>"


def get_tt(tt):
    return tt
    #result = "<ul> "
    #for x in tt: result += "<li>" + x + "</li>"
    #result += "</ul>"
    #return result


def get_wol(wol, key=user_key, alt_url=ros_url):
    lst = wol.split("|")
    lst.sort(key=lambda a: len(a))
    api = API(user_key=user_key, service_url=alt_url)
    params = DocumentParameters()
    params['language'] = 'eng'
    rtotal = []
    for line in lst:
        params['content'] = line
        json_obj = json.loads(json.dumps(api.entities(params, True), indent=2,
                                         ensure_ascii=False))
        if json_obj['entities'] and len(rtotal) < 4:
            rtotal.append(line)
    result = "<ul> "
    for x in lst: result += "<li>" + x + "</li>"
    result += "</ul>"
    return result
