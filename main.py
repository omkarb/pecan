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
    twi_result = ts.timed_process(query)

    info = {
        "syn": syn_result,
        "sp": sp_result,
        "tt": tt_result,
        "wol": wol_result,
        "twi": twi_result
    }
    return info

print(handle_query("nba"))

