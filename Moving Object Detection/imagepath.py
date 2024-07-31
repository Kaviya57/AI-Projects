import cv2
import imutils

# Provide the correct path to your image
image_path = "C:\\Users\\jaaya\\Downloads\\Day-4\\Day_4\\your_image.jpg"  # Update this path

# Load the image using OpenCV
img = cv2.imread(image_path)

# Check if the image was loaded correctly
if img is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    # Resize the image
    img_resized = imutils.resize(img, width=1000)
    print("Image resized successfully.")

    # Display the resized image (optional)
    cv2.imshow("Resized Image", img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
