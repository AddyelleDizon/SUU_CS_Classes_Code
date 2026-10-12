package com.example.rotmgdpscalculator

import android.os.Bundle
import android.view.View
import android.widget.TextView
import androidx.fragment.app.Fragment

class DPSResultFragment : Fragment(R.layout.fragment_dps_result) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val resultText = view.findViewById<TextView>(R.id.txtResultFragment)
        val detailText = view.findViewById<TextView>(R.id.txtResultDetails)

        val dps = arguments?.getDouble("DPS") ?: 0.0
        val attack = arguments?.getInt("ATTACK") ?: 0
        val dexterity = arguments?.getInt("DEXTERITY") ?: 0
        val defense = arguments?.getInt("DEFENSE") ?: 0

        resultText.text = getString(R.string.average_dps_value, dps)
        detailText.text = getString(R.string.result_stats_value, attack, dexterity, defense)
    }
}
