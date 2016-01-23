import wolframalpha

APP_ID = "PXUYE6-7E7RWKKX3Y"


def main():
    client = wolframalpha.Client(APP_ID)
    query = "Kanye West"
    res = client.query(query)

    for pod in res.pods:
        print(pod.text)


if __name__ == '__main__':
    main()
