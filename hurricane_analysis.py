# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


def update_damages(damage_list):
    updated_damage = []
    for damage in damage_list:
        if damage == 'Damages not recorded':
            updated_damage.append(damage)
        elif damage[-1] == 'M':
            updated_damage.append(float(damage[:-1]) * conversion.get('M'))
        elif damage[-1] == 'B':
            updated_damage.append(float(damage[:-1]) * conversion.get('B'))
        else:
            return 'Error. Damage out of data range'
    return updated_damage


# print(update_damages(damages))

# test function by updating damages
updated_damages = update_damages(damages)

# 2 
# Create a Table
hurricanes = []
for index in range(len(names)):
    hurricanes.append({'Name': names[index], "Month": months[index], "Year": years[index],
                       "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
                       "Damage": updated_damages[index], "Deaths": deaths[index]})


# print(hurricanes)
# Create and view the hurricanes dictionary
def create_hurricanes_dict(names, hurricanes):
    hurricanes_dict = {key: value for key, value in zip(names, hurricanes)}
    return hurricanes_dict


# print(create_hurricanes_dict(names, hurricanes))
# 3
# Organizing by Year
def create_hurricanes_by_year_dict(years, hurricanes):
    hurricanes_by_year_dict = {key: value for key, value in zip(years, hurricanes)}
    return hurricanes_by_year_dict


# create a new dictionary of hurricanes with year and key
# print(create_hurricanes_by_year_dict(years, hurricanes))
hurricanes_by_year_dict = create_hurricanes_by_year_dict(years, hurricanes)


# 4
# Counting Damaged Areas
def count_areas(areas_list):
    areas_dict = {}
    for areas in areas_list:
        for area in areas:
            if area not in areas_dict:
                areas_dict.update({area: 1})
            elif area in areas_dict:
                areas_count = areas_dict.get(area)
                areas_dict.update({area: areas_count + 1})
    return areas_dict


# create dictionary of areas to store the number of hurricanes involved in
area_count_dict = count_areas(areas_affected)


# print(area_count_dict)
# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(areas):
    max_affect = 0
    max_area = ''
    for keys, values in areas.items():
        if values > max_affect:
            max_affect = values
            max_area = keys
    return {max_area: max_affect}


# print(max_hurricane_count(area_count_dict))
# find most frequently affected area and the number of hurricanes involved in

# 6
# Calculating the Deadliest Hurricane
def most_deaths(hurricanes, deaths):
    deadly_hurricanes = {key: value for key, value in zip(hurricanes, deaths)}
    deadliest_hurricane = ''
    most_deaths = 0
    for key, value in deadly_hurricanes.items():
        if value > most_deaths:
            most_deaths = value
            deadliest_hurricane = key
    return {deadliest_hurricane: most_deaths}


# find highest mortality hurricane and the number of deaths
# print(most_deaths(names, deaths))
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


def hurricanes_by_mortality(hurricanes, deaths):
    deadly_hurricanes = {key: value for key, value in zip(hurricanes, deaths)}
    # print(deadly_hurricanes)
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in deadly_hurricanes.items():
        if value == 0:
            hurricanes_by_mortality[0].append({key: value})
        elif value > 0 and value < 100:
            hurricanes_by_mortality[1].append({key: value})
        elif value >= 100 and value < 500:
            hurricanes_by_mortality[2].append({key: value})
        elif value >= 500 and value < 1000:
            hurricanes_by_mortality[3].append({key: value})
        elif value >= 1000 and value < 10000:
            hurricanes_by_mortality[4].append({key: value})
        else:
            hurricanes_by_mortality[5].append({key: value})
    return hurricanes_by_mortality


# print(hurricanes_by_mortality(names, deaths))

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
def max_damage(hurricanes):
    max_damage = 0
    max_damage_name = ''
    for hurricane in hurricanes:
        if hurricane.get('Damage') == 'Damages not recorded':
            continue
        elif hurricane.get('Damage') > max_damage:
            max_damage = hurricane.get('Damage')
            max_damage_name = hurricane.get('Name')
    return {max_damage_name:max_damage}
# find highest damage inducing hurricane and its total cost

#print(max_damage(hurricanes))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def damage_by_rating(hurricanes):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4:[], 5: []}
    for hurricane in hurricanes:
        if hurricane.get('Damage') == 0 or hurricane.get('Damage') == 'Damages not recorded':
            hurricanes_by_damage[0].append({hurricane.get('Name'):hurricane.get('Damage')})
        elif hurricane.get('Damage') > 0 and hurricane.get('Damage') < 100000000:
            hurricanes_by_damage[1].append({hurricane.get('Name'):hurricane.get('Damage')})
        elif hurricane.get('Damage') >= 100000000 and hurricane.get('Damage') < 1000000000:
            hurricanes_by_damage[2].append({hurricane.get('Name'):hurricane.get('Damage')})
        elif hurricane.get('Damage') >= 1000000000 and hurricane.get('Damage') < 10000000000:
            hurricanes_by_damage[3].append({hurricane.get('Name'):hurricane.get('Damage')})
        elif hurricane.get('Damage') >= 10000000000 and hurricane.get('Damage') < 50000000000:
            hurricanes_by_damage[4].append({hurricane.get('Name'):hurricane.get('Damage')})
        else:
            hurricanes_by_damage[5].append({hurricane.get('Name'): hurricane.get('Damage')})
    return hurricanes_by_damage

print(damage_by_rating(hurricanes))