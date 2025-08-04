"""Module providing a function printing python version."""

import os

if os.name == 'nt':
    print('windows')
else:
    print('otro')