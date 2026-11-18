# Task 2: Display Custom Text Message on Image using OpenCV

import cv2
import numpy as np

# Check and print OpenCV version
print("OpenCV version:", cv2.__version__)

# Create a black image (height=300, width=400, 3 color channels)
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Write a custom text message on the image
# Arguments: image, text, starting position (x, y), font, font scale, color (BGR), thickness
cv2.putText(
    image,
    "Welcome to IPT Lab!",
    (30, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (255, 255, 255),
    2
)

# Display the image (supports both Google Colab and local Python / VS Code)
try:
    from google.colab.patches import cv2_imshow
    cv2_imshow(image)
except ImportError:
    cv2.imshow("Custom Message", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
