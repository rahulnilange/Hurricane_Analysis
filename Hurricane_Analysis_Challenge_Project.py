# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


conversion = {"M": 1000000,
              "B": 1000000000}

def update(damage):
    updated_damages = []
    for record in damage:
        if record == 'Damages not recorded':
            updated_damages.append(record)
        elif 'M' in record:
            updated_damages.append(conversion['M'] * float(record[:-1]))
        else:
            updated_damages.append(conversion['B'] * float(record[:-1]))
    return updated_damages

print(update(damages))    

def hurricane_data():
    hurricane_dict = {}
    # iterate through names list
    for i in range(len(names)):
        # sub_dict is going to be a value in 
        # hurricane_dict
        sub_dict = {}
        sub_dict['Name'] = names[i]
        sub_dict['Month'] = months[i]
        sub_dict['Year'] = years[i]
        sub_dict['Max Sustained Wind'] = max_sustained_winds[i]
        sub_dict['Areas Affected'] = areas_affected[i]
        sub_dict['Damage'] = damages[i]
        sub_dict['Deaths'] = deaths[i]

        # update hurricane_dict
        hurricane_dict[names[i]] = sub_dict
    return hurricane_dict

print(hurricane_data())    
hurricane_dict = hurricane_data()

def year_data():
    # create an empty dictionary where
    # we will append the data
    new_dict = {}
    for i in range(len(years)):
        if not new_dict.get(years[i]):
            new_dict[years[i]] = [hurricane_dict[names[i]]]
        else:
            new_dict[years[i]].append(hurricane_dict[names[i]])
    return new_dict   
print(year_data())    

areas_set = set().union(*areas_affected)

areas_affected_dict = {}

for area in areas_set:
    count = 0
    for sub_list in areas_affected:
        if area in sub_list:
            count += 1
    areas_affected_dict[area] = count

print(max(areas_affected_dict))

def most_affected_area(area_dict):
    max_value = max(area_dict.values())
    key_with_max_value = max(area_dict, key=area_dict.get)

    return key_with_max_value, max_value

print(most_affected_area(areas_affected_dict))    

def most_damaging_hurricane():
    max_deaths = max(deaths)
    max_deaths_index = deaths.index(max_deaths)

    return names[max_deaths_index], max_deaths

print(most_damaging_hurricane())  

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}


mortality_ratings = []

def calculate_mortality_ratings():
    for count in deaths:
        if count == 0:
            mortality_ratings.append(0)
        elif 0 < count <= 100:
            mortality_ratings.append(1)
        elif 100 < count <= 500:
            mortality_ratings.append(2)
        elif 500 < count <= 1000:
            mortality_ratings.append(3)
        else:
            mortality_ratings.append(4)
    
# calculate mortality ratings
calculate_mortality_ratings()

# create empty mortality dictionary
mortality_dict = {}

def mortality_data():
    # iterate through mortality_ratings list
    for index in range(len(mortality_ratings)):
        if not mortality_dict.get(mortality_ratings[index]):
            mortality_dict[mortality_ratings[index]] = [hurricane_dict[names[index]]]
        else:
            mortality_dict[mortality_ratings[index]].append(hurricane_dict[names[index]])

mortality_data()            
print(mortality_dict)

updated_damages = update(damages)

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

print(updated_damages)   

clean_updated_damages = [-1 if type(damage) == str else damage for damage in updated_damages]

max_value = max(clean_updated_damages)
max_index = clean_updated_damages.index(max_value)

print(f"Hurricane {names[max_index]} caused the greatest damage and it cost {damages[max_index]}")

damage_scale = []

def calculate_damage_scale():
    for damage in updated_damages:
        if damage == 'Damages not recorded':
            damage_scale.append(damage)
        elif 0 < damage <= 100000000:
            damage_scale.append(1)
        elif 100000000 < damage <= 1000000000:
            damage_scale.append(2)
        elif 1000000000 < damage <= 10000000000:
            damage_scale.append(3)
        else:
            damage_scale.append(4)

calculate_damage_scale()            
print(damage_scale)

damage_dict = {}

def create_damage_dict():
    for i in range(len(damage_scale)):
        if not damage_dict.get(damage_scale[i]):
            damage_dict[damage_scale[i]] = [hurricane_dict[names[i]]]
        else:
            damage_dict[damage_scale[i]].append(hurricane_dict[names[i]])


create_damage_dict()

print(damage_dict)   
