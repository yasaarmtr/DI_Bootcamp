// function bSong() {
//     let bottles;
//     let bottlesLeft;
//     for (i = 99; i >= 1; i--) {
//       if (i == 1) {
//         bottles = "bottle";
//         bottlesLeft = "No bottles of beer on the wall!";
//       } else {
//         bottles = "bottles";
//         bottlesLeft = i - 1 + " bottles of beer on the wall!";
//       } console.log(i+ " " + bottles + " of beer on the wall,");
//       console.log(i+ " " + bottles + " of beer,");
//       console.log("Take one down, pass it around,");
//       console.log(bottlesLeft);
//       }
  
//   }
//   console.log(bSong());

//hangman

//to check
function hangmanGame(){
  let word_to_guess = "";
  do{
    // step1 get user hidden word
    word_to_guess = prompt("please enter a word to guess - min 8 words");
  console.log(word_to_guess.length);
  }
  while(word_to_guess.length < 8) //should be 8 min of 8 letters

  let word_arr = word_to_guess.split("");
  let word_hidden = "*".repeat(word_to_guess.length).split("");  //star display

  console.log(word_hidden.join(" "));

  let guesses = 0;
  while(guesses < 10){
    let letter = prompt("Please guesse a letter");

    // check if letter exists
    for (var i = 0; i < word_arr.length; i++){
      if(word_arr[i]===letter){
        word_hidden[i]= letter;

      }

    }
    console.log(word_hidden.join(" "));

    if(!word_hidden.includes("*")){
      console.log("You won");
      return;
    }

    if (word_hidden.includes(""))

    guesses++;
  }
  if (guesses>=10){
    console.log('You lose')
  }
}
  return hangmanGame();

//step2 get user2 letter

//to check
//step3 10 guesses for user2

//to check
//prevent choode the same letter

