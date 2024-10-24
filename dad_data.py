# Victoria Lutz
import pathlib
from pathlib import Path

maximum = 0
minimum = 100
minimum_country = ''
maximum_country = ''
min_year = ''
max_year = ''

file_path = Path('../life-expectancy.csv')
text = file_path.read_text().rstrip()
lines = text.splitlines()

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


print(
    f'The max life expectancy was in {maximum_country} with {maximum} in the year {max_year}')
print(
    f'The minimum life expectancy was in {minimum_country} with {minimum} in the year {min_year}')
