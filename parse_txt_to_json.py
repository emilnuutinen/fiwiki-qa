import json
import re

in_file = "test_data/example.txt"

fields =['title', 'paragraphs']

articles = {}

with open(in_file) as f:
    paragraphs, cleaned_paragraphs = [], []
    paragraph, title = "", ""
    count = 0
    for line in f:
        if "<doc" in line:
            title = "".join(re.findall(r'title="([^;]*)">', line))
        if not "<doc" in line:
            paragraph += line.replace('</doc>','').replace('\n', '')
        if not line.strip():
              pass
        if "\n" in line:
            paragraphs.append(paragraph)
            paragraph = ""
        if "</doc>" in line:
            if not ("tarkoittaa seuraavia" or "voi viitata seuraaviin asioihin") in paragraph:
                for p in paragraphs:
                    if p.strip():
                        cleaned_paragraphs.append(p)
                article = [title,cleaned_paragraphs]
                i = 0
                dict2 = {}
                while i<len(fields):
                    dict2[fields[i]]= article[i]
                    i += 1

                articles[count] = dict2
                count += 1
            text = ""



out_file = open('test_data/example.json', 'w')
json.dump(articles, out_file, indent=4, sort_keys=False)
out_file.close()


