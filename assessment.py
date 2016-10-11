"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages of object orientation are:

    a. Abstraction. Abstraction allows us to hide details we don't need. An example of this would be the random class.
    I can import the random class and use the methods defined within without ever having to see or touch that code again.
    If random class did not exist, I'd have to redefine randint every time I wished to use it. 

    b. encapsulation: Encapsulation is the mechanism for restricting the access to some of an object's components. It gives 
    the programmer more control as access to this data is only achieved when the class is called. It also bundles the methods together in one place.

    c. polymorphism: Polymorphism allows for the interchangeability of componennts. They're the same interface even if they
    do different things. Polymorphism has two major applications in an OOP language. The first is that an object may provide different 
    implementations of one of its methods depending on the type of the input parameters. The second is that code written for a 
    given type of data may be used on data with a derived type, i.e. methods understand the class hierarchy of a type. 

2. What is a class?
     A class is a 'Type' of thing, like String (str) or File(file).

3. What is an instance attribute?

    An instance attribute is set directly on the object. If the instance attribute is changed, it won't affect the class. Example
    class Animals(object):
        species = 'cat' <-- species is a class attribute. All animals assigned to this class will be automatically be'cat'

    Fluffy = Aniamls()
    fluffy.species = 'dog' <-- I've just created an instance attribute of the object 'Fluffy'.

4. What is a method?
    A method is a function called within a class

5. What is an instance in object orientation?

    An object is an instance in object oriented orientation.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   class Animals(object):
        species = 'cat' <-- species is a class attribute. All animals assigned to this class will be automatically be'cat'

    Fluffy = Aniamls()
    fluffy.species = 'dog' <-- I've just created an instance attribute of the object 'Fluffy'.


"""


# Parts 2
#1. 
class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

#2. 
class Question(object):


    def __init__(self, question, correct_answer):
        """Initialize question attributes."""
        self.question = question
        self.correct_answer = correct_answer
        
        def ask_and_evaluate(self):
            print self.question
            answer = raw_input('Please answer the question:')
            if answer == self.correct_answer:
                print True
            else:
                print False
#3. 
        def administrator(self):
            score = 0
            for self.correct_answer in self.question:
                if self.ask_and_evaluate() == True:
                    score += 1
            return score

class Exam(Question):

    def __init__(self, name):
        super(Exam, self).__init__(question, correct_answer)
        self.name = name


        def add_question(self):
            return "The new question is: %s. The answer is %s" % (question, correct_answer)


exam = Exam('midterm')
exam.add_question('What is the method for adding an element to a set?', '.add()')


