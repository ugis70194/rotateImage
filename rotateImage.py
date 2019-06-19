from PIL import Image
import sys, os, os.path

def addMargin(img, width, height):
    left = width // 4
    top = height // 4
    newWidth = width + left*2
    newHeight = height + top*2

    color = img.getpixel((0, 0))

    addedMargin = Image.new(img.mode, (newWidth, newHeight), color)
    addedMargin.paste(img, (left, top))

    return addedMargin

def rotateImage(img, deg, num, saveDirPath, fileName, ext, qty, width, height):
    if num > qty: return 

    left = width // 4
    top = height // 4

    rotated = img.rotate(deg)
    CropImg = rotated.crop((left,top,width+left,height+top));
    CropImg.save(saveDirPath + '/' + fileName + str(num) + ext)

    rotateImage(rotated, deg / 2, 2*num, saveDirPath, fileName, ext, qty, width, height)
    rotateImage(rotated, -deg / 2, 2*num + 1, saveDirPath, fileName, ext, qty, width, height)

def main():
    args = sys.argv

    if len(args) < 3 :
        print('Insufficient arguments', file=sys.stderr)
        return 

    dirPath = str(args[1])
    qty = int(args[2])

    saveDirPath = dirPath + '/rotated'
    if os.path.isdir(saveDirPath) == False:
        os.mkdir(saveDirPath)

    # 子ディレクトリを持つディレクトリの中身を走査する
    for root, dirs, files in os.walk(dirPath) :
        for dirName in dirs:
            for fileName in files:

                ext = fileName[-4:]
                if ext != '.jpg' and ext != '.png' :
                    break

                fileName = fileName[-len(fileName):-4:1]

                img = Image.open(dirPath + '/' + fileName + ext)
                width, height = img.size
                left = width // 4
                top = height // 4

                img = addMargin(img, width, height)

                CropImg = img.crop((left,top,width+left,height+top));
                CropImg.save(saveDirPath + '/' + fileName + ext)

                rotateImage(img, 180, 1, saveDirPath, fileName, ext, qty, width, height)

main()
