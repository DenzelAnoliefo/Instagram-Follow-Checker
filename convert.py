import json

with open('followers_1.json', 'r') as f:
    data_followers = json.load(f)

with open('following.json', 'r') as f:
    data_following = json.load(f)


followers = []
following = [] 

# followers
for acct in range(len(data_followers)):
    usr = data_followers[acct]['string_list_data'][0]['value']
    followers.append(usr)

# following
for acct in data_following['relationships_following']:
    usr = acct['title']
    following.append(usr)


unfollow = list(set(following) - set(followers))

print("Followers count:", len(followers))
print("Following count:", len(following)) 

print(unfollow)

