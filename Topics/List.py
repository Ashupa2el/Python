friends = ["Kevin", "Karen", "Jim", "Oscar", "Tam", ["Ashwin", "Power", "Maddy"]]
# friends.sort()
# friends.reverse()
# friends.insert(2, "Rahul")
# friends.pop(3)
# print(friends)
friends1 = [friend for friend in friends if isinstance(friend, list)]
# friends1.sort(reverse=True)
print(friends1)