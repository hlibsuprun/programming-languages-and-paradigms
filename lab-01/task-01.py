def split_packages(weights, max_weight):
    for weight in weights:
        if weight > max_weight:
            raise ValueError(f"Package weight {weight} exceeds the allowed maximum weight per trip ({max_weight} kg).")

    sorted_weights = sorted(weights, reverse=True)
    trips = []

    for weight in sorted_weights:
        added = False
        for trip in trips:
            if sum(trip) + weight <= max_weight:
                trip.append(weight)
                added = True
                break

        if not added:
            trips.append([weight])

    return len(trips), trips


weights = [20, 5, 8, 15, 10, 10, 7]
max_weight = 25

num_trips, trips = split_packages(weights, max_weight)
for i, trip in enumerate(trips, 1):
    print(f"Trip {i}: {trip} \t Total weight: {sum(trip)} kg")
