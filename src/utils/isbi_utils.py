import logging
import numpy as np
import tifffile as tiff

from src.utils.runtime import funcname


def isbi_get_data_montage(imgs_path, msks_path, nb_rows, nb_cols, rng):
    '''Reads the images and masks and arranges them in a montage for sampling in training.'''
    logger = logging.getLogger(funcname())
    imgs = tiff.imread('%s/0.tif'%imgs_path)
    imgs = imgs.transpose(2,0,1)
    for i in range(1,25):
        im = tiff.imread('%s/%d.tif'%(imgs_path,i))
        im = im.transpose(2,0,1)
        imgs = np.concatenate((imgs,im),axis=0)
        # print(imgs.shape)
    msks = tiff.imread('%s/0.tif'%msks_path)
    msks = msks.transpose(2,0,1)
    for i in range(1,25):
        ms = tiff.imread('%s/%d.tif'%(msks_path,i))
        ms = ms.transpose(2,0,1)
        msks = np.concatenate((msks,ms),axis=0)
        # print(msks.shape)
    msks = msks / 255

    # imgs, msks = tiff.imread(imgs_path), tiff.imread(msks_path) / 255
    montage_imgs = np.empty((nb_rows * imgs.shape[1], nb_cols * imgs.shape[2]), dtype=np.float32)
    montage_msks = np.empty((nb_rows * imgs.shape[1], nb_cols * imgs.shape[2]), dtype=np.int8)

    idxs = np.arange(imgs.shape[0])
    rng.shuffle(idxs)
    idxs = iter(idxs)

    for y0 in range(0, montage_imgs.shape[0], imgs.shape[1]):
        for x0 in range(0, montage_imgs.shape[1], imgs.shape[2]):
            y1, x1 = y0 + imgs.shape[1], x0 + imgs.shape[2]
            idx = next(idxs)
            montage_imgs[y0:y1, x0:x1] = imgs[idx]
            montage_msks[y0:y1, x0:x1] = msks[idx]

    return montage_imgs, montage_msks
