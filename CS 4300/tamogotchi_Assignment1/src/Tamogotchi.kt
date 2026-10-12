class Tamogotchi(
    val name: String
    // This allows for an initial, even if the string is empty.
){
    var age: Int = 0
    var hunger: Int = 100
        set(value) {
            // Forces the values to be in the range of 0 <= value <= 100
            // Unsure if it was a require or a snapper, so I settled with the snapper below
            //require(value in 0..100)
            field = value

            // This part ensures that the values snap to 100 if value > 100
            if (field > 100){
                field = 100
            }

            // This part ensures that the values snap to 0 if value < 0
            if (field < 0){
                field = 0
            }
        }
        get(){
            return field
        }

    var happiness: Int = 0
        set(value) {
            // Similarly to the previous setter, this one requires the values to be between 0 and 100
            //require(value in 0..100)
            field = value

            // This part ensures that the values snap to 100 if value > 100
            if (field > 100){
                field = 100
            }

            // This part ensures that the values snap to 0 if value < 0
            if (field < 0){
                field = 0
            }
        }
        get(){
            return field
        }

    var energy: Int = 50
        set(value) {
            // Requires the value to be between 0 and 100
            //require(value in 0..100)
            field = value

            // This part ensures that the values snap to 100 if value > 100
            if (field > 100){
                field = 100
            }

            // This part ensures that the values snap to 0 if value < 0
            if (field < 0){
                field = 0
            }
        }
        get(){
            return field
        }

    fun display(){
        // Simple Tamogotchi data display
        println("Tamogotchi: $name")
        println("Age: $age days")
        println("Hunger: $hunger / 100")
        println("Happiness: $happiness / 100")
        println("Energy: $energy / 100")
    }

    fun eat(): String = when {
        hunger > 0 -> {
            // Checks to see if Tamogotchi's not hungry, it will be fed
            hunger -= 25
            happiness += 3
            energy += 10
            "$name is eating some food!"
        }
        else -> {
            // Otherwise, print to console that Tamogotchi is full
            "$name is full!"
        }
    }

    fun play(): String = when{
        // Checks to see if Tamogotchi is not that hungry and has the energy to play
        hunger <= 50 && energy >= 20 -> {
            hunger += 10
            happiness += 4
            energy -= 20
            "$name is playing around!"
        }
        else -> {
            // Otherwise, it does not feel like playing
            "$name does not feel like playing right now."
        }
    }

    fun sleep(): String = when {
        hunger > 70 -> {
            // If the Tamogotchi is hungry, refuse to sleep until it's full enough
            "$name is hungry! Feed $name!"
        }
        else -> {
            // Otherwise, let the Tamogotchi sleep, but lose some states and increase age
            hunger += 30
            happiness -= 10
            energy += 10
            age += 1
            "$name is going to sleep for the rest of the day, and wakes up the next day."
        }
    }
}
