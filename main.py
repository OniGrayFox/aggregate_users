
with open("input.txt", "r") as f:
    content = f.readlines()
    users = {}
    for line in content:
        user, contacts = line.strip().split('->')
        users[user] = set(contacts.split(','))


def merge_users(data):
    seen = set()
    for user1 in users:
        for user2 in users:
            if user1 != user2:
                contact = users[user1].intersection(users[user2])
                if contact:
                    users[user1] = users[user1].union(users[user2])
                    users[user2] = users[user1]

    for key in data.copy().keys():
        value = tuple(data[key])
        if value in seen:
            del data[key]
        else:
            seen.add(value)

    return data


merge_users(users)

with open('output.txt', 'w') as answer_file:
    for user, data in users.items():
        answer_file.write(f'{user}->{",".join(data)}\n')