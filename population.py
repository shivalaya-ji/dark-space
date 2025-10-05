import pandas as pd

def year_with_highest_population(logs):
    if logs.empty:
        print("Error: No data to analyze (empty list or file).")
        return None, None

    min_year = int(logs['Birth'].min())
    max_year = int(logs['Death'].max())
    changes = [0] * (max_year + 2)
    for _, row in logs.iterrows():
        birth = int(row['Birth'])
        death = int(row['Death'])
        changes[birth] += 1
        changes[death] -= 1

    max_pop = 0
    curr_pop = 0
    year_max = min_year
    for year in range(min_year, max_year + 1):
        curr_pop += changes[year]
        if curr_pop > max_pop:
            max_pop = curr_pop
            year_max = year

    return year_max, max_pop

def main():
    try:
        file_path = input("Enter Excel file path (or press Enter for 'sample_population_data.xlsx'): ")
        if not file_path:
            file_path = 'sample_population_data.xlsx'

        df = pd.read_excel(file_path)
        print(f"Loaded {len(df)} entries from {file_path}")

        year_max, max_pop = year_with_highest_population(df)
        if year_max is not None:
            print(f"The year with the highest population is: {year_max}")
            print(f"Population in that year: {max_pop} people")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
