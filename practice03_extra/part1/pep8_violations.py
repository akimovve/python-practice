# whitespace before "("
def p1 (x):
    print (x)


# missing whitespace around operator
def p2(x):
    print(x>1)


# missing whitespace after ","
def p3(x):
    print(x,x,x)


# unexpected spaces around keyword / parameter equals
def p4(x = 2):
    print(x)


# expected 2 blank lines, found 1
def p5_1(x):
    print(x)

def p5_2(x):
    print(x)


# multiple statements on one line (colon)
def p6(x):
    if x > 0: print(x)


# multiple statements on one line (semicolon)
def p7(x):
    print(x); print(x)


# comparison to None should be "if cond is None:"
def p8(x):
    if x == False:
        print(0)
    if x == None:
        print(1)


# comparison to True should be 'if cond is True:' or 'if cond:'
def p9():
    x = True
    if x == True:
        print(x)
