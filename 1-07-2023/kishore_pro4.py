movies = {
 'actors':{
 'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
 'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
 'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1}, 
'remuneration':70, 'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married',
'sRate':'50%'},
 'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
 'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5}, 'hits':{'industry':2, 
'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%','remuneration':50},
 },
 'actress':{
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1}, 
'remuneration':10, 'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.9, 'mStatus':'single',
'sRate':'40%'},
 'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':12,'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.9, 'mStatus':'single',
'sRate':'30%'},
 'saipallavi':{'knownAs': 'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2}, 
'remuneration':8, 'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.9,'mStatus':'single',
'sRate':'60%'},
 'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
 'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':5.9, 'mStatus':'married','sRate':'60%'},
 }
}

#32. Totally How many unmarried actors and actress are acting in movies?

unmarried_actors_count = 0
unmarried_actresses_count = 0

# Count unmarried actors
for actor, details in movies['actors'].items():
    if details['mStatus'] == 'single':
        unmarried_actors_count += 1

# Count unmarried actresses
for actress, details in movies['actress'].items():
    if details['mStatus'] == 'single':
        unmarried_actresses_count += 1

print("Number of unmarried actors:", unmarried_actors_count)
print("Number of unmarried actresses:", unmarried_actresses_count)
print("----------------------------------")

#33.Which actress is having more industry hit movies?

max_industry_hits = 0
actress_with_max_hits = ""

for actress, details in movies['actress'].items():
    if 'industry' in details['hits'] and details['hits']['industry'] > max_industry_hits:
        max_industry_hits = details['hits']['industry']
        actress_with_max_hits = actress

print("Actress with the most industry hits:", actress_with_max_hits)
print("----------------------------------")

#34. Which actress does not have atleast one industry hit also?

actresses_without_industry_hit = []

for actress, details in movies['actress'].items():
    if 'industry' not in details['hits'] or details['hits']['industry'] == 0:
        actresses_without_industry_hit.append(actress)

print("Actresses without at least one industry hit:", actresses_without_industry_hit)
print("----------------------------------")

#35.What are the total number of industry and super hits of tallest actresses?

tallest_height = 0
tallest_actresses = []

# Find the tallest height
for actress, details in movies['actress'].items():
    height = details.get('height', 0)
    if height > tallest_height:
        tallest_height = height

# Find the actresses with the tallest height
for actress, details in movies['actress'].items():
    height = details.get('height', 0)
    if height == tallest_height:
        tallest_actresses.append(actress)

total_industry_hits = 0
total_super_hits = 0

# Calculate the total number of industry and super hits for the tallest actresses
for actress in tallest_actresses:
    hits = movies['actress'][actress]['hits']
    total_industry_hits += hits.get('industry', 0)
    total_super_hits += hits.get('super', 0)

print("Total number of industry hits of tallest actresses:", total_industry_hits)
print("Total number of super hits of tallest actresses:", total_super_hits)
print("----------------------------------")

#36. Which actress is having lengthiest nick name?

lengthiest_nickname = ""
actress_with_lengthiest_nickname = ""

for actress, details in movies['actress'].items():
    nickname = details.get('knownAs', "")
    if len(nickname) > len(lengthiest_nickname):
        lengthiest_nickname = nickname
        actress_with_lengthiest_nickname = actress

print("Actress with the lengthiest nickname:", actress_with_lengthiest_nickname)
print("Length of the lengthiest nickname:", len(lengthiest_nickname))
print("----------------------------------")

#37. Who are the youngest unmarried actor and actress?

youngest_unmarried_actors = []
youngest_unmarried_actresses = []

# Find the youngest unmarried actors
for actor, details in movies['actors'].items():
    age = details.get('age', 0)
    marital_status = details.get('mStatus', '')
    
    if marital_status == 'single':
        if not youngest_unmarried_actors or age < youngest_unmarried_actors[0]['age']:
            youngest_unmarried_actors = [{'name': actor, 'age': age}]
        elif age == youngest_unmarried_actors[0]['age']:
            youngest_unmarried_actors.append({'name': actor, 'age': age})

# Find the youngest unmarried actresses
for actress, details in movies['actress'].items():
    age = details.get('age', 0)
    marital_status = details.get('mStatus', '')
    
    if marital_status == 'single':
        if not youngest_unmarried_actresses or age < youngest_unmarried_actresses[0]['age']:
            youngest_unmarried_actresses = [{'name': actress, 'age': age}]
        elif age == youngest_unmarried_actresses[0]['age']:
            youngest_unmarried_actresses.append({'name': actress, 'age': age})

print("Youngest unmarried actors:")
for actor in youngest_unmarried_actors:
    print("Name:", actor['name'], "Age:", actor['age'])

print("\nYoungest unmarried actresses:")
for actress in youngest_unmarried_actresses:
    print("Name:", actress['name'], "Age:", actress['age'])
print("----------------------------------")

#38.What are the total number of Industry hits and Super Hits of the actress who got more 
#SIIMA awards?

most_siima_awards = 0
actress_with_most_siima = None

# Find the actress with the most SIIMA awards
for actress, details in movies['actress'].items():
    siima_awards = details.get('awards', {}).get('siima', 0)
    if siima_awards > most_siima_awards:
        most_siima_awards = siima_awards
        actress_with_most_siima = actress

# Calculate the total number of industry hits and super hits for the actress
total_industry_hits = movies['actress'][actress_with_most_siima].get('hits', {}).get('industry', 0)
total_super_hits = movies['actress'][actress_with_most_siima].get('hits', {}).get('super', 0)

print("Actress with the most SIIMA awards:", actress_with_most_siima)
print("Total number of industry hits:", total_industry_hits)
print("Total number of super hits:", total_super_hits)
print("----------------------------------")

#39. What are the ages of Darling and Milky Beauty?

darling_age = movies['actors']['prabhas'].get('age')
milky_beauty_age = movies['actress']['tamanna'].get('age')

print("Age of Darling (Prabhas):", darling_age)
print("Age of Milky Beauty (Tamanna):", milky_beauty_age)
print("----------------------------------")

#40.What are names of actors whose nick name contains star?

actors_with_star = []

for actor_name, actor_details in movies['actors'].items():
    known_as = actor_details.get('knownAs', '')
    if 'star' in known_as.lower():
        actors_with_star.append(actor_name)

print("Actors whose nickname contains 'star':", actors_with_star)
print("----------------------------------")

#41. What is the total remuneration of all actors?

total_remuneration = 0

for actor_details in movies['actors'].values():
    remuneration = actor_details.get('remuneration', 0)
    total_remuneration += remuneration

print("Total remuneration of all actors:", total_remuneration)
print("----------------------------------")

#42. What is the remuneration of an actor who has more flops?

max_flops = 0
remuneration = 0
actor_name = ""

# Find the actor with the most number of flops
for actor_name, actor_details in movies['actors'].items():
    flops = actor_details['hits']['flops']
    if flops > max_flops:
        max_flops = flops
        remuneration = actor_details.get('remuneration', 0)
        actor_name = actor_name

print("Actor with the most number of flops:", actor_name)
print("Remuneration of the actor:", remuneration)
print("---------------continue in kishore_pro5.py-------------------")

