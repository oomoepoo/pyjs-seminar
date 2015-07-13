function make_selector() {
  
  var alms = document.getElementById('alignments');
  var txt = '<select>';
  var words = Object.keys(REFS);
  words.sort();

  for (var i=0,word; word = words[i]; i++) {
    txt += '<option onclick="change_selection(\''+word+'\');" value="'+word+'">'+word+'</option>';
  }
  txt += '</select><div id="alm_display"></div>';
  alms.innerHTML = txt;

 change_selection(words[0]);

  
}

function change_selection(value) {
  REFS['_selected'] = value;
  
  /* reduce the taxonomic units which don't have an item */
  var taxa = REFS[value];
  console.log('taxa',taxa);
  for (var taxon in taxa) {
    console.log('type',typeof ALMS[REFS[value][taxon]]);
    if (typeof ALMS[REFS[value][taxon]] == 'undefined') {
      svg.select('#taxon_'+taxon)
	.attr('fill', 'lightgray')
	.attr('r', 5)
	;
    }
    else {
      svg.select('#taxon_'+taxon)
	.attr('fill', function(d) {return CHINESE.conf.groups_colors[CHINESE.groups[d.name]];})
	.attr('r',10)
	;
    }
  }

}


function back2normal(name) {

  var word = REFS['_selected'];
  var cogid = String(REFS[word][name]);
  var taxa = ALMS[cogid]['taxa'];
  for (var i=0,taxon; taxon=taxa[i]; i++) {
    svg.select('#taxon_'+taxon)
      .attr('fill', function(d){return CHINESE.conf.groups_colors[CHINESE.groups[d.name]]})
      .attr('r', 10)
      ;
  }
}

  

function show_alignment(name) {
  var word = REFS['_selected'];
  console.log(name,REFS[word][name]);

  var ad = document.getElementById('alm_display');

  try {
    var cogid = String(REFS[word][name]);
    var taxa = ALMS[cogid]['taxa'];
    var alms = ALMS[cogid]['alignment'];

    var txt = '<b>Alignment for '+alms.length+' reflexes of &quot;'+word+'&quot;:</b>';
    txt += '<table class="msa">';
    for (var i=0,alm; alm=alms[i]; i++) {
      var taxon = taxa[i];
      svg.select('#taxon_'+taxon)
	.attr('r',15)
	.attr('fill', 'white')
	;
      txt += '<tr>';
      txt += '<th>'+taxon+'</th>';
      txt += plotWord(alm.join(' '), 'td');
      txt += '</tr>';
    }
    txt += '</table>';
  }
  catch (e) {
    var txt = '<font color="red">The word for '+name +' occurs only once in the data, no alignment possible.</font>';
  }
  ad.innerHTML = txt;

  /* get the alignment */
}

make_selector()

