import rawpy
import imageio
import os

inPrefix = "/Volumes/Shared/photogrammetry/shoot2/DSC_"
inExt = ".NEF"

outDir = "/Volumes/Shared/photogrammetry/shoot2tif/"
os.makedirs(outDir, exist_ok=True);
outPrefix = outDir+"DSC_"
outExt = ".tiff"
for i in range(203, 408):
    print("Processing "+str(i));
    num = '{0:04d}'.format(i)
    name = inPrefix + num + inExt
    with rawpy.imread(name) as raw:
        rgb = raw.postprocess(output_bps=16)
        imageio.imsave(outPrefix+num+outExt, rgb)
