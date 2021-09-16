var stringMatching = function (words) {
  
  let a = new Set();

  for (let i = 0; i < words.length - 1; i++) {
    for (let j = i + 1; j < words.length; j++) {
      if (words[i].includes(words[j])) {
        a.add(words[j]);
      }
      if (words[j].includes(words[i])) {
        a.add(words[i]);
      }
    }
  }

  return [...a];


};
