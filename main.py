from mapOper import *


if __name__ == "__main__":
    kawaraMap = creatingMap()
    kawaraMap.save("output/kawaraMap.html")
    print('done')