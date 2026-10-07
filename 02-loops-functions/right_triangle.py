# my version of the right triangle example from the module
# sorting the sides was easier than swapping with tmp


def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


def main():
    a = int(input("First side: "))
    b = int(input("Second side: "))
    c = int(input("Third side: "))
    if is_right_triangle(a, b, c):
        print("Right triangle")
    else:
        print("NOT a right triangle")


if __name__ == "__main__":
    main()
