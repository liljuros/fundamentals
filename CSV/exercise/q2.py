import csv


def write_data_to_csv(data, file_name):
    # Get the union of all keys across all dictionaries
    all_keys = set()
    for record in data:
        all_keys.update(record.keys())

    # Convert the set of keys to a sorted list (optional, for consistent column order)
    all_keys = sorted(all_keys)

    # Write to the CSV file
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=all_keys)

        # Write the header row
        writer.writeheader()

        # Write each row of the data
        for record in data:
            writer.writerow(record)


# Example usage
data = [
    {'a': '1_a', 'b': '1_b', 'c': '1_c'},
    {'c': '2_c', 'd': '2_d'},
    {'a': '3_a', 'c': '3_c', 'e': '3_e'}
]

write_data_to_csv(data, 'output.csv')
