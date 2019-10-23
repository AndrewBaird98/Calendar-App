class Event:

#initiates event attributes
    def __init__(self, name, date, time, city, state, price, address, category, description, link, restriction):
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
        print(a.name)
        print(a.date)
        print(a.time)
        print(a.city)
        print(a.state)
        print(a.price)
        print(a.address)
        print(a.category)
        print(a.description)
        print(a.link)
        print(a.restriction)





#initilize event attributes
a = Event("Taco Tuesday", "10 Oct 2019", "8:00 PM", "San Marcos", "CA", "$6", "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21")

#display them
a.displayExample()