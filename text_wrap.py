def wrap(string, max_width):
    
    s = ""
    l = len(string)
    
    for c in range(0, l, max_width):
        s += string[c : c + max_width] + "\n"
    
    return s
     
