const readline = require('readline');

function fillArray(sequence) {
    const n = sequence.length;
    const equals = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        equals[i] = equals[i - 1];
        if (sequence[i] === sequence[i - 1]) {
            equals[i] += 1;
        }
    }
    return equals;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', (line) => {
    input.push(line.trim());
});

rl.on('close', () => {
    const sequence = input[0];
    const queries = parseInt(input[1], 10);
    const resultArray = fillArray(sequence);

    for (let i = 2; i < 2 + queries; i++) {
        const [li, ri] = input[i].split(" ").map(Number);
        console.log(resultArray[ri - 1] - resultArray[li - 1]);
    }
});