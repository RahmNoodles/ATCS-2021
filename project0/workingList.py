careers = ["programmer", "truck driver", "banker", "lawyer"]

print(careers.index("banker"))
print("banker" in careers)
careers.append("cop")
careers.insert(0, "actor")
for i in careers:
    print(i)
