1. var arr = [8,6,7,5,3,0,9]
for(var i = 0; i < arr.length; i++){    
    console.log(arr[i]);
}

arr	[8,6,7,5,3,0,9]						
i	0	1	2	3	4	5	6
arr[0]	8	6	7	5	3	0	9
output	8	6	7	5	3	0	9

output: 
8,6,7,5,3,0,9

2. var arr = [7,3,8,4,2,0,1];
for(var i = 0; i < arr.length; i++){ 
    if(arr[i] % 2 == 0){
        console.log(arr[i]);
    } 
    else{
        console.log("That is odd!");
    }
}

arr     [7,3,8,4,2,0,1]						
i	    0	1	2	3	4	5	6
arr[i]	7	3	8	4	2	0	1
output	"that is odd!"	"that is odd!"	8	4	2	0	"that is odd!"

output: 
"that is odd!", "that is odd!", 8, 4, 2, 0, "that is odd!" 

3. var arr = [1,3,8,-5,0,-2,4,-1];
var newArr = [];
for(var i = 0; i< arr.length; i++){
    if(arr[i] < 0){
        newArr.push(arr[i]);
        arr[i] = arr[i] * -1;
    }
    else if(arr[i] == 0){
        arr[i] = "Zero";
    }
    else{
        arr[i] = arr[i] * -1;
    }
}
console.log(arr);
console.log(newArr);

arr	[1,3,8,-5,0,-2,4,-1]							
i	    0	1	2	3	4	5	6	7
arr[i]	1	3	8	-5	0	-2	4	-1
newArr	[]	[]	[]	[-5]	[-5]	[-5,-2]	[-5,-2]	[-5,-2,-1]
output	[-1,3,8,-5,0,-2,4-1]	[-1,-3,8,-5,0,-2,4-1]	[-1,-3,-8,-5,0,-2,4,-1]	[-1,-3,-8,5,0,-2,4,-1]	[-1,-3,-8,5,"Zero",-2,4,-1]	[-1,-3,-8,5,"Zero",2,4,-1]	[-1,-3,-8,5,"Zero",2,-4,-1]	[-1,-3,-8,5,"Zero",2,-4,1]

output: 
[-1,-3,-8,5,"Zero",2,-4,1]
[-5,-2,-1]