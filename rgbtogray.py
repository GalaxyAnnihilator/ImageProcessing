import os
import numpy as np
import cv2
import pytest

def rgb_to_gray(image):
    """
    Convert an RGB image to grayscale using this formula:
        Y = 0.299*R + 0.587*G + 0.114*B
    
    Args:
        image: np.array of shape (height,width,3) with RGB values

    Returns:
        gray: np.array of shape (height,width) with grayscale values

    
    """
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Input must be an RGB image")
    
    r,g,b = image[:,:,0], image[:,:,1], image[:,:,2]

    gray = 0.299*r + 0.587*g + 0.114*b

    return np.round(gray).astype(np.uint8)

# --- Tests ---
#Method 1: basic test with image pairs
def test_using_image_pairs(list_image_pairs):
    for rgb_img_path, gray_gt_image_path in list_image_pairs:
        rgb_img = cv2.imread(rgb_img_path)
        gray_gt_image = cv2.imread(gray_gt_image_path,cv2.IMREAD_GRAYSCALE) #expected outcome

        gray_result_img = rgb_to_gray(rgb_img) #actual outcome

        assert gray_result_img.shape == gray_gt_image.shape, f"Shape mismatch for {rgb_img_path}"

        max_diff = np.max(np.abs(gray_result_img.astype(np.int16)-gray_gt_image).astype(np.int16))

        assert max_diff <= 1, f"Max difference of {max_diff} exceeds threshold"

test_using_image_pairs([("./tiger.jpg","./tiger.jpg")])
            

    