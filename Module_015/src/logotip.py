# ============================================================================

# Coding            : utf-8

# Script Name	    : Написание примитивной ORM
# File              : module_14_*.py

# Author			: Sergey Romanov
# Created			: 01.10.2024
# Last Modified	    : 01.10.2024
# Version			: 1.0.001

# Modifications	:
# Modifications	: 1.0.1 - Tidy up the comments and syntax

# Description       : aiogram script
# Description		: This will go through
#                     and backup all my automator services workflows

# ============================================================================

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = True

import cv2
import numpy as np

logo = np.zeros ( (400, 400, 3), dtype = 'uint8' )

cv2.circle (
    logo, (logo.shape [ 0 ] // 2, logo.shape [ 1 ] // 2), 150,
        (255, 255, 255),
    thickness = 3
    )

cv2.ellipse (
    logo, (logo.shape [ 0 ] // 2, logo.shape [ 1 ] // 2), (50, 50), 0, 0, 180,
    (40, 240, 80), thickness = 3
    )
cv2.ellipse (
    logo, (logo.shape [ 0 ] // 2, logo.shape [ 1 ] // 2), (25, 25), 0, 0, 180,
    (40, 240, 80), thickness = 3
    )

cv2.line (
    logo, (logo.shape [ 0 ] // 2 - 25, logo.shape [ 1 ] // 2),
    (logo.shape [ 0 ] // 2 - 25, logo.shape [ 1 ] // 2 - 50),
    (255, 0, 0), thickness = 3
    )
cv2.line (
    logo, (logo.shape [ 0 ] // 2 - 50, logo.shape [ 1 ] // 2),
    (logo.shape [ 0 ] // 2 - 50, logo.shape [ 1 ] // 2 - 50),
    (255, 0, 0), thickness = 3
    )
cv2.line (
    logo, (logo.shape [ 0 ] // 2 + 25, logo.shape [ 1 ] // 2),
    (logo.shape [ 0 ] // 2 + 25, logo.shape [ 1 ] // 2 - 50),
    (255, 0, 0), thickness = 3
    )
cv2.line (
    logo, (logo.shape [ 0 ] // 2 + 50, logo.shape [ 1 ] // 2),
    (logo.shape [ 0 ] // 2 + 50, logo.shape [ 1 ] // 2 - 50),
    (255, 0, 0), thickness = 3
    )
cv2.line (
    logo, (logo.shape [ 0 ] // 2 - 25, logo.shape [ 1 ] // 2 - 50),
    (logo.shape [ 0 ] // 2 - 50, logo.shape [ 1 ] // 2 - 50),
    (0, 0, 255), thickness = 3
    )
cv2.line (
    logo, (logo.shape [ 0 ] // 2 + 25, logo.shape [ 1 ] // 2 - 50),
    (logo.shape [ 0 ] // 2 + 50, logo.shape [ 1 ] // 2 - 50),
    (0, 0, 255), thickness = 3
    )

cv2.imshow ( 'Logo', logo )
cv2.waitKey ( 0 )
