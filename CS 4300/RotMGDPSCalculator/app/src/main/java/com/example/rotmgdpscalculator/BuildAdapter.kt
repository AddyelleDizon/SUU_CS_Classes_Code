package com.example.rotmgdpscalculator

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.rotmgdpscalculator.data.Build

class BuildAdapter(private val builds: List<Build>) :
    RecyclerView.Adapter<BuildAdapter.ViewHolder>() {

    class ViewHolder(v: View) : RecyclerView.ViewHolder(v) {
        val txtClass: TextView = v.findViewById(R.id.txtBuildClass)
        val txtWeapon: TextView = v.findViewById(R.id.txtBuildWeapon)
        val txtAbility: TextView = v.findViewById(R.id.txtBuildAbility)
        val txtArmor: TextView = v.findViewById(R.id.txtBuildArmor)
        val txtRing: TextView = v.findViewById(R.id.txtBuildRing)
        val txtDps: TextView = v.findViewById(R.id.txtBuildDps)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val v = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_build, parent, false)
        return ViewHolder(v)
    }

    override fun getItemCount(): Int = builds.size

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val b = builds[position]

        holder.txtClass.text = "Class: ${b.classType}"
        holder.txtWeapon.text = "Weapon: ${b.weapon}"
        holder.txtAbility.text = "Ability: ${b.ability}"
        holder.txtArmor.text = "Armor: ${b.armor}"
        holder.txtRing.text = "Ring: ${b.ring}"
        holder.txtDps.text = "DPS: ${"%.2f".format(b.dps)}"
    }
}