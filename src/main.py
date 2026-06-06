import calc

def main() -> None:
    '''Main function
    Displays the menu and waits for the user to select a menu number.
    Calls the appropriate function based on the menu number.
    Exits the program if the user selects the exit menu.'''
    print("Health Stats")
    file_path = "data/health_data.csv"
    data = []
    data = calc.load_data(file_path)
    while True:
        print("-------------")
        print("1. Load Data")
        print("2. Display All Health Records")
        print("3. Display Average, Maximum, and Minimum Blood Pressure (Systolic and Diastolic) for the Entire Period")
        print("4. Display Average, Maximum, and Minimum Weight for the Entire Period")
        print("5. Display Summary by Morning/Evening")
        print("6. Exit")
        print("-------------")
        print("Enter the menu number: ", end="")
        menu_number = input()
        if menu_number == "1":
            data = calc.load_data(file_path)
        elif menu_number == "2":
            if calc.is_data_empty(data):
                print("No data found")
                continue
            else:
                'Display all health records'
                for index, record in enumerate(data):
                    print(f"Index: {index + 1}, Date: {record['date']}, Time: {record['time']}, Period: {record['period']}, Systolic: {record['systolic']}, Diastolic: {record['diastolic']}, Weight: {record['weight']}")
                print(f"Record count: {len(data)}")
                continue
        elif menu_number == "3":
            if calc.is_data_empty(data):
                print("No data found")
                continue
            else:
                'Display average, maximum, and minimum blood pressure (systolic and diastolic) for the entire period'
                blood_pressure_stats = calc.calc_blood_pressure_stats(data)
                print(f"Blood Pressure (Systolic / Diastolic):")
                print(f"    Average: {blood_pressure_stats['systolic']['average']} / {blood_pressure_stats['diastolic']['average']}")
                print(f"    Maximum: {blood_pressure_stats['systolic']['maximum']} / {blood_pressure_stats['diastolic']['maximum']}")
                print(f"    Minimum: {blood_pressure_stats['systolic']['minimum']} / {blood_pressure_stats['diastolic']['minimum']}")
        elif menu_number == "4":
            if calc.is_data_empty(data):
                print("No data found")
                continue
            else:
                'Display average, maximum, and minimum weight for the entire period'
                weight_stats = calc.calc_weight_stats(data)
                print(f"Weight:")
                print(f"    Average: {weight_stats['average']}")
                print(f"    Maximum: {weight_stats['maximum']}")
                print(f"    Minimum: {weight_stats['minimum']}")
        elif menu_number == "5":
            if calc.is_data_empty(data):
                print("No data found")
                continue
            else:
                'Display summary by morning/evening'
                morning_data = calc.filter_data_by_period(data, 'morning')
                evening_data = calc.filter_data_by_period(data, 'evening')
                morning_blood_pressure_stats = calc.calc_blood_pressure_stats(morning_data)
                evening_blood_pressure_stats = calc.calc_blood_pressure_stats(evening_data)
                morning_weight_stats = calc.calc_weight_stats(morning_data)
                evening_weight_stats = calc.calc_weight_stats(evening_data)
                print(f"Morning:")
                print(f"    Blood Pressure (Systolic / Diastolic):")
                print(f"        Average: {morning_blood_pressure_stats['systolic']['average']} / {morning_blood_pressure_stats['diastolic']['average']}")
                print(f"        Maximum: {morning_blood_pressure_stats['systolic']['maximum']} / {morning_blood_pressure_stats['diastolic']['maximum']}")
                print(f"        Minimum: {morning_blood_pressure_stats['systolic']['minimum']} / {morning_blood_pressure_stats['diastolic']['minimum']}")
                print(f"    Weight:")
                print(f"        Average: {morning_weight_stats['average']}")
                print(f"        Maximum: {morning_weight_stats['maximum']}")
                print(f"        Minimum: {morning_weight_stats['minimum']}")
                print(f"Evening:")
                print(f"    Blood Pressure (Systolic / Diastolic):")
                print(f"        Average: {evening_blood_pressure_stats['systolic']['average']} / {evening_blood_pressure_stats['diastolic']['average']}")
                print(f"        Maximum: {evening_blood_pressure_stats['systolic']['maximum']} / {evening_blood_pressure_stats['diastolic']['maximum']}")
                print(f"        Minimum: {evening_blood_pressure_stats['systolic']['minimum']} / {evening_blood_pressure_stats['diastolic']['minimum']}")
                print(f"    Weight:")
                print(f"        Average: {evening_weight_stats['average']}")
                print(f"        Maximum: {evening_weight_stats['maximum']}")
                print(f"        Minimum: {evening_weight_stats['minimum']}")
                continue
        elif menu_number == "6":
            print("Exiting program...")
            return
        else:
            print("Invalid menu number")

if __name__ == "__main__":
    main()
