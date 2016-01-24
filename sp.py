import requests


months = {0: "Jan", 1: "Feb", 2: "Mar", 3: "Apr", 4: "May",
          5: "Jun", 6: "Jul", 7: "Aug", 8: "Sep", 9: "Oct",
          10: "Nov", 11: "Dec"}


def look_up(key_word):
    url = 'http://www.google.com/trends/fetchComponent?hl=en-US&q=' + key_word + \
          '&cid=TIMESERIES_GRAPH_0&export=5&w=500&h=300'
    try:
        r = requests.get(url, timeout=2)
    except requests.exceptions.RequestException as e:
        return "Unexpected error with message: " + e
    if "chartData" not in r.text and "drawChart()" not in r.text:
        return "Did not successfuly scrape google"
    return parse_insane(r.text)


def read_between(strg, char1, char2):
    return strg[strg.find(char1):strg.find(char2) + 1]


def parse_single(target_string):
    actual_target = target_string.split("},")
    val = int(actual_target[1].split(",")[2])
    first = read_between(actual_target[0], "(", ")").split(",")
    year = first[0].strip(' ()')
    month = months[int(first[1].strip())]
    return month + " " + year, val


def parse_insane(string):
    split = "[" + read_between(string, "[[", "]]") + "]"
    splitted = split.split("],[")
    return [parse_single(x) for x in splitted]
