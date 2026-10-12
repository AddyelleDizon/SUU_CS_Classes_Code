import os

os.environ["KERAS_BACKEND"] = "torch"

try:
    import torch
    import keras
    
    print("Successfully imported Torch and Keras!")
    print(f"   • Torch Version: {torch.__version__}")
    print(f"   • Keras Version: {keras.__version__}")
    print(f"   • Keras Backend: {keras.backend.backend()}\n")

    if torch.cuda.is_available():
        print(f"GPU Available: Yes ({torch.cuda.get_device_name(0)})")
    else:
        print("GPU Available: No (Running on CPU)")
        
    print("\nRunning a quick Keras-Torch operation...")
    layer = keras.layers.Dense(units=3, input_shape=(5,))
    print("Keras layer built successfully!")
    
except ImportError as e:
    print(f"Error during import: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")