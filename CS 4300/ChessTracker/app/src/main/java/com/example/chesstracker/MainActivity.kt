package com.example.chesstracker

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.chesstracker.adapter.MoveAdapter
import com.example.chesstracker.databinding.ActivityMainBinding
import com.example.chesstracker.model.ChessMove
import com.example.chesstracker.viewmodel.ChessViewModel

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val viewModel: ChessViewModel by viewModels()
    private lateinit var adapter: MoveAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        adapter = MoveAdapter()
        binding.moveList.layoutManager = LinearLayoutManager(this)
        binding.moveList.adapter = adapter

        val openings = resources.getStringArray(R.array.chess_openings)

        // first five moves of the 5 openings given
        val openingMovesMap = mapOf(
            "King Pawn Opening" to listOf("e2 e4", "e7 e5", "g1 f3", "b8 c6", "f1 c4"),
            "Queen Gambit" to listOf("d2 d4", "d7 d5", "c2 c4", "e7 e6", "g1 f3"),
            "Ruy Lopez" to listOf("e2 e4", "e7 e5", "g1 f3", "b8 c6", "f1 b5"),
            "Sicilian Defense" to listOf("e2 e4", "c7 c5", "g1 f3", "d7 d6", "d2 d4"),
            "French Defense" to listOf("e2 e4", "e7 e6", "d2 d4", "d7 d5", "g1 f3")
        )

        val spinnerAdapter = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_item,
            openings
        )
        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        binding.openingSpinner.adapter = spinnerAdapter

        binding.openingSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>?, view: View?, position: Int, id: Long
            ) {
                val selectedOpening = openings[position]
                viewModel.resetGame() // clear current moves
                openingMovesMap[selectedOpening]?.forEach { move ->
                    viewModel.addMove(move)
                }
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {}
        }

        binding.addMoveBtn.setOnClickListener {
            val move = binding.moveInput.text.toString().trim()
            if (move.isNotEmpty()) {
                viewModel.addMove(move)
                binding.moveInput.text.clear()
            }
        }

        binding.resetBtn.setOnClickListener {
            viewModel.resetGame()
        }

        viewModel.moves.observe(this) { moves ->
            val numberedMoves = moves.mapIndexed { index, chessMove ->
                ChessMove("${index + 1}. ${chessMove.moveText}")
            }
            adapter.submitList(numberedMoves.toList())
        }
    }
}