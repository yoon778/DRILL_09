from pico2d import *


WIDTH, HEIGHT = 800, 600
SIZE = 100
x, y = WIDTH / 2, HEIGHT / 2


def main():
    open_canvas(WIDTH, HEIGHT)
    hide_lattice()
    ground = load_image('TUK_GROUND.png')
    running = True
    while running:
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
        clear_canvas()
        ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
        update_canvas()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()

