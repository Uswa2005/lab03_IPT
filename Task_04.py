# Task 4: Draw Red Text in OpenCV using BGR Color Order

import cv2
import numpy as np

# Check and print OpenCV version
print("OpenCV version:", cv2.__version__)

# Create a black image (height=300, width=400, 3 color channels)
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Write text using RED color in BGR format: (0, 0, 255) -> (Blue=0, Green=0, Red=255)
cv2.putText(
    image,
    "Hello OpenCV!",
    (40, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Display text color information
print("Text Color: Red - BGR format (0, 0, 255)")

# Display the image (supports both Google Colab and local Python / VS Code)
try:
    from google.colab.patches import cv2_imshow
    cv2_imshow(image)
except ImportError:
    cv2.imshow("Red Text (BGR Order)", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
