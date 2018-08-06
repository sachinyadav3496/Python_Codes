import facebook

print("\n\n\n\n")


access_token = "EAACEdEose0cBANAssyCPNemis5sq7hBDdnQBHIX9at3IJU8srxHjc8ZClJepXs6R8RV5ZBYXcGnr0vG8SrsGSAEyRMD5n894VSZBkZCy4SJzq0yd1m4ixdAuzhmYw1lo9fOKTpVdWlC7D4nljIbHFGTT9lVt897abawNwNGPJW0sasvZB2AlnmKFQg0PIT2qKE34lHRf3RQZDZD"

graph = facebook.GraphAPI(access_token)




friends = graph.get_object("me?fields=posts.limit(50){message}")


print(friends)
