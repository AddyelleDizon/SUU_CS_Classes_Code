package com.example.rotmgdpscalculator

data class EquipmentItem(
    val name: String,
    val type: String,
    val classRestriction: String,
    val minDamage: Int = 0,
    val maxDamage: Int = 0,
    val attackBonus: Int = 0,
    val dexBonus: Int = 0,
    val defenseBonus: Int = 0,
    val hpBonus: Int = 0
)