import wolframalpha
import bs4
import requests

# Open Wolfram API ID from local file
def wolframapi():
    fileName = 'WolframAPI.txt'
    f = open(fileName, 'r')

    APP_ID = f.readline()
    return APP_ID

# Parse the suggested url given by xml
def parseExamplePage(url):
    website = requests.get(url)

    soup = bs4.BeautifulSoup(website.text, "html.parser")

    # find all suggested actions
    actions = soup.findAll("div", { "class" : "ex-caption" })

    # find all suggested examples
    examples = soup.findAll("span", { "class" : "content"})

    for action in actions:
        print action.text

    for example in examples:
        print example.text

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
        parseExamplePage(suggested_url)

    else:
        for pod in res.pods:
            #print(pod.title)
            print(pod.text)


if __name__ == '__main__':
    main()
