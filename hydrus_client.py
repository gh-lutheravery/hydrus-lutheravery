#!/usr/bin/env python3

# Hydrus is released under WTFPL
# You just DO WHAT THE FUCK YOU WANT TO.
# https://github.com/sirkris/WTFPL/blob/master/WTFPL.md

#from hydrus import hydrus_client_boot

if __name__ == '__main__':
    print('client')
    from pycallgraph2 import PyCallGraph
    from pycallgraph2.output import GraphvizOutput

    with PyCallGraph(output=GraphvizOutput()):
        code_to_profile()
    #from hydrus.core import HydrusConstants as HC
    #hydrus_client_boot.boot()
    
