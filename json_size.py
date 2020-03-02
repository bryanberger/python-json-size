import gzip
import json
import os
import sys

if not os.path.exists('output'):
  os.makedirs('output')

outputFile = 'output/output.json'
outputMinFile = 'output/output.min.json'
outputMinGzipFile = 'output/output.min.json.gz'

dict = {}

numItems = 1000

for a in range(0, numItems):
  dict[a] = {
    'firstname': 'SomeValue',
    'lastname': 'SomeValue',
    'favoriteColor': 'SomeColor'
  }

output = json.dumps(dict, indent = 2)
outputMinified = json.dumps(dict, separators = (',', ':'))

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