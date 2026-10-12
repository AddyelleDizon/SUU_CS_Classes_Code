package com.example.rotmgdpscalculator

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class EquipmentSelectionFragment : Fragment(R.layout.fragment_equipment_selection) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val recycler = view.findViewById<RecyclerView>(R.id.recyclerEquipment)

        val sampleItems = listOf(
            "Staff of Cosmic Whole",
            "Scepter of Devotion",
            "Soulless Robe",
            "Bracer of the Guardian"
        )

        recycler.layoutManager = LinearLayoutManager(requireContext())
        recycler.adapter = EquipmentAdapter(sampleItems)
    }
}