package com.example.lab6

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class SecondaryActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_MESSAGE = "com.example.lab6.MESSAGE"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.secondary_activity)

        val textView = findViewById<TextView>(R.id.textViewMessage)
        val buttonBack = findViewById<Button>(R.id.buttonBack)

        // Get the extra from the Intent
        val message = intent.getStringExtra(EXTRA_MESSAGE)

        textView.text = message

        buttonBack.setOnClickListener {
            finish()   // closes this activity and returns to MainActivity
        }
    }
}