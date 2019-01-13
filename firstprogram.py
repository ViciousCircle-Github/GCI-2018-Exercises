# check if the number is a multiple of 3. if it is check also if it is multiple of 7



print ("Enter a number")
number = int(input())
if number % 3 is 0:
    print("Number is only multiple of 3")
    if number % 7 is 0:
        print("number is only multiple of 7")
        if number % 7 is 0 and number % 3 is 0:
            print("number is multiple of 3 and 7")
       