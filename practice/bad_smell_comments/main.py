
class Unit:

    def move_by_field(self, field, x: int, y: int, moving_direction:str, fly : bool, sneak: bool, base_speed: int):

        if fly and sneak:
            raise ValueError('Рожденный ползать летать не должен!')

        if moving_direction == 'UP':
            new_y = y + base_speed
        elif moving_direction == 'DOWN':
            new_y = y - base_speed
        elif moving_direction == 'LEFT':
            new_x = x - base_speed
        elif moving_direction == 'RIGHT':
            new_x = x + base_speed


        field.set_unit(x=new_x, y= new_y, unit=self)

