class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = sum(self.scores)
        avg = total/len(self.scores)
        if avg>=90:
            return 'O'
        elif avg>=80:
            return 'E' 
        elif avg>=70:
            return 'A'
        elif avg>=55:
            return 'P'
        elif avg>=40:
            return 'D'
        else:
            return 'T'


line = input("Enter your full name and id number: ").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input("Enter your scores: ").split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
