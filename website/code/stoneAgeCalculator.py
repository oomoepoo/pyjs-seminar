def stoneAgeCalculator(intA,intB,calc = '+'):
    """
    This is the famous stoneAgeCalculator, a program written by the very first
    men on earth who brought the fire to us and were the first to dance naked
    on the first of May.
    """
    # check for inconsistencies in the input for keyword calc
    if calc not in ['+','-','*','/']:
        raise ValueError('The operation you chose is not defined.')

    # start the calculation, catch errors from input with a simple
    # try-except-structure
    try:
        if calc == '+':
            return intA + intB
        elif calc == '-':
            return intA - intB
        elif calc == '*':
            return intA * intB
        else:
            return intA / intB
    except:
        raise ValueError('No way to operate on your input.')
