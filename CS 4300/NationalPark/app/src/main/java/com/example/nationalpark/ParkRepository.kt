package com.example.nationalpark

import android.content.Context
import androidx.room.Room
import kotlinx.coroutines.flow.Flow

class ParkRepository private constructor(context: Context) {

    private val database: ParkDatabase = Room.databaseBuilder(
        context.applicationContext,
        ParkDatabase::class.java,
        "park-database"
    )
        .createFromAsset("app/src/main/assets/park-database.db")
        .build()

    private val parkDao = database.parkDao()

    fun getParks(): Flow<List<Park>> = parkDao.getParks()

    suspend fun getPark(id: Int): Park = parkDao.getPark(id)

    companion object {
        private var INSTANCE: ParkRepository? = null

        fun initialize(context: Context) {
            if (INSTANCE == null) {
                INSTANCE = ParkRepository(context)
            }
        }

        fun get(): ParkRepository {
            return INSTANCE ?: throw IllegalStateException("ParkRepository must be initialized")
        }
    }
}