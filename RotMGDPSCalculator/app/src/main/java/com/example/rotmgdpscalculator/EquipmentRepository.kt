package com.example.rotmgdpscalculator

// Change to class; singleton pattern, only one repository
// Create repository,
object EquipmentRepository {

    val allItems = listOf(
        EquipmentItem("Staff of Cosmic Whole", "weapon", "Wizard", 95, 160),
        EquipmentItem("Staff of Extreme Prejudice", "weapon", "Wizard", 85, 175),
        EquipmentItem("Elemental Detonation", "ability", "Wizard", attackBonus = 4),
        EquipmentItem("Soulless Robe", "armor", "Wizard", defenseBonus = 10),
        EquipmentItem("Ring of Decades", "ring", "Wizard", hpBonus = 60),

        EquipmentItem("Pixie-Enchanted Sword", "weapon", "Knight", 60, 90),
        EquipmentItem("Divine Coronation", "weapon", "Knight", 110, 160),
        EquipmentItem("Shield of Ogmur", "ability", "Knight", defenseBonus = 6),
        EquipmentItem("Dominion Armor", "armor", "Knight", defenseBonus = 18),
        EquipmentItem("Crown", "ring", "Knight", attackBonus = 4, dexBonus = 4),

        EquipmentItem("Bow of the Void", "weapon", "Archer", 110, 145),
        EquipmentItem("Leaf Bow", "weapon", "Archer", 70, 110),
        EquipmentItem("Quiver of Thunder", "ability", "Archer", dexBonus = 5),
        EquipmentItem("Hallowed Hide", "armor", "Archer", defenseBonus = 12),
        EquipmentItem("Ring of Exalted Health", "ring", "Archer", hpBonus = 80)
    )

    fun getItemsForClassAndType(className: String, type: String): List<EquipmentItem> {
        return allItems.filter {
            it.classRestriction == className && it.type == type
        }
    }
}