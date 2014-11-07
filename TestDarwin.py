import random
from io import StringIO
from unittest import main,TestCase
from Darwin import Species, Creature, Darwin

class TestDarwin(TestCase):

    def test_add_instr1(self):
        s1 = Species([],'h')
        s1.add_instr('go')
        self.assertEqual(s1.type,'h')
        self.assertEqual(s1.program[0],'go')

    def test_add_instr2(self):
        s1 = Species([],'g')
        s1.add_instr('go ha')
        self.assertEqual(s1.type,'g')
        self.assertEqual(s1.program[0],'go ha')

    def test_add_instr3(self):
        s1 = Species([],'p')
        s1.add_instr('go haha')
        self.assertEqual(s1.type,'p')
        self.assertEqual(s1.program[0],'go haha')

    def test_next_instr1(self):
        s1 = Species([],'h')
        s1.add_instr('go')
        self.assertEqual(s1.next_instr(0),'go')

    def test_next_instr2(self):
        s1 = Species([],'h')
        s1.add_instr('hop')
        self.assertEqual(s1.next_instr(0),'hop')

    def test_next_instr3(self):
        s1 = Species([],'h')
        s1.add_instr('hop2')
        self.assertEqual(s1.next_instr(0),'hop2')

    def test_next_instr4(self):
        s1 = Species([],'h')
        s1.add_instr('hop3')
        self.assertEqual(s1.next_instr(0),'hop3')

    def test_rotate1(self):
        c = Creature('h',1)
        c.rotate('right')
        self.assertEqual(c.direction,2)

    def test_rotate2(self):
        c = Creature('h',2)
        c.rotate('right')
        self.assertEqual(c.direction,3)

    def test_rotate3(self):
        c = Creature('h',3)
        c.rotate('right')
        self.assertEqual(c.direction,4)


    def test_add_creature1(self):
        D = Darwin(1,1)
        D.add_creature("x",0,0)
        self.assertEqual(D.grid[0][0],'x')

    def test_add_creature2(self):
        D = Darwin(2,2)
        D.add_creature("y",1,1)
        self.assertEqual(D.grid[1][1],'y')

    def test_add_creature3(self):
        D = Darwin(3,3)
        D.add_creature("z",0,0)
        self.assertEqual(D.grid[0][0],'z')

    def test_print_grid1(self):
        D = Darwin(2,2)
        hopper = Species([], 'h')
        h1 = Creature(hopper, 1)
        D.add_creature(h1,1,1)
        self.assertEqual(D.print_grid(0),None)

    def test_print_grid2(self):
        D = Darwin(1,1)
        hopper = Species([], 'h')
        h1 = Creature(hopper, 2)
        D.add_creature(h1,0,0)
        self.assertEqual(D.print_grid(0),None)

    def test_print_grid3(self):
        D = Darwin(3,3)
        food = Species([], '')
        f = Creature(food, 2)
        D.add_creature(f,1,1)
        self.assertEqual(D.print_grid(0),None)

    def test_get_next1(self):
        D = Darwin(2,2)
        D.add_creature("y",1,1)
        self.assertEqual(D.get_next(2,1,1),(None, 1, 1))

    def test_get_next2(self):
        D = Darwin(3,3)
        D.add_creature("x",2,1)
        self.assertEqual(D.get_next(2,1,1),('.',1,2))

    def test_get_next3(self):
        D = Darwin(2,2)
        D.add_creature("z",1,1)
        self.assertEqual(D.get_next(1,1,1),('.', 0, 1))

    def test_run1(self):

        food = Species([], 'f')
        food.add_instr(['left'])
        food.add_instr(['go', 0])

        hopper = Species([], 'h')
        hopper.add_instr(['hop'])
        hopper.add_instr(['go', 0])

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

        self.assertEqual(g1.run(5),None)


    def test_run2(self):
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

        t1 = Creature(trap, 3)
        h1 = Creature(hopper, 2)
        r1 = Creature(rover, 1)
        t2 = Creature(trap, 4)

        g2 = Darwin(7, 9)
        g2.add_creature(t1, 0, 0)
        g2.add_creature(h1, 3, 2)
        g2.add_creature(r1, 5, 4)
        g2.add_creature(t2, 6, 8)

        self.assertEqual(g2.run(5),None)

    def test_run3(self):
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

        g3 = Darwin(72, 72)
        creatureTypes = [food, hopper, rover, trap]
        for ctype in creatureTypes:
            for i in range (0, 10):
                row = random.randrange(0, 72)
                col = random.randrange(0, 72)
                direction = random.randrange(0, 4)
                g3.add_creature(Creature(ctype, direction), row, col)
        self.assertEqual(g3.run(5),None)


main()

