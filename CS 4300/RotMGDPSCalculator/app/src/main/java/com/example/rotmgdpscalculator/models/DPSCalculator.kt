package com.example.rotmgdpscalculator.models

object DPSCalculator {

    fun calculate(
        minDamage: Int,
        maxDamage: Int,
        attack: Int,
        dexterity: Int,
        enemyDefense: Int,
        shots: Int,
        rateOfFire: Double
    ): Double {

        val avg = (minDamage + maxDamage) / 2.0
        val atkMult = 0.5 + (attack / 75.0)
        val dmgAfterDef = maxOf(0.0, avg - enemyDefense)
        val attackSpeed = 1.5 + (dexterity / 75.0)

        return dmgAfterDef * atkMult * attackSpeed * shots * rateOfFire
    }
}