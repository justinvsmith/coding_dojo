1. Print Values and Sum

var testArr = [6,3,5,1,2,4];

var sum = 0;

for(var i = 0; i < testArr.length; i++){
  sum += testArr[i];
  console.log("Num: "+testArr[i]);
  console.log("Sum: "+sum);
}

2. Value * Position

var testArr = [6,3,5,1,2,4];

for(var i = 0; i < testArr.length; i++){
  testArr[i] = testArr[i]*i;
}

console.log(testArr);