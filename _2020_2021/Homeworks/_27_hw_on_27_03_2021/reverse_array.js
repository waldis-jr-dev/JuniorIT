array1 = ['Python', 'is', 'better', 'and', 'smarter', 10011]
reversed_array = []
let i;
for (i in array1){
    let element = array1[i]
    if (isNaN(element)) {
        reversed_array.push(element.split("").reverse().join(""))
    }
    else{
        reversed_array.push(Number(element.toString().split("").reverse().join("")))
    }
};
console.log(reversed_array)
