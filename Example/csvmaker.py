import json
import csv

with open('json1', 'r') as myfile:
    A= myfile.read().replace('\n', '')

A = json.loads(A)

f = csv.writer(open("test.csv", "wb+"))

f.writerow(["numberBlock", "timeFromLast"])

for x in A:
    f.writerow([x["numberBlock"],
                x["timeFromLast"]
                ])