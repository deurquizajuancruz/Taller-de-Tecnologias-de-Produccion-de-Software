const maxHits = missiles => {
    const n = missiles.length;
    let lis = new Array(n).fill(1);
    let prev = new Array(n).fill(-1);

    for (let i = n - 1; i > -1; i--) {
        for (let j = i + 1; j < n; j++) {
            if (missiles[i] < missiles[j] && lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
                prev[i] = j;
            }
        }
    }

    let maxIndex = 0;
    for (let i = 1; i < n; i++) {
        if (lis[i] > lis[maxIndex]) {
            maxIndex = i;
        }
    }

    let hits = [];
    let current = maxIndex;
    while (current !== -1) {
        hits.push(missiles[current]);
        current = prev[current];
    }
    return hits;
}

console.log(maxHits([1, 6, 2, 3, 5]));