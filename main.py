from flying_bird import FlyingBird
from penguin import Penguin

def make_bird_move(bird):
    bird.move()

birds = [FlyingBird(), Penguin()]

for bird in birds:
    make_bird_move(bird)
