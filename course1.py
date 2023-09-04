from abc import ABC, abstractmethod
import pickle
import random

class baseDeptProgram(ABC):
    
    @abstractmethod
    def theory_course(self):
        pass 

    @abstractmethod
    def lab_course(self):
        pass
        
    @abstractmethod
    def theoryCumPractice_course(self):
        pass

    @abstractmethod
    def labIntegratedTheory_courses(self):
        pass

class IT(baseDeptProgram):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super(IT, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.file = open('IT.pickle', 'rb')
        self.data = pickle.load(self.file)
        self.selected_courses = {'theory': [], 'lab': [], 'theoryCumPractice':[], 'labIntegratedTheory': [] }

    @property
    def theory_credit(self):
        return 3

    def theory_course(self):
        theory_course = self.data['theory']
        return (3, theory_course)

    @property
    def lab_credit(self):
        return 2

    def lab_course(self):
        lab_course = self.data['lab']
        return (2, lab_course)

    @property
    def theoryCumPractice_credit(self):
        return 4

    def theoryCumPractice_course(self):
        theory_practice = self.data['theoryCumPractice']
        return (4, theory_practice)

    @property
    def labIntegratedTheory_credit(self):
        return 4

    def labIntegratedTheory_courses(self):
        lab_theory = self.data['labIntegratedTheory']
        return (4, lab_theory)

class CSE(baseDeptProgram):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super(CSE, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.file = open('CSE.pickle', 'rb')
        self.data = pickle.load(self.file)
        self.selected_courses = {'theory': [], 'lab': [], 'theoryCumPractice':[], 'labIntegratedTheory': [] }

    @property
    def theory_credit(self):
        return 3

    def theory_course(self):
        theory_course = self.data['theory']
        return (3, theory_course)

    @property
    def lab_credit(self):
        return 2

    def lab_course(self):
        lab_course = self.data['lab']
        return (2, lab_course)

    @property
    def theoryCumPractice_credit(self):
        return 4

    def theoryCumPractice_course(self):
        theory_practice = self.data['theoryCumPractice']
        return (4, theory_practice)

    @property
    def labIntegratedTheory_credit(self):
        return 4

    def labIntegratedTheory_courses(self):
        lab_theory = self.data['labIntegratedTheory']
        return (4, lab_theory)

#factory 
class EngineeringProgram:
    def __init__(self, dept):
        self.dept = dept()
        self.lst_of_courses = self.dept.data

        if self.dept.selected_courses['theory'] == []:
            course = CourseSelection(self.lst_of_courses)
            self.dept.selected_courses = course.showSelection()
        else:
            print('The previous set of courses selected ar:\n', self.dept.selected_courses)
            ch = int(input('1.Want new selection\n2.Retain prev courses\nEnter your choice: '))
            if (ch == 1):
                course = CourseSelection(self.lst_of_courses)
                self.dept.selected_courses = course.showSelection()
            elif (ch!=2 and ch!=1):
                raise Exception("Enter valid input no.")
    
    def showCourses(self):
        return self.dept.selected_courses

class baseCourseSelection(ABC):
    @abstractmethod
    def courseCount(self): return 0

    @abstractmethod
    def pre_req(self): return 0

    @abstractmethod
    def sem(self): return 0

class CourseSelection:
    def __init__(self, course):
        self.course = course
        self.selectedCourse = {'theory': [], 'lab': [], 'theoryCumPractice':[], 'labIntegratedTheory': [] }
        self.select()

    def select(self):
        self.courseCount()
        #self.pre_req()
        #self.sem()
        #self.evaluateCourses()

    def courseCount(self):
        cnt = 0
        #theory
        while (cnt != 8):
            course = random.choice(self.course['theory'])
            if (course not in self.selectedCourse['theory']):
                self.selectedCourse['theory'].append(course)
                cnt+=1

        #print(self.selectedCourse['theory'])

        cnt = 0
        #lab
        while (cnt != 7):
            course = random.choice(self.course['lab'])
            if (course not in self.selectedCourse['lab']):
                self.selectedCourse['lab'].append(course)
                cnt+=1

        cnt = 0
        #thoery cum lab
        while (cnt != 4):
            course = random.choice(self.course['theoryCumPractice'])
            if (course not in self.selectedCourse['theoryCumPractice']):
                self.selectedCourse['theoryCumPractice'].append(course)
                cnt+=1

        cnt = 0
        #lab integrated theory
        while (cnt != 5):
            course = random.choice(self.course['labIntegratedTheory'])
            if (course not in self.selectedCourse['labIntegratedTheory']):
                self.selectedCourse['labIntegratedTheory'].append(course)
                cnt+=1

    def showSelection(self):
        return self.selectedCourse

choice = int(input('1.IT\n2.CSE\nEnter dept to select course: '))
dept = None
if choice == 1:
    dept = EngineeringProgram(IT)
elif choice == 2:
    dept = EngineeringProgram(CSE)
else:
    raise Exception("Invalid input")

print(dept.showCourses())
        