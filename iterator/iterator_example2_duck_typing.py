

class User:
    def __init__(self, name):
        self.name = name


class FacebookIterator:
    def __init__(self, users):
        self.users = users
        self.index = -1

    def current_user(self):
        if self.index < 0 or self.index >= len(self.users):
          raise Exception("Invalid operation")
        return self.users[self.index]

    def has_next_user(self):
        return self.index + 1 < len(self.users)

    def next_user(self):
        if not self.has_next_user():
            raise Exception("Invalid operation")
        self.index += 1
        return self.users[self.index]


class UserCollection:
    def __init__(self, users):
        self.users = users

    def create_iterator(self):
        return FacebookIterator(self.users)


class Client:
    def show_users(self, collection):
        iterator = collection.create_iterator()

        while iterator.has_next_user():
            user = iterator.next_user()
            print(user.name)


users = [User("Alice"), User("Bob"), User("Charlie")]
user_collection = UserCollection(users)

client = Client()
client.show_users(user_collection)

