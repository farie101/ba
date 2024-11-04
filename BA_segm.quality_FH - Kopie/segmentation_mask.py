import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def create_segmentation_mask(components, image_shape):
    """
    Create a segmentation mask from components.

    Parameters:
    - components (list of Component): List of components, each containing a set of pixels.
    - image_shape (tuple): Shape of the original image (height, width).

    Returns:
    - segmentation_mask (ndarray): 2D array with unique labels for each component.
    """
    # Initialize an empty mask
    segmentation_mask = np.zeros(image_shape[:2], dtype=np.int32)  # 2D mask for labels

    # Assign unique labels to each component
    for label, component in enumerate(components, start=1):  # start=1 to avoid 0 for background
        for (row, col) in component.pixels:
            segmentation_mask[row, col] = label  # Assign a unique label for each component

    return segmentation_mask


def overlay_segmentation_on_image(original_image, segmentation_mask, alpha=0.5):
    """
    Overlay segmentation mask on the original image.

    Parameters:
    - original_image (ndarray): The original image as a 3D array (H, W, 3).
    - segmentation_mask (ndarray): 2D array with unique labels for each segment (H, W).
    - alpha (float): Transparency for the overlay (0 = fully transparent, 1 = fully opaque).
    """
    # Define a color map for different segments (e.g., 10 distinct colors for 10 segments)
    num_segments = segmentation_mask.max() + 1  # assuming labels are 0, 1, ..., num_segments-1
    np.random.seed(0)  # for reproducible colors
    colors = np.random.randint(0, 255, size=(num_segments, 3), dtype=np.uint8)

    # Create an RGB overlay for the segmentation
    segmentation_overlay = np.zeros((*segmentation_mask.shape, 3), dtype=np.uint8)
    for segment_label in range(1, num_segments):  # Start from 1 to avoid background (label 0)
        segmentation_overlay[segmentation_mask == segment_label] = colors[segment_label]

    # Blend the overlay with the original image
    overlay_image = (alpha * segmentation_overlay + (1 - alpha) * original_image).astype(np.uint8)

    # Display the result
    plt.figure(figsize=(10, 10))
    plt.imshow(overlay_image)
    plt.axis('off')
    plt.show()
