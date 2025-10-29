from collections import defaultdict
books = [
    {"Title": "BookA", "Author": "Author1", "PublishedYear": 2018, "Country": "India", "Language": "English", "Pages": 250},
    {"Title": "BookB", "Author": "Author2", "PublishedYear": 2019, "Country": "USA", "Language": "English", "Pages": 300},
    {"Title": "BookC", "Author": "Author3", "PublishedYear": 2018, "Country": "UK", "Language": "English", "Pages": 150},
    {"Title": "BookD", "Author": "Author4", "PublishedYear": 2020, "Country": "India", "Language": "Tamil", "Pages": 200},
    {"Title": "BookE", "Author": "Author5", "PublishedYear": 2019, "Country": "Canada", "Language": "French", "Pages": 180},
]
mapped = []
for book in books:
    year = book["PublishedYear"]
    mapped.append((year, 1))  # Emit (year, 1)
print("Mapped Output:")
print(mapped)
shuffled = defaultdict(list)
for key, value in mapped:
    shuffled[key].append(value)
print("\nShuffled Output:")
print(dict(shuffled))
reduced = {}
for year, values in shuffled.items():
    reduced[year] = sum(values)  # Sum counts per year
print("\nReduced Output (Books per Year):")
print(reduced)
max_year = max(reduced, key=reduced.get)
print(f"\nYear with maximum books published: {max_year} ({reduced[max_year]} books)")

