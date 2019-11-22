class Event:
   
#initiates event attributes
    def __init__(self, name, date, location, startTime, endTime, price, category, description, link, restriction, recurrence, attendees):
        self.name = name
        self.date = date
        self.location = location
        self.startTime = startTime
        self.endTime = endTime
        self.price = price
        self.category = category
        self.description = description
        self.link = link
        self.restriction = restriction
        self.recurrence = recurrence
        self.attendees = attendees

#this function used as an example to display event attrubites
    def displayExample(self):
        print(self.name)
        print(self.date)
        print(self.startTime)
        print(self.endTime)
        print(self.city)
        print(self.state)
        print(self.price)
        print(self.address)
        print(self.category)
        print(self.description)
        print(self.link)
        print(self.restriction)
        print(self.recurrence)
        print(self.attendees)



#attendees = ['baird013@cougars.csusm.edu']
#initilize event attributes
#a = Event("Taco Tuesday", "2019-11-28", "09:00:00-07:00", "17:00:00-07:00", "San Marcos", "CA", "$6", "300 San Marcos Blvd", "Nightlife", "Enjoy Tacos half price", "www.google.com", "+21", 'RRULE:FREQ=DAILY;COUNT=2;', attendees)

#display them
#a.displayExample()
