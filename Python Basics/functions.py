# *args can take infinite number of arguments
def infinite(*args):
    list = [x*2 for x in args]
    for l in list:
        print(l)

infinite(1,2,3,4,5,6)

# ----------------------------------------------------

# in kwargs the tuple gets split into key:value
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

# ------------------------------------------------------------

def volume(a, b, c=10): # c is a default argument
    return a * b * c
 
print(volume(b=3,2)) # b goes to b in the formal arguments .......2 goes to a