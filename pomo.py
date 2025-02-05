import time
import curses

def pomodoro_timer(stdscr, duration):
    stdscr.clear()
    curses.curs_set(0)

    while duration:
        mins, secs = divmod(duration, 60)
        timer = f'{mins:02d}:{secs:02d}'
        stdscr.addstr(0, 0, "Pomodoro Timer")
        stdscr.addstr(1, 0, timer)
        stdscr.refresh()
        time.sleep(1)
        duration -= 1

    stdscr.addstr(2, 0, "Time's up!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(lambda stdscr: pomodoro_timer(stdscr, 1500))

