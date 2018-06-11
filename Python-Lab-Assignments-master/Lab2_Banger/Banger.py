#Kelcy Gooch Kjg116

class Banger():

    #the constructor to get the values
    def __init__(self, driver = "unknown", model = "unknown"):
        self.driver = driver
        self.model = model
        self.hits = 0

    def __repr__(self):
        return self.driver + '\t' + self.model

    #Used to receive value for driver
    def get_driver(self):
        return self.driver

    #Used to receive value for model
    def get_model(self):
        return self.model


    #Used to receive a value for the amount of hits
    def get_hits(self):
        return self.hits


    #Used to add the amount of hits
    def add_hits(self):
        self.hits = self.hits + 1

