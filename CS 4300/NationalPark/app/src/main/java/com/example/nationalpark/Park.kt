package com.example.nationalpark

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class Park(
    @PrimaryKey val id: Int,
    val name: String,
    val founded: Int,
    val state: String
)