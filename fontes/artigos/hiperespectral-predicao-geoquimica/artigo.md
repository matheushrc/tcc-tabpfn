---
title: "Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement"
source: "https://doi.org/10.1080/08120099.2022.2094465"
retrieved_from: "https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465"
archived_at: "2026-10-09"
format: "Markdown"
---

A. Kutzke, H. Eichstaedt & R. Kahnt

## Abstract

This paper summarises an evaluation of the application of artificial intelligence to hyperspectral drill-core scans for more effective mineral exploration. The dataset used was based on publicly available core scans and related geochemical analysis from Australia. Prior to unification, a detailed quality assessment of the geochemical data was undertaken. Special focus was paid to gold, silver, copper, iron, uranium, nickel, lead, tin, antimony, arsenic and bismuth contents. The dataset was labelled with defined ore grades related to economic cutoff values. The impact on predictions of different setups is related to the amounts of data used for learning, data design and implementation of the geological domains. Based on 1-metre bins, the results from more than 700 km of drill cores were used and analysed with the potential for geological exploration in different scenarios discussed. The results indicate the enormous potential of the use of hyperspectral scans in combination with artificial intelligence for the development of exploration scenarios and to provide support for exploration geologists and target detection. The application of predictors on scanned drill cores from Australia also indicates mineralised zones that have not been analysed chemically for all metals above economic cutoffs. This result shows the enormous potential of the approach for strategic exploration but also mining operations. Prediction of geochemical concentrations for gold, copper and iron based on a neural network in drill cores is possible. Using mineral abundances from hyperspectral core scans as learning records, and existing elemental geochemical analyses as labels, the predictions are given with an accuracy of better than 80–90%.

### KEY POINTS
- The trained artificial intelligence system has for the first time enabled direct estimation of metal grades from hyperspectral scans.
- It also shows potential for applications to analyse airborne hyperspectral data for direct mapping of metal grades.
- Finally, it may pave the way for better plant management by the usage of hyperspectral data for direct grade estimations in operational mining and ore sorting.

