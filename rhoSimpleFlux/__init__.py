#!/usr/bin/env python

#--------------------------------------------------------------------------------------
## VulaSHAKA (Simultaneous Neutronic, Fuel Performance, Heat And Kinetics Analysis)
## Copyright (C) 2009-2010 Pebble Bed Modular Reactor (Pty) Limited (PBMR)
## 
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
## 
## See https://vulashaka.svn.sourceforge.net/svnroot/vulashaka
##
## Author : Alexey PETROV
##


#---------------------------------------------------------------------------
from Foam import FOAM_VERSION
if FOAM_VERSION( "==", "010600" ):
    from rhoSimpleFlux.r1_6 import *
    pass

    
#--------------------------------------------------------------------------------------
def entry_point():
    try:
       import sys; argv = sys.argv
       return main_standalone( len( argv ), argv )
    except NameError:
       print
       print "There is no implementation of the current OpenFOAM version"
       print
       pass


#--------------------------------------------------------------------------------------
if __name__ == "__main__" :
    entry_point()
    pass
    
    
#--------------------------------------------------------------------------------------