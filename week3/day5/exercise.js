function reverseWord(str){
   
    return reverseStr
  }
  
  
  function reverseSentance(sent){
    // convert to arr
    // loop the arr
    // send each word to reverseWord
    // push or add it to a string
    //retun the reverse sentence
  }
//--------------------------------------------

let words = 'word in a given String';
//'drow ni a nevig gnirtS'

function reversWord(str){
  let ret = "";
  for(let i = str.length-1; i >= 0; i--){
    ret += str[i]
  }
  return ret
}

function reverseWords(str){
  let arr = str.split(" ");
  let ret = [];
  for(let i = 0; i < arr.length; i++){
    ret.push(reversWord(arr[i]));
  }
  return ret.join(" ");
}


console.log(reverseWords(words));

//question1 pnagram---------------------------------------------------------------------------------
Write a function called pangrams that will
take one string, s as input.
A pangram is a sentence that contains
every letter of the alphabet.
The goal of this function is to determine
if the sentence given is a pangram or not.
If it is not a pangram, the function will return not pangram.
If it is a pangram,
the function will return pangram. Here is an example:
"The quick brown fox jumps over the lazy dog"
"We promptly judged antique ivory buckles for the prize"
x is missing

//hint indexoff
function Wsplit(str){
    let arr = str.split(" ");

}


//question2 ---------------------------------------------------------------------------------
let b = 3; 
let d = b; 
let u = b;
const tree = ++d * d*b * b++ +
 + --d+ + +b-- +
 + +d*b+ +
 u

console.log(tree); // 163
//----------------------------------------