from __future__ import division

X = 80
DELTA = X/20
GAMMA = 1

#######BOARD########
### 0   1   2  3  ##
####################
# 0#i1--i2--OO--i3##
#  #--------------##
# 1#i4--XX--##--i5##
#  #--------------##
# 2#SS--i6--i7--i8##
####################

# State List

class State:
    
    def __init__(self,c):
        self.x = c[0]
	self.y = c[1]
	self.utility = 0
	    
    def act(self,action):
	# resultSet(state,p) 
	resultSet = action[self]
	return resultSet
	
    def setUtility(self, u):
    	self.utility = u	

    def getUtility(self):
        return self.utility

i1 = State((0,0))
i2 = State((0,1))
i3 = State((0,3))
i4 = State((1,0))
i5 = State((1,3))
i6 = State((2,1))
i7 = State((2,2))
i8 = State((2,3))
sS = State((2,0))
xX = State((1,1))
oO = State((0,2))

# set utility
oO.setUtility(X)
xX.setUtility(-1*X)

StateList = []

StateList.append(i1)
StateList.append(i2)
StateList.append(i3)
StateList.append(i4)
StateList.append(i5)
StateList.append(i6)
StateList.append(i7)
StateList.append(i8)
StateList.append(sS)
#StateList.append(xX)
#StateList.append(oO)


# Action-State Mapping :

North = {
	
    i1:((i1,0.8),(i1,0.1),(i2,0.1)),
    i2:((i2,0.8),(oO,0.1),(i1,0.1)),
    i3:((i3,0.8),(oO,0.1),(i3,0.1)),
    i4:((i1,0.8),(xX,0.1),(i4,0.1)),
    i5:((i3,0.8),(i5,0.1),(i5,0.1)),
    i6:((xX,0.8),(i7,0.1),(sS,0.1)),
    i7:((i7,0.8),(i8,0.1),(i6,0.1)),
    i8:((i5,0.8),(i8,0.1),(i7,0.1)),
    sS:((i4,0.8),(sS,0.1),(i6,0.1))
}

East = {
	
    i1:((i2,0.8),(i4,0.1),(i1,0.1)),
    i2:((oO,0.8),(i2,0.1),(xX,0.1)),
    i3:((i3,0.8),(i3,0.1),(i5,0.1)),
    i4:((xX,0.8),(i1,0.1),(sS,0.1)),
    i5:((i5,0.8),(i3,0.1),(i8,0.1)),
    i6:((i7,0.8),(xX,0.1),(i6,0.1)),
    i7:((i8,0.8),(i7,0.1),(i7,0.1)),
    i8:((i8,0.8),(i5,0.1),(i8,0.1)),
    sS:((i6,0.8),(i4,0.1),(sS,0.1))
}

West = {
	
    i1:((i1,0.8),(i1,0.1),(i4,0.1)),
    i2:((i1,0.8),(i2,0.1),(xX,0.1)),
    i3:((oO,0.8),(i3,0.1),(i5,0.1)),
    i4:((i4,0.8),(i1,0.1),(sS,0.1)),
    i5:((i5,0.8),(i3,0.1),(i8,0.1)),
    i6:((sS,0.8),(xX,0.1),(i6,0.1)),
    i7:((i6,0.8),(i7,0.1),(i7,0.1)),
    i8:((i7,0.8),(i5,0.1),(i8,0.1)),
    sS:((sS,0.8),(i4,0.1),(sS,0.1))
}

South = {
	
    i1:((i4,0.8),(i1,0.1),(i2,0.1)),
    i2:((xX,0.8),(oO,0.1),(i1,0.1)),
    i3:((i5,0.8),(oO,0.1),(i3,0.1)),
    i4:((sS,0.8),(xX,0.1),(i4,0.1)),
    i5:((i8,0.8),(i5,0.1),(i5,0.1)),
    i6:((i6,0.8),(i7,0.1),(sS,0.1)),
    i7:((i7,0.8),(i8,0.1),(i6,0.1)),
    i8:((i8,0.8),(i8,0.1),(i7,0.1)),
    sS:((sS,0.8),(i6,0.1),(sS,0.1))

}

Actions = [ North, East, West, South ]

#Reward Function

def reward():
    return -1*(X/20)

def ValueIteration():
 

    maxDelta = 0
    for i in StateList:
        maxUtility = i.getUtility()
	print 'for state (' + '%.3f'%(i.x) + ',' + '%.3f'%(i.y) + '): '
    	print 'U[t+1] =',
	print 'max( ',
	for a in Actions:
            temp = 0	
	    
	    for j in i.act(a):
	        print  '' + '%.3f'%(j[0].getUtility()) + '*' + '%.3f'%(j[1]) + ' + ',
		temp += j[0].getUtility()*j[1]
	    	
	    utility = reward() + GAMMA*temp
            print str(reward()) + ',',
            
            if utility > maxUtility:
	        maxUtility = utility
    	
	print ') ='
	print '%.3f'%(maxUtility)
	
	delta = abs(maxUtility-i.getUtility())
	if delta > maxDelta:
	    maxDelta = delta
	print "delta for this state is: " + str(delta) + " and maxDelta is: " + str(maxDelta)	
	
        i.setUtility(maxUtility)
    
    print 'maxDelta =' + str(maxDelta)	
    return maxDelta
	
if __name__ == '__main__' :
    
# faster execution
#StateList = StateList.reverse()

    counter = 0
    print '--------------------------------------------------------------------'
    print 'ITERATION NUMBER :' + str(counter)
    print '--------------------------------------------------------------------'
     
    while ValueIteration() > DELTA :
        print 
        print '--------------------------------------------------------------------'
        print 'ITERATION NUMBER :' + str(counter)
        print '--------------------------------------------------------------------'
        counter = counter+1

        print '--------------------------------------------------------------------'
        print 'MATRIX'
        print '--------------------------------------------------------------------'
        print '%5s'%'# ' + '    0   ' + '   1   ' + '   2   ' + '   3' 
        print 
        print '%5s'%'0 ' + '  %.3f  '%i1.utility + '%.3f  '%i2.utility + '%.3f  '%oO.utility + '%.3f  '%i3.utility
        print 
        print '%5s'%'1 ' + '  %.3f  '%i4.utility + '%.3f  '%xX.utility + ' W    ' + '%.3f  '%i5.utility
        print 
        print '%5s'%'2 ' + '  START  ' + '%.3f  '%i6.utility + '%.3f  '%i7.utility + '%.3f  '%i8.utility 
        print 
        print '--------------------------------------------------------------------'
        print
    
    print 
    print '--------------------------------------------------------------------'
    print 'ITERATION NUMBER :' + str(counter)
    print '--------------------------------------------------------------------'
    print '--------------------------------------------------------------------'
    print 'MATRIX'
    print '--------------------------------------------------------------------'
    print '%5s'%'# ' + '    0   ' + '   1   ' + '   2   ' + '   3' 
    print 
    print '%5s'%'0 ' + '  %.3f  '%i1.utility + '%.3f  '%i2.utility + '%.3f  '%oO.utility + '%.3f  '%i3.utility
    print 
    print '%5s'%'1 ' + '  %.3f  '%i4.utility + '%.3f  '%xX.utility + ' W    ' + '%.3f  '%i5.utility
    print 
    print '%5s'%'2 ' + '  START  ' + '%.3f  '%i6.utility + '%.3f  '%i7.utility + '%.3f  '%i8.utility 
    print 
    print '--------------------------------------------------------------------'
    print



    print 
    print "TOTAL REWARD FROM VI: " + str(sS.getUtility())
