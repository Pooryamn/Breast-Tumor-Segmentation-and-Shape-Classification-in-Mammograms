# Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms
Breast Tumor Segmentation and Shape Classification in Mammograms using Generative Adversarial and Convolutional Neural Network

# Abstract:
Mammogram inspection in search of breast tumors is a tough assignment that radiologists
must carry out frequently. Therefore, image analysis methods are needed for the
detection and delineation of breast tumors, which portray crucial morphological information
that will support reliable diagnosis. In this paper, we proposed a conditional
Generative Adversarial Network (cGAN) devised to segment a breast tumor within a
region of interest (ROI) in a mammogram. The generative network learns to recognize
the tumor area and to create the binary mask that outlines it. In turn, the adversarial
network learns to distinguish between real (ground truth) and synthetic segmentations,
thus enforcing the generative network to create binary masks as realistic as possible.
The cGAN works well even when the number of training samples are limited. As a
consequence, the proposed method outperforms several state-ofthe-art approaches. Our
working hypothesis is corroborated by diverse experiments performed on two datasets,
the public INbreast and a private in-house dataset. The proposed segmentation model
provides a high Dice coefficient and Intersection over Union (IoU) of 94% and 87%,
respectively. In addition, a shape descriptor based on a Convolutional Neural Network
(CNN) is proposed to classify the generated masks into four tumor shapes: irregular,
lobular, oval and round. The proposed shape descriptor was trained on Digital
Database for Screening Mammography (DDSM) yielding an overall accuracy of 80%,
which outperforms the current state-of-the-art.

## Keywords: 
Mammograms, conditional generative adversarial network, convolutional
neural network, tumor segmentation and shape classification.

## Figures:
![[alt text]([https://github.com/Pooryamn/Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms/blob/master/Fig1.png])

![[alt text]([https://github.com/Pooryamn/Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms/blob/master/Fig2.png])

![[alt text]([https://github.com/Pooryamn/Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms/blob/master/Fig3.png])

![[alt text]([https://github.com/Pooryamn/Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms/blob/master/Fig4.png])

![[alt text]([https://github.com/Pooryamn/Breast-Tumor-Segmentation-and-Shape-Classification-in-Mammograms/blob/master/Fig5.png])
