import gzip
import json
import os
import sys

if not os.path.exists('output'):
  os.makedirs('output')

outputFile = 'output/output.json'
outputMinFile = 'output/output.min.json'
outputMinGzipFile = 'output/output.min.json.gz'

outputList = []

numItems = 1000

for a in range(0, numItems):
  outputList.append({
    "index": a,
    "guid": "20c3e6d3-036e-4714-bd1d-1f5a03fb2be2",
    "eyeColor": "blue",
    "phone": "+1 (996) 494-3583",
    "address": "787 Louis Place, Townsend, Connecticut, 9325",
    "about": "Qui nulla officia ullamco nisi reprehenderit magna. Est excepteur fugiat ut adipisicing reprehenderit est magna tempor aute elit. Ullamco dolore aliquip velit excepteur ex.\r\n"
  })

output = json.dumps(outputList, indent = 2)
outputMinified = json.dumps(outputList, separators = (',', ':'))

with open(outputFile, 'wb') as outfile:
  outfile.write(output)

with open(outputMinFile, 'wb') as outfile:
  outfile.write(outputMinified)

with gzip.GzipFile(outputMinGzipFile, 'wb') as outfile:
  outfile.write((outputMinified).encode('utf-8'))

with gzip.GzipFile(outputMinGzipFile, 'r') as inputfile:
  gzipData = json.loads(inputfile.read().decode('utf-8'))

print("Number of Items " + str(numItems) + "\n")
print("Estimated Size: " + str(sys.getsizeof(output) / 1024) + "KB")
print("Actual Size: " + str(os.path.getsize(outputFile) / 1024) + "KB")
print("Estimated Minified Size: " + str(sys.getsizeof(outputMinified) / 1024) + "KB")
print("Actual Minified Size: " + str(os.path.getsize(outputMinFile) / 1024) + "KB")
print("Estimated Gzip Size: " + str(sys.getsizeof(gzipData) / 1024) + "KB")
print("Actual Gzip Size: " + str(os.path.getsize(outputMinGzipFile) / 1024) + "KB")