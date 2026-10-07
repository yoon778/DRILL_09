from pico2d import *


WIDTH, HEIGHT = 800, 600
SIZE = 100
x, y = WIDTH / 2, HEIGHT / 2


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False


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
        draw()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()

