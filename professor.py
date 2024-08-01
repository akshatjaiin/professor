import random
score = 10
def main():
    level = get_level()
    generate_integer(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass

def generate_integer(level):
   if level == 1:
       n = 0
   else:
       n = 10**(level-1)
   m = 10**level-1
   for i in range(10):
    X = random.randint(n,m)
    Y = random.randint(n,m)
    checkint(X,Y)

def checkint(X,Y):
    count = 0
    while count != 3:
        try:
            A = int(input(f"{X} + {Y} = "))
            if A != X+Y:
                raise ValueError
            else:
                return
        except (ValueError, TypeError):
            print("EEE")
            count += 1
    print(f"{X} + {Y} = {X+Y}")
    global score
    score -= 1

if __name__ == "__main__":
    main()