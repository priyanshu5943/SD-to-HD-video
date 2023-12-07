# Swin2SR 

## [Swin2SR: for video resolution mp4 to HD]


[ <a href="https://colab.research.google.com/drive/1luTg43OPI5tasPoac2J99kIDwcXCjO7s?usp=sharinghttps://colab.research.google.com/drive/1luTg43OPI5tasPoac2J99kIDwcXCjO7s?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>](https://colab.research.google.com/drive/1luTg43OPI5tasPoac2J99kIDwcXCjO7s?usp=sharing )




<br>



------------------



<p align="center">
  <img src="examples/swin2sr.png" alt="swin2sr" width="800" border="0"></a>
</p>

> Compression plays an important role on the efficient transmission and storage of images and videos through band-limited systems such as streaming services, virtual reality or videogames. However, compression unavoidably leads to artifacts and the loss of the original information, which may severely degrade the visual quality. For these reasons, quality enhancement of compressed images has become a popular research topic. While most state-of-the-art image restoration methods are based on convolutional neural networks, other transformers-based methods such as SwinIR, show impressive performance on these tasks.
In this paper, we explore the novel Swin Transformer V2, to improve SwinIR for image super-resolution, and in particular, the compressed input scenario. Using this method we can tackle the major issues in training transformer vision models, such as training instability, resolution gaps between pre-training and fine-tuning, and hunger on data. We conduct experiments on three representative tasks: JPEG compression artifacts removal, image super-resolution (classical and lightweight), and compressed image super-resolution. Experimental results demonstrate that our method, Swin2SR, can improve the training convergence and performance of SwinIR, and is a top-5 solution at the "AIM 2022 Challenge on Super-Resolution of Compressed Image and Video". 



---------------------------------------------------






## Results

SWINS2R model has achieved state-of-the-art performance on classical, lightweight and real-world video Super-Resolution (SR), JPEG compression artifact reduction, and compressed input super-resolution. it  use mainly the DIV2K Dataset and Flickr2K datasets for training, and for testing:  RealSRSet, 5images/Classic5/Set5, Set14, BSD100, Urban100 and Manga109  


<br>

|Compressed inputs | Swin2SR output|
|       :---       |     :---:     |
| <img src="examples/gorillabefore.png" alt="frog_in" width="300" border="0"> | <img src="examples/gorillaafter.png" alt="frog_swin2sr" width="300" border="0"> |
| <img src="examples/tokyo.jpg" alt="div2k_in" width="300" border="0"> | <img src="examples/enhancedtokyo.png" alt="div2k_swin2sr" width="300" border="0"> |
| <img src="examples/buildings_0.png" alt="buildings_in" width="300" border="0"> | <img src="examples/buildings_1.png" alt="buildings_swin2sr" width="300" border="0"> |
| <img src="examples/cheetabefore.jpg" alt="buildings_in" width="300" border="0"> | <img src="examples/cheetaafter.png" alt="buildings_swin2sr" width="300" border="0"> |





### Basic inference setup


1. clone the repositery      

```
! git clone https://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@github.com/priyanshu5943/SD-to-HD-video.git

```

2. Make image sequences out of videos  the model expects low quality and will then convert these images to enhnaced ones.
#### The general code is      !python make_image_sequence.py --file_path copy_the_path_of_video

```
! python make_image_sequence.py --file_path /content/videotovideoimage/tokyo.mp4

```


3.  install timm which is deep-learning library created by Ross Wightman and is a collection of SOTA computer vision models, layers, utilities, optimizers, schedulers, data-loaders, augmentations and also training/validating scripts with ability to reproduce ImageNet training results.

```
! pip install timm
```

3. run the model using `main_test_swin2sr.py` and `--save_img_only`. 


4. we process the images in `real-inputs` and the outputs are stored in `results/swin2sr_{TASK}_x{SCALE}` where TASK and SCALE are the selected options. You can just navigate through `results/`

the general code is this 

#### ! python main_test_swin2sr.py --task compressed_sr --scale 4 --training_patch_size 48 --model_path model_zoo/swin2sr/Swin2SR_CompressedSR_X4_48.pth --folder_lq path_of_image_sequences --save_img_only



```
! python main_test_swin2sr.py --task compressed_sr --scale 4 --training_patch_size 48 --model_path model_zoo/swin2sr/Swin2SR_CompressedSR_X4_48.pth --folder_lq /content/SD-to-HD-video/testsets/real-inputs --save_img_only

```

5. We convert back the enhanced images sequences again into video frame by frame.

the general code is this 

#### python make_video.py HD_image_sequence_path     original_video_path   Provide_Enhanced_video_name


```
! python make_video.py /content/SD-to-HD-video/results/swin2sr_compressed_sr_x4    /content/SD-to-HD-video/tokyo.mp4    enhancedtokyo.mp4

```

------

