class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []  # List for the posts
        self.comments = []  # Comments list
        self.likes = []  # List likes

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def comment_post(self, post, text):
        comment = Comment(text, self, post)
        self.comments.append(comment)
        return comment

    def like_post(self, post):
        if post not in self.likes:
            self.likes.append(post)

    def __str__(self):
        return self.username


class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.comments = []
        self.likes = []

    #when comment added the list appends
    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        if user not in self.likes:
            self.likes.append(user)

    #for easy read
    def __str__(self):
        return f"Post By {self.user.username}: {self.content}"


class Comment:
    def __init__(self, text, user, post):
        self.text = text
        self.user = user
        self.post = post

    
    def __str__(self):
        return f"Comment By {self.user.username}: {self.text}"

#creating users
user1 = User("Amaya De Silva", "amaya@gmail.com")
user2 = User("Sam de Silva", "sam@gmail.com")
user3 = User("Perera", "perera@gmail.com")

#creating posts
post1 = user1.create_post("Hello! This is Amaya")
post2 = user2.create_post("Good Morning Friends")

#creating comments
comment1 = user3.comment_post(post1, "Hi! Amaya")
comment2 = user3.comment_post(post2, "Good Morning!!")

#likes
user3.like_post(post1)
user3.like_post(post2)

#print all the functionality
print(post1)
print(post2)

print(comment1)
print(comment2)

print(f"{user3} likes {post1 }")
