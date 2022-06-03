# Weaviate Wikipedia Search (Finnish Wikipedia, multilingual model)

Data: Finnish Wikipedia

Model: [paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)


## Usage (with Weaviate console)

1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8484`]().
3. Run `python import_data.py` to import the wine data to Weaviate.
4. Navigate to [console.semi.technology](https://console.semi.technology/), connect to `http://localhost:8484`, navigate to the query module.
5. Run query's like:
```graphql
{
  Get {
    Article(
      ask:{
        question:"Who is the grandfather of Aleksis Kivi?"
        rerank:true
      }
      limit:3,
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
              "certainty": 0.4585587501525879,
              "hasAnswer": true,
              "result": "anders johan stenvall"
            }
          },
          "text": "Aleksis Kivi Aleksis Kivi (oik. Alexis Stenvall;Kivien nimet. Yle.fi: Aristoteleen kantaapää. 10. lokakuuta 1834 Nurmijärvi – 31. joulukuuta 1872 Tuusula) oli suomalainen kirjailija. Kivi kirjoitti kansallisromaanin aseman saavuttaneen romaanin \"Seitsemän veljestä\" (1870), näytelmiä kuten \"Nummisuutarit\" (1864) ja runoja.\"Suuri henkilökirja\" 2001, s.336. Kiven teksteissä on sekä romanttisia että realistisia piirteitä. Kivi kykeni luomaan usealla kirjallisuuden alalla korkeatasoisen tuotannon aikana, jolloin suomenkielisen kirjallisuuden perinnettä, kansanrunoutta lukuun ottamatta, ei ollut olemassa. Kivi oli ensimmäinen suomalainen ammattikirjailija. 1900-luvun alun Kivi-renessanssista alkaen hän on ollut Suomen kansalliskirjailija. Useita Aleksis Kiven runoja ja teoksiin sisältyviä laulutekstejä on sävelletty lauluiksi. Näitä ovat muun muassa ”Onnelliset”, ”Keinu”, ”Metsämiehen laulu”, ”Oravan laulu”, ”Sydämeni laulu”, ”Seitsemän miehen voima” ja ”Mitä minä huolin”. Kiven isoisän isällä Johan Stenvallilla oli ollut Nurmijärven Palojoella sotilastorppa vuodesta 1766. Vanhimmat tunnetut esivanhemmat ovat Yrjö Blomstedtin mukaan Janakkalasta. Äidinisä Antti Hamberg eli seppänä Tuusulan Nahkelassa. Aleksis Kiven isänisä Anders Johan Stenvall oli merimies. Kirjailijan oma isä Erik Stenvall oli asunut lapsuutensa Helsingissä.......
          ",
          "title": "Aleksis Kivi"
        },
        ....
```

### Testing locally


1. Start up Weaviate: `docker-compose up -d`. Once completed, Weaviate is running on [`http://localhost:8484`]().
2. Run `python import_data.py` to import the test data to Weaviate.
3. Replace the query in `query.py` with your own.
4. Run `python query.py > result.txt`
