import json
import re

in_file = "test_data/example.txt"

fields =['title', 'text']

dict = {}

with open(in_file) as f:
    title, text = "", ""
    count = 0
    for line in f:
        if "<doc" in line:
            title = "".join(re.findall(r'title="([^;]*)">', line))
        if not "<doc" in line and line.strip():
            text += line.replace('\n', ' ').replace('</doc>',
                    '').replace('\xa0', '')
        if "</doc>" in line:
            if not ("tarkoittaa seuraavia" or "voi viitata seuraaviin asioihin") in text:
                article = [title,text]
                i = 0
                dict2 = {}
                while i<len(fields):
                    dict2[fields[i]]= article[i]
                    i += 1

                dict[count] = dict2
                count += 1
            text = ""

out_file = open('test_data/example.json', 'w')
json.dump(dict, out_file, indent=4, sort_keys=False)
out_file.close()
