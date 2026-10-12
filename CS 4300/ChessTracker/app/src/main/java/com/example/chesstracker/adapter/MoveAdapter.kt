package com.example.chesstracker.adapter

import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.example.chesstracker.model.ChessMove

class MoveAdapter :
    ListAdapter<ChessMove, MoveAdapter.MoveViewHolder>(DiffCallback()) {

    class MoveViewHolder(val textView: TextView) : RecyclerView.ViewHolder(textView)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MoveViewHolder {
        val textView = TextView(parent.context)
        textView.textSize = 18f
        textView.setPadding(16,16,16,16)
        return MoveViewHolder(textView)
    }

    override fun onBindViewHolder(holder: MoveViewHolder, position: Int) {
        holder.textView.text = getItem(position).moveText
    }

    class DiffCallback : DiffUtil.ItemCallback<ChessMove>() {
        override fun areItemsTheSame(oldItem: ChessMove, newItem: ChessMove) = oldItem == newItem
        override fun areContentsTheSame(oldItem: ChessMove, newItem: ChessMove) = oldItem == newItem
    }
}