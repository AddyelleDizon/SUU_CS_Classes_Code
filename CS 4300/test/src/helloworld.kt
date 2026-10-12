fun main(){
    print("Enter your name: ")
    var name: String = readln()
    var role: String = when (name){
        "Ray" -> "Instructor"
        else -> "Student"
    }
    when (role){
        "Instructor" -> {
            println("Welcome Professor $name")
            println("Which class are you teaching?")
            var classname: String = readln()
        }

        "Student" -> {
            println("Welcome $name")
            println("Which class are you taking?")
            var classname: String = readln()
        }
    }
    for (index in 1..10) {
        println("$index")
    }

    val money = 1092.765
    val moneyString = String.format("%.2f", money)
    // truncates and rounds; can use val moneyString = ".2f".format(money); works the same way
}

fun sayHello(name: String){
    println("Hello $name")
}

fun evenOrOdd(num: Int) = when (val result = num % 2) {
    1 -> "odd"
    0 -> "even"
}
// use \ for dollar sign