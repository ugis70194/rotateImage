from PIL import Image
import sys

def addMargin(img):
    width, height = img.size
    left = width // 5
    top = height // 5
    newWidth = width + left*2
    newHeight = height + top*2

    addedMargin = Image.new(img.mode, (newWidth, newHeight), (0, 0, 0))
    addedMargin.paste(img, (left, top))

    return addedMargin

def rotateImage(img, deg, num, dirPath, fileName, ext, qty):
    if num > qty: return 

    rotated = img.rotate(deg)
    rotated.save(str(dirPath) + str(fileName) + str(num) + str(ext))

    rotateImage(rotated, deg / 2, 2*num, dirPath, fileName, ext, qty)
    rotateImage(rotated, -deg / 2, 2*num + 1, dirPath, fileName, ext, qty)

def main():
    args = sys.argv

    if len(args) < 3 :
        print('Insufficient arguments', file=sys.stderr)
        return 

    dirPath = str(args[1])
    fileName = str(args[2])
    ext = fileName[-4:]
    qty = int(args[3])
    fileName = fileName[-len(fileName):-4:1]

    img = Image.open(str(dirPath) + str(fileName) + str(ext))
    img = addMargin(img)

    rotateImage(img, 180, 1, dirPath, fileName, ext, qty)

main()
