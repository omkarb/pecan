import wolframalpha
import bs4

def main():
    client = wolframalpha.Client(APP_ID)

    query = raw_input("Enter converstion topic: ")

    res = client.query(query)

    print "res: "
    print res

    print "results: "
    print res.results

    print "tree: "
    print res.tree

    print "pods: "
    print res.pods

    print "# pods: "
    print len(res.pods)

    for pod in res.pods:
        print(pod.text)
        print('---')

if __name__ == '__main__':
    main()
