import json
import requests
import os

data = open("D:\\myfiles\data.json", "r") #Put filepath to json data here
todos = json.loads(data)



# Map of userId to number of complete TODOs for that user
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            ]
            todos_by_user[todo["userId"]] += 1
        except KeyError:
         
            todos_by_user[todo["userId"]] = 1

# Create a sorted list 
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)


max_complete = top_users[0][1]


users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))




max_users = " and ".join(users)



# Define a function to filter out completed TODOs 
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
