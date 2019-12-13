#!/usr/bin/python3

import sys
import os
import numpy as np
from PIL import Image

input_file = sys.argv[1]
output = sys.argv[2]

im = Image.open(input_file)
np_im = np.array(im)


def group1():
  imgs_comb = np.hstack((np_im, ) * 7)

  return imgs_comb


def group2():
  empty_img = np.zeros(np_im.shape, dtype=np.uint8)
  empty_img.fill(255)

  im_list = []

  for i in range(7):
    if i%2 == 0:
      im_list.append(np_im)
    else:
      im_list.append(empty_img)

  imgs_comb_1 = np.hstack(im_list)

  im_list = []

  for i in range(7):
    if i%2 == 1:
      im_list.append(np_im)
    else:
      im_list.append(empty_img)

  imgs_comb_2 = np.hstack(im_list)
  imgs_comb_2 = np.flipud(imgs_comb_2)

  imgs_comb = np.vstack((imgs_comb_1, imgs_comb_2))

  return imgs_comb


def group3_base():
  im_flip = np.fliplr(np_im)
  imgs_comb = np.hstack([im_flip, np_im])

  return imgs_comb


def group3():
  im_base = group3_base()
  im_list = []

  for _ in range(4):
    im_list.append(im_base)

  imgs_comb = np.hstack(im_list)

  return imgs_comb


def group4():
  imgs_comb_1 = group1()
  imgs_comb_2 = np.flipud(imgs_comb_1)

  imgs_comb = np.vstack((imgs_comb_1, imgs_comb_2))

  return imgs_comb


def group5():
  empty_img = np.zeros(np_im.shape, dtype=np.uint8)
  empty_img.fill(255)

  im_list = []

  for i in range(8):
    if i%2 == 0:
      im_list.append(np_im)
    else:
      im_list.append(empty_img)

  imgs_comb_1 = np.hstack(im_list)

  im_flip = np.flipud(np.fliplr(np_im))
  im_list = []

  for i in range(8):
    if i%2 == 1:
      im_list.append(im_flip)
    else:
      im_list.append(empty_img)

  imgs_comb_2 = np.hstack(im_list)

  imgs_comb = np.vstack((imgs_comb_1, imgs_comb_2))

  return imgs_comb


def group6():
  im_base = group3_base()

  empty_img = np.zeros(im_base.shape, dtype=np.uint8)
  empty_img.fill(255)

  im_list = []

  for i in range(4):
    if i%2 == 0:
      im_list.append(im_base)
    else:
      im_list.append(empty_img)

  imgs_comb_1 = np.hstack(im_list)

  im_list = []

  for i in range(4):
    if i%2 == 1:
      im_list.append(im_base)
    else:
      im_list.append(empty_img)

  imgs_comb_2 = np.flipud(np.hstack(im_list))

  imgs_comb = np.vstack((imgs_comb_1, imgs_comb_2))

  return imgs_comb


def group7():
  im_base = group3_base()

  im_list = []

  for _ in range(4):
    im_list.append(im_base)

  imgs_comb_1 = np.hstack(im_list)
  imgs_comb_2 = np.flipud(np.hstack(im_list))

  imgs_comb = np.vstack((imgs_comb_1, imgs_comb_2))

  return imgs_comb


def generate():
  groups = [group1(), group2(), group3(), group4(), group5(), group6(), group7()]

  for i in range(len(groups)):
    new_im = Image.fromarray(groups[i])
    new_im.save(os.path.join(output,"friso" + str(i + 1) + ".png"))

generate()