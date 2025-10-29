from collections import defaultdict
logs = [
    {"UserId": 111115, "TrackId": 222, "Shared": 0, "Radio": 1, "Skip": 0},
    {"UserId": 111113, "TrackId": 225, "Shared": 1, "Radio": 0, "Skip": 0},
    {"UserId": 111117, "TrackId": 223, "Shared": 0, "Radio": 1, "Skip": 1},
    {"UserId": 111115, "TrackId": 225, "Shared": 1, "Radio": 0, "Skip": 0},
]
mapped = []
for log in logs:
    mapped.append(("unique_listener", log["UserId"]))
    mapped.append(("shared", log["Shared"]))
    mapped.append(("radio", log["Radio"]))
    mapped.append(("listened_total", 1))   # each row = 1 listen
    mapped.append(("skipped", log["Skip"]))
print("Mapped Output (sample):")
print(mapped[:10])
shuffled = defaultdict(list)
for key, value in mapped:
    shuffled[key].append(value)

print("\nShuffled Output:")
for k, v in shuffled.items():
    print(k, ":", v)
results = {}
for key, values in shuffled.items():
    if key == "unique_listener":
        results[key] = len(set(values))  # count distinct UserIds
    else:
        results[key] = sum(values)       # sum for other fields

print("\nFinal Results:")
for k, v in results.items():
    print(f"{k}: {v}")

