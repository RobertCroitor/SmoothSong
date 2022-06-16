from postgres import getUserByUsername

username = "user"
rows = getUserByUsername.getUserByUsername(username)
print(rows)
for row in rows:
    print("id =", row[0])
    print("username =", row[1])
    print("password =", row[2])
    print("uuid =", row[3])
    print("isAdmin =", row[4], "\n")
