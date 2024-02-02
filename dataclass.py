from dataclasses import dataclass

@dataclass
class Riders:
    name:str
    team:str
    overall_points:int

def main():
    SX250_WEST = [
        Riders("Jordan Smith", "Yamaha", 84),
        Riders("Levi Kitchen", "Kawasaki", 84),
        Riders("RJ Hampshire", "Husqvarna", 76),
        Riders("Garrett MarchBanks", "Yamaha", 70),
        Riders("Jo Shimoda", "Honda", 54)
    ]

    print(SX250_WEST)

if __name__=="__main__":
    main()