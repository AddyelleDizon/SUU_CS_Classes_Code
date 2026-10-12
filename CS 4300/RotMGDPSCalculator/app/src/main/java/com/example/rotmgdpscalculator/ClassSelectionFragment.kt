package com.example.rotmgdpscalculator

import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.Spinner
import androidx.fragment.app.Fragment
import com.example.rotmgdpscalculator.models.Classes

class ClassSelectionFragment : Fragment(R.layout.fragment_class_selection) {

    private var onClassSelected: ((String) -> Unit)? = null
    private var spinner: Spinner? = null

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        spinner = view.findViewById<Spinner>(R.id.spinnerClass).apply {
            adapter = ArrayAdapter(
                requireContext(),
                android.R.layout.simple_spinner_dropdown_item,
                Classes.ALL
            )
            onItemSelectedListener = object : android.widget.AdapterView.OnItemSelectedListener {
                override fun onItemSelected(
                    parent: android.widget.AdapterView<*>?,
                    view: View?,
                    position: Int,
                    id: Long
                ) {
                    onClassSelected?.invoke(Classes.ALL[position])
                }

                override fun onNothingSelected(parent: android.widget.AdapterView<*>?) = Unit
            }
        }
    }

    fun setOnClassSelectedListener(listener: (String) -> Unit) {
        onClassSelected = listener
        spinner?.selectedItem?.toString()?.let(listener)
    }

    fun getSelectedClass(): String {
        return spinner?.selectedItem?.toString() ?: Classes.ALL.first()
    }
}
