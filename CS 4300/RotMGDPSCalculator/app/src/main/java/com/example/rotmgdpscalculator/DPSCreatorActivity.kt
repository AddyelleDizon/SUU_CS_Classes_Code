package com.example.rotmgdpscalculator

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.SeekBar
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.rotmgdpscalculator.models.DPSCalculator

class DPSCreatorActivity : AppCompatActivity() {

    private var defense = 0
    private lateinit var classSelectionFragment: ClassSelectionFragment
    private lateinit var equipmentSelectionFragment: EquipmentSelectionFragment

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dps_creator)

        if (savedInstanceState == null) {
            classSelectionFragment = ClassSelectionFragment()
            equipmentSelectionFragment = EquipmentSelectionFragment()

            supportFragmentManager.beginTransaction()
                .replace(R.id.classFragmentContainer, classSelectionFragment, "class_fragment")
                .replace(R.id.equipmentFragmentContainer, equipmentSelectionFragment, "equipment_fragment")
                .commitNow()
        } else {
            classSelectionFragment = supportFragmentManager.findFragmentByTag("class_fragment") as ClassSelectionFragment
            equipmentSelectionFragment = supportFragmentManager.findFragmentByTag("equipment_fragment") as EquipmentSelectionFragment
        }

        val defenseSeekBar = findViewById<SeekBar>(R.id.seekDefense)
        val defenseTextView = findViewById<TextView>(R.id.txtDefense)
        val calculateButton = findViewById<Button>(R.id.btnCalculate)

        classSelectionFragment.setOnClassSelectedListener { selectedClass ->
            equipmentSelectionFragment.showItemsForClass(selectedClass)
        }
        equipmentSelectionFragment.showItemsForClass(classSelectionFragment.getSelectedClass())

        defenseSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                defense = progress
                defenseTextView.text = getString(R.string.enemy_defense_value, progress)
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) = Unit
            override fun onStopTrackingTouch(seekBar: SeekBar?) = Unit
        })

        calculateButton.setOnClickListener {
            val selectedClass = classSelectionFragment.getSelectedClass()
            val selectedWeaponName = equipmentSelectionFragment.getSelectedWeaponName()
            val selectedAbilityName = equipmentSelectionFragment.getSelectedAbilityName()
            val selectedArmorName = equipmentSelectionFragment.getSelectedArmorName()
            val selectedRingName = equipmentSelectionFragment.getSelectedRingName()

            val weapon = EquipmentRepository.allItems.find { it.name == selectedWeaponName }
            val ability = EquipmentRepository.allItems.find { it.name == selectedAbilityName }
            val armor = EquipmentRepository.allItems.find { it.name == selectedArmorName }
            val ring = EquipmentRepository.allItems.find { it.name == selectedRingName }

            val totalAttack =
                75 +
                    (weapon?.attackBonus ?: 0) +
                    (ability?.attackBonus ?: 0) +
                    (armor?.attackBonus ?: 0) +
                    (ring?.attackBonus ?: 0)

            val totalDexterity =
                75 +
                    (weapon?.dexBonus ?: 0) +
                    (ability?.dexBonus ?: 0) +
                    (armor?.dexBonus ?: 0) +
                    (ring?.dexBonus ?: 0)

            val minDamage = weapon?.minDamage ?: 0
            val maxDamage = weapon?.maxDamage ?: 0

            val dps = DPSCalculator.calculate(
                minDamage = minDamage,
                maxDamage = maxDamage,
                attack = totalAttack,
                dexterity = totalDexterity,
                enemyDefense = defense,
                shots = 1,
                rateOfFire = 1.2
            )

            val intent = Intent(this, DPSResultActivity::class.java).apply {
                putExtra("DPS", dps)
                putExtra("CLASS", selectedClass)
                putExtra("WEAPON", selectedWeaponName)
                putExtra("ABILITY", selectedAbilityName)
                putExtra("ARMOR", selectedArmorName)
                putExtra("RING", selectedRingName)
                putExtra("ATTACK", totalAttack)
                putExtra("DEXTERITY", totalDexterity)
                putExtra("DEFENSE", defense)
            }

            startActivity(intent)
        }
    }
}
