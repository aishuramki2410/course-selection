import pickle



class cse:
    
    def write(self):
        file = open('CSE.pickle', 'ab')
        text = {'theory': ['physics', 'chemistry', 'networks', 'maths', 'engineering graphics','understanding harmony','hardware working','systemSecurity','discrete maths', 'dataScience', 'digitalLogics'],
        'lab':['python','database','machineLearning', 'networking','javascripts','algorithms', 'c','webdev','c++','digitallogic'],
        'theoryCumPractice':['dataStructures', 'oops', 'advancedProgramming', 'java'],
        'labIntegratedTheory':['oracle', 'appDev', 'digitalCommunication', 'c++', 'os']}
        pickle.dump(text, file)
        file.close()

    def read(self):
        file = open('CSE.pickle', 'rb')
        text = pickle.load(file)
        print(text)


class it:

    def write(self):
        file = open('IT.pickle', 'ab')
        text = {'theory': ['languagecommunication','physics','universalharmony','Engineeringgraphics', 'chemistry', 'java','designPatterns', 'maths', 'python', 'database', 'digitalLogics','computerorganization','discrete mathematics','complex function'],
        'lab':['python','database','openSource', 'networking','os lab','algorithm','digital pratices lab','networks','webDev', 'c','c++','java'],
        'theoryCumPractice':['dataStructures', 'oops', 'advancedProgramming', 'java','advanced ds','java programming'],
        'labIntegratedTheory':['oracle', 'appDev', 'digitalCommunication', 'c++', 'os']}
        pickle.dump(text, file)
        file.close()
    
    def read(self):
        file = open('IT.pickle', 'rb')
        text = pickle.load(file)
        print(text)        

       

itCourse = it()
cseCourse = cse()

#cseCourse.write()
#cseCourse.read()
#itCourse.write()
# itCourse.read()

