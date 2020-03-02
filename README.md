# Simple json object array byte size estimator

## Why?
I wanted to estimate the size of the JSON output of an array full of the same object.

## How To
- open `json_size.py`
- edit the `numItems` to account for how many items to estimate.
- edit the object to duplicate.

## Run
```
$ python json_size.py
```

## Output
This script outputs the mock json, minified json, and gzipped json into a local `output` folder:

```
Number of Items 1000

Estimated Size: 1206KB
Actual Size: 1206KB
Estimated Minified Size: 851KB
Actual Minified Size: 851KB
Estimated Gzip Size: 48KB
```

#### Credits
Based on the SO answer here: https://stackoverflow.com/a/39047897