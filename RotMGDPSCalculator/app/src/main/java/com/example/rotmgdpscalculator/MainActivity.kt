package com.example.rotmgdpscalculator

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        findViewById<Button>(R.id.btnCreate).setOnClickListener {
            startActivity(Intent(this, DPSCreatorActivity::class.java))
        }

        findViewById<Button>(R.id.btnView).setOnClickListener {
            startActivity(Intent(this, BuildListActivity::class.java))
        }
    }
}