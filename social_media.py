class User:
    user_names = []

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.is_logged_in = False

    @classmethod
    def register(cls, first_name, last_name, user_name, password):
        new_user = cls(first_name, last_name, user_name, password)
        if user_name in cls.user_names:
            raise ValueError('Username is already taken!')
        cls.user_names.append(user_name)
        return new_user

    def log_in(self, username, password):
        if self.user_name == username and self.password == password:
            self.is_logged_in = True
            return 'Logged in!'
        raise ValueError('incorrect user or password')

    def log_out(self):
        if not self.is_logged_in:
            raise ValueError('You are not logged in')
        self.is_logged_in = False
        return 'Logged out!'


class Post:
    published_posts = []
    deleted_posts = []
    all_posts = []

    def __init__(self, author, title, body):
        self.author = author
        self.title = title
        self.body = body
        self.is_published = False
        self.is_deleted = False

        if not self.author.is_logged_in:
            raise ValueError('Please login first ')

        self.all_posts.append(self)

    def publish(self):
        self.is_published = True
        self.published_posts.append(self)

    def delete(self):
        self.is_deleted = True
        self.deleted_posts.append(self)

    @classmethod
    def get_published_posts(cls):
        return cls.published_posts

    @classmethod
    def get_deleted_posts(cls):
        return cls.deleted_posts

    @classmethod
    def get_all_posts(cls):
        return cls.all_posts

    def __str__(self):
        return f'{self.title} - {self.body}'


user = User('sina', 'kamrani', 'kamrani.sina', '1234')

print(user.log_in('kamrani.sina', '1234'))



