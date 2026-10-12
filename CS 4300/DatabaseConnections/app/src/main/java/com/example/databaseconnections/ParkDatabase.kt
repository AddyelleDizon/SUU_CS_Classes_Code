package com.example.nationalpark

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = [Park::class], version = 1)
abstract class ParkDatabase : RoomDatabase() {
    abstract fun parkDao(): ParkDAO
}