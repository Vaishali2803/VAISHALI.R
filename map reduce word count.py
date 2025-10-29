!pip install mrjob
from collections import defaultdict
data = [
    "Hadoop MapReduce is simple",
    "MapReduce works with big data",
    "MapReduce is powerful"
]
def mapper(line):
    for word in line.split():
        yield word.lower(), 1
mapped = []
for line in data:
    mapped.extend(mapper(line))
print("Mapped Output:")
print(mapped)
shuffled = defaultdict(list)
for word, count in mapped:
    shuffled[word].append(count)
print("\nShuffled Output:")
print(dict(shuffled))
def reducer(word, counts):
    return word, sum(counts)
reduced = []
for word, counts in shuffled.items():
    reduced.append(reducer(word, counts))
print("\nReduced Output (Final Word Count):")
print(reduced)

