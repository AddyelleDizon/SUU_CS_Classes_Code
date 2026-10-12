package com.example.rotmgdpscalculator

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.SeekBar
import android.widget.Spinner
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.rotmgdpscalculator.models.Classes
import com.example.rotmgdpscalculator.models.DPSCalculator

class DPSCreatorActivity : AppCompatActivity() {

    private var defense = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dps_creator)

        val classSpinner = findViewById<Spinner>(R.id.spinnerClass)
        val weaponSpinner = findViewById<Spinner>(R.id.spinnerWeapon)
        val abilitySpinner = findViewById<Spinner>(R.id.spinnerAbility)
        val armorSpinner = findViewById<Spinner>(R.id.spinnerArmor)
        val ringSpinner = findViewById<Spinner>(R.id.spinnerRing)
        val defenseSeekBar = findViewById<SeekBar>(R.id.seekDefense)
        val defenseTextView = findViewById<TextView>(R.id.txtDefense)
        val calculateButton = findViewById<Button>(R.id.btnCalculate)

        classSpinner.adapter = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_dropdown_item,
            Classes.ALL
        )

        fun setSpinnerItems(spinner: Spinner, items: List<String>) {
            val safeItems = if (items.isEmpty()) listOf("None Available") else items
            spinner.adapter = ArrayAdapter(
                this,
                android.R.layout.simple_spinner_dropdown_item,
                safeItems
            )
        }

        fun updateEquipmentSpinners(selectedClass: String) {
            val weapons = EquipmentRepository
                .getItemsForClassAndType(selectedClass, "weapon")
                .map { it.name }

            val abilities = EquipmentRepository
                .getItemsForClassAndType(selectedClass, "ability")
                .map { it.name }

            val armors = EquipmentRepository
                .getItemsForClassAndType(selectedClass, "armor")
                .map { it.name }

            val rings = EquipmentRepository
                .getItemsForClassAndType(selectedClass, "ring")
                .map { it.name }

            setSpinnerItems(weaponSpinner, weapons)
            setSpinnerItems(abilitySpinner, abilities)
            setSpinnerItems(armorSpinner, armors)
            setSpinnerItems(ringSpinner, rings)
        }

        classSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>?,
                view: View?,
                position: Int,
                id: Long
            ) {
                val selectedClass = Classes.ALL[position]
                updateEquipmentSpinners(selectedClass)
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {
            }
        }

        updateEquipmentSpinners(Classes.ALL.first())

        defenseSeekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                defense = progress
                defenseTextView.text = "Enemy Defense: $progress"
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {
            }

            override fun onStopTrackingTouch(seekBar: SeekBar?) {
            }
        })

        calculateButton.setOnClickListener {
            val selectedClass = classSpinner.selectedItem?.toString() ?: "Select A Class"
            val selectedWeaponName = weaponSpinner.selectedItem?.toString() ?: "None Available"
            val selectedAbilityName = abilitySpinner.selectedItem?.toString() ?: "None Available"
            val selectedArmorName = armorSpinner.selectedItem?.toString() ?: "None Available"
            val selectedRingName = ringSpinner.selectedItem?.toString() ?: "None Available"

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
            }

            startActivity(intent)
        }
    }
}