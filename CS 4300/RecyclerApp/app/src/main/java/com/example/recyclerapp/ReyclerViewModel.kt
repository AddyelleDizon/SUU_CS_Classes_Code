package com.example.recyclerapp

import java.util.UUID

class RecyclerViewModel {
    val data : MutableList<DataModel> = generate()
}

fun generate() : MutableList<DataModel> {
    val data : MutableList<DataModel> = mutableListOf()
    for (index in 0..11) {
        data.add(DataModel(names[index], uuid[index], desc[index]))
    }

    return data
}

val names : List<String> = listOf(
    "Bill",
    "Mike",
    "Heather",
    "Jamie",
    "Evelyn",
    "Thomas",
    "Henry",
    "Shawna",
    "Xiaoyu",
    "Mirabella",
    "Constance",
    "Yuting"
)

val uuid : List<UUID> = listOf(
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID(),
    UUID.randomUUID()
)

val desc : List<String> = listOf(
    "inflate fantasy exotic",
    "toast weapon reliable",
    "consolidate tease similar",
    "pioneer habit expose",
    "maze remember attractive",
    "import old barrier",
    "duty donor sermon",
    "sailor dramatic neighbor",
    "wonder speed frighten",
    "volcano follow variation",
    "brake sentence private",
    "restoration hostile solid"
)