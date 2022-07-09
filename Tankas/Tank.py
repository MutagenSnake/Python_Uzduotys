class Tank:
    location = {'x': 0, 'y': 0}
    direction = 'n'
    shots_total = {'n': 0, 'e': 0, 's': 0, 'w': 0}
    tank_move_history = [{'x': 0, 'y': 0}]
    tank_shot_history =[]

    def move_north(self):
        new_x = self.location['x'] + 1
        self.location.update({'x': new_x})
        self.direction = 'n'
        self.tank_move_history.append({'x': new_x, 'y': self.location['y']})
        print(f'moved to:{self.location}')

    def move_east(self):
        new_y = self.location['y'] + 1
        self.location.update({'y': new_y})
        self.direction = 'e'
        self.tank_move_history.append({'x': self.location['x'], 'y': new_y})
        print(f'moved to:{self.location}')

    def move_south(self):
        new_x = self.location['x'] - 1
        self.location.update({'x': new_x})
        self.direction = 's'
        self.tank_move_history.append({'x': new_x, 'y': self.location['y']})
        print(f'moved to:{self.location}')

    def move_west(self):
        new_y = self.location['y'] - 1
        self.location.update({'y': new_y})
        self.direction = 'w'
        self.tank_move_history.append({'x': self.location['x'], 'y': new_y})
        print(f'moved to:{self.location}')

    def shoot(self):
        shot_distance = int(input('Shot distance (max: 10):'))
        if shot_distance in range(1,11):
            target_coords = {}
            if self.direction == 'n':
                target_coords = {'x': self.location['x'] + shot_distance, 'y': self.location['y']}
                self.shots_total.update({'n': self.shots_total['n']+1})
            elif self.direction == 'e':
                target_coords = {'x': self.location['x'], 'y': self.location['y'] + shot_distance}
                self.shots_total.update({'e': self.shots_total['e'] + 1})
            elif self.direction == 's':
                target_coords = {'x': self.location['x'] + shot_distance, 'y': self.location['y']}
                self.shots_total.update({'s': self.shots_total['s'] + 1})
            elif self.direction == 'w':
                target_coords = {'x': self.location['x'], 'y': self.location['y'] - shot_distance}
                self.shots_total.update({'w': self.shots_total['w'] + 1})
            self.tank_shot_history.append(target_coords)
            print(f'Shots fired at {target_coords} !!!')
        else:
            print("Can't shoot there")

    def turn(self):
        self.direction = input('Choose direction (n,e,s,w): ')

    def info(self):
        print('--------------------------------------------------')
        print(f'Direction: {self.direction}')
        print(f'Coordinates: {self.location}')
        print(f'Shots taken:{sum(self.shots_total.values())}')
        print(f'Shots by direction:{self.shots_total}')
        print(f'Moves taken: {self.tank_move_history}')
        print(f'Shot history: {self.tank_shot_history}')
        print('--------------------------------------------------')


AbramsA1 = Tank()

while True:
    action = int(input('Shoot: 1\nScoot: 2\nStatus report: 3\nChange direction: 4\nRetreat: 5\n'))
    if action == 2:
        direction = input('Choose direction (n,e,s,w): ')
        if direction == 'n':
            AbramsA1.move_north()
        elif direction == 'e':
            AbramsA1.move_east()
        elif direction == 's':
            AbramsA1.move_south()
        elif direction == 'w':
            AbramsA1.move_west()
        else: print("Bad input!")
    elif action == 1:
        print(f'Location: {AbramsA1.location}')
        print(f'Facing:{AbramsA1.direction}')
        AbramsA1.shoot()
    elif action == 3:
        AbramsA1.info()
    elif action == 4:
        AbramsA1.turn()
    elif action == 5:
        print('Retreating!')
        break
    else:
        print('Bad input!')