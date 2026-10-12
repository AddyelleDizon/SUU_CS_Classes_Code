package com.example.nationalpark

import android.app.Application

class NationalParkApplication : Application() {

    override fun onCreate() {
        super.onCreate()
        ParkRepository.initialize(this)
    }
}