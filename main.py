# This is a sample Python script.
from zombies_plants import war
zombies = [1, 3, 5, 7]
plants = [2, 4, 6, 8]
zombies1 = [1, 3, 5, 7]
plants1 = [2, 4]
zombies2 = [1, 3, 5, 7]
plants2 = [2, 4, 0, 8]
zombies3 = [2, 1, 1, 1]
plants3 = [1, 2, 1, 1]
def resul_war(ar1, ar2):
    print(war(ar1, ar2))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    resul_war(zombies2, plants2)


