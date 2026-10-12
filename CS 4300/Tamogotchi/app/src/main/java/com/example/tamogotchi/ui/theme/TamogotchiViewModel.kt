package com.example.tamogotchi.ui.theme

import com.example.tamogotchi.Tamogotchi

class TamogotchiViewModel {
    private val tamo = Tamogotchi("Tamo")

    fun name(): String {
        return tamo.name
    }

    fun age(): Int {
        return tamo.age
    }

    fun hunger(): Int {
        return tamo.hunger
    }

    fun happiness(): Int {
        return tamo.happiness
    }

    fun energy(): Int {
        return tamo.energy
    }

    fun play(): String {
        return tamo.play()
    }

    fun sleep(): String {
        return tamo.sleep()
    }

    fun eat(): String {
        return tamo.eat()
    }
}