any([False, True, False]) # True
all([False, True, False]) # False

notes = [12, 14, 20, 10, 8]
any([x > 18 for x in notes]) #True une note == 20