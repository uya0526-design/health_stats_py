import csv

def load_data(file_path: str) -> list[dict]:
    '''Data loading process
    Reads CSV column headers as a dictionary.
    Converts `systolic` to `int`, `weight` to `float`, and retrieves others as `str`.
    Skips rows as invalid if required columns are missing, numerical conversion is not possible, or `period` is anything other than `morning` or `evening`.
    Displays a message if the file cannot be retrieved or if there are invalid rows.'''
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
            required_columns = {'date', 'time', 'period', 'systolic', 'diastolic', 'weight'}
            return_data = []
            for index, row in enumerate(data):
                if len(required_columns.difference(row.keys())) > 0:
                    print(f"Required columns are missing at record {index + 1}")
                    continue
                if 'systolic' in row:
                    try:
                        row['systolic'] = int(row['systolic'])
                    except ValueError:
                        print(f"Error converting numerical value(systolic) at record {index + 1}")
                        continue
                if 'diastolic' in row:
                    try:
                        row['diastolic'] = int(row['diastolic'])
                    except ValueError:
                        print(f"Error converting numerical value(diastolic) at record {index + 1}")
                        continue
                if 'weight' in row:
                    try:
                        row['weight'] = float(row['weight'])
                    except ValueError:
                        print(f"Error converting numerical value(weight) at record {index + 1}")
                        continue
                if 'period' in row and row['period'] not in ['morning', 'evening']:
                    print(f"Invalid period: {row['period']} at record {index + 1}")
                    continue
                return_data.append(row)
            return return_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def is_data_empty(data: list[dict]) -> bool:
    '''Check if the data list is empty'''
    return len(data) == 0

def filter_data_by_period(data: list[dict], period: str) -> list[dict]:
    '''Filter data by period
    Returns a list containing only data where the period is the same as the input period.'''
    return [record for record in data if record['period'] == period]

def calc_stats(data: list[int | float]) -> dict:
    '''Calculate statistics
    Returns the average, maximum, and minimum values ​​of a list of numbers in a dictionary.'''
    average = round(sum(data) / len(data), 2)
    maximum = round(max(data), 2)
    minimum = round(min(data), 2)
    return {
        'average': average,
        'maximum': maximum,
        'minimum': minimum
    }

def calc_weight_stats(data: list[dict]) -> dict:
    '''Regarding weight, calculate the average, maximum, and minimum values.'''
    return calc_stats([record['weight'] for record in data])

def calc_blood_pressure_stats(data: list[dict]) -> dict:
    '''For systolic and diastolic blood pressure, calculate the average, maximum, and minimum values.'''
    return {
        'systolic': calc_stats([record['systolic'] for record in data]),
        'diastolic': calc_stats([record['diastolic'] for record in data])
    }
