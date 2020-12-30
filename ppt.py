# This file is intended to be a treminal 
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

            if len(temp_slide):
                slides.append(temp_slide)

            temp_slide =[]
            temp_text = []
            temp_slide.append(trimmed)   

        elif len(temp_slide) and trimmed != '':
            temp_text.append(trimmed)
    
    if len(temp_text):
        temp_slide.append(temp_text)
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

# Reading the line parameter
argv = sys.argv[1]
simple_print(get_slides(read_slides_data_file(argv)))






