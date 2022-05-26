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


INTERSPACE = 5      # spaces between partitions on plot
BLACK_CHORDS = True # chords are black, do not use UNH_COLORS

SHOW_PARTS_WITH_ONE_NODE = False # show partitions with only 1 node
WHITE_PARTS = True  # partitions are white, do not use UNH_COLORS
PLOT_TITLE = True   # display sheet name on plot

SAVE_PLOT_IMAGE = True              # save plots as 'partition name'_'sheet'.pdf
SAVE_PLOT_IMAGE_FOLDER = 'images/'  # saved plots folder
PLOT_DPI = 300                      # dpi of PNG image

SHOW_COLOR_BAR = True              # show color bar of UNH_COLORS

# debug variables
DBG_CREATE_CSV = True
DBG_CREATE_CSV_FOLDER = 'csv/'
