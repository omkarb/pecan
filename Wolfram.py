import wolframalpha
import re
import bs4
import requests

# Open Wolfram API ID from local file
def wolframapi():
    fileName = 'WolframAPI.txt'
    f = open(fileName, 'r')

    APP_ID = f.readline()
    return APP_ID


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr,'', raw_html)
    return cleantext


def main():
    # get the Wolfram API
    APP_ID = wolframapi()

    # Connect to Wolfram
    client = wolframalpha.Client(APP_ID[:-1])

    query = raw_input("Enter converstion topic: ")

    res = client.query(query)

    # When query is broad
    if (len(res.pods) == 0):
        suggested_url = res.tree.find('examplepage').get('url')
        website = requests.get(suggested_url)
        soup = bs4.BeautifulSoup(website.text, "html.parser")

        actions = soup.findAll("div", { "class" : "ex-caption" })
        examples = soup.findAll("span", { "class" : "content"})

        for action in actions:
            print action.text

        for example in examples:
            print example.text

    #new_res = client.query(split_uppercase(suggested_query))

    #print  ET.tostring(res.tree.getroot())
    # Print pods
    else:
        for pod in res.pods:
            print(pod.title)
            print(pod.text)
            print('')

if __name__ == '__main__':
    main()
