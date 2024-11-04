const jumbo = (lst, j) => {
    const res = lst.map((word) => {
        let s = '';
         //     console.log(word);
        for (let i = 0; i < word.length; i++) {
            if (word[i].toLowerCase() === j[s.length]) {
                s += word[i];
              }
            if (s === j) break;
        }
        if(s === j){
         return "JUMBO";
        } else {
         return word;
        }
    });

    return res;
}


const lst = ['jumbo', 'robot', 'abjuvombo'];
const j = "jumbo";

console.log(jumbo(lst, j))