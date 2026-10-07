from pico2d import *


WIDTH, HEIGHT = 800, 600
SIZE = 100
x, y = WIDTH / 2, HEIGHT / 2
face = 1  # 1: 오른쪽, -1: 왼쪽
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
    global x, y, face
    dx = int(SDLK_RIGHT in keys) - int(SDLK_LEFT in keys)
    dy = int(SDLK_UP in keys) - int(SDLK_DOWN in keys)
    # 위아래로만 움직일 때는 마지막 좌우 방향을 유지한다.
    if dx:
        face = dx
    x += dx * 2
    y += dy * 2


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

