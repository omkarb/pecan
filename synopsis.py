import wikipedia


# Search topic query
def search_topic():
    topic = input("Enter conversation topic: ")
    return topic


# Grab summary from wikipedia
def wikipedia_summary(query):
    return wikipedia.summary(query)


def main():
    topic = search_topic()
    print(wikipedia_summary(topic))

if __name__ == '__main__':
    main()
