import csv
import json
 
 
def make_json(csvFilePath, jsonFilePath):

    data = []
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            if 'tags' in rows:
                tags = rows.get('tags').split(",")
                rows.update({"tags": tags})

                data.append(rows)
            else:
                data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

authors_csvFilePath = r'authors.csv'
authors_jsonFilePath = r'authors.json'

make_json(authors_csvFilePath, authors_jsonFilePath)

quotes_csvFilePath = r'quotes.csv'
quotes_jsonFilePath = r'quotes.json'

make_json(quotes_csvFilePath, quotes_jsonFilePath)