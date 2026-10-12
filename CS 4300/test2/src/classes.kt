open class BankAccount(
    initialBalance: Double,
    // val type: String // type does not need nondefault setters or getters, used only if the default is needed
) {
    // balance needs a nondefault setter, therefore given here
    var balance: Double = initialBalance
        set(value) {
            require(value >= 0)
            println("Something Something")
            field = value
        }
        get(){
            return field
        }

    init { // this is an error checking initialization block
        require(balance >= 0)
//        require(listOf("checking", "savings").contains(type.lowercase()))
    }

    // secondary constructor to the primary
//    constructor(initDep: Double, bonus: Double): this(initDep, "Checking") {
//        balance += bonus
//    }
//    var type: String = accountType
//        set(value) {
//            require(value == "Checking" || value == "Savings")
//            field = value
//        }
//        get(){
//            return "Type: " + field
//        }

    fun deposit(amount: Double) {
        balance += amount
    }

    fun withdraw(amount: Double) {
        balance -= amount
    }

    fun setAmount(amount: Double) {
        balance = amount
    }
}

class CheckingAccount(deposit: Double): BankAccount(deposit){
    // if we ever need to inherit a function from the parent class,
    // its created with "open" at the front of the function
    // ex: open fun setAmount()...
}

var someFunction: (String) -> String = {
    it.uppercase()
}

fun main(){
    var account: BankAccount = BankAccount(100.0)
    account.setAmount(100.0)
}

