const jumpBuildings = (n, heights) => {
    const minEnergy = new Array(n).fill(Infinity);
    minEnergy[0] = 0;
    for (let i = 0; i < n; i++) {
        // Itero sobre las potencias de 2
        for (let jump = 1; (i + jump < n); jump *= 2) {
            // Edificio al que salta
            const j = i + jump;
            const energy = Math.abs(heights[j] - heights[i]);
            // Mínimo entre la energía que tenía y la nueva energía + lo que cuesta llegar al edificio donde estoy
            minEnergy[j] = Math.min(minEnergy[j], energy + minEnergy[i]);
        }
    }
    return minEnergy[n - 1];
}

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');

for (let i = 0; i < input.length; i += 2) {
    const n = parseInt(input[i]);
    const heights = input[i + 1].split(' ').map(Number);
    console.log(jumpBuildings(n, heights));
}