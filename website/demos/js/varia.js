function wind (country, season) {
  /* Return the typical wind conditions for a country */

  /* carry out type check of season, to set the basic value */
  if (typeof season == "undefined") {
    season = "summer";
  }

  if (country == "Germany" && season == "summer") {
    return "There's strong wind in "+country+".";
  }
  else {
    return "This part hasn't been programmed yet.";
  }
}


