import os
current_dir = os.path.dirname(__file__)
relative_path = "../"
joined_path = os.path.join(current_dir, relative_path)
import sys
sys.path.append(joined_path)
