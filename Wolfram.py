import wolframalpha
import xml.etree.ElementTree as ET

# Open Wolfram API ID from local file
def wolframapi():
    fileName = 'WolframAPI.txt'
    f = open(fileName, 'r')

    APP_ID = f.readline()
    return APP_ID

def main():
    # get the Wolfram API
    APP_ID = wolframapi()

    # Connect to Wolfram
    client = wolframalpha.Client(APP_ID[:-1])

    query = raw_input("Enter converstion topic: ")

    res = client.query(query)

    print "res: "
    print res

    print "results: "

    for r in res.results:
        print r

    print "tree: "
    #print  ET.tostring(res.tree.getroot())

    print res.tree.find('examplepage').get('category')

    print "pods: "
    print res.pods

    print "# pods: "
    print len(res.pods)

    for pod in res.pods:
        print(pod.text)
        print('---')

if __name__ == '__main__':
    main()
