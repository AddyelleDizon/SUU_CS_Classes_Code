import cv2
import os


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return None

    print("Image loaded successfully.")
    return image


def show_image_info(image):
    height, width, channels = image.shape

    print("\nImage Information:")
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Channels: {channels}")
    print(f"Data type: {image.dtype}")


def resize_image(image, width=800):
    h, w = image.shape[:2]
    aspect_ratio = h / w
    new_height = int(width * aspect_ratio)

    resized = cv2.resize(image, (width, new_height))
    print(f"Resized image to {width}x{new_height}")
    return resized


def convert_to_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Converted to grayscale.")
    return gray


def save_image(image, path):
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)

    success = cv2.imwrite(path, image)

    if success:
        print(f"Saved image to: {path}")
    else:
        print(f"Failed to save image to: {path}")


def split_image(image, num_splits):
    height = image.shape[0]
    chunk_size = height // num_splits

    chunks = []
    for i in range(num_splits):
        start = i * chunk_size
        end = height if i == num_splits - 1 else (i + 1) * chunk_size
        chunks.append(image[start:end])

    print(f"Split image into {num_splits} chunks.")
    return chunks


def main():
    # Get folder where this Python file is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Input image (same folder as script)
    input_path = os.path.join(script_dir, "input.jpg")

    # Output folder (next to script)
    output_folder = os.path.join(script_dir, "output")

    os.makedirs(output_folder, exist_ok=True)

    print("Script directory:", script_dir)
    print("Output folder:", output_folder)

    image = load_image(input_path)
    if image is None:
        return

    show_image_info(image)

    resized_image = resize_image(image)
    gray_image = convert_to_grayscale(resized_image)

    save_image(resized_image, os.path.join(output_folder, "original.jpg"))
    save_image(gray_image, os.path.join(output_folder, "grayscale.jpg"))

    chunks = split_image(gray_image, 4)
    print(f"Number of chunks created: {len(chunks)}")


if __name__ == "__main__":
    main()