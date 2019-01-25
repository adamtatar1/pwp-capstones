#Defining the User class

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        print("E-mail address has been updated")

    def __repr__(self):
        return "User {name}, email: {email}, books read: {number_books}".format(name=self.name, email=self.email, number_books=len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        number_rated_books = 0
        for rating in self.books.values():
            if rating != None:
              total += rating
              number_rated_books += 1
        return total / number_rated_books

#Defining the Book class

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("The ISBN for {title} has been updated.".format(title=self.title))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        total = 0
        number_of_ratings = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total += rating
                number_of_ratings += 1
            return total / number_of_ratings

    def __hash__(self):
        return hash((self.title, self.isbn))

#Defining Fiction subclass of book

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

#Defining the Non-Fiction subclass of book

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

#Creating TomeRater

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Users: {users}\n Books: {books}".format(users=self.users, books=self.books)

    def __eq__(self, other_rater):
        if isinstance(other_rater, self):
            return self.users == other_rater.users and self.books == other_rater.books
        return False

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn,)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email {email}".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_reads = 0
        most_book = ""
        for book, reads in self.books.items():
            if reads > most_reads:
                most_book = book
                most_reads = most_reads
            else:
                continue
            return most_book

    def highest_rated_book(self):
        highest_book = ""
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_book = book
                highest_rating = rating
        return highest_book

    def most_positive_user(self):
        positive_user = ""
        positive_rating = 0
        for user in self.users.values():
            avg_user_rating = user.get_average_rating()
            if avg_user_rating > positive_rating:
                positive_user = user
                positive_rating = avg_user_rating
        return positive_user
