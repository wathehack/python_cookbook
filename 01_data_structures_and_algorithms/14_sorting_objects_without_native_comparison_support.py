from operator import attrgetter


# Sorting objects of the same class without natively support comparison
# operations.
class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99), User(47)]
print(users)

# The built-in sorted() function takes a key argument that can be passed a
# callable that will return some value in the object that sorted will use to
# compare the objects.
print(sorted(users, key=lambda u: u.user_id))

# Instead of using lambda, an alternative approach is to use
# operator.attrgetter(). However, attrgetter() is often a tad bit faster and
# also has the added feature of allowing multiple fields to be extracted
# simultaneously.
print(sorted(users, key=attrgetter('user_id')))

print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
