//ex1
// function infoAboutMe(me){
//     let age = 22;
//     let hobbie = "hiking";
//     console.log("My name is" + me + ", i have " + age + "years old and " + hobbie + "is my hobbie");
// }

// console.log(infoAboutMe("saad"));


// ex1.2,1.3
// function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbie){
//     let arr = [personName, personAge, personFavoriteColor];
//     console.log("Your name is " + personName + ", you are " + personAge + " years old and your favourite colour is " + personFavoriteColor );
    
//     for(let i =0; i<personHobbie.length; i++){
//         console.log(personHobbie[i])
//     }
// }
// infoAboutPerson("David", 45 ,"blue", ["tennis", "painting"])
// infoAboutPerson("josh", 12 ,"green", ["videoGame", "hanging out with friends", "playing cards"])
 
//ex2
// function checkDriverAge(age){
//     // let age = prompt("Please enter your age")
//     // age=Number(age)
//     if(age<18){
//         alert ("Sorry, you are too young to drive this car. Powering off");
//     }
//     else if (age>18){
//         alert ("You are old enough to drive, Powering On. Enjoy the ride!")
//     }
//     else{
//         alert ("Congratulations on your first year of driving. Enjoy the ride!")
//     }
// }
// checkDriverAge(20);

//ex3 checknum
// function checkNumber(){
//     for(let i = 0; i < 99; i++){
//         //check if the number is even
//         if(number % 2 == 0){
//         console.log("The number " + i+1 +" is even.");
//         }
//         // if the number is odd
//         else {
//         console.log("The number " + i+1 + " is odd.");
//         }
//     }
// }
// checkNumber()

//ex4 tips
// function tipCalculator(){
//     let bill = prompt("Please enter the bill amount")
//     bill=Number(bill);
//     let tip=0;

//     if(bill<50){
//         tip= bill*.2
//     }
//     else if(bill>50 && bill<200){
//         tip= bill*.15
//     }
//     else{
//         tip= bill*.1
//     }
// //    return bill + tip 
// // finalbill = bill + tip;
// console.log("Tip amount is " + tip);
// console.log("Bill + tip is " + (tip+bill));
// }
// tipCalculator()

//ex5 
function isDivisible(){
    let arr = []
    

    for (let i =0; i<500; i++){
        

        if (i%23 == 0){
            arr.push(i)
            
        }
    }
    console.log(arr)
    let sum =0
    for (let j=0; j<arr.length; j++){
        sum+=arr[j]
    }
    console.log(sum)
}
isDivisible()







 