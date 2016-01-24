import wikipedia
import api_key
import json
from rosette.api import API, NameMatchingParameters
user_key = api_key.user_key
ros_url = api_key.ros_url

# Search topic query
def search_topic():
    topic = input("Enter conversation topic: ")
    return topic


# Grab summary from wikipedia
def wikipedia_summary(query, key=user_key, alt_url=ros_url):
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
    if max[0] != 'error':
        return wikipedia.summary(max[0])
    else:
        raise Exception("No wiki articles found")


def main():
    topic = search_topic()
    print(wikipedia_summary(topic).substring())

if __name__ == '__main__':
    main()
