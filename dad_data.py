# Victoria Lutz
from pathlib import Path

maximum = float('-inf')
minimum = float('inf')
minimum_country = ''
maximum_country = ''
year_sum = 0
year_count = 0
year_average = 0
year_min = float('inf')
year_min_country = ''
year_max = float('-inf')
year_max_country = ''

file_path = Path('../life-expectancy.csv')
text = file_path.read_text().rstrip()
lines = text.splitlines()

year_input = input("Enter the year of interest: ")

for index, line in enumerate(lines):
    if index > 0:
        parts = line.split(',')
        country = parts[0]
        code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])
        if life_expectancy < minimum:
            minimum = life_expectancy
            minimum_country = country
            min_year = year
        if life_expectancy > maximum:
            maximum = life_expectancy
            maximum_country = country
            max_year = year
        if year == year_input:
            year_sum += life_expectancy
            year_count += 1
            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_country = country
            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_country = country

print(
    f'\nThe overall max life expectancy is: {maximum} from {maximum_country} in {max_year}')
print(
    f'The overall min life expectancy is: {minimum} from {minimum_country} in {min_year}')

if year_count > 0:
    year_average = year_sum / year_count
    print(f"\nFor the year {year_input}:")
    print(
        f"\tThe average life expectancy across all countries was {year_average}")
    print(
        f"\tThe max life expectancy was in {year_max_country} with {year_max}")
    print(
        f"\tThe min life expectancy was in {year_min_country} with {year_min}")
else:
    print("\nThere is no data available for the year you entered. ")
