
import numpy as np

def create_masked_stipple(stipple_img: np.ndarray, mask_img: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Applies a block letter mask to a stippled image.

    Args:
        stipple_img: The stippled image (2D numpy array).
        mask_img: The mask image (2D numpy array), where dark areas are the mask.
        threshold: The threshold to determine what is considered "dark" in the mask.

    Returns:
        A 2D numpy array with the mask applied.
    """
    # Where the mask is dark (below threshold), set the pixel to white (1.0).
    # Otherwise, keep the original stipple pattern.
    masked_image = np.where(mask_img < threshold, 1.0, stipple_img)
    return masked_image
