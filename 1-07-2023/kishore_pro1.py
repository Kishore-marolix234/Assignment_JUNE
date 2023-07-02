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

#1. Write a program to display all actors names?

actors = movies['actors']
actor_names = list(actors.keys())

print("Actor names:")
for name in actor_names:
    print(name)

print("----------------------------------")
#2. Write a program to display all actress names?

actresses = movies['actress']
actress_names = list(actresses.keys())

print("Actress names:")
for name in actress_names:
    print(name)
print("----------------------------------")

#3. Who is Darling?

actors = movies['actors']
prabhas = actors['prabhas']
known_as = prabhas['knownAs']

print("Prabhas is known as:", known_as)
print("----------------------------------")

#4. What are the total number of Nandi Awards won by actors?

actors = movies['actors']
total_nandi_awards = 0

for actor in actors.values():
    if 'awards' in actor and 'nandi' in actor['awards']:
        total_nandi_awards += actor['awards']['nandi']

print("Total number of Nandi Awards won by actors:", total_nandi_awards)
print("----------------------------------")

#5. What is the name of Prince?
name = ""

for actor, details in movies['actors'].items():
    if details['knownAs'] == 'Prince':
        name = actor

print('The name of the Prince is:-',name)
print("----------------------------------")

#6. What are the total number of awards own by Ram Charan?

total_awards = 0
for actor, details in movies['actors'].items():
    if actor == 'ramcharan':
        awards = details['awards']
        total_awards += sum(awards.values())

print("Total number of awards owned by Ram Charan:", total_awards)
print("----------------------------------")

#7. Which actor won more number of Nandi Awards?
max_nandi_awards = 0
actor_with_max_awards = ''

for actor, details in movies['actors'].items():
    nandi_awards = details['awards']['nandi']
    if nandi_awards > max_nandi_awards:
        max_nandi_awards = nandi_awards
        actor_with_max_awards = actor

print("Actor with the most number of Nandi Awards:", actor_with_max_awards)
print("----------------------------------")

#8. What is the success rate of Prince?
actor_name = 'mahesh'
actor_details = movies['actors'][actor_name]
success_rate = actor_details['sRate']
print("Success rate of Prince (Mahesh):", success_rate)

#or
print("by calculation:")
actor_name = 'mahesh'
actor_details = movies['actors'][actor_name]
success_rate = actor_details['hits']['super'] / (actor_details['hits']['super'] + actor_details['hits']['flops'])
success_rate_percentage = success_rate * 100

print("Success rate of Prince (Mahesh):", success_rate_percentage, "%")
print("----------------------------------")

#9. Which actor and actress has more number of Hits?

max_actor_hits = 0
max_actress_hits = 0
max_actor = ""
max_actress = ""

# Find actor with most hits
for actor in movies['actors'].values():
    if actor['hits']['super'] > max_actor_hits:
        max_actor_hits = actor['hits']['super']
        max_actor = actor['knownAs']

# Find actress with most hits
for actress in movies['actress'].values():
    if actress['hits']['super'] > max_actress_hits:
        max_actress_hits = actress['hits']['super']
        max_actress = actress['knownAs']

print("Actor with most hits:", max_actor)
print("Actress with most hits:", max_actress)
print("----------------------------------")

#10. Who is Milky Beauty?

for actress, details in movies['actress'].items():
    if details['knownAs'] == 'Milky Beauty':
        name = actress
        break

print('Milky Beauty is:-',name)
print("---------------continue in kishore_pro2.py-------------------")
