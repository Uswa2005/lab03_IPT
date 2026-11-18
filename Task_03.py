# Task 3: Create Image with Modified Dimensions (200, 500, 3)

import cv2
import numpy as np

# Check and print OpenCV version
print("OpenCV version:", cv2.__version__)

# Create an image with dimensions height=200, width=500, and 3 color channels
image = np.zeros((200, 500, 3), dtype=np.uint8)

# Write text on the image centered for the new dimensions
cv2.putText(
    image,
    "Hello OpenCV!",
    (50, 110),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Display image dimensions to confirm shape
print("Image Dimensions (Shape):", image.shape)

# Display the image (supports both Google Colab and local Python / VS Code)
try:
    from google.colab.patches import cv2_imshow
    cv2_imshow(image)
except ImportError:
    cv2.imshow("Custom Dimensions (200x500)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
