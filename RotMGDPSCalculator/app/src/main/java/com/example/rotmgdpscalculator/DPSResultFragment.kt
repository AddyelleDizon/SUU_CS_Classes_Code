package com.example.rotmgdpscalculator

import android.os.Bundle
import android.view.View
import android.widget.TextView
import androidx.fragment.app.Fragment

class DPSResultFragment : Fragment(R.layout.fragment_dps_result) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val resultText = view.findViewById<TextView>(R.id.txtResultFragment)

        val dps = arguments?.getDouble("DPS") ?: 0.0
        resultText.text = "Average DPS: %.2f".format(dps)
    }
}