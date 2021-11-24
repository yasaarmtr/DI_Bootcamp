

// function sum(a,b){
//     let sum = a + b;
//     let arr[{a:1},{b:2}];

//     return sum;
// }
// let res = sum(1,2);
// console.log(res);

//checkage
// let age = 18
// function checkAge(theage){
//     if (theage >=18){
//         return true;

//     }
//     else{
//         return false;
//     }
// }

// let result = checkAge(age)
// console.log(result);
// if (result == 'true'){
//     console.log('ok');

// }
// else{
//     console.log("Not ok");
// }

//ex1
// function myAge(myAge){

//     let mumage = myAge*2
//     let dadage = myAge*1.2
//     let arr= [mumage, dadage]
//     return arr
// }
// let result = myAge(22)
// console.log("my mum age is " + result[0] + "& my dad age is " + result[1] );

//
// function yesMessage(){
//     return 'yes';
// }
// function noMessage(){
//     return 'no';
// }
// function check(num){
//     if (num >10){
//         let res = yesMessage();
//         alert(res);
//     }
//     else{
//         let res = noMessage();
//         console.log(res);
//     }
// }
// check(20)

//
// function ask(question){
//     if (question.lenght > 3){
//         return "good";

//     }
//     else{
//         return 'not good';
//     }
// }

// let ask = function(question){
//     if (question.lenght > 3){
//         return "good";

//     }
//     else{
//         return 'not good';
//     }
// }

// let ask = (question) ={
//     if (question.lenght > 3){
//         return "good";

//     }
//     else{
//         return 'not good';
//     }
// }


//
var x = 6;

//console.log(x);

let obj ={
    a: function(){
        var x = 10;
        console.log(this.x)
    }
}

console.log(obj.a())