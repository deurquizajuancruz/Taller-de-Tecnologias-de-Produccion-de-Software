const largest = (numbers) => {
    const n = numbers.length;
    const lis = new Array(n).fill(1);

    for (let i = n - 1; i >= 0; i--) {
        for (let j = i + 1; j < n; j++) {
            if (numbers[i] < numbers[j]) {
                lis[i] = Math.max(lis[i], 1 + lis[j]);
            }
        }
    }

    return Math.max(...lis);
}

const input_data = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

for (let i = 0; i < input_data.length; i += 2) {
    const n = parseInt(input_data[i]);
    const numbers = input_data[i + 1].split(' ').map(Number);
    console.log(largest(numbers));
}