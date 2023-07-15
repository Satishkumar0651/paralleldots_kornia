import cv2
import kornia as K
import kornia.feature as KF
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import torch
from kornia_moons.viz import draw_LAF_matches
import kornia.geometry as KG
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import os

def matchimage_save_output(fname1,fname2):
    # Save image files to temporary files
    filename1 = secure_filename(fname1.filename)
    temp_filepath1 = os.path.join('/tmp', filename1)
    fname1.save(temp_filepath1)

    filename2 = secure_filename(fname2.filename)
    temp_filepath2 = os.path.join('/tmp', filename2)
    fname2.save(temp_filepath2)

    img1 = K.io.load_image(temp_filepath1, K.io.ImageLoadType.RGB32)[None, ...]
    img2 = K.io.load_image(temp_filepath2, K.io.ImageLoadType.RGB32)[None, ...]

    img1 = K.geometry.resize(img1, (600, 375), antialias=True)
    img2 = K.geometry.resize(img2, (600, 375), antialias=True)


    matcher = KF.LoFTR(pretrained="outdoor")

    input_dict = {
        "image0": K.color.rgb_to_grayscale(img1),  # LofTR works on grayscale images only
        "image1": K.color.rgb_to_grayscale(img2),
    }

    with torch.inference_mode():
        correspondences = matcher(input_dict)
    mkpts0 = correspondences["keypoints0"].cpu().numpy()
    mkpts1 = correspondences["keypoints1"].cpu().numpy()
    Fm, inliers = cv2.findFundamentalMat(mkpts0, mkpts1, cv2.USAC_MAGSAC, 0.5, 0.999, 100000)
    inliers = inliers > 0
    image_matches = draw_LAF_matches(
        KF.laf_from_center_scale_ori(
            torch.from_numpy(mkpts0).view(1, -1, 2),
            torch.ones(mkpts0.shape[0]).view(1, -1, 1, 1),
            torch.ones(mkpts0.shape[0]).view(1, -1, 1),
        ),
        KF.laf_from_center_scale_ori(
            torch.from_numpy(mkpts1).view(1, -1, 2),
            torch.ones(mkpts1.shape[0]).view(1, -1, 1, 1),
            torch.ones(mkpts1.shape[0]).view(1, -1, 1),
        ),
        torch.arange(mkpts0.shape[0]).view(-1, 1).repeat(1, 2),
        K.tensor_to_image(img1),
        K.tensor_to_image(img2),
        inliers,
        draw_dict={"inlier_color": (0.2, 1, 0.2), "tentative_color": None, "feature_color": (0.2, 0.5, 1), "vertical": False},
    )
    result_path = os.path.join('/tmp', 'result1.png')
    plt.savefig(result_path)
    return result_path