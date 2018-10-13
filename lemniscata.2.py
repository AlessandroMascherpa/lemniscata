#! python3
# -*- coding: utf-8 -*-

import sys
import threading
import numpy as np
from datetime import datetime

import common as cmn



# Compute points that: ( x^2 + y^2 )^2 = A ( x^2 -y^2 )
#



parameters_list = [ '<lower>', '<upper>', '<count>', '<A>', '<threads-count>' ]



def  lemniscata( x, y, A ):
    return  ( x**2 + y**2 )** 2  -  A * ( x**2 - y**2 )


def  resolve_window( iL, steps, xL, delta, yL, count, A, L ):

    i = iL
    x = xL
    while ( i < iL + steps ):

        j = 0
        y = yL
        while ( j < count ):

            L[ j, i ] = lemniscata( x, y, A )

            y += delta
            j += 1

        x += delta
        i += 1


def  resolve( lower, upper, count, A, cTs ):
    print( lower, upper, count )

    delta = ( upper - lower ) / count
    print( delta )

    L = np.zeros( shape= ( count, count ) )

    threads = []
    iL      = 0
    s       = (int) ( count / cTs )
    xL      = lower
    for i in range( cTs - 1 ):
        t  = threading.Thread( target= resolve_window, args= ( iL, s, xL, delta, lower, count, A, L, ) )
        threads.append( t )
        iL += s
        xL += s * delta

    t  = threading.Thread( target= resolve_window, args= ( iL, count - iL, xL, delta, lower, count, A, L, ) )
    threads.append( t )


    start = datetime.now()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    elapsed = datetime.now() - start
    print( "Elapsed time: " + str( elapsed ) )

    return L


def prepare( params ):
    lower = int( sys.argv[ 1 ] )
    upper = int( sys.argv[ 2 ] )
    N     = int( sys.argv[ 3 ] )
    A     = float( sys.argv[ 4 ] )
    T     = int( sys.argv[ 5 ] )

    L = resolve( lower, upper, N, A, T )

    cmn.contour( lower, upper, N, L, 'L-2' )


if  __name__ == "__main__":
    print( sys.platform )
    if ( len( sys.argv ) >= 1 + len( parameters_list ) ):
        prepare( sys.argv )
    else:
        cmn.show_help( sys.argv[ 0 ], parameters_list )
