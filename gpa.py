def main():
    num = int(input("Please enter how many grades you would like to include?: "))
    total = 0
    for i in range(num):
        grade = input("Please enter a grade for student: ")
        if grade == "A":
            total += 4
        elif grade == "B":
            total += 3
        elif grade == "C":
            total += 2
        elif grade == "D":
            total += 1
        elif grade == "F":
            total += 0

    gpa = total / num
    ltr = "l"
    if gpa >= 4:
        ltr = "A"
    if gpa >= 3 and gpa < 4:
        ltr = "B"
    if gpa >= 2 and gpa < 3:
        ltr = "C"
    if gpa >= 1 and gpa < 2:
        ltr = "D"
    if gpa < 1:
        ltr = "F"

    print("The average grade score for the class is: ", ltr)


if __name__ == "__main__":
    main()
