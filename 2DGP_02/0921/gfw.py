# version 2020-0921
from pico2d import *

running = True
frame_interval = 0.01

def quit():
    global running
    running = False

def run(state):
    global running

    open_canvas()
    state.enter()

    while running:
        # event handling
        evts = get_events()
        for e in evts:
            state.handle_event(e)

        # game logic
        state.update()

        # game rendering
        clear_canvas()
        state.draw()
        update_canvas()

        delay(frame_interval)

    close_canvas()
