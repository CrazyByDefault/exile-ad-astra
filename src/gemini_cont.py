import cv2

def extract_overlay(image_path):
    """
    Extracts the overlay map from the given image using OpenCV.

    Args:
        image_path: Path to the input image.

    Returns:
        Extracted overlay map as a NumPy array.
    """

    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary mask
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Remove noise using morphological operations (optional)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # Extract the overlay by masking the original image
    overlay = cv2.bitwise_and(img, img, mask=thresh)

    return overlay

if __name__ == "__main__":
    image_path = "/home/shashank/personal/poe/codex-helper/images/praetor/Praetor_2.png"  # Replace with the actual path
    overlay = extract_overlay(image_path)

    # Display the result
    cv2.imshow("Overlay Map", overlay)
    cv2.waitKey(0)
    cv2.destroyAllWindows()