import subject_popularity.sp
import transitional_topics.tt
import synopsis
import twitter_streaming
import Wolfram

def handle_query(query):
    sp_result = sp.look_up(query)
    tt_result = tt.look_up(query)
    syn_result = synopsis.wikipedia_summary(query)
    wol_result = Wolfram.main(query)
    twi_result = twitter_streaming