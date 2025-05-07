var Scorer = {
    score: result => {
      var [docName, title, anchor, descr, score, filename] = result
	  
	  // Deprioritize instrument details (but still include them in results)
	  if (docName.includes("instrument_details")) {
	    score -= 100000;
	  }
	  
	  // Deprioritize retrospective-notes heavily (but still include them in results)
	  if (docName.includes("retrospective-notes")) {
	    score -= 1000000;
	  }

      return score
    },

    // query matches the full name of an object
    objNameMatch: 11,
    // or matches in the last dotted part of the object name
    objPartialMatch: 6,
    // Additive scores depending on the priority of the object
    objPrio: {
		0: 15,
		1: 5,
		2: -5,
    },
    //  Used when the priority is not in the mapping.
    objPrioDefault: 0,

    // query found in title
    title: 15,
    partialTitle: 7,

    // query found in terms
    term: 5,
    partialTerm: 2,
};
