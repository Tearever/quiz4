from module_1 import function1 as function1
from module_2 import function2 as function2
from module_3 import function3 as function3

def main()->None:
    print(f"{function1.MovieCharacter()} {function2.Activity()} {function3.Twist()}")

if __name__=="__main__":
    main()