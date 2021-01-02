# TextSlides

## TLDR
A simple terminal oriented Text based slides presenter in ptyhon

## Back story
This simple tool was created as a part of checking out the curses python library.

## What it does
It take the given txt file and plays it as kind of slides in the terminal.

## How it works
Just use the command like:
`python ppt.pt slide_file.txt`

Where the 'slide_file.txt' is a text file with simple structure.
The structure is like this:
- lines starting with `#` start new slide and is treated as **slide title**
- normal text lines are just slide text

Each slide is placed on separated screen with the title in top. If the tekst is longer than the available space it will be cut to the possible to show area.

Then use:
- `n` `.` _space_ for next slide
- `p` `,` for previous slide
- `q` `z` to quit


## Example side file text
```
# First slide title

First slide text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris lacinia leo ligula, vitae congue odio bibendum quis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus lobortis fermentum tincidunt. Sed eu venenatis felis.

# Second slide title

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris lacinia leo ligula, vitae congue odio bibendum quis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus lobortis fermentum tincidunt. Sed eu venenatis felis.
```

## Can it be useful?

I believe yes, if you want to make a quick talk and you do have a terminal that can work in full screen and preferably with support for the font size change. 
And if you believe that such simple tool can't do the job I do encourage you to look for the "Death by PowerPoint talk" on YouTube :) 
