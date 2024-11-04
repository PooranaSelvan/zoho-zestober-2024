const longestWord = (words, ch) => {
     let res = '';
 
     for (let i = 0; i < words.length; i++) {
          
          let input = ch.toLowerCase();
          let word = words[i].toLowerCase();
 
          if (word[0] === input) {
             if (word.length > res.length) {
               res = word;
             }
          }
     }
 
     return res;
}
 
let words = ['explore', 'adventure', 'uncharted', 'expedition'];
let ch = 'e';
console.log(longestWord(words, ch));