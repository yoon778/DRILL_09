from pico2d import *


WIDTH, HEIGHT = 800, 600
SIZE = 100
x, y = WIDTH / 2, HEIGHT / 2
keys = set()
ARROWS = {SDLK_LEFT, SDLK_RIGHT, SDLK_UP, SDLK_DOWN}


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key in ARROWS:
            keys.add(event.key)
        elif event.type == SDL_KEYUP:
            keys.discard(event.key)


def update():
    global x
    dx = int(SDLK_RIGHT in keys) - int(SDLK_LEFT in keys)
    x += dx * 2


def draw():
    clear_canvas()
    ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    # 시트 테두리 1px을 제외한 오른쪽 IDLE 첫 프레임
    character.clip_draw(1, 301, SIZE, SIZE, x, y)
    update_canvas()


def main():
    global ground, character, running
    open_canvas(WIDTH, HEIGHT)
    hide_lattice()
    ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    running = True
    while running:
        handle_events()
        update()
        draw()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()

