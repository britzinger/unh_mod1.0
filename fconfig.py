# fconfig.py

# Input file for Chords
EXCEL_INPUT_FILE = 'Partitions_new.xlsx'

# https://matplotlib.org/3.5.0/gallery/color/named_colors.html
UNH_COLORS = {
    1: 'deepskyblue',
    2: 'lightsalmon',
    3: 'purple',
    4: 'hotpink',
    5: 'red',
    6: 'gray',
    7: 'blue',
    8: 'yellow',
    9: 'black',
    10: 'saddlebrown',
    11: 'darkgreen',
    12: 'limegreen',
    13: 'lightskyblue',
    14: 'thistle'
 }

CHORD_WIDTH = 1     # lines on plot width. 1 is min
INTERSPACE = 5      # spaces between partitions on plot
BLACK_CHORDS = False # draw chords with black not defined colors

SHOW_PARTS_WITH_ONE_NODE = True # show partitions with only 1 node
WHITE_PARTS = True

DBG_CREATE_CSV = True
DBG_CSV_FOLDER = 'csv/'
