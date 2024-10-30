# Victoria Lutz


import pathlib
from pathlib import Path

minimum_country = ''
maximum_country = ''
input_country_max = ''
input_country_min = ''
min_year = ''
max_year = ''

country_year_small = 100
country_year_big = 0
country_data_min = 100
country_data_max = 0
maximum = 0
minimum = 100
year_maximum = 0
year_minimum = 100
year = 0
year_sum = 0
year_count = 0
year_average = 0

file_path = Path('../life-expectancy.csv')
text = file_path.read_text()
lines = text.splitlines()

year_input = int(input('Please enter the year of interest: '))
country_input = input('Please enter a country: ')


for index, line in enumerate(lines):

    if index > 0:
        parts = line.split(',')
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        if life_expectancy < minimum:
            minimum = life_expectancy
            minimum_country = country
            min_year = year

        if life_expectancy > maximum:
            maximum = life_expectancy
            maximum_country = country
            max_year = year

        if year_input == year:
            year_sum += life_expectancy
            year_count += 1

            if life_expectancy < year_minimum:
                year_minimum = life_expectancy
                input_country_min = country
            if life_expectancy > year_maximum:
                year_maximum = life_expectancy
                input_country_max = country
<<<<<<< HEAD
                
        if country_input.lower() == country.lower():
          country_input = country
          if life_expectancy < country_data_min:
            country_data_min = life_expectancy
            country_year_small= year
          if life_expectancy > country_data_max:
            country_data_max = life_expectancy
            country_year_big = year
                     
=======

        if country_input == country:
            country_input = country
            if life_expectancy < country_data_min:
                country_data_min = life_expectancy
                country_year_small = year
            if life_expectancy > country_data_max:
                country_data_max = life_expectancy
                country_year_big = year

>>>>>>> 44b3bfe477afbea4cbe536bb84dd912a9287edef

print(
    f'The overall max life expectancy was in {maximum_country} with {maximum} in the year {max_year}')
print(
    f'The overall minimum life expectancy was in {minimum_country} with {minimum} in the year {min_year}')


<<<<<<< HEAD
if country_input.lower() == country.lower():
  print(f'For the country {country_input}')
  print(
    f'The max life expectancy in {country_input} was in {country_year_big} with {country_data_max}\n')
  print(f'The min life expectancy in {country_input} was in {country_year_small} with {country_data_min}\n ')

=======
if country_input == country:
    print(f'For the country {country_input}')
    print(
        f'The max life expectancy in {country_input} was in {country_year_big} with {country_data_max}\n')
    print(
        f'The min life expectancy in {country_input} was in {country_year_small} with {country_data_min}\n ')
>>>>>>> 44b3bfe477afbea4cbe536bb84dd912a9287edef


if year_count > 0:
    year_average = year_sum / year_count

    print(f'For the year {year_input}:')

    print(
        f'The average life expectancy across all countries was {year_average}\n')
    print(
        f'The max life expectancy was in {input_country_max} with {year_maximum}\n')
    print(
        f'The min life expectancy was in {input_country_min} with {year_minimum}\n')
else:
    print("There is no data available for the year you entered. ")
