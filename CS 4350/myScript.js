document.getElementById("demo").innerHTML = "Hello World";

function myFunction(){
    document.getElementById("demo").innerHTML = "Hello Again";
}

function myFunction2(){
    var length = 5
    var width = 2
    var area = length*width
    area = Number.MIN_VALUE
    document.getElementById("demo").innerhtml = "The area is: " + area;
}