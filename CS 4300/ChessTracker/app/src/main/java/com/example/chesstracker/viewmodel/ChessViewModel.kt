package com.example.chesstracker.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.chesstracker.model.ChessMove

class ChessViewModel : ViewModel() {

    private val _moves = MutableLiveData<MutableList<ChessMove>>(mutableListOf())
    val moves: LiveData<MutableList<ChessMove>> = _moves

    fun addMove(move: String) {
        val list = _moves.value ?: mutableListOf()
        list.add(ChessMove(move))
        _moves.value = list
    }

    fun resetGame() {
        _moves.value = mutableListOf()
    }
}