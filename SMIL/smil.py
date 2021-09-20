input = input()
for i, char in enumerate(input):
    if (char == ":" or char == ";") and len(input[i:]) > 1:
        if input[i+1] and input[i+1] == ")":
            print(i)
        elif (input[i+1] == "-")  and len(input[i:]) > 2:
            if input[i+2] == ")":
                print(i)