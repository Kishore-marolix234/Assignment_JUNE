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

#11. What is the nick name of Rashmika?

for actress, details in movies['actress'].items():
    if actress == 'rashmika':
        nickname = details['knownAs']
        break
print(nickname)
print("----------------------------------")

#12. What are actress names who did not win at least one Nandi Award?

actresses_without_nandi_award = []
print("Actress who did not win at least one nandi awards are:")
for actress, details in movies['actress'].items():
    if details['awards']['nandi'] == 0:
        actresses_without_nandi_award.append(actress)

print(actresses_without_nandi_award)
print("----------------------------------")

#13. What are the total number of SIIMA awards won by both actors and actress?
total_siima_awards_actors = 0

# Count SIIMA awards won by actors
for actor in movies['actors'].values():
    total_siima_awards_actors += actor['awards']['siima']

print("Total SIIMA awards won by actors are:",total_siima_awards_actors)
total_siima_awards_actresses = 0

# Count SIIMA awards won by actresses
for actress in movies['actress'].values():
    total_siima_awards_actresses += actress['awards']['siima']

print("Total SIIMA awards won by actresses are:",total_siima_awards_actresses)

total_siima_awards_combined = total_siima_awards_actors + total_siima_awards_actresses

print("Total Siima Awards Won:-",total_siima_awards_combined)
print("----------------------------------")

#14. What are the actor and actress names who has more success rate('sRate')?

# Find the actor with the highest success rate
max_actor_sRate = 0
actor_name = None

for actor, details in movies['actors'].items():
    sRate = details['sRate']
    if sRate.endswith('%'):
        sRate = sRate[:-1]  # Remove the '%' character
    success_rate = float(sRate)
    
    if success_rate > max_actor_sRate:
        max_actor_sRate = success_rate
        actor_name = actor

# Find the actress with the highest success rate
max_actress_sRate = 0
actress_name = None

for actress, details in movies['actress'].items():
    sRate = details['sRate']
    if sRate.endswith('%'):
        sRate = sRate[:-1]  # Remove the '%' character
    success_rate = float(sRate)
    
    if success_rate > max_actress_sRate:
        max_actress_sRate = success_rate
        actress_name = actress

# Display the results
print("Actor with the highest success rate:", actor_name)
print("Actress with the highest success rate:", actress_name)
print("----------------------------------")

#15. What is the age of actor who has more super hit movies?

max_super_hits = 0
actor_age = None

for actor, details in movies['actors'].items():
    super_hits = details['hits']['super']
    if super_hits > max_super_hits:
        max_super_hits = super_hits
        actor_age = details['age']

print("Age of the actor with the most super hit movies:", actor_age)
print("----------------------------------")

#16. What is the actress name who is married?

married_actress = []

for actress, details in movies['actress'].items():
    if details['mStatus'] == 'married':
        married_actress.append(actress)

print("Married actress:", married_actress)
print("----------------------------------")

#17. Who is the tallest actress?
# Initialize variables to store the tallest actresses
tallest_actresses = []

# Find the tallest height among the actresses
max_actress_height = max(details['height'] for details in movies['actress'].values())

# Find all the actresses with the tallest height
for actress, details in movies['actress'].items():
    if details['height'] == max_actress_height:
        tallest_actresses.append(actress)

# Print the names of the tallest actresses
print("Tallest Actresses:", tallest_actresses)
print("----------------------------------")

#18. Who is the Youngest actor and actress?

# Initialize variables to store the youngest actors and actresses
youngest_actors = []
youngest_actresses = []

# Find the youngest age among the actors
min_actor_age = min(details['age'] for details in movies['actors'].values())

# Find all the actors with the youngest age
for actor, details in movies['actors'].items():
    if details['age'] == min_actor_age:
        youngest_actors.append(actor)

# Find the youngest age among the actresses
min_actress_age = min(details['age'] for details in movies['actress'].values())

# Find all the actresses with the youngest age
for actress, details in movies['actress'].items():
    if details['age'] == min_actress_age:
        youngest_actresses.append(actress)

# Print the names of the youngest actors and actresses
print("Youngest Actors:", youngest_actors)
print("Youngest Actresses:", youngest_actresses)
print("----------------------------------")

#19. Who are unmarried actress?
# Initialize a list to store the names of unmarried actresses
unmarried_actresses = []

# Find the unmarried actresses
for actress, details in movies['actress'].items():
    if details['mStatus'] == 'single':
        unmarried_actresses.append(actress)

# Print the names of unmarried actresses
print("Unmarried Actresses:", unmarried_actresses)
print("----------------------------------")

#20.Who is smallest actress?

smallest_height = None
smallest_actress = None

for actress, details in movies['actress'].items():
    if smallest_height is None or details['height'] < smallest_height:
        smallest_height = details['height']
        smallest_actress = actress

print(f"The smallest actress is {smallest_actress} with a height of {smallest_height} feet.")
print("----------------------------------")

#21. Which actress has more Flops?

max_flops = 0
flop_actress = None

for actress, details in movies['actress'].items():
    flops = details['hits']['flops']
    if flops > max_flops:
        max_flops = flops
        flop_actress = actress

print(f"The actress with the most number of flops is {flop_actress}.")
print("---------------continue in kishore_pro3.py-------------------")
