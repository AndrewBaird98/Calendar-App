class Event:

    # initiates event attributes
    # def __init__(self, name, date, location, startTime, endTime, price, category, description, link, restriction, recurrence, attendees):
    def __init__(self, name, date, location, startTime, endTime, price, category, description, link, filled, contact,
                 dateTime):
        self.name = name
        self.date = date
        self.location = location
        self.startTime = startTime
        self.endTime = endTime
        self.price = price
        self.category = category
        self.description = description
        self.link = link
        self.Filled = filled
        self.Contact = contact
        self.DateTime = dateTime

    # this function used as an example to display event attrubites
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
