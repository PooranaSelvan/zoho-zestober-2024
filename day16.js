function Chords(s) {
  const freq = {};

  for (let i = 0; i < s.length; i++) {
    let ch = s[i];
    freq[ch] = (freq[ch] || 0) + 1;
  }

  let chord = '';
  let count = 0;

  for (let j in freq) {
    if (freq[j] > count) {
      chord = j;
      count = freq[j];
    }
  }

  if (count > Math.ceil(s.length / 2)) return "Not Possible";

  const result = Array(s.length).fill("");
  let index = 0;

  for (let i = 0; i < count; i++) {
    result[index] = chord;
    index += 2;
  }
  freq[chord] = 0;

  for (let k in freq) {
    while (freq[k] > 0) {
      if (index >= s.length) index = 1;
      result[index] = k;
      index += 2;
      freq[k]--;
    }
  }

  return result.join('');
}

console.log(Chords("AAABBBCCC"));
console.log(Chords("AAAAA"));
