package com.example.rotmgdpscalculator

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class EquipmentAdapter(private val items: List<EquipmentItem>) :
    RecyclerView.Adapter<EquipmentAdapter.ViewHolder>() {

    class ViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val txtName: TextView = view.findViewById(R.id.txtItemName)
        val txtType: TextView = view.findViewById(R.id.txtItemType)
        val txtStats: TextView = view.findViewById(R.id.txtItemStats)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_equipment, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val item = items[position]
        holder.txtName.text = item.name
        holder.txtType.text = item.type.replaceFirstChar { it.uppercase() }
        holder.txtStats.text = buildString {
            if (item.minDamage > 0 || item.maxDamage > 0) append("Damage ${item.minDamage}-${item.maxDamage}  ")
            if (item.attackBonus != 0) append("ATK +${item.attackBonus}  ")
            if (item.dexBonus != 0) append("DEX +${item.dexBonus}  ")
            if (item.defenseBonus != 0) append("DEF +${item.defenseBonus}  ")
            if (item.hpBonus != 0) append("HP +${item.hpBonus}")
            if (isBlank()) append("No bonus stats")
        }.trim()
    }

    override fun getItemCount(): Int = items.size
}
