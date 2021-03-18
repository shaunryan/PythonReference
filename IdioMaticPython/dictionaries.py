# https://www.youtube.com/watch?v=OSGv2VnC0go

from pprint import pprint

d = {
    'matthew': 'blue',
    'rachel': 'green',
    'raymond': 'red'
}


# method 1
for k in d:
    print(k)


# method 2 - when mutating the dictionary
delete = [k for k in d if k.startswith("r")]


# looping keys and values
for k, v in enumerate(d):
    print(v)


# construct dictionary using lists
names = ['Shaun', 'Sarah', 'Finley']
colors = ['red', 'green', 'yellow']

d = dict(zip(names, colors))
pprint(d)


# counting with dictionaries
colors = ['red', 'green', 'yellow', 'red', 'black']
d = {}
for c in colors:
    d[c] = d.get(c, 0) + 1

pprint(d)
# better
# https://realpython.com/python-defaultdict/
# default the dict using int(0)
from collections import defaultdict
d = defaultdict(int)
for c in colors:
    d[c] += 1



# group with dictionaries
d = {}
for c in colors:
    key = len(c)
    if key not in d:
        d[key] = []
    d[key].append(c)
pprint(d)
# better
d = {}
for c in colors:
    key = len(c)
    # if no key exist will insert key value pair
    d.setdefault(key, []).append(c)
pprint(d)
# better still
d = defaultdict(list)
for c in colors:
    key = len(c)
    d[key].append(c)
pprint(dict(d))

# 28:20