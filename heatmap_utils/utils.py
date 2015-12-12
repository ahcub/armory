import heatmap
import numpy as np
from PIL import Image


if __name__ == "__main__":
    pts = np.genfromtxt(r'D:\GitHub\armory\heatmap_utils\data_sample\coordinates_data\Capture.csv', delimiter=',')

    # for x in range(400):
    #
    #     random_ = (random.randint(0, 600), random.randint(0, 400))
    #     print(random_)
    #     pts.append(random_)

    img2 = Image.open(r"D:\GitHub\armory\heatmap_utils\data_sample\images\Capture.PNG")


    print "Processing %d points..." % len(pts)

    hm = heatmap.Heatmap()
    img = hm.heatmap(pts, size=img2.size, area=((0, 0), img2.size))
    heat_map_file_path = r"D:\GitHub\armory\heatmap_utils\data_sample\out_folder\heatmaps\Capture.png"
    img.save(heat_map_file_path)
    # img2 = cv2.imdecode(np.array(img.tobytes()), -1)

    print(img.size)
    print(img2.size)
    result = Image.alpha_composite(img2, img)
    # background.paste(img, (0, 0), img)
    result.show()

    # print(dir(img))
    # print(dir(img2))

    # s_img = cv2.imread("smaller_image.png", -1)
    # for c in range(0,3):
    #     l_img[:s_img.shape[0], :s_img.shape[1], c] =
    #     s_img[:,:,c] * (s_img[:,:,3]/255.0) +  l_img[:s_img.shape[0], :s_img.shape[1], c] * (1.0 - s_img[:,:,3]/255.0)
