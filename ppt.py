# This file is intended to be a terminal 
# Text Slides Presenter

# imports
import sys,os
import curses
import time
import random

######################################
# Global variables for convenience 
next_keys = ['n',' ','.']
prev_keys = ['p',',']
quit_keys = ['q','z']

# preparing the key variables
next_keys = [ord(k) for k in next_keys]
prev_keys = [ord(k) for k in prev_keys]
quit_keys = [ord(k) for k in quit_keys]
######################################


def read_slides_data_file(slide_file):
    '''
    This functions read the given text file
    and return the list of text for slides
    Inputs:
    slide_file - text file made with defined syntax
    '''
    try:
        with open(slide_file, 'r') as sf:
            try:    
                input_data = sf.readlines()
            except:
                print('Issue with the input file, cant read it...')
                return None
    except:
        print('Issue with the data file access...')
        return None
    else:
        print(f'read {len(input_data)} lines')
        return input_data

def get_slides(raw_data):
    '''
    This function creates the each slide data in form of list.
    inputs:
        raw_data - a list of text lines with defined syntax
    output:
        list of sides.
    '''

    slides = []

    temp_slide =[]
    temp_text = []

    for line_of_data in raw_data:

        trimmed = line_of_data.strip().replace('\n','')

        if  "#" in trimmed:
            # Handling the main title line
            if len(temp_text):
                temp_slide.append(temp_text)
            elif len(temp_slide):
                temp_slide.append([''])

            if len(temp_slide):
                slides.append(temp_slide)

            temp_slide =[]
            temp_text = []
            temp_slide.append(trimmed[1:])

        elif len(temp_slide) and trimmed != '':
            temp_text.append(trimmed)   

    # Handling the last slides aspect. 
    if len(temp_text):
        temp_slide.append(temp_text)
        slides.append(temp_slide)
    elif len(temp_slide):
        temp_slide.append('')
        slides.append(temp_slide)

    return slides


def animate_line(stdscr, line, start_x, y, n):
    '''
    Just a simple procedure to make the line appear as 
    like be drawn.
    input:
        stdscr - screen object of curse
        line - text to be placed
        start_x - start x position
        y - y position of the line
        n - delay in form of number of random marks
    '''

    jubbrisch = '#@$^%*&?><{}!'
    jubbrisch = [k for k in jubbrisch]
     
    for _ in range(n):
        x = start_x
        for _ in line:
            j = random.choice(jubbrisch)
            stdscr.addstr(y, x, j)
            x += 1
        stdscr.refresh()
        time.sleep(0.01)

    stdscr.addstr(y, start_x, line)
    stdscr.refresh()



def animate_chr(stdscr, line, start_x, y, n):
    '''
    Just a simple procedure to make the line appear as 
    like be drawn.
    input:
        stdscr - screen object of curse
        line - text to be placed
        start_x - start x position
        y - y position of the line
        n - delay in form of number of random marks
    '''

    jubbrisch = '#@$^%*&?><{}!'
    jubbrisch = [k for k in jubbrisch]
     
    x = start_x

    for k in line:
        for _ in range(n):
            j = random.choice(jubbrisch)
            stdscr.addstr(y, x, j)
            time.sleep(0.01)
            stdscr.refresh()
        stdscr.addstr(y, x, k)
        stdscr.refresh()
        x += 1


def break_line(line, max_length):
    # making title split to words
    words = line.strip().split(' ')
    new_line = []
    temp_line = ''

    for word in words:
        if len(temp_line) <= max_length:
            if word != '':
                temp_line += word + ' '
        else:
            new_line.append( temp_line )
            if word != '':
                temp_line = word + ' '

    new_line.append( temp_line )
    return new_line


def simple_print(slides_data):
    '''
    This procedure is about simple print out
    the slide data to terminal. 
    input:
        slides_data - list of list with slides data
    '''
    for slide in slides_data:
        print(f'::: {slide[0]} :::')
        print('\n')

        for text in slide[1]:
            print(text)
        
        print('\n')
        print('\n')

        input('press enter...')


def slide_show(stdscr, slides_data):
    '''
    This procedure displays the slides 
    on the full terminal window using the
    curses framework.
    inputs:
        - slides_data - list of lists with strings
    '''
    # stdscr = curses.initscr()
    slide_position = 0
    max_slide_pos = len(slides_data)-1

    stdscr.move(0, 0)

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    k = stdscr.getch()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (k not in quit_keys):
        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        desired_text_width = width // 2
        start_x = (width - desired_text_width) // 2

        current_slide = slides_data[slide_position]
        new_title = break_line(current_slide[0], desired_text_width)

        new_lines = []
        for line in current_slide[1]:
            new_lines.extend(break_line(line, desired_text_width))

        start_y = max(0, (height - len(new_title) - len(new_lines) - 1) // 2)

        # Rendering title
        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        for line in new_title:
            if start_y < height:
                stdscr.addstr(start_y, start_x, line) 
            start_y += 1 

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Rendering the text
        for line in new_lines:
            if start_y < height:
                # stdscr.addstr(start_y, start_x, line)
                animate_line(stdscr, line, start_x, start_y, 5)
                
            stdscr.move(0, 0)
            start_y += 1

        # Refresh the screen
        stdscr.move(0, 0)
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

        if k in next_keys:
            slide_position += 1
            slide_position = min(slide_position, max_slide_pos)
        elif k in prev_keys:
            slide_position -=1
            slide_position = max( slide_position, 0 )

    curses.echo()
    curses.endwin()




# Reading the line parameter
if len(sys.argv) > 1:
    argv = sys.argv[1]
    # simple_print(get_slides(read_slides_data_file(argv)))
    curses.wrapper(slide_show, get_slides(read_slides_data_file(argv)))
else:
    print('Please provide a slides data file...')






