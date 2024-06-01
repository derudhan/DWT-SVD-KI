clc
close all

%ori
image = imread("original\host.jpg");
watermark = imread("original/EWatermark.jpg");

% attacked image
compressed_image = imread('attacked/compressed_image.jpg');
cropped_image = imread('attacked/cropped_image.jpg');
filtered_image = imread('attacked/filtered_image.jpg');
noised_image = imread('attacked/noised_image.jpg');
object_image = imread('attacked/object_image.jpg');
resized_image = imread('attacked/resized_image.jpg');
rotated_image = imread('attacked/rotated_image.jpg');

% extracted image
compressed_watermark = imread('hasil/compressed_watermark.jpg');
cropped_watermark = imread('attacked/cropped_watermark.jpg');
filtered_watermark = imread('attacked/filtered_watermark.jpg');
noised_watermark = imread('attacked/noised_watermark.jpg');
object_watermark = imread('attacked/object_watermark.jpg');
resized_watermark = imread('attacked/resized_watermark.jpg');
rotated_watermark = imread('attacked/rotated_watermark.jpg');

% display 1
figure;
subplot(2, 2, 1);
imshow(image, []);
title('Watermarked Image');
subplot(2, 2, 2);
imshow(watermark, []);
title('Extracted Watermark');
subplot(2, 2, 3);
imshow(compressed_image, []);
title('Compressed Image');
subplot(2, 2, 4);
imshow(compressed_watermark, []);
title('Extracted Watermark');

% display 2
figure;
subplot(2, 2, 1);
imshow(cropped_image, []);
title('Cropped Image');
subplot(2, 2, 2);
imshow(cropped_watermark, []);
title('Extracted Watermark');
subplot(2, 2, 3);
imshow(filtered_image, []);
title('Filtered Image');
subplot(2, 2, 4);
imshow(filtered_watermark, []);
title('Extracted Watermark');

% display 3
figure;
subplot(2, 2, 1);
imshow(noised_image, []);
title('Noised Image');
subplot(2, 2, 2);
imshow(noised_watermark, []);
title('Extracted Watermark');
subplot(2, 2, 3);
imshow(object_image, []);
title('Objected Image');
subplot(2, 2, 4);
imshow(object_watermark, []);
title('Extracted Watermark');

% display 4
figure;
subplot(2, 2, 1);
imshow(resized_image, []);
title('Resized Image');
subplot(2, 2, 2);
imshow(resized_watermark, []);
title('Extracted Watermark');
subplot(2, 2, 3);
imshow(rotated_image, []);
title('Rotated Image');
subplot(2, 2, 4);
imshow(rotated_watermark, []);
title('Extracted Watermark');

% psnr
ref = imread("original/Watermarked.jpg");
psnr(ref, image)
immse(ref, image)