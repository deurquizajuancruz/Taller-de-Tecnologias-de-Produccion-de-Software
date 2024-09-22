const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const [x, y] = input.trim().split(' ').map(Number);

const howMuch = (code, quantity) => {
    const objects = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    };
    return 'Total: R$ ' + Number.parseFloat(objects[code] * quantity).toFixed(2);
}

console.log(howMuch(x, y));