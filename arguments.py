import argparse

def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument(dest="fav_word", help="Favorite Word",type=str)
    parser.add_argument(dest="fav_num", help="Favorite Number",type=int)
    parser.add_argument(dest="fav_decimal", help="Favorite Decimal",type=float)

    args = parser.parse_args()

    word=args.fav_word	
    number=args.fav_num 
    decimal=args.fav_decimal

    print("Favorite Word: ", word) 	
    print("Favorite Number: ",number)
    print("Favorite Decimal: ",decimal)

if __name__=='__main__': 	
    main()