## Keywords
- [exploration](https://www.tandfonline.com/keyword/exploration)
- [drill core](https://www.tandfonline.com/keyword/drill+core)
- [hyperspectral](https://www.tandfonline.com/keyword/hyperspectral)
- [core scan](https://www.tandfonline.com/keyword/core+scan)
- [artificial intelligence](https://www.tandfonline.com/keyword/artificial+intelligence)
- [neural network](https://www.tandfonline.com/keyword/neural+network)
- [metals](https://www.tandfonline.com/keyword/metals)

[Previous article](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2076741) [View issue table of contents](https://www.tandfonline.com/toc/taje20/69/8?nav=tocList) [Next article](https://www.tandfonline.com/doi/full/10.1080/08120099.2023.2126007)

## Introduction

This study evaluates the potential of a specially designed neural network for the prediction of geochemical properties in drill cores based on hyperspectral core scans. The importance of different parameters to the training of the neural network is assessed for the prediction of geochemical properties. The evaluation is set to support the implementation on multi-dimensional prediction methods of artificial intelligence for supporting operational and strategic tasks in geological exploration using hyperspectral drill-core information.

### Motivation

In an exploration scenario, mapping of minerals using hyperspectral scans of drill cores, on the one hand, and geochemical analysis of sampled core segments, on the other hand, are two tools for geologists to identify areas with higher grades of targeted ore, and alteration and mineralisation zones (Moon *et al*., [2006](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0022)). Arne ([2014](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0002)), Lampinen *et al*. ([2016](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0020)) and Sun *et al*. ([2019](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0029)) demonstrated the relationship of minerals mapped via hyperspectral analysis and geochemical assays to describe geological settings. Typically, owing to high costs, geologists select the locations of geochemical analysis is limited and may be biased by their knowledge and experience; reduced geochemical sampling might lead to relevant segments of core being overlooked in the design of the exploration model. The specially designed neural network can bridge this gap between complete core information from hyperspectral scanning and the incomplete geochemical information. The evaluation of different setups provides an understanding of the impact of different implementation parameters on the results and therefore the usability of the workflow in geological exploration.

### Literature review and theoretical background

Improvements in knowledge of geology have developed differently over the decades. While the documenting of geological properties in field studies still plays a major role, the application of new geophysical and spectral investigation methods combined with the implementation of computational and mathematical fundamental knowledge behind geological theories is rapidly increasing (Dramsch, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0009)). Machine automation has become an important tool to enhance geological understanding, especially in geophysics. Modern deep learning hardware and methods combined with the availability of big data in geological archives has opened new opportunities for analysing complex datasets (Geng, [2016](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0015); Karpatne *et al*., [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0018)). Kulesza *et al.* ([2014](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0019)) and Roh *et al.* ([2018](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0027)) highlighted the importance of structuring data for artificial intelligence and labelling. Grade of ore, geophysical well-log properties and sharp fault detection on seismic images are examples of successful labelling in geological applications. Caté *et al.* ([2017](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0007)) used machine-learning algorithms connecting petrophysical properties with gold-bearing intervals to improve the selection of gold intervals for assay sampling. Acosta *et al.* ([2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0001)) integrated hyperspectral and geochemical data via a superpixel-based machine-learning classification that gave a model improvement of 20% in the accuracy of results against an individuals analysis of the datasets on the pixel.

Rodger and Laukamp ([2021](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0026)) developed an approach using hyperspectral data to predict geochemical quantities using a trained workflow consisting of a non-negative matrix function step for data reduction and a random forest regression with an accuracy for predictions of up to 0.96 for *R*<sup>2</sup>. Their method was based on the use of reflectance spectra between 400 and 25 000 nm. In a different approach, Eichstaedt *et al.* ([2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0011)) used airborne spectral data from a specially designed test field with controlled coverage of clay containing target materials to derive quantitative estimations. Fouedjio *et al.* ([2018](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0014)) highlighted the possibilities of geostatistical methods to keep spatial relations between drill holes as part of geological domain definitions coupled with geochemical measurements.

The methodological research on convolutional neural networks and the minimum requirements and best setups to achieve learning vary widely and reflect problems in the preparation of suitable datasets (Du *et al.*, [2018](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0010)). The increase in sample numbers is important for increased accuracies of the network predictions. The design, as well as the strategies applied to the conditioning of the datasets, is of major importance for the performance of the neural networks (Bao, [2019](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0005); Neyshabur *et al.*, [2017](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0023)).

The following evaluation is focused on the potential impact of using a convolutional neural network with mineral abundances derived from hyperspectral data, and the stability of the results. The network architecture is described in detail in Eichstaedt *et al.* ([2022](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0012)). This paper focusses on the performance of different methods for the evaluation of drill-core scans.

## Geological context and data

Australia has a rich history of research in geological and ore-forming processes, and exploration has led to expertise in many mineral and metal commodities. The Australian continent is prospective for bauxite (aluminium ore), iron ore, lithium, gold, lead, diamonds, rare earth elements, uranium, zinc, manganese, antimony, nickel, silver, cobalt, copper and tin from over 350 operating mines (Geoscience Australia, [2021](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0004); Jaques *et al.*, [2002](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0017)). The intense exploration programs by the well-established mining industry and Australian State and Territories government agencies have cumulated in more than 3.2 million drill holes with thousands hyperspectrally scanned under the framework of the AuScope National Virtual Core Library (AuScope, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0003)). Approximately 70 million records of geochemical analyses are available to the public by individual states websites and geological surveys.

### Material

To train a specialised neural network, hyperspectral drill-core data collected by means of HyLogger (Schodlok *et al.*, [2016](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0028)) and the mineralogical interpretations derived from the hyperspectral data using matching algorithms, such as The Spectral Assistant (Berman *et al.*, [2017](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0006)), were collected from AuScope and Australian State and Territories. The acquired data were processed with The Spectral Geologist (TSG<sup>®</sup>) software provided by Commonwealth Scientific Industrial Research Organisation (CSIRO). We used pre-interpreted spectral analyses of minerals in the visible and infrared, short-wave infrared and thermal longwave bands (VNIR/SWIR/TIR) (Green, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0016); Leybourne *et al.*, [2013](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0021)). Mineral species were used for the development of the neural network. The NVCL and CSIRO studies have shown that the accuracy of The Spectral Assistant (TSA) at the mineral species level is lower than the results at the mineral group level (Laukamp, personal communication). Data were captured as relative abundances in percentage per 1-metre intervals from over 2700 drill holes with depth ranges between 60 and 4400 m. TSA, which is a general unmixing algorithm, was used to identify selected minerals and calculate abundances for SWIR and TIR in 1-metre intervals. These abundances for each spectrum are calculated proportions of the library spectra required to best fit the measured spectrum. In this study, SWIR and TIR responses were matched to mineral libraries using the scalar information of system TSA (sTSAT)-based spectral reflectance measurements (Green, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0016); Schodlok *et al.*, [2016](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0028)). The SWIR wavelength only identifies hydrous silicates and carbonates. Since 2017, the TSA interpretation for the TIR, the sTSAT, has been progressively replaced by the joint Constrained Least Squares (jCLST) algorithms, another unmixing classifier (Green, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0016)). jCLST interprets the TIR data using the results from the SWIR spectra and scalars focused on selected features in the visible near infrared (VNIR) and TIR wavelengths (Green, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0016)). Up to December 2021, a total of 2709 drill holes with 927 206 m sampling were collected for SWIR, and 876 857 m for TIR.

For the development of the neural network, geochemical assays of the elements, gold, silver, copper, iron, uranium, nickel, lead, tin, antimony, arsenic and bismuth were extracted. Of the 70 million geochemical records, 110 000 were matched with 703 250 one-metre intervals of the TIR/SWIR hyperspectral measurements and used for development, training and evaluation of the neural network. In the geochemical samples, same-depth intervals of the hyperspectral 1-metre bins were rounded to the majority covered by the spectral bin. Geochemical samples cover a 2-metre segment of core, so the geochemical record was duplicated for both covered hyperspectral bins.

## Methodology

The geochemical dataset for the neural network was labelled based on threshold limits given in [Table 1](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0003). The thresholds for the classes focused on typical values for exploration and additionally on the requirements for balancing the data amounts to ensure a good performance of neural networks. For the evaluation, two, three and four ore-grade classes were implemented, starting on top grades. Above and below the threshold, the same amount of data has been randomly sampled to achieve a balanced learning data pool.

**Table 1. Overview of accuracies achieved in a two-class learning approach with the neural network based on the 20% test dataset.**

<table>
  <thead>
    <tr>
      <th>Element</th>
      <th>Threshold equals or above</th>
      <th>Training samples above threshold</th>
      <th>Accuracy of prediction based on confusion matrix 20% test dataset percentage correct allocated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ag</td>
      <td>0.5 ppm</td>
      <td>21 400</td>
      <td>80.95</td>
    </tr>
    <tr>
      <td rowspan="2">Au</td>
      <td>0.17 ppm</td>
      <td>16 245</td>
      <td>81.86</td>
    </tr>
    <tr>
      <td>0.09 ppm</td>
      <td>22 619</td>
      <td>80.02</td>
    </tr>
    <tr>
      <td rowspan="4">Fe</td>
      <td>36.50 wt%</td>
      <td>5350</td>
      <td>94.03</td>
    </tr>
    <tr>
      <td>21.20 wt%</td>
      <td>10 700</td>
      <td>92.19</td>
    </tr>
    <tr>
      <td>12.80 wt%</td>
      <td>16 050</td>
      <td>91.38</td>
    </tr>
    <tr>
      <td>9.20 wt%</td>
      <td>21 400</td>
      <td>88.30</td>
    </tr>
    <tr>
      <td rowspan="3">Cu</td>
      <td>3890 ppm</td>
      <td>10 700</td>
      <td>83.75</td>
    </tr>
    <tr>
      <td>2000 ppm</td>
      <td>16 050</td>
      <td>81.13</td>
    </tr>
    <tr>
      <td>1150 ppm</td>
      <td>21 400</td>
      <td>79.59</td>
    </tr>
    <tr>
      <td rowspan="3">U</td>
      <td>10 ppm</td>
      <td>5350</td>
      <td>88.93</td>
    </tr>
    <tr>
      <td>4.27 ppm</td>
      <td>10 700</td>
      <td>88.83</td>
    </tr>
    <tr>
      <td>0.881 ppm</td>
      <td>16 050</td>
      <td>89.27</td>
    </tr>
    <tr>
      <td>Ni</td>
      <td>22 ppm</td>
      <td>3300</td>
      <td>92.60</td>
    </tr>
    <tr>
      <td>Pb</td>
      <td>5 ppm</td>
      <td>5350</td>
      <td>90.28</td>
    </tr>
    <tr>
      <td>Zn</td>
      <td>68 ppm</td>
      <td>5350</td>
      <td>91.57</td>
    </tr>
    <tr>
      <td>Sb</td>
      <td>0.25 ppm</td>
      <td>5350</td>
      <td>93.68</td>
    </tr>
    <tr>
      <td>As</td>
      <td>6 ppm</td>
      <td>5350</td>
      <td>92.62</td>
    </tr>
    <tr>
      <td>Bi</td>
      <td>0.12 ppm</td>
      <td>5350</td>
      <td>94.90</td>
    </tr>
  </tbody>
</table>

The thresholds are defined by the upper percentiles of the geochemical records in the database.

For this work, a specially developed neural network was tested with the aim to evaluate the impact of specific parameters on the geochemical prediction results. To evaluate the accuracy of the methodology, 60% of the label set of 110 000 geochemical records were randomly chosen for learning, 20% for verification and 20% for independent testing. All classes of the test dataset were complete, with no missing values in any variable or outliers.

The developed neural network can be classified as a convolutional neural network. It employs convolutional layers as filters (kernel) to transform data into a randomised number of values in a grid (O’Shea & Nash, [2015](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0024)). The CNN model base was built prior to this experiment in the context of Dimap’s chemoin-format and geological studies. It has proven to be more stable and efficient than other widely used convolutional networks and enables predictions from independent individual multiple-value datasets (Eichstaedt *et al.*, [2020](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0011)). These investigations demonstrate that these networks have enough degrees of freedom and a suitable capacity for the analysis of the specific kinds of data, especially considering the necessary compromise between accuracy and generalisation error. For the network, the Rectified Linear Unit was applied as an activation function and Softmax for the multi-class classification to ensure the output probabilities (predictor values) for the classes add up to 1. The neural network was realised using Keras and TensorFlow. The training was conducted over 200 epochs with 400 features and data augmentation in one direction, to ensure a stable and steady learning environment. [Figure 1](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0003) shows the general design of the neural network. The results of each test were measured in a confusion matrix, which showed the correct and incorrect predicted classes for the 20% test dataset.

Figure 1.  Schematic model illustration of the neural network designed for the evaluation (Eichstaedt *et al.*, [2022](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0012)).

![Figure 1.  Schematic model illustration of the neural network designed for the evaluation (Eichstaedt et al., 2022).](https://www.tandfonline.com/cms/asset/0cbcf68a-9d93-49c5-b08e-8d6468a8438e/taje_a_2094465_f0001_c.jpg)

For the comparison of results of the predictor values generated by Keras/Tensorflow, paired sample *t*-tests were used, composed of two competing hypotheses. The null hypothesis assumes that the true mean difference between the paired samples is zero, which would mean that all observable differences are explained by random variation. The alternative hypothesis assumes that the true mean difference between the paired samples is not equal to zero. While the direction of the difference does not matter, a two-tailed hypothesis was used (Rasch *et al.*, [2015](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0025)).

For the analysis of the geological domains, the public available dataset for the Gawler Craton was used (CSIRO, [2021](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0008)). The craton borders were excluded from this, and all available hyperspectrally scanned drill holes in the craton area were used, including specific lithologies such as skarns and regolith. The accuracy of the mapped geological structure dataset was 1:500 000.

## Results

In the following, the influence of different parameters on the prediction of geochemical properties are presented with results focused on scenarios that are relevant for geological practice. Technical details of the artificial intelligence setup are reported but not described in detail.

[Table 1](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004) provides an overview of the achieved accuracies in the test datasets with the related thresholds for minimum grades. These thresholds have been defined based on percentiles from the highest measured geochemical value downwards. The accuracy values are described by the correctly predicted percentages below and above threshold cases in the test dataset against the overall cases. While the general accuracy is always 80% or more, there are differences between the elements. Dominant and visible elements, such as iron, and non mineral defining elements, such as gold and silver, show different accuracies. Iron has high accuracies with predictions around 90% or more, while gold and silver are only above 80%. Copper also shows accuracies of 80% or above. One explanation might be that copper can be found in a wide variety of deposits, and therefore the learning is less successful. Uranium, nickel and other base metals can be predicted with accuracies of 90% or higher. The most probable reason is that there is a clear correlation with very specific mineral combinations (such as uranium and granites), and the measurements of these elements were only taken when high grades were expected.

### Dependency of results based on the amount of data for learning

For this evaluation, an experimental series was setup where the number of geochemical samples per class was stepwise increased, and the results of the learning were observed for the classes as well as the overall accuracy. The number of samples of class 1—the prospective class—was always taken from the highest grade. The corresponding number of class 0 samples—the non-prospective class—was randomly taken out of this group to ensure a balanced dataset for the learning in the neural network. For practical reasons, 5% percentiles were used to increase the sample size.

[Figure 2](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2001) shows the results for iron for two and three classes, and for gold for three classes as typical examples of this analysis. In all investigated samples, a low number of samples that automatically represent the highest geochemically measured grades reached very high accuracies. This behaviour may result from the strong correlation of high grades of elements and typical mineral species combinations, which are easy to learn for a neural network, even where sample numbers are lower. With increasing number of samples, and therefore including lower grades, the accuracy decreased to a plateau. For the two-class problems, this plateau was at around 30 000 samples, whereas for the three-class problems, the plateau was reached at around 15 000–18 000 samples. With increasing variability in the grade, the learning performance was less optimal, even when the sample number increased up to 30 000. This behaviour is found in iron, gold, silver and uranium, but for other elements the dataset included insufficient high-grade sample data for this kind of evaluation.

Figure 2.  Dependency of overall accuracies of the neural network results from the number of samples included in the learning for iron for a two- and three-class approach and for gold for a three-class approach.

![Figure 2.  Dependency of overall accuracies of the neural network results from the number of samples included in the learning for iron for a two- and three-class approach and for gold for a three-class approach.](https://www.tandfonline.com/cms/asset/9a84289c-b953-4088-8ce6-11fd5e8b919c/taje_a_2094465_f0002_c.jpg)

Above 30 000 samples for two classes and 18 000 samples for three classes, the accuracy results increase again, even when the lower-grade measurements are included and therefore most likely with fewer dominant correlations between grades and mineral species combinations. It is expected that the increased number of samples allows the neural network to be better trained, even if the mineral species combinations are more diverse. Again, this behaviour has been observed for iron, gold, silver and uranium. The strength of the correlation between sample numbers and overall accuracies has an *R*<sup>2</sup> of 0.96 ([Figure 1](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2001)), modelled best with a second order polynomial equation.

The results show the importance of high sample numbers for the selected machine-learning concept and that high grades can be predicted with good accuracies. This allows multiple implementation scenarios for the neural network for the prediction of geochemical assays.

[Figure 2](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2001) shows the different overall accuracies of the predictions for different elements. Iron has an accuracy above 78% in the three-class approach, whereas the accuracies for gold are about 64% for the three-class approach. Two-class approaches achieve generally increased accuracies in the prediction, for iron by about 8% and for gold by about 15–18%.

### Influence of knowledge of geological domains on predictions

In a subsequent evaluation step, the influence of individual geological domains on the prediction results and their accuracies was analysed. The test was performed for two different scenarios. The first scenario was characterised by comparing the results of learning on datasets from selected geological domains and comparing them against the prediction results generated for the complete Australian prediction set. In the second scenario, the neural network was trained on one geological domain, and the trained network was used for predictions on another geological domain and then compared against the complete Australian prediction set. Only drill-hole data that could clearly be allocated to the domains outlined by CSIRO, including an inverted buffer of 3 km, were incorporated. The data were then processed with similar parameters and thresholds through the neural network. The same predictor values were used for post-processing.

In a first evaluation, the training dataset was split into data from drill core from craton structures (Gawler, Yilgarn, Pilbara) and non-craton structures. [Table 2](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2002) shows the results on a pairwise cross-tabulation of the prediction results (positive-class 1). The predictors were then analysed in a paired *t*-test. To do so, for each sample, the predictor value for the specific geo-domain was subtracted from the overall learning predictor value. For the craton dataset, the overall accuracy of the learning performance based on confusion matrices was slightly improved by up to 5%, but in the case of uranium reduced by 4%. This suggests that the neural network learning was not significantly better, even if the dataset were geologically more focused. Comparing the prediction results between the craton-only learning and the overall Australia learning, the similarities are typically above 90%, and up to 96%, except for silver with a lower level of about 87%. The predictor values correlate strongly, and the mean differences of the individual pairs of prediction are typically below 0.05 ppm. Gold has values of about 0.14 ppm higher with poorer correlations, as well as higher *t*-values.

**Table 2. Results of the comparison of the neural network performance for geological domains (data from craton and non-cratons).**

| Geo-domain | Element | Threshold in ppm | *n* geochem class 1 (1) | Overall accuracy (2) | Overall similarity (3) | Correlation predictor (4) | Mean predictor difference (5) | SD predictor difference (6) | *t* value | Sig. (two-tailed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Craton | Ag | 0.5 | 65 830 | 88.02 | 87.00 | 0.83 | 0.02 | 0.19 | 61.00 | <0.0001 |
|  | Au | 0.17 | 31 610 | 83.44 | 96.31 | 0.60 | 0.14 | 0.27 | 270.05 | <0.0001 |
|  |  | 0.09 | 43 604 | 82.96 | 90.15 | 0.55 | 0.14 | 0.29 | 270.68 | <0.0001 |
|  | U | 0.881 | 28 156 | 85.7 | 94.40 | 0.81 | 0.04 | 0.21 | 97.94 | <0.0001 |
|  | Cu | 1150 | 41 742 | 87.54 | 95.63 | 0.81 | 0.02 | 0.19 | 61.42 | <0.0001 |
| Non-craton | Ag | 0.5 | 2264 | 89.67 | 70.81 | 0.02 | −0.09 | 0.43 | −105.56 | <0.0001 |
|  | Au | 0.09 | 1634 | 94.82 | 77.35 | 0.07 | 0.02 | 0.50 | 23.87 | <0.001 |
|  | U | 0.881 | 4212 | 96.22 | 97.12 | 0.19 | 0.25 | 0.32 | 474.03 | <0.0001 |
|  | Cu | 1150 | 1944 | 93.79 | 90.63 | 0.13 | −0.05 | 0.38 | −58.69 | <0.0001 |

Shown are the sample size used to learn (column 1), the overall accuracy achieved in the confusion matrix on the test set (column 2), the similarities on predictions using a pairwise analysis between the whole Australian dataset and the geo-domain dataset (column 3), the correlation of the predictor values (column 4), the mean of the difference of the predictor values (column 5), the standard deviation of this differences (column 6) and the parameters of the paired sample *t*-tests.

For the non-craton dataset, the number of learning samples was lower. The higher learning accuracy results might therefore represent the effects shown above. The prediction similarities for uranium and copper are still high, for gold and silver only 70%. In the case of higher grades of gold, the sample dataset was too small for learning, and so no results are shown. The correlations are very weak between the non-craton learned prediction and the overall Australia prediction, which has mean differences higher than in the craton dataset. Overall, it is not clear whether this is due to lower sample numbers in the dataset for learning or real differences in learning. This point indicates that using the large dataset of the whole Australia in a neural network for predicting geochemical properties has greater advantages

The learning results on separate data samples from the Yilgarn and Gawler cratons for gold and copper are shown in [Table 3](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2002), with the overall learning accuracies compared. The evaluation was only performed for gold and copper because they represent larger datasets. The similarities between the predictions of the individual cratons and the overall Australian dataset are mostly above 90%. Only for lower gold grades in the Yilgarn Craton is the similarity lower with 85.7%. Correlations between the prediction results of the individual cratons and the overall Australian predictions are strong but higher in the Gawler Craton, probably owing to the larger training datasets. Mean differences between the predictions of the individual cratons and the overall Australian predictions are typically less than 0.1%, whereas they are significantly higher for gold. Summarising the results for both individual cratons, the neural network applied to individual cratons does not improve the predictions compared with the overall Australian learning model. This may be a result of the lower number of learning samples on individual cratons.

**Table 3. Results of the comparison of the neural network performance for craton structures (data from Yilgarn and Gawler).**

| Geo-domain | Element | Threshold in ppm | *n* geochem class 1 (1) | Overall accuracy (2) | Overall similarity (3) | Correlation predictor (4) | Mean predictor difference (5) | SD predictor difference (6) | *t* value | Sig. (two-tailed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yilgarn | Au | 0.17 | 8902 | 81.14 | 93.07 | 0.59 | 0.27 | 0.26 | 365.95 | <0.0001 |
|  |  | 0.09 | 10 278 | 81.30 | 85.74 | 0.55 | 0.30 | 0.27 | 387.32 | <0.0001 |
|  | Cu | 1150 | 2080 | 88.17 | 92.33 | 0.49 | −0.07 | 0.28 | −92.98 | <0.0001 |
| Gawler | Au | 0.17 | 22 348 | 85.78 | 97.71 | 0.75 | 0.04 | 0.21 | 83.17 | <0.0001 |
|  |  | 0.09 | 32 838 | 82.68 | 95.21 | 0.74 | 0.03 | 0.22 | 53.32 | <0.0001 |
|  | Cu | 1150 | 39 624 | 83.86 | 94.92 | 0.81 | 0.06 | 0.21 | 123.40 | <0.0001 |

For more details about the columns, refer to Table 2 footnote.

In a final evaluation, comparing the results of different geological domains, an experiment was set up where the sample dataset from the Gawler Craton was used to learn, and the resulting model was used for predictions in the Yilgarn Craton with no geochemical records. The predictions were again compared against the overall Australian predictions. [Table 4](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2002) shows the results of the comparison for the Yilgarn Craton. The overall accuracies of the learning are only valid for the Gawler Craton, as these were learned. The similarities between the Yilgarn Craton predictions and the overall Australian predictions were mostly high, above 90%, excluding those for lower-grade gold, which were only about 83%. Correlations between predictor values of Yilgarn Craton predictions and overall Australian predictions were lower than learning on Yilgarn Craton directly (see [Table 3](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2002) for gold and copper). Mean differences in the predictor values and *t*-values were higher for these elements. The results for silver and uranium showed higher correlations and lower *t*-values. In summary, learning on one craton, Gawler, and applying this model to another craton, Yilgarn, is possible, but the noise in the prediction results is larger. Overall, the results for [Table 3](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2002) show more stable solutions on the predictor values when training with geochemical labels on the Yilgarn Craton to make predictions for the same craton. When analysing only the similarities on grade prediction (classification), both methods show good results. The high similarities between the Gawler Craton learned, Yilgarn Craton applied predictions and the overall Australian predictions for uranium and copper with more than 99%, which are better when learning on the Yilgarn Craton directly, are based on general geological domain differences between the cratons.

**Table 4. Results of the comparison of the neural network performance for data learned on Gawler Craton and used for predictions of Yilgarn Craton data.**

| Geo-domain | Element | Threshold in ppm | *n* geochem class 1 (1) | Overall accuracy (2) | Overall similarity (3) | Correlation predictor (4) | Mean predictor difference (5) | SD predictor difference (6) | *t* value | Sig. (two-tailed) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yilgarn | Ag | 0.5 | 65 372 | **87.84** | 98.35 | 0.70 | 0.05 | 0.10 | 176.68 | <0.0001 |
|  | Au | 0.17 | 22 348 | **88.02** | 92.68 | −0.02 | 0.52 | 0.34 | 548.73 | <0.0001 |
|  |  | 0.09 | 32 838 | **87.62** | 83.15 | −0.05 | 0.52 | 0.33 | 566.37 | <0.0001 |
|  | U | 0.881 | 28 156 | **85.42** | 99.17 | 0.72 | 0.05 | 0.15 | 113.58 | <0.0001 |
|  | Cu | 1150 | 39 624 | **88.14** | 99.62 | 0.31 | 0.13 | 0.20 | 231.19 | <0.0001 |

For more details about the columns, refer to Table 2 footnote. The overall accuracies (column 2) for the Gawler Craton, which were used for learning, are shown in bold.

### Potential for resource estimation in Australia

To analyse the potential of the prediction results, a dataset of 2270 complete hyperspectral scanned drill holes, which are also available with a collar coordinate, were summarised. Column 3 of [Table 5](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2003) shows the number of holes in which geochemical analysis prospectivity was established. Column 4 shows the number of holes in which the neural network predicted additional prospectivity to the existing geochemical measurements. In column 5, the table shows holes in which, without existing geochemical measurements, the neural network predicted grades above the threshold. The last column of [Table 5](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2003) shows the number of holes in which 10 or more consecutive 1 m bins with grades above threshold were predicted—not having any geochemical measurement. Using the last two columns as identification of the potential of the neural network for increased deposit estimations shows that additional resources between 64% and more than 1000% can be achieved. The last column in [Table 5](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0004-S2003), the increase in per cent (in parentheses) for the holes with more than 10 one-metre bins can be compared with the holes with geochemical records (sum of the columns 3 and 4). These data could improve existing exploration models. Copper and high-grade uranium have smaller increases, but especially remarkable are the improvements for nickel and bismuth.

**Table 5. Exploration potential based on the predictions with the special designed neural network analysed on 2270 hyperspectral scanned drill holes.**

<table>
  <thead>
    <tr>
      <th>Element</th>
      <th>Threshold</th>
      <th>Holes geochemical measured, but no additional prediction</th>
      <th>Holes with geochemical measurements and additional predictions</th>
      <th>Holes with no geochemical measurements but additional predictions</th>
      <th>Holes with no geochemical record but 10 or more predictions (percentage of increased potential)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ag</td>
      <td>0.5 ppm</td>
      <td>119</td>
      <td>235</td>
      <td>991</td>
      <td>438 (124%)</td>
    </tr>
    <tr>
      <td rowspan="2">Au</td>
      <td>0.17 ppm</td>
      <td>224</td>
      <td>81</td>
      <td>893</td>
      <td>317 (104%)</td>
    </tr>
    <tr>
      <td>0.09 ppm</td>
      <td>178</td>
      <td>337</td>
      <td>1214</td>
      <td>616 (120%)</td>
    </tr>
    <tr>
      <td rowspan="4">Fe</td>
      <td>36.50 wt%</td>
      <td>50</td>
      <td>19</td>
      <td>277</td>
      <td>73 (106%)</td>
    </tr>
    <tr>
      <td>21.20 wt%</td>
      <td>48</td>
      <td>101</td>
      <td>520</td>
      <td>136 (91%)</td>
    </tr>
    <tr>
      <td>12.80 wt%</td>
      <td>56</td>
      <td>79</td>
      <td>631</td>
      <td>193 (143%)</td>
    </tr>
    <tr>
      <td>9.20 wt%</td>
      <td>63</td>
      <td>103</td>
      <td>713</td>
      <td>247 (149%)</td>
    </tr>
    <tr>
      <td rowspan="3">Cu</td>
      <td>3890 ppm</td>
      <td>124</td>
      <td>45</td>
      <td>188</td>
      <td>22 (13%)</td>
    </tr>
    <tr>
      <td>2000 ppm</td>
      <td>140</td>
      <td>75</td>
      <td>287</td>
      <td>52 (24%)</td>
    </tr>
    <tr>
      <td>1150 ppm</td>
      <td>139</td>
      <td>126</td>
      <td>464</td>
      <td>86 (32%)</td>
    </tr>
    <tr>
      <td rowspan="3">U</td>
      <td>10 ppm</td>
      <td>98</td>
      <td>28</td>
      <td>81</td>
      <td>17 (13%)</td>
    </tr>
    <tr>
      <td>4.27 ppm</td>
      <td>47</td>
      <td>117</td>
      <td>489</td>
      <td>80 (49%)</td>
    </tr>
    <tr>
      <td>0.881 ppm</td>
      <td>25</td>
      <td>169</td>
      <td>956</td>
      <td>235 (121%)</td>
    </tr>
    <tr>
      <td>Ni</td>
      <td>22 ppm</td>
      <td>17</td>
      <td>2</td>
      <td>781</td>
      <td>253 (1332%)</td>
    </tr>
    <tr>
      <td>Pb</td>
      <td>5 ppm</td>
      <td>107</td>
      <td>47</td>
      <td>749</td>
      <td>209 (136%)</td>
    </tr>
    <tr>
      <td>Zn</td>
      <td>68 ppm</td>
      <td>115</td>
      <td>36</td>
      <td>502</td>
      <td>93 (62%)</td>
    </tr>
    <tr>
      <td>Sb</td>
      <td>0.25 ppm</td>
      <td>76</td>
      <td>17</td>
      <td>704</td>
      <td>258 (277%)</td>
    </tr>
    <tr>
      <td>As</td>
      <td>6 ppm</td>
      <td>17</td>
      <td>25</td>
      <td>954</td>
      <td>269 (640%)</td>
    </tr>
    <tr>
      <td>Bi</td>
      <td>0.12 ppm</td>
      <td>14</td>
      <td>9</td>
      <td>899</td>
      <td>380 (1652%)</td>
    </tr>
  </tbody>
</table>

Shown are the number of drill holes per element and for different threshold with positive classified 1-metre bins. The geochemical measured bins are shown for comparison. The last column shows the increase in holes as a percentage compared with the holes with geochemically measured high grades for the elements.

## Discussion

The evaluation shows that hyperspectral core-scan derived mineral abundances combined with sparse geochemical measurements can be used successfully with neural network methods for geological prediction. While testing the performance of the method under different conditions, the robustness of the method and importance of some key parameters have been evaluated. Regarding the input material, further evaluation of differences in hyperspectral measurements with different sensitivities and representation of the elements in the processed core scans that may influence the prediction results is needed. For the Australian core scans, which were collected over a longer time frame and processed by different operators, the authors can attest to the robustness of the data in a complex learning system. No differences between the Australian states were identified, and the predicted data were applicable for the whole Australian territory. Spectrally automatic unmixing to system scalars (*i.e.* sTSAS, sTSAT or sjCLST) provided a level of consistency in The Spectral Geologist software that different user scalars for the same dataset cannot. Therefore, the Australian-based public drill-core-scan system was a valuable tool for the evaluation of the influences of different parameters on an artificial intelligence system using drill-core.

While the geochemical databases provided by the Australian state geological surveys partly include information on the measurements, the authors developed the neural network under the assumption that geochemical measurements were taken under industry standards and in industry typical units. Owing to the amount of data (70 million geochemical records), in this study classical mathematical methods such as outlier and logic tests were adapted to identify critical geochemical data sets. A further assumption made was that the geochemical datasets gave a reasonable and valid representation of the corresponding depth interval allocated, as the sampled intervals from the original records are inconsistent.

Based on the results of Eichstaedt *et al.* ([2022](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#CIT0012)) on the methodological comparison of deep learning and neural network methods for the prediction of geochemical properties out of large hyperspectral drill-core archives, this article evaluates the practical implications of the specially developed neural network. The work was conducted on all elements with sufficient grade measurements in the geochemical database and includes not only gold, iron and copper but also strategically important elements such as nickel and others. Based on practical requirements, the number of classes in labelling the geochemical data was adopted. Separation based on high grades from the rest of the data or having maximum tree classes allowed better learning accuracies than more classes.

The usage of thresholds for geochemical labelling in this evaluation was still based on statistical background, but evaluating different grades for more commonly measured elements (gold, iron, copper, uranium) shows that the threshold can be adapted to strictly exploration-orientated or project-specific cutoff values. For practical applications, the neural network was able to perform predictions with high accuracies for very-high-grade segments on the drill core, even with the learning samples limited to a couple of thousand records. It must be assumed that this is based on strong correlations between hyperspectral features and high grades of the specific elements or alternative specific accompanying minerals. These effects allow the prediction of the less common base metals such as nickel, lead, antimony, bismuth and others. Here, the artificial intelligence system acts like a specialised geologist with experience in specific geological situations.

On the other hand, it was shown that with increasing numbers of learning samples, the accuracy of the prediction increases. Separating geological domains did not significantly improve the results of the prediction, and moreover the neural network with increasing numbers of learning samples was able to predict geochemical properties with good accuracies in all geological domains. The artificial intelligence systems worked here like a geologist with experience in a wide range of different projects in different regions using a vast broad knowledge. This finding indicates that the neural network trained on data from Australia can be applied to other regions globally. This will be targeted and hopefully verified by our upcoming work.

The conclusions derived open a wide range of practical applications for the developed workflow. After training on a large dataset, such as the Australian publicly available hyperspectral/geochemical databases, the system can be used on a strategic but also operational level. Scanning and hyperspectral analysis of large core collections collected by governments or private shareholders will allow a review of the geochemical potential in a short time and the allocation of new prospects in the changing world of commodities, for instance for elements used in battery production. The review could reflect changed orientation on strategic important elements and minerals supporting political decisions, economic modelling, risk evaluations and decisions on project investments. [Table 5](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0005) can be used as a starting-point for such scenarios, where additionally identified drill core with nickel potential would be plotted, that might lead to geochemical samples and mineralogical zones with newly defined extensions, exploration programs reviewed, and new funding for discovery initiatives. Adding additional data into the learning data stack will improve the accuracy of the neural network prediction and the extension into potential similar neural networks for the prediction of lithological units and alteration.

The neural network can also be used in operational exploration work. Scanning core while drilling and using the predictor to identify geochemically interesting areas can free the geologist from a tedious analysis of facts that may be difficult to identify in the field and to work interactively with prediction systems on online generation of deposit models. The neural network can use the vast amounts of learning data from various geological domains with cost savings on staff, more targeted geochemical sampling and decision support during the drilling, which would outweigh the costs for core scanning with direct processing on site. Additionally, we see the application of this workflow will reduce the subjective component of interpretation and so develop a valuable tool for supporting geological staff.

[Figure 3](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465#S0005) shows the potential of the neural network on an example of drill holes in southern Australia identifying additional segments with higher uranium predictions. Using such datasets for densification of 3D modelling will allow a better understanding and growth of resources.

Figure 3.  Geochemical identified higher uranium grades (above 4.5 ppm—red) and with neural network predicted additional 1 m segments with uranium contents above 4.5 ppm (green); the depth scale is on the right in metres.

![Figure 3.  Geochemical identified higher uranium grades (above 4.5 ppm—red) and with neural network predicted additional 1 m segments with uranium contents above 4.5 ppm (green); the depth scale is on the right in metres.](https://www.tandfonline.com/cms/asset/1197c75d-d64f-4fbf-b18c-07e8920e8ed2/taje_a_2094465_f0003_c.jpg)

The application scenarios described above will allow drill-core data for predicted datasets such as 3D-deposit modelling and further targeting for exploration success.

## Conclusions

Elemental geochemical concentrations of hundreds of kilometres of drill cores can be predicted using integrated hyperspectral drill-core scan data and limited related geochemical datasets. In this evaluation, the effects of different practical influences on the results of the prediction were tested. A specially designed convolutional-based neural network algorithm allowed predictions for geochemical properties trained on large data samples with good accuracies but also the identification of more rare elements with accuracies higher than 90%. Learning and predictions on different geological domains can be supported with large learning samples covering the whole of Australia or larger geological units such as the Gawler and Yilgarn cratons. At this stage the specially designed neural network can be used for predicting geochemical properties for the Australian region using new and existing drill core that will have commercial impact on strategic and operational exploration activities. Predicting geochemistry from hyperspectral data will allow industry to reduce costs and get a better picture of the geochemistry in drill cores. The article shows a way to identify more prospective regions or to revisit existing core under different commodity prices and requirements, as well as changed mining methods. Established technologies such as HyLogger and TSG can be used for assessment of existing and newly scanned drill core.

### Acknowledgements

Authors show their gratitude towards staff members of all Australian Geological State surveys, especially Alan Mauger (SA, retired), Lena Hankock (WA), Mick Ramsey (NT), Dr Joseph Tang (Queensland), David Masters (NSW), Colin Marson (Victoria) and David Green (Tasmania). Special thanks to Dr Frederik Beuth, for his introduction and help with the implementation of the neural networks, and Joanne Ho, for preparation of parts of the material. We further thank Carsten Laukamp, for his review of the manuscript and advice for improvement.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Additional information

### Funding

This project was funded internally by Dimap Group and G.E.O.S. Engineering.

## References

- Acosta, I. C. C., Khodadadzadeh, M., Tolosana-Delgado, R., & Gloaguen, R. (2020). Drill-core hyperspectral and geochemical data integration in a superpixel-based machine learning framework. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, *13*, 4214–4228. https://doi.org/10.1109/JSTARS.2020.3011221 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_2_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000557351700004&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1109%2FJSTARS.2020.3011221&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D13%26publication_year%3D2020%26pages%3D4214-4228%26journal%3DIEEE%2BJournal%2Bof%2BSelected%2BTopics%2Bin%2BApplied%2BEarth%2BObservations%2Band%2BRemote%2BSensing%26author%3DI.%2BC.%2BC.%2BAcosta%26author%3DM.%2BKhodadadzadeh%26author%3DR.%2BTolosana-Delgado%26author%3DR.%2BGloaguen%26title%3DDrill-core%2Bhyperspectral%2Band%2Bgeochemical%2Bdata%2Bintegration%2Bin%2Ba%2Bsuperpixel-based%2Bmachine%2Blearning%2Bframework%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1109%252FJSTARS.2020.3011221&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1109%2FJSTARS.2020.3011221&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Arne, D. (2014). *Geochemical and hyperspectral orientation study of the Redton Cu–Mo project* [Technical Report for Kiska Metals Corporation]. Kiska Metals Corporation. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DArne%252C%2BD.%2B%25282014%2529.%2BGeochemical%2Band%2Bhyperspectral%2Borientation%2Bstudy%2Bof%2Bthe%2BRedton%2BCu%25E2%2580%2593Mo%2Bproject%2B%255BTechnical%2BReport%2Bfor%2BKiska%2BMetals%2BCorporation%255D.%2BKiska%2BMetals%2BCorporation.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- AuScope. (2020). *AuScope discovery portal* [Online]. [http://portal.auscope.org.au](http://portal.auscope.org.au/). [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DAuScope.%2B%25282020%2529.%2BAuScope%2Bdiscovery%2Bportal%2B%255BOnline%255D.%2B.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Geoscience Australia. (2021). *Australian mineral facts*. Geoscience Australia. ga.gov.au. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DGeoscience%2BAustralia.%2B%25282021%2529.%2BAustralian%2Bmineral%2Bfacts.%2BGeoscience%2BAustralia.%2Bga.gov.au.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Bao, H. (2019). Investigations of the influences of a CNN’s receptive field on segmentation of subnuclei of bilateral amygdala. *Advances in Engineering: An International Journal*, *2*(4), 1. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D2%26publication_year%3D2019%26pages%3D1%26journal%3DAdvances%2Bin%2BEngineering%253A%2BAn%2BInternational%2BJournal%26issue%3D4%26author%3DH.%2BBao%26title%3DInvestigations%2Bof%2Bthe%2Binfluences%2Bof%2Ba%2BCNN%25E2%2580%2599s%2Breceptive%2Bfield%2Bon%2Bsegmentation%2Bof%2Bsubnuclei%2Bof%2Bbilateral%2Bamygdala&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Berman, M., Bischof, L., Lagerstrom, R., Guo, Y., Huntington, J., Mason, P., & Green, A. A. (2017). A comparison between three sparse unmixing algorithms using a large library of shortwave infrared mineral spectra. *IEEE Transactions on Geoscience and Remote Sensing*, *55*(6), 3588–3610. https://doi.org/10.1109/TGRS.2017.2676816 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_7_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=WOS%3A000402063500040&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1109%2FTGRS.2017.2676816&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D55%26publication_year%3D2017%26pages%3D3588-3610%26journal%3DIEEE%2BTransactions%2Bon%2BGeoscience%2Band%2BRemote%2BSensing%26issue%3D6%26author%3DM.%2BBerman%26author%3DL.%2BBischof%26author%3DR.%2BLagerstrom%26author%3DY.%2BGuo%26author%3DJ.%2BHuntington%26author%3DP.%2BMason%26author%3DA.%2BA.%2BGreen%26title%3DA%2Bcomparison%2Bbetween%2Bthree%2Bsparse%2Bunmixing%2Balgorithms%2Busing%2Ba%2Blarge%2Blibrary%2Bof%2Bshortwave%2Binfrared%2Bmineral%2Bspectra%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1109%252FTGRS.2017.2676816&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1109%2FTGRS.2017.2676816&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Caté, A., Perozzi, L., Gloaguen, E., & Blouin, M. (2017). Machine learning as a tool for geologists. *The Leading Edge*, *36*(3), 215–219. https://doi.org/10.1190/tle36030215.1 [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D36%26publication_year%3D2017%26pages%3D215-219%26journal%3DThe%2BLeading%2BEdge%26issue%3D3%26author%3DA.%2BCat%25C3%25A9%26author%3DL.%2BPerozzi%26author%3DE.%2BGloaguen%26author%3DM.%2BBlouin%26title%3DMachine%2Blearning%2Bas%2Ba%2Btool%2Bfor%2Bgeologists%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1190%252Ftle36030215.1&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1190%2Ftle36030215.1&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- CSIRO. (2021). [http://nvclwebservices.csiro.au/geoserver/wfs?&request=GetFeature&service=WFS&typename=gml:ProvinceFullExtent&outputFormat=SHAPE-ZIP&version=1.1.0](http://nvclwebservices.csiro.au/geoserver/wfs?&request=GetFeature&service=WFS&typename=gml:ProvinceFullExtent&outputFormat=SHAPE-ZIP&version=1.1.0) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DCSIRO.%2B%25282021%2529.%2B&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Dramsch, J. S. (2020). 70 Years of machine learning in geoscience in review. *Advances in Geophysics*, *61*, 1–55. https://doi.org/10.1016/bs.agph.2020.08.002 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_10_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000610723500002&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1016%2Fbs.agph.2020.08.002&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D61%26publication_year%3D2020%26pages%3D1-55%26journal%3DAdvances%2Bin%2BGeophysics%26author%3DJ.%2BS.%2BDramsch%26title%3D70%2BYears%2Bof%2Bmachine%2Blearning%2Bin%2Bgeoscience%2Bin%2Breview%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1016%252Fbs.agph.2020.08.002&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1016%2Fbs.agph.2020.08.002&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Du, S., Wang, Y., Zhai, X., Balakrishnan, S., Salakhutdinov, R., Singh, A. (2018). *How many samples are needed to estimate a convolutional Neural Network?* [Paper presentation]. 32nd Conference on Neural Information Processing Systems (NeurIPS 2018), Montreal, Canada [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DDu%252C%2BS.%252C%2BWang%252C%2BY.%252C%2BZhai%252C%2BX.%252C%2BBalakrishnan%252C%2BS.%252C%2BSalakhutdinov%252C%2BR.%252C%2BSingh%252C%2BA.%2B%25282018%2529.%2BHow%2Bmany%2Bsamples%2Bare%2Bneeded%2Bto%2Bestimate%2Ba%2Bconvolutional%2BNeural%2BNetwork%253F%2B%255BPaper%2Bpresentation%255D.%2B32nd%2BConference%2Bon%2BNeural%2BInformation%2BProcessing%2BSystems%2B%2528NeurIPS%2B2018%2529%252C%2BMontreal%252C%2BCanada&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Eichstaedt, H., Beuth, F., Kahnt, R., & Helbig, M. (2020). *Balanced applications of machine learning and geological expertise*. Explorer Challenge South Australia. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26publication_year%3D2020%26author%3DH.%2BEichstaedt%26author%3DF.%2BBeuth%26author%3DR.%2BKahnt%26author%3DM.%2BHelbig%26title%3DBalanced%2Bapplications%2Bof%2Bmachine%2Blearning%2Band%2Bgeological%2Bexpertise&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Eichstaedt, H., Ho, C. Y. J., Kutzke, A., & Kahnt, R. (2022). Performance measurements of machine learning and different neural network designs for prediction of geochemical properties based on hyperspectral core scans. *Australian Journal of Earth Sciences*, *69*(5), 733–741. https://doi.org/10.1080/08120099.2022.2017344 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_13_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000752326900001&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1080%2F08120099.2022.2017344&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D69%26publication_year%3D2022%26pages%3D733-741%26journal%3DAustralian%2BJournal%2Bof%2BEarth%2BSciences%26issue%3D5%26author%3DH.%2BEichstaedt%26author%3DC.%2BY.%2BJ.%2BHo%26author%3DA.%2BKutzke%26author%3DR.%2BKahnt%26title%3DPerformance%2Bmeasurements%2Bof%2Bmachine%2Blearning%2Band%2Bdifferent%2Bneural%2Bnetwork%2Bdesigns%2Bfor%2Bprediction%2Bof%2Bgeochemical%2Bproperties%2Bbased%2Bon%2Bhyperspectral%2Bcore%2Bscans%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1080%252F08120099.2022.2017344&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1080%2F08120099.2022.2017344&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Eichstaedt, H., Tsedenbaljir, T., Kahnt, R., Denk, M., Ogen, Y., Glaesser, C., Loeser, R., Suppes, R., Alyeksandr, U., Oyunbuyan, T., & Michalski, J. (2020). Quantitative estimation of clay minerals in airborne hyperspectral data using a calibration field. *Journal of Applied Remote Sensing*, *14*(03), 034524. https://doi.org/10.1117/1.JRS.14.034524 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_14_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=WOS%3A000575857800001&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1117%2F1.JRS.14.034524&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D14%26publication_year%3D2020%26pages%3D034524%26journal%3DJournal%2Bof%2BApplied%2BRemote%2BSensing%26issue%3D03%26author%3DH.%2BEichstaedt%26author%3DT.%2BTsedenbaljir%26author%3DR.%2BKahnt%26author%3DM.%2BDenk%26author%3DY.%2BOgen%26author%3DC.%2BGlaesser%26author%3DR.%2BLoeser%26author%3DR.%2BSuppes%26author%3DU.%2BAlyeksandr%26author%3DT.%2BOyunbuyan%26author%3DJ.%2BMichalski%26title%3DQuantitative%2Bestimation%2Bof%2Bclay%2Bminerals%2Bin%2Bairborne%2Bhyperspectral%2Bdata%2Busing%2Ba%2Bcalibration%2Bfield%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1117%252F1.JRS.14.034524&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1117%2F1.JRS.14.034524&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Fouedjio, F., Hill, E. J., & Laukamp, C. (2018). Ore body domaining through geostatistical clustering: Case study at the Rocklea Dome Channel Iron Ore Deposit, Western Australia. *Applied Earth Science**, Volume* *127*(1), 15–29. https://doi.org/10.1080/03717453.2017.1415114 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_15_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000435705400003&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1080%2F03717453.2017.1415114&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D127%26publication_year%3D2018%26pages%3D15-29%26journal%3DApplied%2BEarth%2BScience%26issue%3D1%26author%3DF.%2BFouedjio%26author%3DE.%2BJ.%2BHill%26author%3DC.%2BLaukamp%26title%3DOre%2Bbody%2Bdomaining%2Bthrough%2Bgeostatistical%2Bclustering%253A%2BCase%2Bstudy%2Bat%2Bthe%2BRocklea%2BDome%2BChannel%2BIron%2BOre%2BDeposit%252C%2BWestern%2BAustralia%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1080%252F03717453.2017.1415114&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1080%2F03717453.2017.1415114&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Geng, X. (2016). Label distribution learning. *IEEE Transactions on Knowledge and Data Engineering*, *28*(7), 1734–1748. https://doi.org/10.1109/TKDE.2016.2545658 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_16_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000380117500010&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1109%2FTKDE.2016.2545658&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D28%26publication_year%3D2016%26pages%3D1734-1748%26journal%3DIEEE%2BTransactions%2Bon%2BKnowledge%2Band%2BData%2BEngineering%26issue%3D7%26author%3DX.%2BGeng%26title%3DLabel%2Bdistribution%2Blearning%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1109%252FTKDE.2016.2545658&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1109%2FTKDE.2016.2545658&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Green, A. (2020). *CorStruth—Automated analysis of HyLogger data from the NVCL* [Online]. [http://www.corstruth.com.au](http://www.corstruth.com.au/). [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DGreen%252C%2BA.%2B%25282020%2529.%2BCorStruth%25E2%2580%2594Automated%2Banalysis%2Bof%2BHyLogger%2Bdata%2Bfrom%2Bthe%2BNVCL%2B%255BOnline%255D.%2B.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Jaques, A. L., Jaireth, S., & Walshe, J. L. (2002). Mineral systems of Australia: An overview of resources, settings and processes. *Australian Journal of Earth Sciences*, *49**(*4), 623–660. https://doi.org/10.1046/j.1440-0952.2002.00946.x [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_18_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000177505500005&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1046%2Fj.1440-0952.2002.00946.x&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D49%26publication_year%3D2002%26pages%3D623-660%26journal%3DAustralian%2BJournal%2Bof%2BEarth%2BSciences%26issue%3D4%26author%3DA.%2BL.%2BJaques%26author%3DS.%2BJaireth%26author%3DJ.%2BL.%2BWalshe%26title%3DMineral%2Bsystems%2Bof%2BAustralia%253A%2BAn%2Boverview%2Bof%2Bresources%252C%2Bsettings%2Band%2Bprocesses%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1046%252Fj.1440-0952.2002.00946.x&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1046%2Fj.1440-0952.2002.00946.x&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Karpatne, A., Ebert-Uphoff, I., Ravela, S., Babaie, H. A., Kumar, V. (2020). *Machine learning for the geosciences: Challenges and opportunities* [Paper presentation]. 2020 IEEE Winter Conference on Applications of Computer Vision (WACV) (pp. 1765–1774). [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DKarpatne%252C%2BA.%252C%2BEbert-Uphoff%252C%2BI.%252C%2BRavela%252C%2BS.%252C%2BBabaie%252C%2BH.%2BA.%252C%2BKumar%252C%2BV.%2B%25282020%2529.%2BMachine%2Blearning%2Bfor%2Bthe%2Bgeosciences%253A%2BChallenges%2Band%2Bopportunities%2B%255BPaper%2Bpresentation%255D.%2B2020%2BIEEE%2BWinter%2BConference%2Bon%2BApplications%2Bof%2BComputer%2BVision%2B%2528WACV%2529%2B%2528pp.%2B1765%25E2%2580%25931774%2529.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Kulesza, T. Amershi, S., Caruana, R., Fisher, D., Charles, D. (2014). *Structured labeling to facilitate concept evolution in machine learning* [Paper presentation]. Conference on Human Factors in Computing Systems—Proceedings (pp. 3075–3084). [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26publication_year%3D2014%26pages%3D3075-3084%26author%3DT.%2BKulesza%26author%3DS.%2BAmershi%26author%3DR.%2BCaruana%26author%3DD.%2BFisher%26author%3DD.%2BCharles%26title%3DStructured%2Blabeling%2Bto%2Bfacilitate%2Bconcept%2Bevolution%2Bin%2Bmachine%2Blearning&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Lampinen, H., Laukamp, C., Occhipinti, S., & Spinks, S. C. (2016). *Relationship of geochemistry and mineralogy to parent lithology and the degree of weathering in regolith* [Paper presentation]. AESC 2016: Uncover Earth’s Past to Discover Our Future (p. 250). [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DLampinen%252C%2BH.%252C%2BLaukamp%252C%2BC.%252C%2BOcchipinti%252C%2BS.%252C%2B%2526%2BSpinks%252C%2BS.%2BC.%2B%25282016%2529.%2BRelationship%2Bof%2Bgeochemistry%2Band%2Bmineralogy%2Bto%2Bparent%2Blithology%2Band%2Bthe%2Bdegree%2Bof%2Bweathering%2Bin%2Bregolith%2B%255BPaper%2Bpresentation%255D.%2BAESC%2B2016%253A%2BUncover%2BEarth%25E2%2580%2599s%2BPast%2Bto%2BDiscover%2BOur%2BFuture%2B%2528p.%2B250%2529.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Leybourne, M. I., Pontual, S., & Peter, J. M. (2013). Integrating hyperspectral mineralogy, mineral chemistry, geochemistry and geological data at different scales in iron ore mineral exploration. Iron Ore Conference, *3*, 10. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D3%26publication_year%3D2013%26pages%3D10%26journal%3DIron%2BOre%2BConference%26author%3DM.%2BI.%2BLeybourne%26author%3DS.%2BPontual%26author%3DJ.%2BM.%2BPeter%26title%3DIntegrating%2Bhyperspectral%2Bmineralogy%252C%2Bmineral%2Bchemistry%252C%2Bgeochemistry%2Band%2Bgeological%2Bdata%2Bat%2Bdifferent%2Bscales%2Bin%2Biron%2Bore%2Bmineral%2Bexploration&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Moon, C., Whateley, M., & Evans, A. (2006). *Introduction to mineral exploration* (2nd ed.). Blackwell. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26publication_year%3D2006%26author%3DC.%2BMoon%26author%3DM.%2BWhateley%26author%3DA.%2BEvans%26title%3DIntroduction%2Bto%2Bmineral%2Bexploration&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Neyshabur, B., Bhojanapalli, S., McAllester, D., & Srebro, N. (2017). *A pac-bayesian approach to spectrally-normalized margin bounds for neural networks*. arXiv preprint arXiv:1707.09564. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DNeyshabur%252C%2BB.%252C%2BBhojanapalli%252C%2BS.%252C%2BMcAllester%252C%2BD.%252C%2B%2526%2BSrebro%252C%2BN.%2B%25282017%2529.%2BA%2Bpac-bayesian%2Bapproach%2Bto%2Bspectrally-normalized%2Bmargin%2Bbounds%2Bfor%2Bneural%2Bnetworks.%2BarXiv%2Bpreprint%2BarXiv%253A1707.09564.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- O’Shea, K., & Nash, R. (2015). *An introduction to convolutional neural networks*. arXiv. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DO%25E2%2580%2599Shea%252C%2BK.%252C%2B%2526%2BNash%252C%2BR.%2B%25282015%2529.%2BAn%2Bintroduction%2Bto%2Bconvolutional%2Bneural%2Bnetworks.%2BarXiv.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Rasch, D., Herrendörfer, G., Bock, J., Victor, N. & Guiard, V. (2015). *Verfahrensbibliothek: Versuchsplanung und -auswertung - Mit CD-ROM*. Oldenbourg Wissenschaftsverlag. https://doi.org/10.1524/9783486843965 [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26publication_year%3D2015%26author%3DD.%2BRasch%26author%3DG.%2BHerrend%25C3%25B6rfer%26author%3DJ.%2BBock%26author%3DN.%2BVictor%26author%3DV.%2BGuiard%26title%3DVerfahrensbibliothek%253A%2BVersuchsplanung%2Bund%2B-auswertung%2B-%2BMit%2BCD-ROM&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1524%2F9783486843965&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Rodger, A., & Laukamp, C. (2021). Quantitative geochemical prediction from spectral measurements and its application to spatially dispersed spectral data. *Applied Sciences*, *12*(1), 282. https://doi.org/10.3390/app12010282 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_27_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=WOS%3A000758397100001&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.3390%2Fapp12010282&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D12%26publication_year%3D2021%26pages%3D282%26journal%3DApplied%2BSciences%26issue%3D1%26author%3DA.%2BRodger%26author%3DC.%2BLaukamp%26title%3DQuantitative%2Bgeochemical%2Bprediction%2Bfrom%2Bspectral%2Bmeasurements%2Band%2Bits%2Bapplication%2Bto%2Bspatially%2Bdispersed%2Bspectral%2Bdata%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.3390%252Fapp12010282&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.3390%2Fapp12010282&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Roh, Y., Heo, G., & Whang, S. E. (2018). *A survey on data collection for machine learning: A big data—AI integration perspective* (p. 18). arXiv. [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DRoh%252C%2BY.%252C%2BHeo%252C%2BG.%252C%2B%2526%2BWhang%252C%2BS.%2BE.%2B%25282018%2529.%2BA%2Bsurvey%2Bon%2Bdata%2Bcollection%2Bfor%2Bmachine%2Blearning%253A%2BA%2Bbig%2Bdata%25E2%2580%2594AI%2Bintegration%2Bperspective%2B%2528p.%2B18%2529.%2BarXiv.&doi=10.1080%2F08120099.2022.2094465&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Schodlok, M. C., Whitbourn, L., Huntington, J., Mason, P., Green, A., Berman, M., Coward, D., Connor, P., Wright, W., Jolivet, M., & Martinez, R. (2016). HyLogger-3, a visible to shortwave and thermal infrared reflectance spectrometer system for drill core logging: Functional description. *Australian Journal of Earth Sciences*, *63*(8), 929–940. https://doi.org/10.1080/08120099.2016.1231133 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_29_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=WOS%3A000396490100002&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.1080%2F08120099.2016.1231133&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D63%26publication_year%3D2016%26pages%3D929-940%26journal%3DAustralian%2BJournal%2Bof%2BEarth%2BSciences%26issue%3D8%26author%3DM.%2BC.%2BSchodlok%26author%3DL.%2BWhitbourn%26author%3DJ.%2BHuntington%26author%3DP.%2BMason%26author%3DA.%2BGreen%26author%3DM.%2BBerman%26author%3DD.%2BCoward%26author%3DP.%2BConnor%26author%3DW.%2BWright%26author%3DM.%2BJolivet%26author%3DR.%2BMartinez%26title%3DHyLogger-3%252C%2Ba%2Bvisible%2Bto%2Bshortwave%2Band%2Bthermal%2Binfrared%2Breflectance%2Bspectrometer%2Bsystem%2Bfor%2Bdrill%2Bcore%2Blogging%253A%2BFunctional%2Bdescription%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.1080%252F08120099.2016.1231133&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.1080%2F08120099.2016.1231133&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
- Sun, L., Peter, S., & Khan, S. (2019). Integrated hyperspectral and geochemical study of sediment-hosted disseminated gold at the Goldstrike District, Utah. *Remote Sensing*, *11*(17), 1987. https://doi.org/10.3390/rs11171987 [Web of Science ®](https://www.tandfonline.com/servlet/linkout?suffix=e_1_3_3_30_1&dbid=128&doi=10.1080%2F08120099.2022.2094465&key=000486874300031&getFTLinkType=true&doiForPubOfPage=10.1080%2F08120099.2022.2094465&refDoi=10.3390%2Frs11171987&linkType=ISI&linkSource=FULL_TEXT&linkLocation=Reference) [Google Scholar](https://www.tandfonline.com/action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D11%26publication_year%3D2019%26pages%3D1987%26journal%3DRemote%2BSensing%26issue%3D17%26author%3DL.%2BSun%26author%3DS.%2BPeter%26author%3DS.%2BKhan%26title%3DIntegrated%2Bhyperspectral%2Band%2Bgeochemical%2Bstudy%2Bof%2Bsediment-hosted%2Bdisseminated%2Bgold%2Bat%2Bthe%2BGoldstrike%2BDistrict%252C%2BUtah%26doi%3Dhttps%253A%252F%252Fdoi.org%252F10.3390%252Frs11171987&doi=10.1080%2F08120099.2022.2094465&doiOfLink=10.3390%2Frs11171987&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT)
