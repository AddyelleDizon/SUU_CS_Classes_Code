import cv2
import os


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return None

    print("Image loaded successfully.")
    return image


def apply_blur_filter(image):
    blurred = cv2.GaussianBlur(image, (351, 351), 0)
    print("Blur filter applied.")
    return blurred


def apply_edge_filter(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    print("Edge detection filter applied.")
    return edges


def save_image(image, path):
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)

    success = cv2.imwrite(path, image)

    if success:
        print(f"Saved image to: {path}")
    else:
        print(f"Failed to save image to: {path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(script_dir, "input.jpg")

    output_folder = os.path.join(script_dir, "output")
    os.makedirs(output_folder, exist_ok=True)

    print("Script directory:", script_dir)
    print("Output folder:", output_folder)

    image = load_image(input_path)
    if image is None:
        return

    blurred_image = apply_blur_filter(image)
    edge_image = apply_edge_filter(image)

    save_image(blurred_image, os.path.join(output_folder, "blurred.jpg"))
    save_image(edge_image, os.path.join(output_folder, "edges.jpg"))


if __name__ == "__main__":
    main()