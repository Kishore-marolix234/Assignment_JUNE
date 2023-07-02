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

#22. What is the age of butter milky beauty?

age = movies['actress']['rashmika']['age']
print(f"The age of Butter Milky Beauty is {age}.")
print("----------------------------------")

#23. What are the total number of flops of all actress?

total_flops = 0
for actress in movies['actress'].values():
    total_flops += actress['hits']['flops']
print(f"The total number of flops for all actresses is {total_flops}.")
print("----------------------------------")

#24. What are the ages of Sam and Kaj?

sam_age = movies['actress']['samantha']['age']
kaj_age = movies['actress']['kajal']['age']
print(f"The age of Sam is {sam_age}.")
print(f"The age of Kaj is {kaj_age}.")
print("----------------------------------")

#25. Which actress own highest total number of Awards?

max_awards = 0
max_awards_actress = ""

for actress, details in movies['actress'].items():
    total_awards = sum(details['awards'].values())
    if total_awards > max_awards:
        max_awards = total_awards
        max_awards_actress = actress

print(f"The actress with the highest total number of awards is {max_awards_actress}.")
print("----------------------------------")

#26. Who is tallest Actor and Actress?

tallest_actor = ""
tallest_actor_height = 0

for actor, details in movies['actors'].items():
    height = details.get('height', 0)
    if height > tallest_actor_height:
        tallest_actor_height = height
        tallest_actor = actor

tallest_actress = ""
tallest_actress_height = 0

for actress, details in movies['actress'].items():
    height = details.get('height', 0)
    if height > tallest_actress_height:
        tallest_actress_height = height
        tallest_actress = actress

print(f"The tallest actor is {tallest_actor} with a height of {tallest_actor_height} feet.")
print(f"The tallest actress is {tallest_actress} with a height of {tallest_actress_height} feet.")
print("----------------------------------")

#27. What are the total number of Industry hits of who has more Success Rate?

highest_success_rate = 0
highest_success_rate_person = ""

for actor, details in movies['actors'].items():
    success_rate = details.get('sRate', '')
    success_rate = int(success_rate[:-1]) if success_rate else 0

    if success_rate > highest_success_rate:
        highest_success_rate = success_rate
        highest_success_rate_person = actor

for actress, details in movies['actress'].items():
    success_rate = details.get('sRate', '')
    success_rate = int(success_rate[:-1]) if success_rate else 0

    if success_rate > highest_success_rate:
        highest_success_rate = success_rate
        highest_success_rate_person = actress

total_industry_hits = 0

if highest_success_rate_person in movies['actors']:
    total_industry_hits = movies['actors'][highest_success_rate_person]['hits'].get('industry', 0)
elif highest_success_rate_person in movies['actress']:
    total_industry_hits = movies['actress'][highest_success_rate_person]['hits'].get('industry', 0)

print(f"The person with the highest success rate is {highest_success_rate_person}.")
print(f"The total number of industry hits for {highest_success_rate_person} is {total_industry_hits}.")
print("----------------------------------")

#28. What is the success rate of youngest actress?

youngest_age = float('inf')
youngest_actresses = []

for actress, details in movies['actress'].items():
    if details['age'] < youngest_age:
        youngest_age = details['age']
        youngest_actresses = [actress]
    elif details['age'] == youngest_age:
        youngest_actresses.append(actress)

success_rates = [movies['actress'][actress]['sRate'] for actress in youngest_actresses]

print("Success rate of the youngest actress(es):", success_rates)
print("----------------------------------")

#29. Who is youngest married actress?

youngest_married_age = float('inf')
youngest_married_actress = ""

for actress, details in movies['actress'].items():
    if details['mStatus'] == 'married' and details['age'] < youngest_married_age:
        youngest_married_age = details['age']
        youngest_married_actress = actress

print("Youngest married actress:", youngest_married_actress)
print("----------------------------------")

#30. Who is oldest unmarried actor?

oldest_unmarried_age = 0
oldest_unmarried_actor = ""

for actor, details in movies['actors'].items():
    if details['mStatus'] != 'married' and details['age'] > oldest_unmarried_age:
        oldest_unmarried_age = details['age']
        oldest_unmarried_actor = actor

print("Oldest unmarried actor:", oldest_unmarried_actor)
print("----------------------------------")

#31. Who are the high successful actor and actress?

highest_success_rate_actor = ""
highest_success_rate_actress = ""
highest_success_rate = 0

# Find highest success rate among actors
for actor, details in movies['actors'].items():
    success_rate = int(details['sRate'].strip('%'))
    if success_rate > highest_success_rate:
        highest_success_rate = success_rate
        highest_success_rate_actor = actor

# Find highest success rate among actresses
for actress, details in movies['actress'].items():
    success_rate = int(details['sRate'].strip('%'))
    if success_rate > highest_success_rate:
        highest_success_rate = success_rate
        highest_success_rate_actress = actress

print("Highly successful actor:", highest_success_rate_actor)
print("Highly successful actress:", highest_success_rate_actress)
print("---------------continue in kishore_pro4.py-------------------")
