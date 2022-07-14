def remap(v,min,max,new_min,new_max):

    old_range = max-min
    new_range = new_max-new_min

    inc = v/old_range
    
    return new_min + (new_range)*inc





