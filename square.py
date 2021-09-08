def main():
    upper = int(input("Please enter a positive integer: "))
    if upper <= 0:
        print("Invalid inpuut; must be positive and greater than 0")
        exit(1)
    square_to(upper)


def square_to(var):
    looping = True
    square = 2
    while looping:
        temp = square ** 2
        if temp > var:
            return
        if temp % 2 == 0:
            print(temp)
        square += 1


if __name__ == "__main__":
    main()
