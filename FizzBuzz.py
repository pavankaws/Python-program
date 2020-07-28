class Puzzle:
    def solve(self):
        for i in range(1, 100):
            if i % 3 == 0 and i % 5 == 0:
                print("Fizz Buzz")
                continue
            elif i % 3 == 0:
                print("Fizz")
                continue
            elif i % 5 == 0:
                print("Buzz")
                continue
            print(i)


if __name__ == "__main__":
    Puzzle().solve()
