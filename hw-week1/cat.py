class Cat:
    # initializer
    def __init__(self, name):
        self.name = name

    # cat introduces itself & greets other cat by their name
    def greet(self, other_cat_name):
        print("Hello I am {}! I see you are also a cool fluffy kitty {}, " \
        "let’s together purr at the human, so that they shall give us food.".format(self.name, other_cat_name))
