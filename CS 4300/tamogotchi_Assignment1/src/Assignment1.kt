fun main() {
    // Instantiate the class and set default gamestate to be off
    println("Welcome to the Tamogotchi Application!")
    print("Please provide a name for your Tamogotchi: ")
    val name = readln()
    val tamo = Tamogotchi(name)
    var gameOff = false

    // User prompt for Tamogotchi name


    // While the game is on, keep display active
    // Ensure gameOff = false for ^
    while (!gameOff) {
        println("============================")
        println("1. Display Tamogotchi")
        println("2. Play with Tamogotchi")
        println("3. Feed Tamogotchi")
        println("4. Put Tamogotchi to bed")
        println("5. Quit")
        print("Enter your choice: ")
        val userChoice: Int = readln().toInt()
        println("============================")

        // "when" is used here since it's similar to switch case
        when (userChoice) {
            1 -> {
                tamo.display()
            }

            2 -> {
                tamo.play()
            }

            3 -> {
                tamo.eat()
            }

            4 -> {
                tamo.sleep()
            }

            5 -> {
                // To quit the program, set the gameOff state from false to true
                println("Goodbye!")
                gameOff = true
            }

            // Returns an invalid if it's none of the choices displayed
            else -> {
                println("Invalid input!")
            }
        }
    }
}
