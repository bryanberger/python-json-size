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
      'type': 'immersive',
      'name': 'Software Engineering Immersive',
      'description':
        'Build rich, interactive, full-stack apps with key languages and dive into computer science essentials like algorithms, data structures, design patterns, and more.',
      'hours': '400+',
      'length': '12 weeks',
      'schedule': 'Mon-Fri',
      'topic_slugs': ['Coding', 'Data', 'Design', 'Marketing', 'Business', 'Career Development'],
      'locations': [
        'Atlanta',
        'Austin',
        'Boston',
        'Chicago',
        'Dallas',
        'Denver',
        'Detroit',
        'Houston',
        'London',
        'Los Angeles',
        'Melbourne',
        'Miami',
        'Minneapolis',
        'New York City',
        'Orlando',
        'Paris',
        'Phoenix',
        'Providence',
        'Raleigh',
        'San Diego',
        'San Francisco',
        'Seattle',
        'Singapore',
        'Stamford',
        'Sydney',
        'Toronto',
        'Washington D.C.',
      ],
      'urls': {
        'campus':
          'http://generalassemb.ly/education/software-engineering-immersive',
        'online':
          'http://generalassemb.ly/education/software-engineering-immersive-remote',
      },
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