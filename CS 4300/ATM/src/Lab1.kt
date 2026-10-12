var checkingBalance: Float = 100.00F
var savingsBalance: Float = 10.00F

// I made the program auto-convert the user input from integer to floats, so if there is an issue, it is that.

fun main(){
    var atmOff = false

    while (!atmOff) {
        println("\nWelcome to the ATM!")
        println("1. Display Account Balances")
        println("2. Withdraw")
        println("3. Deposit")
        println("4. Quit")
        print("Choice: ")
        val userChoice: Int = readln().toInt()

        if (userChoice == 1) {
            displayAccountBalances()
        }

        else if (userChoice == 2) {
            withdrawScreen()
        }

        else if (userChoice == 3) {
            depositScreen()
        }

        else if (userChoice == 4) {
            println("Quitting ATM...")
            atmOff = true
        }

        else {
            println("Invalid choice!")
        }
    }
}

fun displayAccountBalances(){
    print("\nSavings Balance: \$")
    println(savingsBalance)
    print("Checking Balance: \$")
    print(checkingBalance)
}

fun depositScreen() {
    print("Choose: ")
    val userChoiceDeposit: String = readln()

    when (userChoiceDeposit) {
        "checking" -> {
            print("Enter amount: ")
            val amount: Float = readln().toFloat()
            depositMoney(amount, userChoiceDeposit)
        }

        "savings" -> {
            print("Enter amount: ")
            val amount: Float = readln().toFloat()
            depositMoney(amount, userChoiceDeposit)
        }

        else -> {
            println("Invalid choice!")
        }
    }
}

fun depositMoney(amount: Float, userChoiceDeposit: String) {
    if (amount < 0) {
        println("Invalid deposit. Please ensure the amount is positive.")
    }

    else {
        when (userChoiceDeposit) {
            "checking" -> {
                checkingBalance += amount
            }

            "savings" -> {
                savingsBalance += amount
            }
        }
    }
}

fun withdrawScreen() {
    print("Choose: ")
    val userChoiceDeposit: String = readln()
    when (userChoiceDeposit) {
        "checking" -> {
            print("Enter amount: ")
            val amount: Float = readln().toFloat()
            withdrawMoney(amount, userChoiceDeposit)
        }

        "savings" -> {
            print("Enter amount: ")
            val amount: Float = readln().toFloat()
            withdrawMoney(amount, userChoiceDeposit)
        }

        else -> {
            println("Invalid choice!")
        }
    }
}

fun withdrawMoney(amount: Float, userChoiceDeposit: String) {
    if (amount <= 0) {
        println("Invalid withdrawal. Please ensure the amount is positive.")
    }

    if (userChoiceDeposit == "savings") {
        if (amount > savingsBalance) {
            println("Invalid withdrawal. Insufficient funds.")
        } else {
            savingsBalance -= amount
        }
    }

    if (userChoiceDeposit == "checking") {
        if (amount > checkingBalance) {
            println("Invalid withdrawal. Insufficient funds.")
        } else {
            checkingBalance -= amount
        }
    }
}



// val money = 1092.765
//    val moneyString = String.format("%.2f", money)
//    // truncates and rounds; can use val moneyString = ".2f".format(money); works the same way
// use \ for dollar sign