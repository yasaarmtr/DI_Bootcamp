//ex1
// let colors = ["blue", "green", "red", "yellow"]
// for (let i=0; i<colors.length; i++){
    
// console.log("My " + (i+1) + "st choice is" + colors[i]);
// }

//ex2
let people = ["Grey", "Mary", "Devon", "James"];
console.log(people);

//remove grey
people.shift();
console.log(people);

//replace james by jason
people.splice (people.indexOf("James"),1, "Jason");
console.log(people);

//saad at the end
people.push("saad");
console.log(people);

for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
        if (people [i]=== "Jason") {
            break;
        }
    //console.log here, remove Jason
  }
console.log(people.slice(1,3))
console.log(people.indexOf("Mary"));

console.log(people.indexOf("foo")); 
console.log(people);

let last = [people.length -1];
console.log(people[people.length]);
