function stoneAgeCalculator(intA, intB, calc) {
  /* This is a very famous StoneAge Calculator. */

  /* check for active values for type */
  if (typeof calc == 'undefined') {
    calc = "+";
  }
  /* check for correct values for calc */
  else if(["+", "-", "*", "/"].indexOf(calc) == -1) {
    return false;
  }

  /* return the stuff */
  if (calc == '+') {return intA + intB;}
  else if (calc == '-') {return intA - intB;}
  else if (calc == '*') {return intA * intB;}
  else if (calc == '/') {return intA / intB;}
  return false;
}

