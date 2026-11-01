from collections import deque

def main():
    players = input("Enter players: ").split(",")
    passes = int(input("Enter number of passes: "))

    circle = deque(players)

    while len(circle) > 1:
        for i in range(passes):
            player = circle.popleft()
            circle.append(player)

        eliminated = circle.popleft()
        print(eliminated, "is out")

    print("Winner:", circle[0])

if __name__ == "__main__":
    main()
