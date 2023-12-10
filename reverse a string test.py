# %%
#write function to reverse a string 
def reversed(s):
    l = 0 
    r = len(s)-1
    while l < r:
        s[l], s[r] = s[r],s[l]
    return s
