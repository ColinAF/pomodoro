import time
import curses

# TODO
# Center Text
# Add start / stop
# Display a cool session counter
# Add cool ascii pretty print 
# Print a nice bit of art and a cool outline
# Add in Intentions
# Add in a ding
# Log Session Stats
# Optional notifications
# Text file for settings

def pomodoro_timer(stdscr, duration):
    stdscr.clear()
    curses.curs_set(0)

	# Fix duration glitch
    while duration:
		# More accurate timer? 
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

