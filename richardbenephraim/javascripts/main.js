

// // // variables



// // // operators

// // const c = 4

// // console.log(c === "4")

// // const h = undefined;


// // let myDate = new Date()

// // console.log(myDate)


// // 2 == "2" ? console.log("hello") : console.log("bye")

// // const num = 14;
// // const num2 = 0;
// //  const cc = num2 || num;

// //  console.log(cc)

// const name = 45;


// typeof name === "string" ? console.log(" this is a string") : console.log("not")


// console.log(typeof name)


// // == CONDITIONS ==


// let school = "open labs";

// if (school.length >= 9) {
//     console.log("this number has 9 or more pictures")
// } else {
// console.log("charaters are less")
// };
// print()


// terniary contion




// function declaration

function main(age, birthYear){
    return birthYear - age;
}
const getResults = main(31, 2026)
console.log(getResults)


// function expression

const calAge = function (){
    return 23 * 5 -32
};

const total = calAge();
console.log(total);



// arrow function 

const calAge3 = birthYearNow => 2026 - birthYearNow;

const age3 = calAge3(31);
console.log(age3)

const project = (bill, paid) => {
    const spent = bill + 2000;
    const left = bill - paid;
    const overAll = ` i ${spent} on the total amount of ${bill} when ${paid} \nwas paid. \nthank you`;

    return overAll;
}

const invent = project (45000, 20000)
console.log(invent)