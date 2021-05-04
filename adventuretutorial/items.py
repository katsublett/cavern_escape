class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def display_data(self):
        return "{}, {}, {}".format(self.name, self.description, self.value)
