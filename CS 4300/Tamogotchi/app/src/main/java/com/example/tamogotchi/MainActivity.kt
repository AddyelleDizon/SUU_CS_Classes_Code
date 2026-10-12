package com.example.tamogotchi

import android.os.Bundle
import android.util.Log
import androidx.activity.ComponentActivity
import com.example.tamogotchi.databinding.ActivityMainBinding
import com.example.tamogotchi.ui.theme.TamogotchiViewModel

class MainActivity : ComponentActivity() {

    private lateinit var binding: ActivityMainBinding
    private val viewModel = TamogotchiViewModel()

    private val TAG = "MAINACTIVITY"

    private val NAMEKEY = "NAME"
    private val AGEKEY = "AGE"
    private val HAPPINESSKEY = "HAPPINESS"
    private val HUNGERKEY = "HUNGER"
    private val ENERGYKEY = "ENERGY"
    private val STATUSKEY = "STATUS"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.eatButton.contentDescription = "Feed pet"
        binding.playButton.contentDescription = "Play with pet"
        binding.sleepButton.contentDescription = "Put pet to sleep"

        if (savedInstanceState != null) {
            Log.d(TAG, "Saved instance state bundle retrieved")

            binding.nameVal.text = savedInstanceState.getString(NAMEKEY)
            binding.ageVal.text = "${savedInstanceState.getInt(AGEKEY)} days"
            binding.happyVal.text = "${savedInstanceState.getInt(HAPPINESSKEY)} / 100"
            binding.hungerVal.text = "${savedInstanceState.getInt(HUNGERKEY)} / 100"
            binding.energyVal.text = "${savedInstanceState.getInt(ENERGYKEY)} / 100"
            binding.statusText.text = savedInstanceState.getString(STATUSKEY, "Pet status restored")

            updateContentDescriptions()
        } else {
            Log.d(TAG, "No saved state bundle found")

            binding.nameVal.text = viewModel.name()
            updateUI()
            binding.statusText.text =
                "Tamagotchi game loaded! Please use the feed, play, or sleep buttons to care for your pet."

            binding.statusText.post {
                binding.statusText.announceForAccessibility(
                    "Tamagotchi game loaded! Please use the feed, play, or sleep buttons to care for your pet."
                )
            }
        }

        binding.eatButton.setOnClickListener {
            val message = viewModel.eat()
            updateUI()
            binding.statusText.text = message
            binding.statusText.announceForAccessibility(message)
        }

        binding.playButton.setOnClickListener {
            val message = viewModel.play()
            updateUI()
            binding.statusText.text = message
            binding.statusText.announceForAccessibility(message)
        }

        binding.sleepButton.setOnClickListener {
            val message = viewModel.sleep()
            updateUI()
            binding.statusText.text = message
            binding.statusText.announceForAccessibility(message)
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)

        Log.d(TAG, "Saved state bundle created")

        outState.putString(NAMEKEY, viewModel.name())
        outState.putInt(AGEKEY, viewModel.age())
        outState.putInt(HAPPINESSKEY, viewModel.happiness())
        outState.putInt(HUNGERKEY, viewModel.hunger())
        outState.putInt(ENERGYKEY, viewModel.energy())
        outState.putString(STATUSKEY, binding.statusText.text.toString())
    }

    private fun updateUI() {
        val name = viewModel.name()
        val age = viewModel.age()
        val hunger = viewModel.hunger()
        val happiness = viewModel.happiness()
        val energy = viewModel.energy()

        binding.nameVal.text = name
        binding.ageVal.text = "$age days"
        binding.hungerVal.text = "$hunger / 100"
        binding.happyVal.text = "$happiness / 100"
        binding.energyVal.text = "$energy / 100"

        updateContentDescriptions()
    }

    private fun updateContentDescriptions() {
        binding.nameVal.contentDescription = "Pet name ${binding.nameVal.text}"
        binding.ageVal.contentDescription = "Age ${binding.ageVal.text}"
        binding.hungerVal.contentDescription =
            "Hunger ${viewModel.hunger()} out of 100"
        binding.happyVal.contentDescription =
            "Happiness ${viewModel.happiness()} out of 100"
        binding.energyVal.contentDescription =
            "Energy ${viewModel.energy()} out of 100"
    }
}