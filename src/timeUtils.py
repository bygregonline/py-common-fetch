import time

from termcolor import colored
__version__ =0.322

class elapsedtime(object):
    '''
    classdocs
    '''
    __version__ = 1.0001

    def __init__(self,decimal=5, color='green'):
        """
        Constructor
        """
        self.start = time.time()
        self.decimal = decimal
        self.color = color 
#
# / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /     
# / __/ / /_/ / /|  / /___   
#/_/    \____/_/ |_/\____/ 
#



    def getElapsedTime(self):
        """
        get epasedtime
        """
        return time.time() -self.start
    
    
#
# / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /     
# / __/ / /_/ / /|  / /___   
#/_/    \____/_/ |_/\____/ 
#
    def printTime(self):
        """
        
        """
        print(colored('Elapsed time    :',self.color),self.__str__())
        
#
# / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /     
# / __/ / /_/ / /|  / /___   
#/_/    \____/_/ |_/\____/ 
#
    def __str__(self):
        """
        To String
        """
        return str( round((time.time() -self.start),self.decimal))

#
# / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /     
# / __/ / /_/ / /|  / /___   
#/_/    \____/_/ |_/\____/ 
#   
    def __unicode__(self):
        return u"representation"
    

        



