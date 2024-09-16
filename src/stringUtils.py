from numpy import nan
from sys import stdout
from time import sleep
from termcolor import colored

__version__ =0.322

#
#
#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#
def sizeof_fmt(num, suffix='b'):
    for unit in [' ',' K',' M',' G',' T',' P',' E',' Z']:
        if abs(num) < 1024.0:
            return "%3.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

#
#
#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#

def str2bool(v):
    if v is not None:
        b=str(v)
        return b.lower() in ('yes', 'true', 't', '1','si','oui','y')
    else:
        return False



#
#
#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#

def alingLeft(word,size):
    return word+' '*(size-len(word))

#
#
#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#
def equalsIgnoreCase(a,b):
    if (a.lower() == b.lower()):
        return True
    else:
        return False

#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#
def percentageToFloat(number):
    aux = nan
    try:
        if aux is not None:
            if isinstance(number, str):
                aux = float(number.strip('%'))/100
    except Exception as e:
        pass

    return aux


#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#

def advance(i,m):
    return '#'*i+' '*(m-i)

#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#

def beep():
    print('\a', end='')

#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#

def showAdvance(msg='', total=10,i = 1,outMessage=''):
    s = '[%s] %d %% '+msg+'%s\r'
    stdout.write(s % (advance(int(i/(total/10)),10),int(i/(total/100)),outMessage))
    stdout.flush()


#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#
def getAsciiInfo(logo=True,withColor=None,attrs=None):
    s="""
           ___________________________________
        / Do not forget it.. The Computer does \\
        \ not  think.. You have to do it       /
           -----------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\\
                     ||----w |
                     ||    ||

       """

    s2="""

      /^       /^^^     /^^  /^^      /^           /^^     /^^     /^^  /^^
     /^ ^^     /^ /^^   /^^  /^^     /^ ^^      /^^   /^^  /^^     /^^  /^^
    /^  /^^    /^^ /^^  /^^  /^^    /^  /^^    /^^         /^^     /^^  /^^
   /^^   /^^   /^^  /^^ /^^  /^^   /^^   /^^   /^^         /^^^^^^ /^^  /^^
  /^^^^^^ /^^  /^^   /^ /^^  /^^  /^^^^^^ /^^  /^^         /^^     /^^  /^^
 /^^       /^^ /^^    /^ ^^  /^^ /^^       /^^  /^^   /^^  /^^     /^^  /^^
/^^         /^^/^^      /^^   ^^/^^         /^^   /^^^^    /^^     /^^  /^^
       """


    if logo:
        if isinstance(withColor,str):
            if isinstance(attrs,list):
                return colored(s2, withColor, attrs=attrs)
            else:
                return colored(s2, withColor)
        else:
            return s2

    else:
        if isinstance(withColor,str):
            if isinstance(attrs,list):
                return colored(s, withColor, attrs=attrs)
            else:
                return colored(s, withColor)
        else:
            return s




#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#





#
#
#   / ____/ / / / | / / ____/
#  / /_  / / / /  |/ / /
# / __/ / /_/ / /|  / /___
#/_/    \____/_/ |_/\____/
#
if __name__ == '__main__':
    #print(equalsIgnoreCase('chench','ChencH0'))
    print(getAsciiInfo(True,'red',['bold']))
    print(getAsciiInfo(True,None,['reverse', 'blink']))
    print(getAsciiInfo(True,None,None))
    print(getAsciiInfo(False,'white',None))
    print(getAsciiInfo(False,None,['reverse', 'blink']))

