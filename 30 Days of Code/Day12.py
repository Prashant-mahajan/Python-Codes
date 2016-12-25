class Student(Person):
    def __init__(self, firstName,lastName, idNum,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg >= 90:
            return 'O'
        elif 90> avg >=80:
            return 'E'
        elif 80 > avg >=70:
            return 'A'
        elif 70 > avg >=55:
            return 'P'
        elif 55 > avg >=40:
            return 'D'
        else:
            return 'T'