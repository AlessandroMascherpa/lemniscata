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

    delta = ( upper - lower ) / count
    print( delta )

    L = np.zeros( shape= ( count, count ) )

    start = datetime.now()

    i = 0
    x = lower
    while ( i < count ):

        j = 0
        y = lower
        while ( j < count ):

            L[ j, i ] = lemniscata( x, y, A )

            y += delta
            j += 1

        x += delta
        i += 1

    elapsed = datetime.now() - start
    print( "Elapsed time: " + str( elapsed ) )

    return L


def prepare( params ):
    lower = int( sys.argv[ 1 ] )
    upper = int( sys.argv[ 2 ] )
    N     = int( sys.argv[ 3 ] )
    A     = float( sys.argv[ 4 ] )

    L = resolve( lower, upper, N, A )

    cmn.contour( lower, upper, N, L, 'L-1' )


if  __name__ == "__main__":
    print( sys.platform )
    if ( len( sys.argv ) >= 1 + len( parameters_list ) ):
        prepare( sys.argv )
    else:
        cmn.gauss_help( sys.argv[ 0 ], parameters_list )
