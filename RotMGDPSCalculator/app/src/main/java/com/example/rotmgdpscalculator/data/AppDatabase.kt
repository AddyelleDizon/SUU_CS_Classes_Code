package com.example.rotmgdpscalculator.data

import androidx.room.Database
import androidx.room.RoomDatabase

@Database(entities = [Build::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {
    abstract fun buildDao(): BuildDao
}