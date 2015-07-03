
var kph = {};

kph.encode = function (word){
  
  /* define substitution settings */
  var substitution = {'ä': 'a', 'ö': 'o', 'ü': 'u', 'ß': 'ss', 'ph': 'f'}
  var exceptions_leading = {
    4: ["ca","ch","ck","cl","co","cq","cu","cx"],
    8: ["dc","ds","dz","tc","ts","tz"]
  };
  var exceptions_following = ["sc","zc","cx","kx","qx"];
  var coding_table = {
    0:   "aeijouy",
    1:   "bp",
    2:   "dt",
    3:   "fvw",
    4:   "cgkq",
    48: "x",
    5:   "l",
    6:   "mn",
    7:   "r",
    8:   "csz"
  };

  /* make sure we only get a string as input */
  if (typeof word != 'string') {
    return -1
  }

  if(typeof word.indexOf(' ') !== -1){
    words = word.split(' ');
  }
  else {
    words = [word];
  }
  
  /* create variable for output */
  var output = [];
  
  /* loop over all elements in the word array */
  for (var k=0,word; word=words[k]; k++) {

    // convert to lower case 
    word = word.toLowerCase();
    for(s in substitution){
      word = word.replace(new RegExp(s, "g"), substitution[s]);
    }

    var value = [];
    var length = word.length;
    
    for(var i = 0; i < length; i++){
    
      var l     = word.substr(i, 1);
      value[i]   = '';
    
      if(i === 0 && length > 1 && word[i] + word[i+1] === 'cr'){
        value[i] = 4;
      }
    
      for(code in exceptions_leading){
        if(exceptions_leading[code].indexOf(word[i] + word[i+1]) != -1){
          value[i] = parseInt(code);
        }
      }
    
      if(i !== 0 && exceptions_following.indexOf(word[i-1] + word[i]) != -1){
        value[i] = 8;
      }
    
      if(value[i] == ''){
        for(code in coding_table){
          if(coding_table[code].indexOf(l) !== -1){
            value[i] = parseInt(code);
            break;
          }
        }
      }
    }
    
    for(var i = 1; i < length; i++){
      if(value[i] == value[i-1]){
        value[i] = "";
      }
      if(value[i] == 0){
        value[i] = "";
      }
    }

    output.push(value.join(''))
  }
  return output.join(' ');
};

/* important for export of the function in node */
exports.encode = function(r) { return kph.encode(r);};
