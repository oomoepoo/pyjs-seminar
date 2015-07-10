/* align two list objects */
function editList(seqA, seqB, debug)
{
  /* check whether debug variable is passed */
  if (typeof debug == 'undefined') {
    debug = false;
  }
  else {
    debug = true;
  }
  
  /* return nothing if either of the lists is empty */
  if(seqA.length == 0 || seqB.length == 0)
  {
    return;
  }
  
  /* get the lengths of the sequences */
  var alen = seqA.length;
  var blen = seqB.length;

  /* declare variables in local environment */
  var i, j; // numbers
  var gapA, gapB, dist; // floats
  var charA, charB; // characters

  /* create the matrix */
  var matrix = [];
  for(var i=0;i<alen+1;i++) {
    var inline = [];
    for(var j=0;j<blen+1;j++) {
      inline.push(0);
    }
    matrix.push(inline);
  }
  
  /* initialize matrix */
  for(i=1;i<blen+1;i++) {
    matrix[0][i] = i;
  }
  for(i=1;i<alen+1;i++) {
    matrix[i][0] = i;
  }
  
  /* create the traceback */
  var traceback = [];
  for(var i=0;i<alen+1;i++) {
    var inline = [];
    for(var j=0;j<blen+1;j++) {
      inline.push(0);
    }
    traceback.push(inline);
  }

  /* initialize traceback */
  for(i=1;i<blen+1;i++) {
    traceback[0][i] = 2;
  }
  for(i=1;i<alen+1;i++) {
    traceback[i][0] = 1;
  }

  /* start the iteration to fill the matrix */
  for(i=1;i<alen+1;i++) {
    for(j=1;j<blen+1;j++) {
      
      /* get the character in both sequences at their respective position */
      charA = seqA[i-1];
      charB = seqB[j-1];
      
      /* check the similarity between the characters to get the local distance */
      if(charA == charB) {
        dist = matrix[i-1][j-1];
      }
      else {
        dist = matrix[i-1][j-1]+1;
      }
      
      /* we have the distance for substitution, now we need the gaps */
      gapA = matrix[i-1][j]+1;
      gapB = matrix[i][j-1]+1;
    
      /* find the minimal value */
      if(dist < gapA && dist < gapB) {
        matrix[i][j] = dist;
      }
      else if(gapA < gapB) {
        matrix[i][j] = gapA ;
        traceback[i][j] = 1;
      }
      else {
        matrix[i][j] = gapB;
        traceback[i][j] = 2;
      }
      
    }
  }
  
  /* get indices for the last cells of the matrix */
  i = matrix.length-1;
  j = matrix[0].length-1;

  /* get the edit-dist */
  var ED = matrix[i][j];

  /* initialize the alignment arrays */
  var almA = [];
  var almB = [];
  
  /* start the traceback */
  while(i > 0 || j > 0) {
    if(traceback[i][j] == 0) {
      almA.push(seqA[i-1]);
      almB.push(seqB[j-1]);
      i--;
      j--
    }
    else if(traceback[i][j] == 1) {
      almA.push(seqA[i-1]);
      almB.push("-");
      i--;
    }
    else {
      almA.push("-");
      almB.push(seqB[j-1]);
      j--
    }   
  }
  
  /* reverse alignments */
  almA = almA.reverse();
  almB = almB.reverse();
  
  /* check for debug to get the right return value */
  if (debug) {
    return [almA, almB, ED, matrix, traceback];
  }
  
  return [almA, almB, ED];
}


/* align two list objects */
function seqAlign(seqA, seqB)
{
  
  /* return nothing if either of the lists is empty */
  if(seqA.length == 0 || seqB.length == 0)
  {
    return;
  }
  
  /* get the lengths of the sequences */
  var alen = seqA.length;
  var blen = seqB.length;

  /* declare variables in local environment */
  var i, j; // numbers
  var gapA, gapB, dist; // floats
  var charA, charB; // characters

  /* create the matrix */
  var matrix = [];
  for(var i=0;i<alen+1;i++) {
    var inline = [];
    for(var j=0;j<blen+1;j++) {
      inline.push(0);
    }
    matrix.push(inline);
  }
  
  /* initialize matrix */
  for(i=1;i<blen+1;i++) {
    matrix[0][i] = i;
  }
  for(i=1;i<alen+1;i++) {
    matrix[i][0] = i;
  }
  
  /* create the traceback */
  var traceback = [];
  for(var i=0;i<alen+1;i++) {
    var inline = [];
    for(var j=0;j<blen+1;j++) {
      inline.push(0);
    }
    traceback.push(inline);
  }

  /* initialize traceback */
  for(i=1;i<blen+1;i++) {
    traceback[0][i] = 2;
  }
  for(i=1;i<alen+1;i++) {
    traceback[i][0] = 1;
  }

  /* start the iteration to fill the matrix */
  for(i=1;i<alen+1;i++) {
    for(j=1;j<blen+1;j++) {
      
      /* get the character in both sequences at their respective position */
      charA = seqA[i-1];
      charB = seqB[j-1];
      
      /* check the similarity between the characters to get the local distance */
      if(charA == charB) {
        dist = matrix[i-1][j-1];
      }
      else {
        dist = matrix[i-1][j-1]+1;
      }
      
      /* we have the distance for substitution, now we need the gaps */
      gapA = matrix[i-1][j]+1;
      gapB = matrix[i][j-1]+1;
    
      /* find the minimal value */
      if(dist < gapA && dist < gapB) {
        matrix[i][j] = dist;
      }
      else if(gapA < gapB) {
        matrix[i][j] = gapA ;
        traceback[i][j] = 1;
      }
      else {
        matrix[i][j] = gapB;
        traceback[i][j] = 2;
      }
      
    }
  }
  
  /* get indices for the last cells of the matrix */
  i = matrix.length-1;
  j = matrix[0].length-1;

  /* get the edit-dist */
  var ED = matrix[i][j];

  /* initialize the alignment arrays */
  var almA = [];
  var almB = [];
  
  /* start the traceback */
  while(i > 0 || j > 0) {
    if(traceback[i][j] == 0) {
      almA.push(seqA[i-1]);
      almB.push(seqB[j-1]);
      i--;
      j--
    }
    else if(traceback[i][j] == 1) {
      almA.push(seqA[i-1]);
      almB.push("-");
      i--;
    }
    else {
      almA.push("-");
      almB.push(seqB[j-1]);
      j--
    }   
  }
  
  /* reverse alignments */
  almA = almA.reverse();
  almB = almB.reverse();
  
  return [almA, almB, ED];
}

