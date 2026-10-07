from math import hypot
from time import perf_counter

from pico2d import *


WIDTH, HEIGHT = 800, 600
SIZE = 100
SPEED = 200
x, y = WIDTH / 2, HEIGHT / 2
face = 1  # 1: 오른쪽, -1: 왼쪽
moving = False
frame = 0
frame_time = 0.0
FRAME_DELAY = 0.1
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
    # pico2d의 get_events는 창 포커스 이벤트를 전달하지 않는다.
    if not SDL_GetKeyboardFocus():
        keys.clear()


def update(dt):
    global x, y, face, moving, frame, frame_time
    # 창 이동 등으로 오래 지연되어도 한 번에 크게 뛰지 않는다.
    dt = min(max(dt, 0.0), 0.1)
    previous = (moving, face)
    old_x, old_y = x, y
    dx = int(SDLK_RIGHT in keys) - int(SDLK_LEFT in keys)
    dy = int(SDLK_UP in keys) - int(SDLK_DOWN in keys)
    # 위아래로만 움직일 때는 마지막 좌우 방향을 유지한다.
    if dx:
        face = dx
    length = hypot(dx, dy)
    if length:
        dx, dy = dx / length, dy / length
    x += dx * SPEED * dt
    y += dy * SPEED * dt
    x = min(max(x, SIZE / 2), WIDTH - SIZE / 2)
    y = min(max(y, SIZE / 2), HEIGHT - SIZE / 2)
    # 경계 제한 뒤 실제 좌표가 변했을 때만 이동 동작을 재생한다.
    moving = (x, y) != (old_x, old_y)
    if previous != (moving, face):
        frame, frame_time = 0, 0.0
    else:
        frame_time += dt
        while frame_time >= FRAME_DELAY:
            frame = (frame + 1) % 8
            frame_time -= FRAME_DELAY


def draw():
    clear_canvas()
    ground.draw(WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
    # pico2d는 이미지 아래쪽을 기준으로 행을 자른다.
    if moving:
        row = 101 if face == 1 else 1
    else:
        row = 301 if face == 1 else 201
    character.clip_draw(1 + frame * SIZE, row, SIZE, SIZE, x, y)
    update_canvas()


def main():
    global ground, character, running
    open_canvas(WIDTH, HEIGHT)
    hide_lattice()
    ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    running = True
    last_time = perf_counter()
    while running:
        now = perf_counter()
        dt = now - last_time
        last_time = now
        handle_events()
        update(dt)
        draw()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()

