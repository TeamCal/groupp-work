from collections import OrderedDict
class Calendar(object):

	def __init__(self, date, eventName):

		self.date = date
		self.eventName = eventName
		self.que=True

	def switch(self):
		input1=input("Welcome to Calendar App; Type one (1) to create new calendar")
		if str(input1).isdigit() and int(input1) == 1:
			input2= input("Insert calendar name: ")
			print("New Calendar: %s"%input2)
			print("New Calendar %s  has been created."%input2)
			#self.TestCalendar()
			while self.que is True:
				input5= input('kindly select 1: to insert events and 3 to exit and view your events')
				if str(input5).isdigit() and int(input5)==1:
					self.setCalendar()
				if str(input5).isdigit() and int(input5)==2: 
					self.viewCalendar()
				if str(input5).isdigit() and int(input5)==3:
					self.que = False
					self.viewCalendar()
				else:
					self.setCalendar()
		else:
			print("Wrong input! Please insert 1 to continue")
		
		
	def viewCalendar(self):
		self.input2 = {self.date:'Date', self.eventName:'Event Name'}
		#od = OrderedDict(zip(self.input2))
		print (self.input2)
		
		
	def setCalendar(self):
		input3 = input("Good work! Write your event name:")
		input4 = input("Set the date(dd-mm-yyyy) for your event %s"%input3)
		self.date = input3
		self.eventName = input4
		self.input2 = {self.date:self.eventName}
		#ListCalendar = self.input2
		
			


a = Calendar('dd-mm-yyyy', 'Wahu\'s birthday')
a.switch()
                          