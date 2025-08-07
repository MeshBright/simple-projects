const prompt = require('prompt-sync')();
let number = [];
let operands = [];
let solution;
let j = 0;

for (let i = 0; i < 3; ++i ) {
    number[i] = Number(prompt("Input a number: "));

    if (j === 2) {
        continue;
    }
    else {
        operands[j] = prompt("Input an operation: "); 
        ++j;
    }
    
}

let i = 0;
j = i + 1;
let k = j + 1;

    if (operands[i] === "+") {
         
        switch (operands[j]) {
            case "+":
            solution = number[i] + number[j] + number[k];
            break;

            case "-":
            solution = (number[i] + number[j]) - number[k];
            break;

            case "/":
            if (number[k] === 0) {
                console.log("Please input a value other than zero!");
                break;
            }
            else {
                solution = number[i] + (number[j] / number[k]);
                break;
            }
            case "*":
            solution = number[i] + (number[j] * number[k]);
            break;
        }
    }

    else if (operands[i] === "-") {

        switch (operands[j]) {
            case "+":
            solution = number[i] - (number[j] + number[k]);
            break;

            case "-":
            solution = number[i] - (number[j] - number[k]);
            break;
            
            case "/":
            if (number[k] === 0) {
                console.log("Please input a value other than zero!");
                break;
            }
            else {
                solution = number[i] - (number[j] / number[k]);
                break;
            }
            
            case "*":
            solution = number[i] - (number[j] * number[k]);
            break;
        }
    }

    else if (operands[i] === "/") {
        if (number[j] === 0) {
            console.log("Please input a value other than zero!");
        }
        else {
            switch (operands[j]) {
                case "+":
                solution = (number[i] / number[j]) + number[k];
                break;

                case "-":
                solution = (number[i] / number[j]) - number[k];
                break;

                case "/":
                if (number[k] === 0) {
                    console.log("Please input a value other than zero!");
                    break;
                }
                else {
                    solution = number[i] / (number[j] / number[k]);
                    break;
                }
                case "*":
                    solution = (number[i] / number[j]) * number[k];
                    break;
                }
        }
    }
   
    else if (operands[i] === "*") {
        switch (operands[j]) {
            case "+":
            solution = (number[i] * number[j]) + number[k];
            break;

            case "-":
            solution = (number[i] * number[j]) - number[k];
            break;

            case "/":
            if (number[k] === 0) {
                console.log("Please input a value other than zero!");
                break;
            }
            else {
                solution = number[i] * (number[j] / number[k]);
                break;
            }
            case "*":
                solution = number[i] * (number[j] * number[k]);
                break;
            }
    }
    

console.log("The solution is: ", solution);
