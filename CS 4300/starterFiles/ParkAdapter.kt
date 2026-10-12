package com.example.nationalpark

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.nationalpark.databinding.ParkListViewBinding



class ParkAdapter(private val data : List<Park>) : RecyclerView.Adapter<ParkListViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ParkListViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val binding = ParkListViewBinding.inflate(inflater, parent, false)
        return ParkListViewHolder(binding)
    }

    override fun getItemCount(): Int {
        return data.size
    }

    override fun onBindViewHolder(holder: ParkListViewHolder, position: Int) {
        val item = data[position]
        holder.binding.apply {
            parkName.text = item.name
            parkState.text = item.state
            parkFounded.text = "Founded in " + item.founded.toString()
        }
    }

}

class ParkListViewHolder(val binding : ParkListViewBinding) : RecyclerView.ViewHolder(binding.root) {}