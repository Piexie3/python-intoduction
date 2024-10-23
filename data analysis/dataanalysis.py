import csv

def read_life_expectancy_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            # Append data as a dictionary
            data.append({
                'entity': row[0],
                'code': row[1],
                'year': int(row[2]),
                'life_expectancy': float(row[3])
            })
    return data
def year_analysis(data, year):
    year_data = [entry for entry in data if entry['year'] == year]
    
    if not year_data:
        return None, None, None

    avg_life_expectancy = sum(entry['life_expectancy'] for entry in year_data) / len(year_data)
    max_life_expectancy = max(year_data, key=lambda x: x['life_expectancy'])
    min_life_expectancy = min(year_data, key=lambda x: x['life_expectancy'])

    return avg_life_expectancy, max_life_expectancy, min_life_expectancy

def main():
    
    data = read_life_expectancy_data("data analysis/life-expectancy.csv")
    
    year_choice= int(input("Enter the year of interest: "))
    
    avg_life, max_life, min_life = year_analysis(data, year_choice)
    
    if avg_life is not None:
        print(f"For the year {year_choice}:")
        print(f"The average life expectancy across all countries was {avg_life:.2f}")
        print(f"The max life expectancy was in {max_life['entity']} with {max_life['life_expectancy']:.2f}")
        print(f"The min life expectancy was in {min_life['entity']} with {min_life['life_expectancy']:.3f}")
    else:
        print(f"No data available for the year {year_choice}.")

if __name__ == "__main__":
    main()
