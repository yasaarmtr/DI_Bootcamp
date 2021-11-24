//driving exercise
// let age = prompt ("What is your age?")
// age = Number(age);
// if (age < 18) { 
//     alert("Sorry, you are too young to drive this car. Powering off.");

// }
// else if  ( age > 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");

// }
//  else {
//      console.log("Powering On. Enjoy the ride!");
//     }

//exercise2
// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' ); //answer
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

//exercise3
// let a = 2 + 2;

// switch (a) {
//   case 4:
//     alert('Right!'); //answer
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }

// exercise from slack
let browser = "Edge";
if ( browser == "Edge"){
    alert( "You’ve got the Edge!" );
}
else if (browser == "Chrome" ||
         browser == "Firefox" ||
         browser == "Safari" ||
         browser == "Opera"){
    alert( "Okay we support these browsers too" );
}
else {
    alert ("We hope that this page looks ok!");
}