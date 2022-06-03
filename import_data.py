import json
import weaviate

client = weaviate.Client("http://localhost:8080")

schema_class = {
    "class": "Article",
    "properties": [
        {
            "name": "title",
            "dataType": ["text"]
        },
        {
            "name": "text",
            "dataType": ["text"]
        }
    ]
}

new_class = client.schema.create_class(schema_class)

file = open('test_data/example.json')
data = json.load(file)

def add_data(data, batch_size=2):
    no_items_in_batch = 0

    for index in data:
        data_object = {
            "title": data[index]["title"],
            "text": data[index]["text"],
        }
        client.batch.add_data_object(data_object, "Article")
        no_items_in_batch += 1
        if no_items_in_batch >= batch_size:
            results = client.batch.create_objects()
            no_items_in_batch = 0
    client.batch.create_objects()
add_data(data)
