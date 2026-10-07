from pico2d import *


def main():
    open_canvas()
    hide_lattice()
    running = True
    while running:
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False
        clear_canvas()
        update_canvas()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()

