# This file is intended to be a terminal 
# Text Slides Presenter

# imports
import sys,os
import curses
import time

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

    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        current_slide = slides_data[slide_position]
        current_title = current_slide[0]
        current_lines = current_slide[1]

        desired_text_width = width // 2

        lines_for_title = len(current_title) // desired_text_width
        
        lines_for_text = 0
        for line in current_lines:
            lines_for_text += len(line) // desired_text_width

        spare_rows = height - lines_for_title - lines_for_text
        if spare_rows > 2:
            start_y = spare_rows // 2



        start_x = (width - desired_text_width) // 2
        start_x = min(start_x, (width - len(current_title) // 2))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x, current_title)
        stdscr.move(0, 0)
        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)



        # Print rest of text
        start_y += 2
        
        for line in current_lines:
            stdscr.addstr(start_y, start_x, line)
            stdscr.move(0, 0)
            start_y += 1

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

        if k == ord('n'):
            slide_position += 1
            slide_position = min(slide_position, max_slide_pos)
        elif k == ord('p'):
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






