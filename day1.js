function knapsack(N, W, w, v) {
    let maxValueTable = [];
  
    for (let i = 0; i <= N; i++) {
      maxValueTable[i] = [];
      for (let j = 0; j <= W; j++) {
        maxValueTable[i][j] = 0;
      }
    }
    
    for (let i = 1; i <= N; i++) {
      for (let j = 1; j <= W; j++) {
        if (w[i - 1] <= j) {
          let valueIfIncluded = v[i - 1] + maxValueTable[i - 1][j - w[i - 1]];
  
          let valueIfNotIncluded = maxValueTable[i - 1][j];
          
          maxValueTable[i][j] = Math.max(valueIfIncluded, valueIfNotIncluded);
        } else {
          maxValueTable[i][j] = maxValueTable[i - 1][j];
        }
      }
    }
    return maxValueTable[N][W];
}

N = 4
W = 10
w = [5, 4, 6, 3]
v = [10, 40, 30, 50]

console.log(knapsack(N, W, w, v))