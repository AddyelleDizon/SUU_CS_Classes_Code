fun main() {
    val myList: List<Int> = listOf(1, 3, -1, 10)
    val first = myList[0]

    val myListMutable = mutableListOf(1, 2, 3, 4, 1, 2)

    for (i in myListMutable) {
        println(i)
    }
}