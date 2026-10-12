package com.example.nationalpark

import androidx.room.Dao
import androidx.room.Query
import kotlinx.coroutines.flow.Flow

@Dao
interface ParkDAO {

    @Query("SELECT * FROM Park")
    fun getParks(): Flow<List<Park>>

    @Query("SELECT * FROM Park WHERE id = :id")
    suspend fun getPark(id: Int): Park
}