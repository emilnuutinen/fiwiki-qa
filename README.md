# Weaviate Wikipedia Search (Finnish Wikipedia, multilingual model)

Data: Finnish Wikipedia

Model: [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)


## Usage

1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8080`]().
3. Run `python import_data.py` to import the wine data to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8080`, navigate to the query module.
5. Run query's like:
```graphql
{
  Get {
    Article(limit: 3, nearText: {concepts: ["Mistä meidät on tehty"]}) {
      title
      text
    }
  }
}
```

Result is:

```graphql
{
  "data": {
    "Get": {
      "Article": [
        {
          "text": "Luettelo alkuaineista Tämä on luettelo tunnetuista alkuaineista....",
          "title": "Luettelo alkuaineista"
        },
        {
          "text": "Alkuaine Alkuaine määritellään aineeksi, jonka atomien ytimissä on tietty määrä protoneja....",
          title": "Alkuaine"
        },
        {
          "text": "Avaruus Avaruus on tähtitieteessä pääosin tyhjiön muodostama osa maailmankaikkeutta...",
          "title": "Avaruus"
        }
      ]
    }
  }
}
```
