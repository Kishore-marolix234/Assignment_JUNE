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

#43. What is the highest remuneration of an unmarried actress?

max_remuneration = 0
actress_name = ""

# Find the highest remuneration and name of an unmarried actress
for actress_name, actress_details in movies['actress'].items():
    if actress_details['mStatus'] == 'single' and actress_details['remuneration'] > max_remuneration:
        max_remuneration = actress_details['remuneration']
        actress_name = actress_name

print("Unmarried Actress with the highest remuneration:", actress_name)
print("Highest remuneration of an unmarried actress:", max_remuneration)
print("----------------------------------")

#44.What are the names of actor and actress who has more remuneration?

actors_highest_remuneration = []
actresses_highest_remuneration = []

highest_remuneration_actors = 0
highest_remuneration_actresses = 0

# Iterate over actors
for actor, details in movies['actors'].items():
    if details['remuneration'] > highest_remuneration_actors:
        highest_remuneration_actors = details['remuneration']
        actors_highest_remuneration = [actor]
    elif details['remuneration'] == highest_remuneration_actors:
        actors_highest_remuneration.append(actor)

# Iterate over actresses
for actress, details in movies['actress'].items():
    if details['remuneration'] > highest_remuneration_actresses:
        highest_remuneration_actresses = details['remuneration']
        actresses_highest_remuneration = [actress]
    elif details['remuneration'] == highest_remuneration_actresses:
        actresses_highest_remuneration.append(actress)

print("Actors with the highest remuneration:", actors_highest_remuneration)
print("Actresses with the highest remuneration:", actresses_highest_remuneration)
print("----------------------------------")

#45. What is the remuneration of high successful Actress?

highest_success_rate = 0
high_successful_actress = ""

for actress, details in movies['actress'].items():
    if 'sRate' in details and float(details['sRate'][:-1]) > highest_success_rate:
        highest_success_rate = float(details['sRate'][:-1])
        high_successful_actress = actress

if high_successful_actress != "":
    remuneration = movies['actress'][high_successful_actress]['remuneration']
    print(f"The remuneration of the high successful actress ({high_successful_actress}): {remuneration}")
else:
    print("No high successful actress found.")
print("----------------------------------")

#46. What is the remuneration of actress who has more industry hits?

most_industry_hits = 0
actress_with_most_industry_hits = ""

for actress, details in movies['actress'].items():
    if 'hits' in details and 'industry' in details['hits']:
        industry_hits = details['hits']['industry']
        if industry_hits > most_industry_hits:
            most_industry_hits = industry_hits
            actress_with_most_industry_hits = actress

if actress_with_most_industry_hits != "":
    remuneration = movies['actress'][actress_with_most_industry_hits]['remuneration']
    print(f"The remuneration of the actress with more industry hits ({actress_with_most_industry_hits}): {remuneration}")
else:
    print("No actress with more industry hits found.")
print("----------------------------------")

#47. What are the ages of an actors whose remuneration is more then 90 crores?

actors_above_90 = []
print("the ages of an actors whose remuneration is more then 90 crores:- ")
for actor, details in movies['actors'].items():
    if details['remuneration'] > 90:
        actors_above_90.append((actor, details['age']))

print(actors_above_90)
print("----------------------------------")

#48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
industry_hits_prince = movies['actors']['mahesh']['hits']['industry']
industry_hits_butter_milky_beauty = movies['actress']['rashmika']['hits']['industry']

total_industry_hits = industry_hits_prince + industry_hits_butter_milky_beauty

print("Total number of industry hits for Prince and Butter Milky Beauty:", total_industry_hits)
print("----------------------------------")

#49. What is the age of Laughing Queen?
age_laughing_queen = movies['actress']['saipallavi']['age']
print("The age of Laughing Queen is:", age_laughing_queen)
print("----------------------------------")

#50. What are the total number of awards won by an actor who has less successful rate?

actor_with_less_success_rate = None
total_awards = 0
actor_name_with_less_success_rate = ""

for actor_name, actor_details in movies['actors'].items():
    success_rate = float(actor_details['sRate'].strip('%'))
    if actor_with_less_success_rate is None or success_rate < actor_with_less_success_rate:
        actor_with_less_success_rate = success_rate
        total_awards = sum(actor_details['awards'].values())
        actor_name_with_less_success_rate = actor_name

print("Actor with less success rate:", actor_name_with_less_success_rate)
print("Total awards won by the actor:", total_awards)
print("----------------END------------------")