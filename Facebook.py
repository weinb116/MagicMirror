
import facebook

token = 'EAACEdEose0cBADoD9VxcPtJnZBZBqH16q0IZA6k9yjkCas0MRQHAnZBNqMZAjTZAbI40c4Nv7f2bJSWn17BZA6qqz5SxYLwJX0e2xytz4HBhtpP0H8WCK7YSZAQv3I1ZCm2UQ0YBNFMnENJl8MhtZC2xmlOFd5qBsDwuqrQPwB1hK7Vt2cWQtKSXcYoP3mk47aR7sSOesV1S7etgZDZD'
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list
