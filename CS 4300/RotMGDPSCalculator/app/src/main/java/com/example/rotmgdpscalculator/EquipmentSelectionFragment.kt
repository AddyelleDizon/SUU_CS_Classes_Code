package com.example.rotmgdpscalculator

import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.Spinner
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class EquipmentSelectionFragment : Fragment(R.layout.fragment_equipment_selection) {

    private lateinit var recycler: RecyclerView
    private lateinit var weaponSpinner: Spinner
    private lateinit var abilitySpinner: Spinner
    private lateinit var armorSpinner: Spinner
    private lateinit var ringSpinner: Spinner

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        recycler = view.findViewById(R.id.recyclerEquipment)
        weaponSpinner = view.findViewById(R.id.spinnerWeapon)
        abilitySpinner = view.findViewById(R.id.spinnerAbility)
        armorSpinner = view.findViewById(R.id.spinnerArmor)
        ringSpinner = view.findViewById(R.id.spinnerRing)

        recycler.layoutManager = LinearLayoutManager(requireContext())
        showItemsForClass(arguments?.getString(ARG_CLASS_NAME) ?: "Wizard")
    }

    private fun setSpinnerItems(spinner: Spinner, items: List<String>) {
        val safeItems = if (items.isEmpty()) listOf("None Available") else items
        spinner.adapter = ArrayAdapter(
            requireContext(),
            android.R.layout.simple_spinner_dropdown_item,
            safeItems
        )
    }

    fun showItemsForClass(className: String) {
        if (!isAdded || view == null) return

        val items = EquipmentRepository.allItems.filter { it.classRestriction == className }
        recycler.adapter = EquipmentAdapter(items)

        setSpinnerItems(weaponSpinner, items.filter { it.type == "weapon" }.map { it.name })
        setSpinnerItems(abilitySpinner, items.filter { it.type == "ability" }.map { it.name })
        setSpinnerItems(armorSpinner, items.filter { it.type == "armor" }.map { it.name })
        setSpinnerItems(ringSpinner, items.filter { it.type == "ring" }.map { it.name })
    }

    fun getSelectedWeaponName(): String = weaponSpinner.selectedItem?.toString() ?: "None Available"
    fun getSelectedAbilityName(): String = abilitySpinner.selectedItem?.toString() ?: "None Available"
    fun getSelectedArmorName(): String = armorSpinner.selectedItem?.toString() ?: "None Available"
    fun getSelectedRingName(): String = ringSpinner.selectedItem?.toString() ?: "None Available"

    companion object {
        private const val ARG_CLASS_NAME = "class_name"
    }
}
