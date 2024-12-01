const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8');

const leftList = [];
const rightList = [];

input
  .trim()
  .split('\n')
  .forEach(line => {
    const [left, right] = line.split(/\s+/).map(Number); 
    leftList.push(left);
    rightList.push(right);
  });

const frequencyMap = {};
rightList.forEach(num => {
  frequencyMap[num] = (frequencyMap[num] || 0) + 1;
});

let similarityScore = 0;
leftList.forEach(num => {
  similarityScore += num * (frequencyMap[num] || 0);
});

console.log(`Similarity Score: ${similarityScore}`);
