import cv2
import numpy as np

# Load image
image_path = "data/test_fire.jpg"
image = cv2.imread(image_path)

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Fire color range (approximate)
lower_fire = np.array([0, 120, 200])
upper_fire = np.array([50, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_fire, upper_fire)

# Count fire pixels
fire_pixels = np.sum(mask > 0)

# Decision
if fire_pixels > 500:
    print("🔥 Fire Detected!")
else:
    print("✅ No Fire Detected")

# Show image
cv2.imshow("Image", image)
cv2.imshow("Fire Mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

