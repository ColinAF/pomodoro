import time
import curses
import threading
import simpleaudio as sa

# TODO
# Increase font size
# Add start / stop do this in a super minimal way < Space Bar > 
# Display a cool session counter
# Add cool ascii pretty print 
# Print a nice bit of art and a cool outline
# Add in Intentions
# Add in a ding
# Log Session Stats
# Optional notifications
# Text file for settings

TIMES_UP = "Time's up!"

def play_sound():
    # The wave file must be in 16-bit PCM format
    wave_obj = sa.WaveObject.from_wave_file("ding.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def pomodoro_timer(stdscr, duration):
    # Start the playback in a daemon thread (it'll exit with the main program)
    sound_thread = threading.Thread(target=play_sound, daemon=True)
    sound_thread.start() 
   
    # Start the playback in its own thread
    #sound_thread = threading.Thread(target=play_sound)
    #sound_thread.start()
    #sound_thread.join()  # Wait for the sound to finish before proceeding
    
    stdscr.clear()
    curses.curs_set(0)
   
    # Fix duration glitch
    while duration:
		# More accurate timer? 
        mins, secs = divmod(duration, 60)
        timer = f'{mins:02d}:{secs:02d}'
        stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - len(timer) // 2, timer)
        stdscr.refresh()
        time.sleep(1)
        duration -= 1

    stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - len(TIMES_UP) // 2, TIMES_UP)
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(lambda stdscr: pomodoro_timer(stdscr, 1500))

