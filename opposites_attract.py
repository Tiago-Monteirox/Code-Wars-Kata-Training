def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0:
    
        if flower2 % 2 != 0:
            return True
        else:
            return False
    elif flower1 % 2 != 0:
        if flower2 % 2 == 0:
            return True
        else:
            return False

# return True if (f1 % 2 == 0 and f2 % 2 != 0) or (f2 % 2 == 0 and f1 % 2 != 0) else False