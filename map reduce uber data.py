from collections import defaultdict
uber_data = [
    {"base": "B02512", "date": "2014-01-01", "active_vehicles": 190, "trips": 1132},
    {"base": "B02512", "date": "2014-01-02", "active_vehicles": 200, "trips": 1200},
    {"base": "B02513", "date": "2014-01-01", "active_vehicles": 100, "trips": 800},
    {"base": "B02513", "date": "2014-01-02", "active_vehicles": 150, "trips": 1600},
    {"base": "B02513", "date": "2014-01-03", "active_vehicles": 170, "trips": 1600},
]
mapped = []
for row in uber_data:
    mapped.append((row["base"], (row["date"], row["trips"])))

print("Mapped Output:")
print(mapped)
shuffled = defaultdict(list)
for key, value in mapped:
    shuffled[key].append(value)

print("\nShuffled Output:")
for k, v in shuffled.items():
    print(k, ":", v)
results = {}

for base, values in shuffled.items():
    # Find max trips for this base
    max_trips = max(trip for _, trip in values)
    # Find all dates with this max trip count
    best_days = [date for date, trip in values if trip == max_trips]
    results[base] = {"max_trips": max_trips, "best_days": best_days}

print("\nFinal Results (Per Base):")
for base, stats in results.items():
    print(f"Base {base}: Max Trips = {stats['max_trips']} on {stats['best_days']}")

