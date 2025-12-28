import setFromArray from "./6-set.js";
import hasValuesFromArray from "./7-has_array_values.js";

console.log(setFromArray([12, 32, 15, 78, 98, 15]));

const mySet = setFromArray([1, 2, 3, 4, 5]);
console.log(hasValuesFromArray(mySet, [1, 2, 3, 4]));
console.log(hasValuesFromArray(mySet, [1, 2, 3, 4, 6]));
