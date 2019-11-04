class Event:
   
#initiates event attributes
    def __init__(self, name, date, startTime, endTime, city, state, price, address, category, description, link, restriction, recurrence, attendees):
        self.name = name
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.city = city
        self.state = state
        self.price = price
        self.address = address
        self.category = category
        self.description = description
        self.link = link
        self.restriction = restriction
        self.recurrence = recurrence
        self.attendees = attendees

#this function used as an example to display event attrubites
    def displayExample(self):
        print(a.name)
        print(a.date)
        print(a.startTime)
        print(a.endTime)
        print(a.city)
        print(a.state)
        print(a.price)
        print(a.address)
        print(a.category)
        print(a.description)
        print(a.link)
        print(a.restriction)
        print(a.recurrence)
        print(a.attendees)



#attendees = ['baird013@cougars.csusm.edu']
#initilize event attributes
#a = Event("Taco Tuesday", "2019-11-28", "09:00:00-07:00", "17:00:00-07:00", "San Marcos", "CA", "$6", "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21", 'RRULE:FREQ=DAILY;COUNT=2;', attendees)

#display them
#a.displayExample()
