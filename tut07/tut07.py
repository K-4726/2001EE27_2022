from platform import python_version
import math
import glob
import os
import pandas as pd
from datetime import datetime
start_time = datetime.now()
import threading

# firstly we have to create columns
# " " , "Octant Id" , "+1" ..... "-4" , "+1 " ..... "-4 " , "   ", "    " for integrating 5th tutorial
# 1 , 3, 4 spaces empty columns 

graph = {0:"+1 " , 1:"-1 "  , 2:"+2 "  , 3:"-2 "  , 4:"+3 "  , 5:"-3 "  , 6:"+4 "  , 7:"-4 "}
