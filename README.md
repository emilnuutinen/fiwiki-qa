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
    Article(
      ask:{
        question:"When was the Liang-dynastia period?"
      }
      limit:1,
    ){
      title
      text
      _additional{
        answer{
          certainty
          result
          hasAnswer
        }
      }
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
          "_additional": {
            "answer": {
              "certainty": 0.7036854743957519,
              "hasAnswer": true,
              "result": "502 – 557"
            }
          },
          "text": "Liang-dynastia Liang-dynastia (梁 [liáng]) hallitsi osaa Etelä-Kiinasta 502 – 557. Liang-dynastia oli yksi Eteläisistä dynastioista. Muut Eteläiset dynastiat olivat: Liang-dynastia oli buddhalaisuuden kulta-aikaa Etelä-Kiinassa. Jiangkangissa sijaitsevassa hovissa kulttuuri kukoisti. Tämäkin rauhanaika kuitenkin päättyi sotilasperheiden (shijia 士家, binghu 兵戶) kapinointiin.  ",
          "title": "Liang-dynastia"
        }
      ]
    }
  }
}
```
