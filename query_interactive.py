import json
import weaviate
import readline

client = weaviate.Client("http://localhost:8484")


while True:
    question=input("Ask me something: ")

    ask = {
        "question": question,
        "rerank": True
    }

    result = (
        client.query
        .get("Article", ["title", "_additional {answer {hasAnswer certainty result} }"])
        .with_ask(ask)
        .with_limit(10)
        .do()
    )

    for article in result["data"]["Get"]["Article"]:
        title=article["title"]
        ans=article["_additional"]["answer"]
        if not ans["hasAnswer"]:
            print("Page:", title,"   ...no answer")
        else:
            print("Page:", title,"   ...",ans["result"])
    print()
    print()
    
        
