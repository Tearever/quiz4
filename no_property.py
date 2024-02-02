class Student:
    def __init__(self, name:str, id:int):
        self._name = name
        self._id = id
    
    def get_name(self):
        return self._name

    def get_id(self):
        return self._id


def main():
    s = Student("Steve", 1123123)
    print(f"| Name: {s.get_name()}  id: {s.get_id()} |\n")

if __name__=="__main__":
    main()