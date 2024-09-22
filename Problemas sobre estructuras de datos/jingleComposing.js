var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

const howMany = (jingles) => {
    const notes = {
        'W': 1,
        'H': 0.5,
        'Q': 0.25,
        'E': 0.125,
        'S': 0.0625,
        'T': 0.03125,
        'X': 0.015625,
    };
    let quantity = 0;
    jingles.split('/').forEach((element) => {
        if (element.length > 0) {
            let sum = 0;
            for (let i = 0; i < element.length; i++)
                sum += notes[element[i]];
            if (sum === 1)
                quantity++;
        }
    });
    return quantity;
}

for (let i = 0; i < lines.length - 2; i++) {
    console.log(howMany(lines[i]));
}

// console.log(howMany('/HH/QQQQ/XXXTXTEQH/W/HW/'));
// console.log(howMany('/W/W/SQHES/'));
// console.log(howMany('/WE/TEX/THES/'));