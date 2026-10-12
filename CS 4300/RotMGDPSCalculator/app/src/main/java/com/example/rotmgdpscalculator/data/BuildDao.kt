package com.example.rotmgdpscalculator.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface BuildDao {

    @Insert
    fun insert(build: Build)

    @Query("SELECT * FROM Build")
    fun getAll(): List<Build>
}