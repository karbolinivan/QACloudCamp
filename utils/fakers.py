from faker import Faker


class Generator:

    def __init__(self, lang=None):
        self.faker = Faker(lang)
        self.title = None
        self.body = None
        self.userid = None

    def get_title(self):
        self.title = self.faker.sentence(nb_words=10)
        return self.title

    def get_body(self):
        self.body = self.faker.text(max_nb_chars=50)
        return self.body

    def get_userid(self):
        self.userid = self.faker.random_digit_not_null()
        return self.userid
