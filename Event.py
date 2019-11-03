class Event:

#initiates event attributes
    def __init__(self, name: object, date: object, time: object, city: object, state: object, price: object, address: object, category: object, description: object, link: object, restriction: object) -> object:
        self.name = name
        self.date = date
        self.time = time
        self.city = city
        self.state = state
        self.price = price
        self.address = address
        self.category = category
        self.description = description
        self.link = link
        self.restriction = restriction

#this function used as an example to display event attrubites
    def displayExample(self):
        print(self.name)
        print(self.date)
        print(self.time)
        print(self.city)
        print(self.state)
        print(self.price)
        print(self.address)
        print(self.category)
        print(self.description)
        print(self.link)
        print(self.restriction)





#initilize event attributes
#a = Event("Taco Tuesday", "10 Oct 2019", "8:00 PM", "San Marcos", "CA", "$6", "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21")

#display them
#a.displayExample()