package com.example.rotmgdpscalculator

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.room.Room
import com.example.rotmgdpscalculator.data.AppDatabase

class BuildListActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_build_list)

        val recycler = findViewById<RecyclerView>(R.id.recyclerBuilds)

        val db = Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "rotmg-db"
        ).allowMainThreadQueries().build()

        recycler.layoutManager = LinearLayoutManager(this)
        recycler.adapter = BuildAdapter(db.buildDao().getAll())
    }
}