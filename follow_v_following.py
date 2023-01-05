import json

followers = open("followers.json", "r")
following = open("following.json", "r")

ers = json.load(followers)
ing = json.load(following)

def parse_json(json_file, str_):
    curr_set = set()
    for user in json_file[str_]:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

not_following = parse_json(ing, 'relationships_following') - parse_json(ers, 'relationships_followers')

def convert(set):
    return sorted(set)

data = convert(not_following)

for i in data:
    print(i)

followers.close()
following.close()