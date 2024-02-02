def count_element_lengths(arr) -> []:
    return [len(str(element)) for element in arr]


def main():
    input_strings = ["abc", "apple", "orange"]
    output_strings = count_element_lengths(input_strings)
    print(output_strings)

if __name__=="__main__":
    main()