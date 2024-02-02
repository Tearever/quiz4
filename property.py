class Student:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name


def main():
    s = Student("Steve")
    print(s.name)

if __name__=="__main__":
    main()
