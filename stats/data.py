import os, glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()