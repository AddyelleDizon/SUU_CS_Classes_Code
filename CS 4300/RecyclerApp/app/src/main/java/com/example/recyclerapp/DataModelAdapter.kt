package com.example.recyclerapp

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.recyclerapp.databinding.AdapterViewHolderBinding

class DataModelAdapter(private val data: List<DataModel>) :
    RecyclerView.Adapter<DataModelAdapter.DataModelViewHolder>() {

    class DataModelViewHolder(val binding: AdapterViewHolderBinding) :
        RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DataModelViewHolder {
        val binding = AdapterViewHolderBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return DataModelViewHolder(binding)
    }

    override fun onBindViewHolder(holder: DataModelViewHolder, position: Int) {
        val item = data[position]
        holder.binding.nameText.text = item.name
        holder.binding.uuidText.text = item.uuid.toString()
        holder.binding.descText.text = item.desc
    }

    override fun getItemCount(): Int = data.size
}