package com.example.rotmgdpscalculator.data

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class Build(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val classType: String,
    val weapon: String,
    val ability: String,
    val armor: String,
    val ring: String,
    val dps: Double
)