#! python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
from datetime import datetime

import common as cmn



# Compute points that: ( x^2 + y^2 )^2 = A ( x^2 -y^2 )
#



parameters_list = [ '<lower>', '<upper>', '<count>', '<A>' ]



def  lemniscata( x, y, A ):
    return  ( x**2 + y**2 )** 2  -  A * ( x**2 - y**2 )


def  resolve( lower, upper, count, A ):
    print( lower, upper, count )

    start = datetime.now()

    b    = np.linspace( lower, upper, num= count )
    x, y = np.meshgrid( b, b )

    L    = lemniscata( x, y, A )


    elapsed = datetime.now() - start
    print( "Elapsed time: " + str( elapsed ) )

    return L


def prepare( params ):
    lower = int( sys.argv[ 1 ] )
    upper = int( sys.argv[ 2 ] )
    N     = int( sys.argv[ 3 ] )
    A     = float( sys.argv[ 4 ] )

    L = resolve( lower, upper, N, A )

    cmn.contour( lower, upper, N, L, 'L-3' )


if  __name__ == "__main__":
    print( sys.platform )
    if ( len( sys.argv ) >= 1 + len( parameters_list ) ):
        prepare( sys.argv )
    else:
        cmn.gauss_help( sys.argv[ 0 ], parameters_list )
