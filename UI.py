import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

import dwt_svd

watermarking = dwt_svd.DWT_SVD_Watermarking()


class APP:
    def __init__(self, root):
        self.root = root
        self.root.title("DWT-SVD Watermarking")

        self.cover_image = None
        self.watermark_image = None
        self.data_watermarked = None
        self.watermarked_image = None

        self.initUI()

    def initUI(self):
        self.container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.container.pack(expand=True)
        self.clabel = ctk.CTkLabel(
            self.container, text="DWT-SVD Watermarking", font=("Arial", 24)
        )
        self.clabel.grid(row=0, column=1, columnspan=2, padx=10, pady=20)

        self.frame1 = ctk.CTkFrame(self.container, border_width=2)
        self.frame1.grid(row=1, column=1, padx=50, pady=50)

        self.title_label = ctk.CTkLabel(self.frame1, text="Embed", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        self.load_cover_btn = ctk.CTkButton(
            self.frame1,
            text="Load Cover Image",
            command=self.load_cover_image,
        )
        self.load_cover_btn.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.load_watermark_btn = ctk.CTkButton(
            self.frame1, text="Load Watermark", command=self.load_watermark_image
        )
        self.load_watermark_btn.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.embed_btn = ctk.CTkButton(self.frame1, text="Start", command=self.embed)
        self.embed_btn.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.frame2 = ctk.CTkFrame(self.container, border_width=2)
        self.frame2.grid(row=1, column=2, padx=50, pady=50)

        self.title_label2 = ctk.CTkLabel(
            self.frame2, text="Extract", font=("Arial", 24)
        )
        self.title_label2.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        self.load_cover_btn2 = ctk.CTkButton(
            self.frame2,
            text="Load Watermarked",
            command=self.load_watermarked_image,
        )
        self.load_cover_btn2.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.load_watermark_btn2 = ctk.CTkButton(
            self.frame2, text="Load Data", command=self.load_data
        )
        self.load_watermark_btn2.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.embed_btn2 = ctk.CTkButton(self.frame2, text="Start", command=self.extract)
        self.embed_btn2.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            ipadx=5,
            ipady=5,
        )

        self.frame3 = ctk.CTkFrame(self.container, border_width=2)
        self.frame3.grid(row=2, column=1, columnspan=2, padx=50, pady=50)
        self.image_label = ctk.CTkLabel(self.frame3, text="Display", font=("Arial", 24))
        self.image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def load_cover_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        if file_path:
            self.cover_image = file_path
            self.display_image(self.cover_image)

    def load_watermark_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        if file_path:
            self.watermark_image = file_path
            self.display_image(self.watermark_image)

    def load_watermarked_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
        )
        if file_path:
            self.watermarked_image = file_path
            self.display_image(self.watermarked_image)

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("npy files", "*.npy")])
        if file_path:
            self.data_watermarked = file_path
            self.image_label.configure(text="Data Berhasil Dimuat", image=None)
            self.image_label.image = None

    def display_image(self, img):
        img = cv2.imread(img)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)

        # Resize the image to fit within the frame
        img_pil = img_pil.resize(
            (600, 400), Image.Resampling.LANCZOS
        )  # Adjust size as needed

        img_tk = ImageTk.PhotoImage(img_pil)
        self.image_label.configure(
            image=img_tk, text=""
        )  # Use 'configure' instead of 'config'
        self.image_label.image = img_tk  # Keep a reference to avoid garbage collection

    def embed(self):
        if self.cover_image is None or self.watermark_image is None:
            messagebox.showerror("Error", "Tolong unggah gambar asli dan watermarknya.")
            return

        watermarked_image = watermarking.embed(self.cover_image, self.watermark_image)
        self.display_image(watermarked_image)
        watermarked_image = cv2.imread(watermarked_image)
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")],
        )
        if save_path:
            cv2.imwrite(save_path, watermarked_image)
            messagebox.showinfo(
                "Berhasil",
                "Watermark tersisipi. Data untuk Ekstraksi dapat dilihat di folder data",
            )

    def extract(self):
        if self.watermarked_image is None or self.data_watermarked is None:
            messagebox.showerror(
                "Error", "Tolong unggah gambar watermarked dan datanya."
            )
            return

        extracted_image = watermarking.extract(
            self.watermarked_image, self.data_watermarked
        )
        self.display_image(extracted_image)
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")],
        )
        if save_path:
            cv2.imwrite(save_path, extracted_image)
            messagebox.showinfo(
                "Berhasil",
                "Watermarking berjalan dengan lancar. Cek di foldern output untuk melihat hasilnya",
            )


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("Template.json")

    root = ctk.CTk()
    root.geometry("1440x1080")  # Adjust window size as needed
    app = APP(root)
    root.mainloop()
