package com.example.rotmgdpscalculator

import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.room.Room
import com.example.rotmgdpscalculator.data.AppDatabase
import com.example.rotmgdpscalculator.data.Build

class DPSResultActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dps_result)

        val dps = intent.getDoubleExtra("DPS", 0.0)
        val classType = intent.getStringExtra("CLASS") ?: "Unknown"
        val weapon = intent.getStringExtra("WEAPON") ?: "Unknown Weapon"
        val ability = intent.getStringExtra("ABILITY") ?: "Unknown Ability"
        val armor = intent.getStringExtra("ARMOR") ?: "Unknown Armor"
        val ring = intent.getStringExtra("RING") ?: "Unknown Ring"
        val attack = intent.getIntExtra("ATTACK", 0)
        val dexterity = intent.getIntExtra("DEXTERITY", 0)
        val defense = intent.getIntExtra("DEFENSE", 0)

        val fragment = DPSResultFragment().apply {
            arguments = Bundle().apply {
                putDouble("DPS", dps)
                putInt("ATTACK", attack)
                putInt("DEXTERITY", dexterity)
                putInt("DEFENSE", defense)
            }
        }

        supportFragmentManager.beginTransaction()
            .replace(R.id.resultFragmentContainer, fragment)
            .commit()

        val db = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "rotmg-db"
        ).allowMainThreadQueries().build()

        findViewById<Button>(R.id.btnSave).setOnClickListener {
            db.buildDao().insert(
                Build(
                    classType = classType,
                    weapon = weapon,
                    ability = ability,
                    armor = armor,
                    ring = ring,
                    dps = dps
                )
            )
            Toast.makeText(this, R.string.build_saved, Toast.LENGTH_SHORT).show()
        }

        findViewById<Button>(R.id.btnRecalculate).setOnClickListener {
            finish()
        }
    }
}
