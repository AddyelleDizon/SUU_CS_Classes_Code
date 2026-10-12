package com.example.lab6

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val editText = findViewById<EditText>(R.id.editTextMessage)
        val buttonStart = findViewById<Button>(R.id.buttonStart)

        buttonStart.setOnClickListener {
            val message = editText.text.toString()

            val intent = Intent(this, SecondaryActivity::class.java)
            intent.putExtra(SecondaryActivity.EXTRA_MESSAGE, message)
            startActivity(intent)
        }
    }
}