# Second task Zombies against plants.
from zombies_plants import *

# we receive the necessary lists one by one
def start(w_list: list):
    num = 0
    for battle in war_list:
        num += 1
        l_an = battle[num]
        r = war(l_an[0], l_an[1])
        print(f"plants: {l_an[0]}, zombies: {l_an[1]} -> {r}")


if __name__ == "__main__":
    start(war_list)



# Press the green button in the gutter to run the script.

