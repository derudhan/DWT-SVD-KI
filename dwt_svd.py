import cv2
import numpy as np
import pywt
import histogram


class DWT_SVD_Watermarking:
    def embed(self, cover, wm):
        # path = input("Enter the path of the watermark: ")
        path = wm
        img = cv2.imread(path, 0)
        cv2.imwrite("output/watermark.jpg", img)
        histogram.get_histogram("output/watermark.jpg", "histogram/watermark.jpg")

        # DWT
        hpath = cover
        img = cv2.imread(hpath, 0)
        histogram.get_histogram(hpath, "histogram/host_image_watermark.jpg")

        Coefficients = pywt.wavedec2(img, wavelet="haar", level=1)
        shape_LL = Coefficients[0].shape

        # SVD
        Uc, Sc, Vc = np.linalg.svd(Coefficients[0], full_matrices=False)
        W = cv2.imread("output/watermark.jpg", 0)

        SLL = np.zeros(shape_LL)
        row = min(shape_LL)
        SLL[:row, :row] = np.diag(Sc)
        Sc = SLL

        # Resize
        wmResized = cv2.resize(W, (shape_LL[0], shape_LL[0]))

        # Watermarking
        alpha = 0.1
        Snew = np.zeros((min(shape_LL), min(shape_LL)))
        for py in range(0, min(shape_LL)):
            for px in range(0, min(shape_LL)):
                Snew[py][px] = Sc[py][px] + alpha * wmResized[py][px]
        np.save("data/Snew.npy", Snew)

        # SVD lagi
        Uw, Sw, Vw = np.linalg.svd(Snew, full_matrices=False)

        LLnew = np.zeros((min(SLL.shape), min(SLL.shape)))
        LLnew = Uc.dot(np.diag(Sw)).dot(Vc)

        Coefficients[0] = LLnew
        i = pywt.waverec2(Coefficients, "haar")
        cv2.imwrite("output/watermarked_image.jpg", i)
        histogram.get_histogram(
            "output/watermarked_image.jpg", "histogram/watermarked_image.jpg"
        )

        return "output/watermarked_image.jpg"

    def extract(self, wm, data):
        Snew = np.load(data)
        path2 = wm
        wimg = cv2.imread(path2, 0)

        # DWT
        Cw = pywt.wavedec2(wimg, wavelet="haar", level=1)
        Cw[0] = cv2.resize(Cw[0], Snew.shape)
        shape_LL = Cw[0].shape  # C[0] is LL

        # SVD
        Ucw, Scw, Vcw = np.linalg.svd(Cw[0], full_matrices=False)

        Ud, Sd, Vd = np.linalg.svd(Snew, full_matrices=False)
        LLnew1 = Ud.dot(np.diag(Scw)).dot(Vd)

        Wdnew = np.zeros((min(shape_LL), min(shape_LL)))

        Scdiag = np.zeros(shape_LL)
        row = min(shape_LL)
        Scdiag[:row, :row] = np.diag(Scw)
        Scw = Scdiag

        alpha = 0.1
        for py in range(0, min(shape_LL)):
            for px in range(0, min(shape_LL)):
                Wdnew[py][px] = (LLnew1[py][px] - Scw[py][px]) / alpha

        cv2.imwrite("output/recovered_watermark.jpg", Wdnew)
        histogram.get_histogram(
            "output/recovered_watermark.jpg", "histogram/recovered_watermark.jpg"
        )
        return "output/recovered_watermark.jpg"
