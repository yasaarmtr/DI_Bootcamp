function playTheGame(){
    let ans = prompt("Would u like to play the game, yes or no?")
    if (ans=no){
        alert("No problem, Goodbye")
    }
    else if (ans=yes){
        let num = prompt("Please enter a number between 0 and 10")
            //if statement inside another one 
            if(isNaN(num)){
                alert("Sorry Not a number, Goodbye")
            }
            else if (num<0 || num>10){
                alert("Sorry it’s not a good number, Goodbye")
            }
            else{
                let computerNumber =
            }

    }

    return ans
}