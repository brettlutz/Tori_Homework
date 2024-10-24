#Victoria Lutz
import pathlib
from pathlib import Path

maximum = 0
minimum = 100
minimum_country = ''
maximum_country = ''
min_year = ''
max_year = ''

file_path = Path('life-expectancy.csv')
text = file_path.read_text()


for index, line in enumerate(text):
    parts = text.split(',')
    country = parts[0]
    code = parts [1]
    Year = parts[2]
    Life_expectancy = parts[3]
if Life_expectancy < minimum:
    Life_expectancy = minimum
    country = minimum_country
    year = min_year
elif Life_expectancy > maximum:
    Life_expectancy = maximum
    country = maximum_country
    year = max_year

     
print (f'The max life expectancy was in {maximum_country} with {maximum} in the year {max_year}')
print (f'The minimum life expectancy was in {minimum_country} with {minimum} in the year {min_year}')
        