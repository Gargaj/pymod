from pymod.tables import *

# Example from http://bjourne.blogspot.com/2007/10/lose-weight-with-min-max-and-clamp.html
def MIN(a, b):
    return (b, a)[a < b]

def MAX(a, b):
    return (b, a)[a > b]

def CLAMP(x, l, h):
    return ((x, l)[x < l], h)[x > h]

def transpose_to_frequency(transp, ftune):
    return 8363.0 * pow(2, (transp * 128.0 + ftune) / 1536.0)

def MOD_FINETUNE(ftune):
    return finetune_table[(ftune & 0xf) ^ 8]
