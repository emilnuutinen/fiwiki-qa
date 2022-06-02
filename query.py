import weaviate

client = weaviate.Client("http://localhost:8484")

query = '{Get {Article(ask:{question:"When was the Liang-dynastia period?" rerank:true} limit:3,){title text _additional{answer{certainty result hasAnswer}}}}}'


result = client.query.raw(query)

print(result)
