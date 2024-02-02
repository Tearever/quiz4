from dataclasses import dataclass

@dataclass
class Riders:
    name:str
    team:str
    overall_points:int

    def more_points(self, other: 'Riders')->str:
        if self.overall_points < other.overall_points:
            return f"{other.name} has {other.overall_points - self.overall_points} more points than {self.name}.\n"
        elif self.overall_points > other.overall_points:
            return f"{self.name} has {self.overall_points - other.overall_points} more points than {other.name}.\n"
        else:
            return f"{self.name} & {other.name} both have {self.overall_points} points.\n"


def main():
    SX250_WEST = [
        Riders("Jordan Smith", "Yamaha", 84),
        Riders("Levi Kitchen", "Kawasaki", 84),
        Riders("RJ Hampshire", "Husqvarna", 76),
        Riders("Garrett MarchBanks", "Yamaha", 70),
        Riders("Jo Shimoda", "Honda", 54)
    ]

    print(f"{SX250_WEST}\n")

    rider1 = SX250_WEST[0]
    rider2 = SX250_WEST[1]

    result = rider1.more_points(rider2)
    print(result)

    rider3 = SX250_WEST[4]
    result = rider2.more_points(rider3)
    print(result)

if __name__=="__main__":
    main()