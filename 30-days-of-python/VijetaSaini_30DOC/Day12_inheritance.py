#Day12 Code
#inheritance(classes)

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person,object):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    #super() function that will make the child class inherit all the methods and properties from its parent:
    def __init__(self,firstName,lastName,idNumber,score):
        super().__init__(firstName,lastName,idNumber)
        self.score=score
        self.average=(sum(score))/(len(score))

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        if(self.average>=90 and self.average<=100):
            return "O"
        elif(self.average>=80 and self.average<90):
            return "E"
        elif(self.average>=70 and self.average<80):
            return "A"
        elif(self.average>=55 and self.average<70):
            return "P"
        elif(self.average>=40 and self.average<55):
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
