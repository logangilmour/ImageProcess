import skimage
import imageio
import os

inDir = "E:\\photogrammetry\\calibration2\\"
inPrefix = "DSC_"
inExt = ".tiff"

outDir = "E:\\photogrammetry\\calibration2BW\\"
os.makedirs(outDir, exist_ok=True)
outPrefix = outDir+"DSC_"
outExt = ".tiff"
for i in range(214, 247):
    print("Processing "+str(i))
    num = '{0:04d}'.format(i)
    name = inDir+inPrefix + num + inExt
    im = imageio.imread(name)
    imgray = skimage.color.rgb2gray(im)
    imageio.imsave(outPrefix+num+outExt, skimage.img_as_uint(imgray))
