const isJolly = (size, nums) => {
    if (size > 3000 || size < 1)
        return 'Integer must be between 1 and 3000.';
    let allValues = new Array(size - 1).fill(false);
    for (let i = 0; i < size - 1; i++) {
        let resultado = Math.abs(nums[i] - nums[i + 1]);
        if (resultado > size || allValues[resultado - 1] || resultado == 0)
            return 'Not Jolly';
        allValues[resultado - 1] = true;
    }
    return allValues.every((value) => value) ? 'Jolly' : 'Not Jolly';
}

// Jolly:
console.log(isJolly(4, [1, 4, 2, 3]));
console.log(isJolly(6, [11, 7, 4, 2, 1, 6]));
console.log(isJolly(5, [8, 5, 9, 7, 6]));
console.log(isJolly(5, [3, 7, 6, 8, 5]));
console.log(isJolly(5, [20, 16, 19, 17, 18]));
// Not Jolly: 
console.log(isJolly(5, [1, 4, 2, -1, 6]));
console.log(isJolly(4, [11, 13, 10, 12]));
console.log(isJolly(5, [2, 5, 1, 4, 3]));
// Out of range:
console.log(isJolly(-6, [4, 5]));
console.log(isJolly(3600, [4, 5]));