from Darwin import Species, Creature, Darwin
import random
from random import randrange, seed
import sys

# food
food = Species([], 'f')
food.add_instr(['left'])
food.add_instr(['go', 0])

# hopper
hopper = Species([], 'h')
hopper.add_instr(['hop'])
hopper.add_instr(['go', 0])

# rover
rover = Species([], 'r')
rover.add_instr(['if_enemy', 9])
rover.add_instr(['if_empty', 7])
rover.add_instr(['if_random', 5])
rover.add_instr(['left'])
rover.add_instr(['go', 0])
rover.add_instr(['right'])
rover.add_instr(['go', 0])
rover.add_instr(['hop'])
rover.add_instr(['go', 0])
rover.add_instr(['infect'])
rover.add_instr(['go', 0])

# trap
trap = Species([], 't')
trap.add_instr(['if_enemy', 3])
trap.add_instr(['left'])
trap.add_instr(['go', 0])
trap.add_instr(['infect'])
trap.add_instr(['go', 0])


print("*** Darwin 8x8 ***")
f1 = Creature(food, 2)
h1 = Creature(hopper, 1)
h2 = Creature(hopper, 2)
h3 = Creature(hopper, 3)
h4 = Creature(hopper, 4)
f2 = Creature(food, 1)

g1 = Darwin(8, 8)
g1.add_creature(f1, 0, 0)
g1.add_creature(h1, 3, 3)
g1.add_creature(h2, 3, 4)
g1.add_creature(h3, 4, 4)
g1.add_creature(h4, 4, 3)
g1.add_creature(f2, 7, 7)
g1.run(5)


print("*** Darwin 7x9 ***")
t1 = Creature(trap, 3)
h1 = Creature(hopper, 2)
r1 = Creature(rover, 1)
t2 = Creature(trap, 4)

g2 = Darwin(7, 9)
g2.add_creature(t1, 0, 0)
g2.add_creature(h1, 3, 2)
g2.add_creature(r1, 5, 4)
g2.add_creature(t2, 6, 8)

g2.run(5)



print("*** Darwin 72x72 without Best ***")
seed(0);

g3 = Darwin(72, 72)
creatureTypes = [food, hopper, rover, trap]
for ctype in creatureTypes:
    for i in range (0, 10):
        row = random.randrange(0, 72)
        col = random.randrange(0, 72)
        direction = random.randrange(0, 4)
        g3.add_creature(Creature(ctype, direction), row, col)

g3.run(1000)


# #print("*** Darwin 72x72 with Best ***")
# seed(0);

# # best
# best = Species([], 'b')
# best.add_instr(['if_enemy', 9])
# best.add_instr(['if_empty', 4])
# best.add_instr(['left'])
# best.add_instr(['go', 0])
# best.add_instr(['hop'])
# best.add_instr(['go', 0])
# best.add_instr(['infect'])
# best.add_instr(['go', 0])


# g4 = Darwin(72, 72)
# creatureTypes = [food, hopper, rover, trap, best]
# for ctype in creatureTypes:
#     for i in range (0, 10):
#         row = random.randrange(0, 72)
#         col = random.randrange(0, 72)
#         direction = random.randrange(0, 4)
#         g4.add_creature(Creature(ctype, direction), row, col)

# #g4.run(1000)


