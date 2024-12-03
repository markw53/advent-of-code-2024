const fs = require('fs');

function sumValidMultiplicationsWithConditions(filePath) {
    const corruptedMemory = fs.readFileSync(filePath, 'utf-8');    
    const mulPattern = /mul\((\d+),(\d+)\)/g;
    const doPattern = /do\(\)/g;
    const dontPattern = /don't\(\)/g;    
    
    let mulEnabled = true;
    let total = 0;

    const instructions = [...corruptedMemory.matchAll(/mul\((\d+),(\d+)\)|do\(\)|don't\(\)/g)];

    for (const instruction of instructions) {
        if (instruction[0].startsWith('do()')) {
            mulEnabled = true;
        } else if (instruction[0].startsWith("don't()")) {
            mulEnabled = false;
        } else if (instruction[0].startsWith('mul(') && mulEnabled) {
            const x = parseInt(instruction[1], 10);
            const y = parseInt(instruction[2], 10);
            total += x * y;
        }
    }
    return total;
}

const filePath = 'input3.txt'; 

const result = sumValidMultiplicationsWithConditions(filePath);
console.log(`The sum of all enabled multiplications is: ${result}`);
