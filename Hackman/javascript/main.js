// console.log("hello world")

// how to write single comments

// const name = "Hackman"
// let myName = "joker"
// hisName = "naah"
// console.log(hisName);


// const myAnswer= prompt("what is your name?");
// console.log(myAnswer);



// data types
    BigInt,
    Boolean,
    null,
    Number,
    String,
    Symbol,
    undefined,
    Object
// 

// bigint
// const num = 4
// const myName = "Hackman" 
// const myFloat = 4.5
// const myBool = false
// let mydate = new Date()

// operators in javascript
// arithmetic operators
// +, -, *, /, %

// assignment operators
// =, +=, -=, *=, /=, %=

// comparison operators
// ==, ===, !=, !==, >, <, >=, <=

// logical operators
// &&, ||, !

// bitwise operators
// &, |, ^, ~, <<, >>, >>>
// 

// equal operators
// console.log(mydate)

// 2 === "2" ? console.log("hello") : console.log("bye");

// tenarry operator should check if the condition is a number or not


// const myNum = 10
// typeof myNum === "int" ? console.log("this is a number") : console.log("this is not a number")

// create a variable and writing an if condition if a length of the word is 7 and print it out in the console
// let myWord = "Hackman"
// if (myWord.length === 7) {
//     console.log(myWord)
// } else {
//     console.log("the length of the word is not 7")
// }   


// print("Hello, World!")
// Higher order functions

map, filter, reduce

// explain each of them and give examples of how to use them in javascript

// map
// The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.
// Example:
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Output: [2, 4, 6, 8, 10]

// filter
// The filter() method creates a new array with all elements that pass the test implemented by the provided function.
// Example:
const ages = [12, 17, 20, 25, 30];
const adults = ages.filter(age => age >= 18);
console.log(adults); // Output: [20, 25, 30]

// reduce
// The reduce() method executes a reducer function on each element of the array, resulting in a single output value.
// Example:
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum); // Output: 15

// callback function is a function that is passed as an argument to another function and is executed after some operation has been completed.