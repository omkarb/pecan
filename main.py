import Wolfram
import sp
import synopsis
import tt
import twitter_streaming as ts


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
    return "<p>" + syn + "</syn>"


def get_tt(tt):
    result = "<ul> "
    for x in tt: result += "<li>" + x + "</li>"
    result += "</ul>"
    return result

def get_wol(wol):
    lst = wol.split("|")
    lst = sorted(lst, key=lambda sentence: len(sentence))
    result = "<ul> "
    for x in lst[:4]: result += "<li>" + x + "</li>"
    result += "</ul>"
    return result

print(get_wol(handle_query("Kanye")['wol']))
