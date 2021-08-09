var matrixRankTransform = function(matrix) {
  let n = matrix.length,
      m = matrix[0].length 
  let rank = new Array(n + m).fill(0)
  let d = {}
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (!d[matrix[i][j]]) d[matrix[i][j]] = []
      d[matrix[i][j]].push([i, j])
    }
  }

  function find(p, i) {
    if (p[i] !== i) p[i] = find(p, p[i])
    return p[i]
  }
  // because JavaScript stores keys as strings, we need a way to process keys from lowest to highest (including negative numbers)
  let orderedKeys = []
  for (let a in d) {
    orderedKeys.push(a)
  }
  orderedKeys.sort((a, b) => a - b)

  for (let a of orderedKeys) {
    let p = []
    for (let i = 0; i < m + n; i++) {
      p.push(i)
    }
    let rank2 = [...rank]
    for (let [i, j] of d[a]) {
      i = find(p, i)
      j = find(p, j + n)
      p[i] = j
      rank2[j] = Math.max(rank2[i], rank2[j])
    }      
    for (let [i, j] of d[a]) {
      rank[i] = rank[j + n] = matrix[i][j] = rank2[find(p, i)] + 1
    }
  }

  return matrix
};
