from collections import OrderedDict
class Calendar(object):

	def __init__(self, date, eventName):

		self.date = date
		self.eventName = eventName
		self.que=True
		self.ListCalendar = []

	def switch(self):
		print('Welcome to Calendar App; ')
		print('--------------------------------------')
		
		input1=input(" Type one (1) to create new calendar:   ")
		if str(input1).isdigit() and int(input1) == 1:
			input2= input("Insert calendar name: ")
			print('--------------------------------------')
			print("New Calendar: %s        "%input2)
			print("New Calendar %s  has been created."%input2)
			#self.TestCalendar()
			print('--------------------------------------')
			print('--------------------------------------')
			
			while self.que is True:
				print('kindly select ')
				print('1: to insert events')
				input5= input('2: to exit and view your events:')
				if str(input5).isdigit() and int(input5)==1:
					self.setCalendar()
					print('--------------------------------------')
				'''if str(input5).isdigit() and int(input5)==2: 
					self.viewCalendar()'''
				if str(input5).isdigit() and int(input5)==2:
					self.que = False
					self.viewCalendar()
					print('--------------------------------------')
				'''else:
					self.setCalendar()'''
		else:
			print("Wrong input! Please insert 1 to continue")
		
		
	def viewCalendar(self):
		self.input2 = {self.date:'Date', self.eventName:'Event Name'}
		#od = OrderedDict(zip(self.input2))
		print (self.input2)
		print(self.ListCalendar) 
		
		
	def setCalendar(self):
		input3 = input("Good work! Write your event name:    ")
		input4 = input("Set the date(dd-mm-yyyy) for your event %s:   "%input3)
		self.date = input3
		self.eventName = input4
		self.input2 = {self.date:self.eventName}
		
		self.ListCalendar.append(self.input2)
			


a = Calendar('Empty Date', 'Empty Event')
a.switch()
                          