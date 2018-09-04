years_str = input("Years: ") # do not change this line

# Missing lines here
years_int = int(years_str)
yearsecs = 60 * 60 * 24 * 365 * years_int

base_population = 307357870
new_population = base_population
new_population += yearsecs // 7 # births
new_population -= yearsecs // 13 # deaths
new_population += yearsecs // 35 # immigrants


print("New population after", years_int, " years is ", int(new_population)) # do not change this line

