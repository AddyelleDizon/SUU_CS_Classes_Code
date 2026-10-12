import cv2
import os
import time
from multiprocessing import Pool, cpu_count

from ImageHandling import load_image, resize_image, convert_to_grayscale, split_image, save_image


# ---- Filter to apply ----
def process_chunk(chunk):
    for _ in range(50000):   # crank this up
        chunk = cv2.GaussianBlur(chunk, (15, 15), 0)
    return chunk


# ---- Sequential Processing ----
def sequential_processing(chunks):
    print("\nStarting sequential processing...")
    start_time = time.time()

    processed_chunks = []
    for chunk in chunks:
        processed_chunks.append(process_chunk(chunk))

    end_time = time.time()
    print(f"Sequential processing time: {end_time - start_time:.4f} seconds")

    return processed_chunks


# ---- Parallel Processing ----
def parallel_processing(chunks):
    print("\nStarting parallel processing...")
    start_time = time.time()

    num_processes = cpu_count()
    print(f"Using {num_processes} processes")

    with Pool(processes=num_processes) as pool:
        processed_chunks = pool.map(process_chunk, chunks)

    end_time = time.time()
    print(f"Parallel processing time: {end_time - start_time:.4f} seconds")

    return processed_chunks


# ---- Recombine image ----
def combine_chunks(chunks):
    return cv2.vconcat(chunks)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, "input.jpg")
    output_folder = os.path.join(script_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Load and preprocess
    image = load_image(input_path)
    if image is None:
        return

    image = resize_image(image)

    # Split into chunks
    chunks = split_image(image, 8)

    # Sequential
    seq_chunks = sequential_processing(chunks)
    seq_image = combine_chunks(seq_chunks)
    save_image(seq_image, os.path.join(output_folder, "sequential.jpg"))

    # Parallel
    par_chunks = parallel_processing(chunks)
    par_image = combine_chunks(par_chunks)
    save_image(par_image, os.path.join(output_folder, "parallel.jpg"))


if __name__ == "__main__":
    main()