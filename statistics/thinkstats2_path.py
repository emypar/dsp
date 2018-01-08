#! /usr/bin/env python3

"""Add location of ThinkStats 2 to sys.path for module imports.
"""

import sys
import os

# Thinkstats 2 is located ../.. from this dir
this_dir = os.path.abspath(os.path.dirname(__file__))
thinkstats2_code_dir = os.path.abspath(os.path.join(this_dir, '..', '..', 'ThinkStats2', 'code'))
if thinkstats2_code_dir not in sys.path:
    sys.path.insert(0, thinkstats2_code_dir)

# Make it the current dir since ThinkStats2 depends on it:
os.chdir(thinkstats2_code_dir)

                                         
                                           

