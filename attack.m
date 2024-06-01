clc
close all

watermarked_image = imread('Watermarked.jpg');
[cols, rows, channel, ~] = size(watermarked_image);

% crop
cropImageAttacked = imcrop(watermarked_image, [75 68 340 380]);
cropImageAttacked = imresize(cropImageAttacked, [cols rows]);
imwrite(uint8(cropImageAttacked), 'attacked/cropped_image.jpg');

% filter
filterImageAttacked = imfilter(watermarked_image, fspecial('motion', 50, 45));
imwrite(uint8(filterImageAttacked), 'attacked/filtered_image.jpg');

% noise
noiseImageAttacked = imnoise(watermarked_image, "salt & pepper", 0.1);
imwrite(uint8(noiseImageAttacked), 'attacked/noised_image.jpg');

% compress
compressImageAttacked = imresize(watermarked_image, 0.4, 'nearest');
compressImageAttacked = imresize(compressImageAttacked, [cols rows]);
imwrite(uint8(compressImageAttacked), 'attacked/compressed_image.jpg');

% resize
resizeImageAttacked = imresize(watermarked_image, [cols-200 rows-200]);
imwrite(uint8(resizeImageAttacked), 'attacked/resized_image.jpg');

% add object (manual)

% rotate
rotateImageAttacked = imrotate(watermarked_image, 30, 'crop');
imwrite(uint8(rotateImageAttacked), 'attacked/rotated_image.jpg');