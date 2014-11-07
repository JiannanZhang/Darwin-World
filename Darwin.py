import random
# defines what each species can do
class Species:
    def __init__(self, program, species_type):
        self.program = []
        assert self.program == []
        self.type = species_type

    def add_instr(self, instr):
        # add each instruction to program
        self.program.append(instr)

    def next_instr(self, pc):
        # return the instruction at given index
        assert self.program != []
        return self.program[pc]

# an instance of a creature
class Creature:
    def __init__(self, species, direction):
        self.species = species
        self.direction = direction
        self.pc = 0
        self.hasMoved = False
        assert self.hasMoved == False

    # rotate to the left or right
    def rotate(self, direction):
        # turn right
        if direction == 'right':
            if self.direction != 4:
                self.direction += 1
            else:
                self.direction = 1
        # turn left
        else:
            if self.direction != 1:
                self.direction -= 1
            else:
                self.direction = 4
        assert self.direction != direction

    def __str__(self):
        # returns species type as string
        return self.species.type


# an instance of the board
class Darwin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        assert self.x == x
        assert self.y == y

        # create empty grid with . in all positions
        self.grid = []
        for i in range(x):
            row = []
            for j in range(y):
                row.append('.')
            self.grid.append(row)


    def add_creature(self, creature, x, y):
        # changes value at the grid to the creature
        self.grid[x][y] = creature

    def print_grid(self, turn_number):
        if turn_number < 10 or turn_number % 100 == 0: 
            # print turn number
            print('Turn =', str(turn_number) + '.', end = '\n')
            
            # print top count
            print('  ', end = '')
            for n in range (self.y):
                if (n < self.y - 1):
                    print (n % 10, end = '')
                else:
                    print(n % 10, end='\n')
            
            # instantiate a counter for vertical numbers
            counter = 0
            for line in self.grid:
                print(counter % 10, end=' ')
                # instantiate index to print newline at the end of each line
                index = 0
                for creature in line:
                    if (index != self.y - 1):
                        if creature == '.':
                            print(creature, end = '')
                        else:
                            print(creature.species.type, end = '')
                    else:
                        if creature == '.':
                            print(creature, end = '\n')
                        else:
                            print(creature.species.type, end = '\n')
                    index += 1
                counter += 1
            # print space between grids
            print('')


    def get_next(self,direction, x_pos,y_pos):
        next_spot = None
        next_x = x_pos
        next_y = y_pos

        # current direction is west
        if direction == 4:
            if y_pos - 1 < 0:
                return next_spot, next_x, next_y
            next_spot = self.grid[x_pos][y_pos - 1]
            next_y -= 1

        # current direction is south
        elif direction == 3:
            if x_pos + 1 > self.x-1:
                return next_spot, next_x, next_y
            next_spot = self.grid[x_pos + 1][y_pos]
            next_x += 1

        # current direction is east
        elif direction == 2:
            if y_pos + 1 > self.y-1:
                return next_spot, next_x, next_y
            next_spot = self.grid[x_pos][y_pos + 1]
            next_y += 1

        # current direction is north
        else:
            if x_pos - 1 < 0:
                return next_spot, next_x, next_y
            next_spot = self.grid[x_pos - 1][y_pos]
            next_x -= 1

        assert next_spot != None
        return next_spot, next_x, next_y
        #return next_spot
    

    def run(self, number_of_turns):
        for num in range (number_of_turns + 1):
            self.print_grid(num)

            # go through the grid 
            for i in range (self.x):
                for j in range (self.y):
                    
                    # find creature at this location
                    c = self.grid[i][j]

                    # skip if space does not contain a creature
                    if c == '.':
                        continue

                    # c is the creature
                    c_species = c.species
                    direction = c.direction

                    # get the instr str
                    instr = c.species.next_instr(c.pc)
                    temp_instr = instr[0]
                    assert temp_instr == instr[0]

                    # get the next creature
                    next_creature, next_x, next_y = self.get_next(direction, i, j)

                    # if the creature hasn't moved, it can execute these commands:
                    while c.hasMoved == False:
                        # get the most recent instruction list and value
                        instr = c.species.next_instr(c.pc)
                        temp_instr = instr[0]

                        # the next space is empty
                        if temp_instr == 'if_empty':
                            if (next_creature == '.'):
                                # execute command mentioned
                                c.pc = instr[1]
                            else:
                                c.pc += 1
                            temp_instr = c_species.next_instr(c.pc)[0]
                            assert temp_instr != instr[0]

                        # the next space is a wall
                        elif temp_instr == 'if_wall':
                            if (next_creature == None):
                                c.pc = instr[1]
                            else:
                                c.pc += 1
                            temp_instr = c_species.next_instr(c.pc)[0]
                            assert temp_instr != instr[0]

                        # randomly choose between executing related command or next command
                        elif temp_instr == 'if_random':
                            if (random.randrange(0, 2) % 2 == 1):
                                c.pc = instr[1]
                            else:
                                c.pc += 1
                            temp_instr = c.species.next_instr(c.pc)[0]
                            assert temp_instr != instr[0]

                        # the next creature is an enemy
                        elif temp_instr == 'if_enemy':
                            if (next_creature != None and next_creature != '.'):
                                c.pc = instr[1]
                            else:
                                c.pc += 1
                            temp_instr = c.species.next_instr(c.pc)[0]
                            assert temp_instr != instr[0]

                        # go to the command provided
                        elif temp_instr == 'go':
                            c.pc = instr[1]
                            temp_instr = c.species.next_instr(c.pc)[0]
                            assert temp_instr != instr[0]

                        # action commands -- break out of the loop
                        # hop forward by one space
                        elif temp_instr == 'hop':
                            if (next_creature == '.'):
                                self.grid[next_x][next_y] = c
                                self.grid[i][j] = '.'
                            c.hasMoved = True
                            c.pc += 1
                            break

                        # turn left or right
                        elif temp_instr == 'left' or temp_instr == 'right':
                            c.rotate(temp_instr)
                            c.hasMoved = True
                            c.pc += 1
                            break

                        # change the next creature's species to this creature's species
                        elif temp_instr == 'infect':
                            next_creature.species = c.species
                            next_creature.pc = 0
                            c.hasMoved = True
                            c.pc += 1
                            break

            # reset the hasMoved value before next turn of game
            for line in self.grid:
                for creat in line:
                    if creat != '.':
                        creat.hasMoved = False
                        assert creat.hasMoved == False