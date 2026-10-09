---
title: "Machine learning applications on lunar meteorite minerals: From classification to mechanical properties prediction"
source: "https://www.sciencedirect.com/science/article/pii/S2095268624001010"
archived_at: "2026-10-09"
format: "Markdown"
---

Eloy Peña-Asensio<sup>a</sup>, Josep M. Trigo-Rodríguez<sup>b, c</sup>, Jordi Sort<sup>d, e</sup>, Jordi Ibáñez-Insa<sup>f</sup>, Albert Rimola<sup>g</sup>

## Abstract

Amid the scarcity of [lunar meteorites](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-meteorite) and the imperative to preserve their scientific value, non-destructive testing methods are essential. This translates into the application of [microscale](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/microbalance) rock mechanics experiments and scanning electron microscopy for surface composition analysis. This study explores the application of Machine Learning algorithms in predicting the mineralogical and mechanical properties of DHOFAR 1084, JAH 838, and NWA 11444 lunar meteorites based solely on their atomic percentage compositions. Leveraging a prior-data fitted network model, we achieved near-perfect classification scores for meteorites, mineral groups, and individual minerals. The regressor models, notably the *K*-Neighbor model, provided an outstanding estimate of the mechanical properties—previously measured by [nanoindentation](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/nanoindentation) tests—such as hardness, reduced Young’s modulus, and elastic recovery. Further considerations on the nature and physical properties of the minerals forming these meteorites, including porosity, crystal orientation, or shock degree, are essential for refining predictions. Our findings underscore the potential of Machine Learning in enhancing mineral identification and mechanical property estimation in [lunar exploration](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-exploration), which pave the way for new advancements and quick assessments in extraterrestrial mineral mining, processing, and research.

## Keywords

Meteorites; Moon; Mineralogy; Machine learning; Mechanical properties

## 1. Introduction

The integration of Machine Learning (ML) technologies into various scientific and engineering disciplines has been met with both acclaim and skepticism. Despite notable success where it has matched or surpassed human performance in diverse material science applications [[1]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0005), there remains a significant degree of disbelief within both academia and industry regarding the practical utility and impact of these technologies, particularly in specialized fields like [mineral processing](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/mineral-processing) [[2]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0010). This skepticism is largely a product of repeated cycles of hype, characterized by overblown promises followed by underperformance, leading to disillusionment, reduced investment, and slowed research and development.

In the context of mineral processing, data-based modeling methods have traditionally been employed as “soft sensors” to predict variables that are either infrequently measured or difficult to measure, using data from variables that are more readily available. Although applications of partial least squares (PLS) methods for predicting elemental composition using reflectance spectroscopy [[3]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0015), [[4]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0020), and the use of neural networks for modeling [hydrocyclones](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/hydrocyclone) [[5]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0025), milling circuits [[6]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0030), [[7]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0035), flotation processes [[8]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0040), [[9]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0045), and furnaces [[10]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0050), [[11]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0055) have been documented, these efforts typically involved relatively simple neural network architectures, constrained by computational resources or the availability of data.

In addition to traditional techniques to achieve the characterization of meteorites, involving a sum of know-how and significant instrumental expertise, Allegretta et al. [[12]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0060) showcased the application of portable X-ray fluorescence spectroscopy (XRF) combined with ML algorithms to achieve precise classification of meteorites. This new XRF approach not only enables the rapid identification of meteorites in diverse environments but also aids in distinguishing genuine meteorite samples from similar terrestrial materials, often referred to as “meteor-wrongs”. By utilizing energy dispersive XRF instruments alongside principal component analysis and algorithms such as the cubic [support vector machine](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/support-vector-machine) and nearest neighbor classifiers, the study achieved a 100% accuracy rate in classifying meteorites into macro-groups.

Further expanding the applications of ML in extraterrestrial mineral analysis, Breitenfeld et al. [[13]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0065) and Dyar et al. [[14]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0070) explored the quantification of mineral compositions in asteroids and the distribution of matter within the Solar System. Breitenfeld et al. [[13]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0065) applied a phyllosilicate-specific model to data from the OSIRIS-REx mission’s target asteroid, Bennu, identifying significant volumes of phyllosilicates and distinguishing between Mg and Fe serpentines. Dyar et al. [[14]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0070) introduced a method to classify asteroids based on spectral characteristics, using ML algorithms to correlate asteroid spectra with known meteorite classes. This approach, rooted in mineralogical composition, allows for the precise evaluation of the distribution of matter in the [asteroid belt](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/asteroid-belts), marking a significant departure from traditional taxonomy methods. Bruschini et al. [[15]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0075) examined impact glass-bearing rocks using a combination of spectroscopies and X-ray diffraction, complemented by a comprehensive database of glass materials’ properties. This database was employed to identify relationships between chemical and physical characteristics and to apply ML algorithms for predicting the oxidation state of iron.

Regarding lunar material, Kodikara et al. [[16]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0080) investigated the use of ML to determine the physical and mineralogical properties of [lunar soil](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-soil) through reflectance spectra analysis. Utilizing the Lunar Soil Characterization Consortium (LSCC) dataset, they assessed the effectiveness of nine ML algorithms—spanning linear, non-linear, and rule-based methods—in classifying lunar soils by type (Mare or Highland), particle size, maturity, and [pyroxene](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/pyroxene) content (high-Ca or low-Ca). Similarly, Korokhin [[17]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0085), introduced an innovative approach for mapping lunar [regolith](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/regolith) composition by integrating a nonlinear spectral mixing model with ML algorithms, significantly outperforming traditional numerical optimization methods in speed. This methodology enables comprehensive mapping of the lunar surface’s regolith properties, such as mineralogical composition, average grain size, and optical maturity, across extensive areas.

Given this context, the present study aims to bridge a gap in the current research landscape by exploring the application of advanced ML techniques to the study and processing of extraterrestrial minerals, specifically those found in [lunar meteorites](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-meteorite). Despite the potential of ML to revolutionize the classification and prediction of mechanical properties of these minerals, efforts to apply ML in the context of extraterrestrial mineral processing have been limited. While there are advancements in ML for analyzing lunar soil and regolith properties, the scientific literature lacks the application of novel techniques to lunar meteorites.

The investigation of lunar meteorites is important for elucidating the Moon’s geological history and its current surface conditions [[18]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0090), [[19]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0095). This is particularly pertinent in light of the Artemis program and the ongoing efforts to establish a lunar base in the Moon’s south [polar region](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/polar-region) [[20]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0100). Currently, our understanding of the mechanical properties of lunar materials remains nascent, and the classification of their constituent minerals poses significant challenges. These issues are pivotal for lunar science and the future practical application of in-situ resource utilization (ISRU) strategies.

Given the rarity of lunar meteorites and the need to conserve the scientific information they contain, researchers try to avoid large-scale destructive testing. Consequently, the scientific community is more inclined to perform micro-/nanoscale rock mechanics experiments (e.g., nanoindentation) as an alternative, nearly non-destructive means to ascertain the mechanical properties and composition of these precious samples [[21]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0105), [[22]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0110), [[23]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0115), [[24]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0120), [[25]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0125), [[26]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0130), [[27]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0135). Similarly, this technique might be applied to characterize the mechanical properties of sample returned materials like these brought back by Hayabusa JAXA mission from asteroid Itokawa [[28]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0140)**.**

The advent of ML algorithms provides innovative approaches for the identification of meteorite mineralogy and the prediction of their mechanical properties from elemental compositions, which can have direct impact in future off-Earth mineral processing and science endeavors. In this work, we explore the use of ML techniques to identify the mineralogical and mechanical properties of DHOFAR 1084, JAH 838, and NWA 11444 lunar meteorites, demonstrating the potential of these advanced technologies to contribute significantly to lunar science and exploration. Both mineral classification and mechanical properties are predicted independently using distinct approaches, both exclusively based on elemental compositions determined by microanalysis techniques.

In [Section 2](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0010) we present the lunar meteorite samples used in this study, in [Section 3](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0015) we introduce the methods and procedures employed, in [Section 4](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0045) we present the results, and in [Section 5](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0060) we summarize our findings.

## 2. Meteorites samples

The thin sections of the meteorites analyzed in this study, DHOFAR 1084, JAH 838, and NWA 11444, are part of the Meteorite Collection at the Institute of Space Sciences (CSIC), Spain, and have been duly classified in the Meteoritical Bulletin Database.[<sup>1</sup>](https://www.sciencedirect.com/science/article/pii/S2095268624001010#fn1) The Meteoritical Bulletin Database, coordinated by the Meteoritical Society, is a comprehensive online resource that provides detailed information on all recognized meteorites (>75000), including their classifications, compositions, and discovery locations, serving as an essential tool for researchers in the field of meteoritics. [Fig. 1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0005) shows false-color enhanced mosaics of the thin sections employed in this work.

![](https://ars.els-cdn.com/content/image/1-s2.0-S2095268624001010-gr1.jpg)

-

-

Fig. 1. Mosaics of the thin sections of lunar meteorites.

DHOFAR 1084, discovered in 2001 in the Dhofar region of Oman, near Zufar, stands out as an exemplary average feldspathic lunar meteorite, offering key insights into the Moon’s geological history [[29]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0145). Chemical analysis reveals high content of aluminum and refractory elements, hinting at its [lunar crust](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-crust) origin. Its composition, characterized by impact glass and brecciated fragments, indicates formation through violent impact events, marking the lunar surface’s history with evidence of such catastrophic occurrences.

In 2003, during a desert expedition 28 km south of Al Ghaftain, Oman, another significant find was made with the discovery of Jiddat al Harasis 838 (JAH 838), classified as a mingled [regolith](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/regolith) [breccia](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/breccia). This meteorite, containing mare and KREEPy material, along with HASP (alumina–silica poor) and chondritic material, provides valuable data on the Moon’s chemical and [isotopic composition](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/isotopic-composition) [[30]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0150). [Isotopic analysis](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/isotopic-analysis) aligns closely with Apollo mission samples, affirming JAH 838’s lunar origin and suggesting its formation in the Moon’s early, volcanically active phase [[31]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0155). JAH 838’s detailed analysis reveals a complex breccia composed of various mineral fragments and lithic clasts, encapsulating a rich history of lunar geological activity within its fine-grained, dark gray matrix that houses an array of minerals and metallic elements.

The discovery of Northwest Africa 11444 (NWA 11444) in 2017, in an undisclosed location in Mauritania, added another piece to the lunar meteorite collection. Classified as a polymictic anorthositic breccia, NWA 11444 comprises [anorthosite](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/anorthosite) fragments—an indication of its rich plagioclase content—melded by the intense heat from a lunar impact event [[32]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0160). This meteorite is a testament to the diversity of lunar geological materials, showcasing a mix of angular fragments, from coarse-grained to aphanitic gabbros and [basalts](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/basalt), within a fine-grain matrix. The composition of NWA 11444, rich in minerals and lithic clasts, highlights the lunar surface’s geological diversity, presenting a comprehensive view of the Moon’s material composition and the dynamic processes that have shaped its surface.

## 3. Methods and procedures

This section explains the methodologies employed to analyze the mineralogical properties and mechanical characteristics of lunar meteorites, structured into three distinct subsections. [Section 3.1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0020) outlines the use of Scanning Electron Microscopy (SEM) for detailed mineralogical analysis. Following this, [Section 3.2](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0025) describes the experimental procedure used to measure the mechanical properties of the meteorites, such as hardness, elastic modulus, and elastic recovery, at the [microscale](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/microbalance). Lastly, [Section 3.3](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0030) introduces the application of advanced ML algorithms to classify and predict the properties of lunar meteorites. More detail about the characterization of these samples can be found in Ref. [[27]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0135).

### 3.1. SEM mineral identification

The thin sections of the samples were analyzed using a Zeiss Scope Axio petrographic [optical microscope](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/optical-microscope) in both reflected and transmitted light modes, employing magnifications of ×50, ×100, and ×250. To systematically identify and catalog various features and components within these sections, high-resolution mosaic images were constructed.

Further analysis was conducted using SEM coupled with energy dispersive X-ray (EDX) analysis at the Catalan Institute of Nanoscience and Nanotechnology (ICN2), Spain, utilizing the FEI Quanta 650 FEG SEM in the low vacuum backscattered electron mode (BSED). Elemental composition was detailed using an Inca 250 SSD Xmax20 EDS detector, which is equipped with Peltier cooling and boasts an active area of 20 mm<sup>2</sup>. This setup facilitated the examination of selected areas at various magnifications, enabling the acquisition of [EDX spectra](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/x-ray-spectra) that offered an in-depth analysis of the mineralogical composition and elemental distribution within the sections. These analyses were instrumental for manually identifying the minerals subjected to indentation. Elemental information for O, Na, Mg, Al, Si, S, Ca, Ti, Cr, and Fe in the meteorites was obtained.

### 3.2. Nanoindentation

The mechanical properties of minerals in this study were determined using the NHT2 Anton Paar nanoindentation instrument, equipped with a Berkovich pyramidal diamond tip, housed at the Autonomous University of Barcelona (UAB), Spain. Nanoindentation involves the application of a controlled force to localized sample areas with the diamond indenter, gradually increasing the force to a set maximum and then decreasing it back to zero, allowing the surface to elastically retract. This process generates load-depth curves, from which data on [deformation mechanisms](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/deformation-mechanism) and elastic recovery are extracted.

For each mineral, a series of 6–12 indentations were executed, applying a maximum force of 25 mN, while maintaining thermal drift below 0.05 nm/s. Corrections for the contact area were made using a calibrated fused silica sample, alongside adjustments for initial indentation depth and instrument compliance, as per [[33]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0165). The hardness (*H)* and the reduced Young’s modulus (*E*<sub>r</sub>) were calculated from the load-displacement curves according to the methodology outlined by Oliver et al. [[34]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0170).

The Young’s modulus quantifies material stiffness, indicating its resistance to deformation under applied force. The *E*<sub>r</sub>, an [elastic property](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/elasticity) assessed in nanoindentation, adjusts Young’s modulus to account for interactions between the sample and indenter tip, combining the material’s and the indenter’s elastic displacements. This is described by the equation $\frac{1}{{E}_{\mathrm{r}}}=\frac{1-{\nu }^{2}}{E}-\frac{1-{\nu }_{i}^{2}}{{E}_{i}}$, where *E* and *ν* are the sample’s Young’s modulus and Poisson’s ratio, respectively; and *E<sub>i</sub>*=1140 GPa and *ν<sub>i</sub>=*0.07 are those of the diamond indenter. Hardness is defined as $H=\frac{{P}_{\mathrm{m}\mathrm{a}\mathrm{x}}}{A}$, with *P*<sub>max</sub> being the maximum load and *A* the contact area.

Elastic recovery was gauged by the ratio of elastic to total indentation energies (*W*<sub>e</sub>*/W*<sub>t</sub>), with *W*<sub>e</sub> calculated from the unloading curve’s area to the displacement axis and *W*<sub>t</sub> from the loading curve’s area. Plastic behavior was similarly characterized, using the plasticity index (*W*<sub>p</sub>*/W*<sub>t</sub>), offering insights into the material’s resistance to permanent deformation. [Fig. 2](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0010) provides a visual overview of the nanoindentation process applied.

![](https://ars.els-cdn.com/content/image/1-s2.0-S2095268624001010-gr2.jpg)

-

-

Fig. 2. Illustrative figures of the nanoindentation process.

### 3.3. Machine learning techniques

The application ML techniques in this study are bifurcated into two primary domains: classification tasks and regression models, each tailored to dissect distinct aspects of lunar meteorites’ mineralogical and mechanical properties. This approach leverages the intrinsic patterns within the elemental composition data to classify meteorite types and predict their mechanical properties. However, prior to initiating the training of the models, we will conduct a Principal Component Analysis (PCA) for the purpose of dimensionality reduction and feature extraction. PCA will enable us to identify the most significant variables in our dataset that contribute to the variation in mechanical properties of lunar meteorites, as well as to check the consistency of our data.

#### 3.3.1. Classification task

For the classification of lunar meteorites and their constituent minerals, we adopted TabPFN [[35]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0175), a transformer-based model specifically designed for handling small tabular datasets. The advent of transformer models has revolutionized the field of [natural language processing](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/natural-language-processing) [[36]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0180), and their extension into tabular data analysis through models like TabPFN represents a significant leap forward. TabPFN, a prior-data fitted network, stands out for its efficiency in managing datasets of limited size, which is often a critical constraint in specialized scientific domains such as lunar [mineralogy](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/mineralogy). The model’s architecture is fine-tuned to perform [supervised classification](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/supervised-classification) tasks, offering an optimized pathway to interpret complex relationships within the data without the need for extensive computational resources.

In our study, TabPFN was retrained with the explicit goal of analyzing lunar meteorites based on their elemental content, measured in weight percent. This retraining process allowed the model to adapt its parameters to the unique characteristics of our dataset, enhancing its ability to discern not only the type of meteorite but also to classify minerals into specific families and identify individual mineral phases.

#### 3.3.2. Regression models

To predict the mechanical properties of lunar meteorites, a selection of regression models from the scikit-learn library (version 1.4) was utilized [[37]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0185). Scikit-learn, a widely recognized library in the ML community, offers a comprehensive suite of tools for [data mining](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/data-mining) and analysis, including an array of algorithms for regression tasks. To determine the most effective approach, the following models are evaluated individually and compared:

- (1) Linear Regression: A foundational model that assumes a linear relationship between the independent variables (elemental composition) and the dependent variable (mechanical property). It is particularly useful for understanding the direct influence of each element on the meteorite’s mechanical characteristics.
- (2) Decision Tree Regressor: This model applies a tree-like graph of decisions and their possible consequences. It is adept at capturing non-linear relationships and interactions between elements.
- (3) Gradient Boosting Regressor: An ensemble technique that builds models sequentially, each new model correcting errors made by previous ones. It is effective for reducing bias and variance.
- (4) AdaBoost Regressor: Another ensemble method that combines multiple weak learners to create a strong predictive model. It adjusts the weights of incorrectly predicted instances, making it robust to outliers and variance in data.
- (5) Random Forest Regressor: A versatile ensemble of decision trees, known for its high accuracy, ability to deal with unbalanced and missing data, and feature importance evaluation.
- (6) *K*-Neighbors Regressor: A non-parametric method that predicts the value of the dependent variable based on the ‘*k*’ nearest neighbors. This approach is useful for capturing the localized patterns in data.

In the development of the predictive models, the dataset was randomly divided into two subsets: 80% was allocated for training and the remaining 20% was reserved for validation. This partitioning ensures that most of the data is used to train the models, while still holding out a substantial portion for the unbiased evaluation of model performance. For the training phase, we employed a hyper-parameter optimization technique that performs a randomized search over specified parameter values for an estimator, using the coefficient of determination (*R*<sup>2</sup>) as score metric.

The search was configured with a 5-fold stratified cross-validation to ensure that each fold is a good representative of the whole by maintaining approximately the same percentage of samples of each target class as the complete set. This stratification is important for dealing with imbalanced datasets, enhancing the reliability of the validation process by ensuring that each fold reflects the overall distribution of the data.

The objective of using a random search grid scheme is to explore a wide range of hyper-parameters and identify the most effective combinations for predicting each mechanical property under study. By randomly selecting from the predefined hyper-parameter grid and evaluating model performance across different subsets of the training data, the process fosters a robust estimation of model accuracy and generalizability. Ultimately, this approach facilitates the selection of the best hyper-parameters, which are then used to validate the models’ performance on unseen data. [Table 1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#t0005) shows all hyper-parameter with their possible values employed to search for the best fit.

Table 1. Hyper-parameters grids for multiple regression models in search of the best fit. For a detailed explanation of each parameter and function, refer to the [[37]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0185) documentation.[<sup>a</sup>](https://www.sciencedirect.com/science/article/pii/S2095268624001010#tblfn1)

<table>
  <thead>
    <tr>
      <th scope="col">Regressor model</th>
      <th scope="col">Hiper-parameter</th>
      <th scope="col">Possible values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linear</td>
      <td>fit_intercept</td>
      <td>True, False</td>
    </tr>
    <tr>
      <td></td>
      <td>positive</td>
      <td>True, False</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td>criterion</td>
      <td>squared_error, friedman_mse, abs_error, poisson</td>
    </tr>
    <tr>
      <td></td>
      <td>splitter</td>
      <td>best, random</td>
    </tr>
    <tr>
      <td></td>
      <td>max_depth</td>
      <td>None, 3, 5, 10, 20</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_split</td>
      <td>2–20 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_leaf</td>
      <td>1–10 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>max_features</td>
      <td>None, sqrt, log2, 0.1, 0.325, 0.55, 0.775, 1.0</td>
    </tr>
    <tr>
      <td></td>
      <td>ccp_alpha</td>
      <td>0.0, 0.01, 0.1</td>
    </tr>
    <tr>
      <td></td>
      <td>min_impurity_decrease</td>
      <td>0.0, 0.01, 0.1</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Gradient Boosting</td>
      <td>loss</td>
      <td>squared_error, absolute_error, huber, quantile</td>
    </tr>
    <tr>
      <td></td>
      <td>learning_rate</td>
      <td>1×10<sup>−3</sup>, 1 (loguniform)</td>
    </tr>
    <tr>
      <td></td>
      <td><em>n</em>_estimators</td>
      <td>50–201</td>
    </tr>
    <tr>
      <td></td>
      <td>subsample</td>
      <td>0.5–1.5 (linear scale)</td>
    </tr>
    <tr>
      <td></td>
      <td>criterion</td>
      <td>friedman_mse, squared_error</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_split</td>
      <td>2–20 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_leaf</td>
      <td>1–11</td>
    </tr>
    <tr>
      <td></td>
      <td>max_depth</td>
      <td>1–11</td>
    </tr>
    <tr>
      <td></td>
      <td>min_impurity_decrease</td>
      <td>0.0–0.1 (linear scale)</td>
    </tr>
    <tr>
      <td></td>
      <td>max_leaf_nodes</td>
      <td>10–51</td>
    </tr>
    <tr>
      <td></td>
      <td>alpha</td>
      <td>0.01–0.99 (linear scale)</td>
    </tr>
    <tr>
      <td></td>
      <td>ccp_alpha</td>
      <td>0.0–0.1 (linear scale)</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>AdaBoost</td>
      <td><em>n</em>_estimators</td>
      <td>25–200</td>
    </tr>
    <tr>
      <td></td>
      <td>learning_rate</td>
      <td>1e−3, 1 (loguniform)</td>
    </tr>
    <tr>
      <td></td>
      <td>loss</td>
      <td>linear, square, exponential</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td><em>n</em>_estimators</td>
      <td>50–200 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>max_features</td>
      <td>auto, sqrt, log2</td>
    </tr>
    <tr>
      <td></td>
      <td>max_depth</td>
      <td>10–30 (randint values)</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_split</td>
      <td>2–20 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>min_samples_leaf</td>
      <td>1–10 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>bootstrap</td>
      <td>True, False</td>
    </tr>
    <tr>
      <td></td>
      <td>criterion</td>
      <td>squared_error, friedman_mse, abs_error, poisson</td>
    </tr>
    <tr>
      <td></td>
      <td>max_leaf_nodes</td>
      <td>10–50 (randint values)</td>
    </tr>
    <tr>
      <td></td>
      <td>ccp_alpha</td>
      <td>0.0–0.1 (linear scale)</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td><em>K</em>-Neighbors</td>
      <td><em>n</em>_neighbors</td>
      <td>1–30 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td>weights</td>
      <td>uniform, distance</td>
    </tr>
    <tr>
      <td></td>
      <td>algorithm</td>
      <td>ball_tree, kd_tree, brute</td>
    </tr>
    <tr>
      <td></td>
      <td>leaf_size</td>
      <td>10–50 (randint)</td>
    </tr>
    <tr>
      <td></td>
      <td><em>p</em></td>
      <td>1, 2, 3</td>
    </tr>
    <tr>
      <td></td>
      <td>metric</td>
      <td>minkowski, manhattan, euclidean, chebyshev</td>
    </tr>
  </tbody>
</table>

a

https://scikit-learn.org/1.4/index.html.

## 4. Results and discussion

The aim of the present work is twofold: first, to explore the usefulness of ML techniques to classify meteorite minerals by using solely elemental compositions measured with SEM-EDS. Second, to explore the ability of different regression models to predict the mechanical properties of mineral meteorites from their elemental composition. For this research, an investigation into the mechanical characteristics of lunar meteorites with nanoindentation measurements was undertaken, alongside the identification of the principal mineral present in each nanoindented region as inferred from its atomic compositions. The results from the nanoindentation tests and the corresponding atomic compositions measured by SEM-EDS for the 126 individual analysis areas (for the different meteorites included in this study) are systematically compiled in [Table A1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0075) of the Supplementary material. Each mineral is identified according to the measured elemental composition. Minerals that did not clearly fall into the categories of [pyroxenes](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/pyroxene), olivines, or feldspars due to indistinct characteristics observed under SEM are classified as ‘other silicate’. [Table 2](https://www.sciencedirect.com/science/article/pii/S2095268624001010#t0010) shows the number of instances per label.

Table 2. Number of instances per label.

| Meteorite | Number | Group | Number | Mineral | Number |
| --- | --- | --- | --- | --- | --- |
| NWA 11444 | 51 | Feldspar | 38 | Anorthite | 38 |
| JAH 838 | 49 | Pyroxene | 36 | Pigeonite/Enstatite | 19 |
| DHOFAR 1084 | 26 | Olivine | 18 | Forsterite | 18 |
|  |  | Other silicate | 12 | Other silicate | 12 |
|  |  | Spinel | 9 | Titanomagnetite | 9 |
|  |  | Carbonate | 9 | Calcite | 9 |
|  |  | Oxide | 4 | Pigeonite | 8 |
|  |  |  |  | Diopside/Augite | 5 |
|  |  |  |  | Diopside | 4 |
|  |  |  |  | Ilmenite | 4 |

Before applying ML methodologies to the compositional data and the nanoindentation experiments, we first pay attention to the nanoindentation results to evaluate their consistency. In [Fig. 3](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0015), the average *H* for each type of mineral is plotted against the corresponding *E*<sub>r</sub>. The data points are grouped by the specific type of identified mineral. It is observed that the three types of ‘other silicate’ minerals, which have been indented, display distinct mechanical properties. There appears to be a clear relationship between their atomic compositions and their mechanical properties: An increase in the percentage of the ‘other’ element within these minerals is associated with increases in both hardness and reduced Young’s modulus. We decide to plot the relationship between ${H}^{3}$ and ${E}_{\mathrm{r}}^{2}$, as this ratio is posited to correlate with wear characteristics—a metric reflecting a material’s resistance to [plastic deformation](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/plastic-deformation) under loaded contact, commonly referred to as yield pressure [[38]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0190), [[39]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0195).

![](https://ars.els-cdn.com/content/image/1-s2.0-S2095268624001010-gr3.jpg)

-

-

Fig. 3. Mean hardness versus mean reduced Young’s modulus for all the nanoindentation tests.

Within each identified mineral group, there is a general homogeneity in composition, albeit with minor variations in certain elements. ${H}^{3}/{E}_{\mathrm{r}}^{2}$, a proxy for the mechanical performance of the minerals, tends to remain uniform across minerals within the same group. Furthermore, there is a notable range in mechanical properties observed among the individual minerals, suggesting variability that may be attributed to factors beyond composition, such as structural or crystallographic differences.

On the other hand, to analyze the potential and consistency of the compositional data for classification purposes, we have performed a PCA. The PCA biplot provided in [Fig. 4](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0020) shows both the scores (transformed coordinates of the original data points, in this case meteorite and mineral groups, in the new principal component space) and loadings (weights assigned to each original variable, in this case elemental composition) of the first two principal components derived from the elemental composition data of different lunar meteorites. From the given transformation matrix, we can infer how each element contributes to the Principal Components (PC).

![](https://ars.els-cdn.com/content/image/1-s2.0-S2095268624001010-gr4.jpg)

-

-

Fig. 4. Principal components of the atomic composition measurements.

Note: Human classification by meteorite and mineral family is shown.

The first PC captures the maximum variance in the dataset. In this case, the elements with the highest loadings (and therefore the greatest influence on PC1) are Fe, Ti, and Cr, as indicated by their vectors pointing towards the positive end of the PC1 axis. Conversely, O, Na, Al, Si, and S show negative loadings, suggesting that they contribute inversely to PC1. This component seems to represent a change from iron, chromium, and titanium-rich minerals to those rich in oxygen, sodium, aluminum, silicon, and sulfur. Oxides and spinels are primarily characterized by elements such as Cr, Ti, and Fe, whereas feldspars exhibit a stronger influence from elements like sodium Na, Al, and Si. Note that, according to the data of [Table A1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0075), the spinels analyzed are mainly the Fe/Ti bearing species, i.e. [titanomagnetite](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/titanomagnetite).

Mg and Si have the strongest negative loading on PC2. The highest positive loading is observed for Ca and Al. Clearly distinguishing between mineral groups exhibits positive and negative variations along PC2, such as carbonates, from those like pyroxenes and olivines.

The biplot indicates that the meteorites are spread across the PC1 and PC2 space, each potentially characterized by different elemental abundances. Specific mineral groups, such as carbonates, oxide, and spinel, are clustered together, indicating similarity in their elemental makeup as captured by the PCA. However, spinel is subclustered in two subgroups, each one corresponding to a different meteorite, suggesting differences in the composition. It is notable that the olivines, feldspar, and ‘other silicate’ are quite distinct in this PCA space, which suggests a more heterogeneous elemental composition.

As can be seen in [Table A1](https://www.sciencedirect.com/science/article/pii/S2095268624001010#s0075) and [Fig. 4](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0020), there are distinct variations in the lunar spinel compositions. A solid solution of magnetite (Fe<sub>3</sub>O<sub>4</sub>) and ulvospinel (TiFe<sub>2</sub>O<sub>4</sub>) (titanomagnetite) could be inferred, as well as broader variations of dark spinels, such as magnesioferrite (MgFe<sub>2</sub>O<sub>4</sub>) and magnesiochromite (MgCr<sub>2</sub>O<sub>4</sub>). The presence of both Mg and Cr would deserve further investigation due to its potential implications for understanding lunar mineral formation and the [geological processes](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/geological-process) involved in their surface occurrence. [Fig. 4](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0020) shows well-separated clusters for different spinels. The separation may result from varying Fe/Ti ratios, but the roles of Mg and Cr require further consideration. The significance of [ilmenite](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/ilmenite) and Ti-spinel species in future [lunar exploration](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-exploration) is of great importance, as lunar ilmenite is a potential source of Ti and He-3 isotopes [[40]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0200). This may open a possibility to better understand the titanium distributions between different minerals in lunar [basalts](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/basalt) after performing similar laboratory analysis for lunar meteorites with identified places of origin on the Moon. Using PCA not only enhances our understanding of the dataset but also enables us to verify the consistency of mineral labeling. Upon confirming the data’s integrity, we can now proceed to apply ML techniques.

### 4.1. TabPFN to classify lunar meteorites and their constituent minerals

The classification outcomes detailed in [Table 3](https://www.sciencedirect.com/science/article/pii/S2095268624001010#t0015) demonstrate an exceptional level of precision in the model’s performance across various categories. Specifically, in the categorization of meteorites, the model achieved a notable accuracy of 92.3% and an F1 score of 90.7%, with the computation concluding in approximately 4 s. These results were obtained on an Intel i9 processor operating at 2.3 GHz. This level of accuracy indicates the model’s robust capability in correctly identifying the meteorite samples from the dataset, with the F1 score reflecting a balanced measure of the model’s precision and recall, thereby confirming its effectiveness in classifying meteorite types.

Table 3. Classification results with TabPFN.

| Target | Accuracy | F1 score | Time (s) |
| --- | --- | --- | --- |
| Meteorite | 0.923 | 0.907 | 4.06 |
| Family | 1 | 1 | 4.20 |
| Mineral | 1 | 1 | 4.94 |

In the classifications concerning the family and individual minerals, the model exhibited unparalleled performance, achieving perfect accuracy and F1 scores of 100%. This indicates that the model is exceptionally adept at distinguishing between different families of minerals and identifying specific minerals within those families, showcasing its detailed understanding and representation of the dataset’s inherent patterns. The slight increase in computational time to 4.20 s for family classification and to 4.94 s for mineral classification is minimal, considering the complexity and the refined granularity of the classification tasks at these levels. The runtime and memory demand of the TabPFN architecture employed in this study increase quadratically with the number of inputs. Consequently, processing larger sequences presents significant challenges on contemporary consumer GPUs.

These results underscore the efficacy of the applied ML model in classifying minerals with small training dataset. The high accuracy and F1 scores across different classification levels highlight the model’s potential as a powerful tool in the scientific analysis of lunar meteorites, providing insights that are not only accurate but also attained with commendable speed and efficiency.

Here we have assessed the usefulness of ML techniques to classify meteorite minerals and samples from semiquantitative compositional data obtained by SEM-EDS. At the present stage, it is clear that this work only has an exploratory character, as only a limited set of meteorites and minerals has been included in the analysis. However, we have seen that TabPFN is capable to correctly classify both meteorites and meteorite minerals with a perfect accuracy. Therefore, it can be envisaged that the present methodology could be easily implemented in SEM-EDS labs to automatically identify minerals and sample types. In the case of meteoritics, for instance, the present methodology could be employed to classify [ordinary chondrites](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/ordinary-chondrite) and [carbonaceous chondrites](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/carbonaceous-chondrite) in a fast and relatively simple manner. With the advent of benchtop SEM-EDS instruments, meteorite classification could be achieved with minor sample preparation, and this could be particularly useful as a non-destructive means to characterize valuable meteorite samples.

### 4.2. *T* prediction of mechanical properties with regression models

The outcomes of the hyperparameter tuning are summarized in [Table 4](https://www.sciencedirect.com/science/article/pii/S2095268624001010#t0020), which details the optimal settings identified for each model and settings when applied to predict different mechanical properties. These settings represent the most effective hyperparameters, as determined by the randomized grid search process, which utilized a stratified 5-fold cross-validation approach.

Table 4. Best hyper-parameters fitted for each model across different mechanical property predictions.

<table>
  <thead>
    <tr>
      <th scope="col">Regressor model</th>
      <th scope="col">Target</th>
      <th scope="col">Best hyper-parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linear</td>
      <td><em>H</em></td>
      <td>positive<em>:</em> False<em>,</em> fit_intercept<em>:</em> True</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>positive<em>:</em> False<em>,</em> fit_intercept<em>:</em> True</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub><em>/W</em><sub>t</sub></td>
      <td>positive<em>:</em> False<em>,</em> fit_intercept<em>:</em> True</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td><em>H</em></td>
      <td>ccp_alpha: 0.0<em>,</em> criterion<em>:</em> friedman_mse<em>,</em> max_depth: 20<em>,</em> max_features: None<em>,</em> min_impurity_decrease: 0.01<em>,</em> min_samples_leaf: 1<em>,</em> min_samples_split: 2<em>,</em> splitter: random</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>ccp_alpha<em>:</em> 0.01<em>,</em> criterion: squared_error, max_depth: None, max_features: 0.55, min_impurity_decrease: 0.0<em>,</em> min_samples_leaf: 1<em>,</em> min_samples_split: 3, splitter: best</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub><em>/W</em><sub>t</sub></td>
      <td>ccp_alpha<em>:</em> 0.0<em>,</em> criterion: squared_error, max_depth: None, max_features: 1.0<em>,</em> min_impurity_decrease: 0.0<em>,</em> min_samples_leaf: 1<em>,</em> min_samples_split: 5<em>,</em> splitter: best</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Gradient Boosting</td>
      <td><em>H</em></td>
      <td>alpha: 0.01<em>,</em> ccp_alpha: 0.0, criterion: friedman_mse, learning_rate: 0.3335, loss: squared_error, max_depth: 3, max_leaf_nodes<em>: 42,</em> min_impurity_decrease: 0.0, min_samples_leaf: 3, min_samples_split: 8, <em>n</em>_estimators<em>:</em> 117, subsample: 0.7</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>alpha: 0.99, ccp_alpha: 0.022, criterion: friedman_mse, learning_rate: 0.3108, loss: huber, max_depth: 6, max_leaf_nodes: 35<em>,</em> min_impurity_decrease: 0.0, min_samples_leaf: 1, min_samples_split: 15, <em>n</em>_estimators: 171, subsample: 1.0</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub>/<em>W</em><sub>t</sub></td>
      <td>alpha: 0.99, ccp_alpha: 0.033, criterion: friedman_mse, learning_rate: 0.1732, loss: absolute_error, max_depth: 3, max_leaf_nodes: 12, min_impurity_decrease: 0.078, min_samples_leaf: 1, min_samples_split: 14, <em>n</em>_estimators: 166, subsample: 0.9</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>AdaBoost</td>
      <td><em>H</em></td>
      <td>learning_rate: 0.9887, loss: exponential, <em>n</em>_estimators: 170</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>learning_rate: 0.9885, loss: square, <em>n</em>_estimators: 82</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub>/<em>W</em><sub>t</sub></td>
      <td>learning_rate: 0.8910, loss: square, <em>n</em>_estimators: 38</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td><em>H</em></td>
      <td>bootstrap: False, ccp_alpha: 0.0, criterion: absolute_error, max_depth: 22, max_features: sqrt<em>,</em> max_leaf_nodes: 25, min_samples_leaf: 1<em>,</em> min_samples_split: 3, <em>n</em>_estimators: 156</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>bootstrap: False, ccp_alpha: 0.011, criterion: squared_error, max_depth: 22, max_features: sqrt, max_leaf_nodes: 24, min_samples_leaf: 1, min_samples_split: 4, <em>n</em>_estimators: 125</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub><em>/W</em><sub>t</sub></td>
      <td>bootstrap: False, ccp_alpha: 0.0, criterion: friedman_mse, max_depth: None, max_features: log2, max_leaf_nodes<em>:</em> 31, min_samples_leaf: 1, min_samples_split: 2, <em>n</em>_estimators: 148</td>
    </tr>
    <tr>
      <td colspan="3"><br/></td>
    </tr>
    <tr>
      <td><em>K</em>-Neighbors</td>
      <td><em>H</em></td>
      <td>algorithm: brute, leaf_size: 25, metric: manhattan, metric_params: None, <em>n</em>_neighbors: 1, p: 3, weights: distance</td>
    </tr>
    <tr>
      <td></td>
      <td><em>E</em><sub>r</sub></td>
      <td>algorithm: brute, leaf_size: 16, metric: manhattan, metric_params: None, <em>n</em>_neighbors: 1, p: 1, weights: distance</td>
    </tr>
    <tr>
      <td></td>
      <td><em>W</em><sub>e</sub><em>/W</em><sub>t</sub></td>
      <td>algorithm: ball_tree, leaf_size: 44, metric: manhattan, metric_params: None, <em>n</em>_neighbors: 1, p: 3, weights: uniform</td>
    </tr>
  </tbody>
</table>

Note: For a detailed explanation of each parameter and function, refer to the Scikit-learn documentation.

The best performance for the regression models applied, measured in terms of the *R*<sup>2</sup>, mean absolute error (MAE), and standard deviation absolute error (SDAE), is detailed for each property and model in [Table 5](https://www.sciencedirect.com/science/article/pii/S2095268624001010#t0025)**.** The performance analysis of various models on mechanical properties indicates that the *K*-Neighbors model demonstrates superior predictive accuracy for properties *H* and *E*<sub>r</sub>, with mean absolute errors of 0.05 and 0.62 GPa, respectively. In contrast, while the Decision Tree Model slightly outperforms the *K*-Neighbors Model in predicting *W*<sub>e</sub>*/W*<sub>t</sub>, it exhibits significant limitations in predicting *E*<sub>r</sub>. All models, including Linear, show robust performance in predicting *W*<sub>e</sub>*/W*<sub>t</sub>, suggesting that it is a simpler property to model. The Decision Tree and the Gradient Boosting significantly reduce their performance when predicting *E*<sub>r</sub>.

Table 5. Mechanical property prediction results with regression models.

<table>
  <thead>
    <tr>
      <th rowspan="2" scope="col">Regressor</th>
      <th colspan="3" scope="col"><em>H</em></th>
      <th colspan="3" scope="col"><em>E</em><sub>r</sub></th>
      <th colspan="3" scope="col"><em>W</em><sub>e</sub><em>/W</em><sub>t</sub></th>
    </tr>
    <tr>
      <th scope="col"><em>R</em><sup>2</sup></th>
      <th scope="col">MAE</th>
      <th scope="col">SDAE</th>
      <th scope="col"><em>R</em><sup>2</sup></th>
      <th scope="col">MAE</th>
      <th scope="col">SDAE</th>
      <th scope="col"><em>R</em><sup>2</sup></th>
      <th scope="col">MAE</th>
      <th scope="col">SDAE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Linear</td>
      <td>0.562</td>
      <td>1.044</td>
      <td>1.197</td>
      <td>0.630</td>
      <td>12.9</td>
      <td>13.507</td>
      <td>0.909</td>
      <td>0.025</td>
      <td>0.022</td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td>0.934</td>
      <td>0.281</td>
      <td>0.551</td>
      <td>0.601</td>
      <td>6.00</td>
      <td>18.439</td>
      <td>0.988</td>
      <td>0.006</td>
      <td>0.010</td>
    </tr>
    <tr>
      <td>Gradient Boosting</td>
      <td>0.943</td>
      <td>0.404</td>
      <td>0.403</td>
      <td>0.738</td>
      <td>4.92</td>
      <td>14.924</td>
      <td>0.951</td>
      <td>0.016</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td>AdaBoost</td>
      <td>0.900</td>
      <td>0.660</td>
      <td>0.375</td>
      <td>0.933</td>
      <td>6.17</td>
      <td>5.019</td>
      <td>0.969</td>
      <td>0.014</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td>0.972</td>
      <td>0.301</td>
      <td>0.268</td>
      <td>0.938</td>
      <td>4.30</td>
      <td>6.321</td>
      <td>0.976</td>
      <td>0.011</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td><em>K</em>-Neighbors</td>
      <td>0.996</td>
      <td>0.050</td>
      <td>0.139</td>
      <td>0.995</td>
      <td>0.62</td>
      <td>2.040</td>
      <td>0.987</td>
      <td>0.004</td>
      <td>0.012</td>
    </tr>
  </tbody>
</table>

Note: Coefficient of determination (*R*<sup>2</sup>), mean absolute error (MAE) in GPa, and standard deviation absolute error (SDAE) in GPA are given.

[Fig. 5](https://www.sciencedirect.com/science/article/pii/S2095268624001010#f0025) serves as a visual representation of the performances, showcasing the predictive accuracy of the regression models for the 20% of the data reserved for validation. Across the three plots, the dashed diagonal line represents the ideal scenario where the predicted values perfectly match the measured values. It can be easily observed the superior performance of the *K*-Neighbor model. In the *E*<sub>r</sub> plot, there is a visible higher dispersion compared to the other mechanical properties, indicating a broader variability in the predictions.

![](https://ars.els-cdn.com/content/image/1-s2.0-S2095268624001010-gr5.jpg)

-

-

Fig. 5. Example of comparative accuracy of regression models in predicting mechanical properties.

The most accurate predictions are observed for *W*<sub>e</sub>*/W*<sub>t</sub>, as evidenced by the data points’ tight clustering around the ideal line. This suggests that the *W*<sub>e</sub>*/W*<sub>t</sub> ratio is predicted with greater consistency and less variance, possibly due to the nature of this ratio capturing a more fundamental aspect of the material behavior that is less sensitive to the individual differences among samples or to the prediction model nuances.

These results underscore the potential of employing ML models, especially K-Neighbors regressors, coupled with a broader range of geological and material properties, to predict the mechanical behaviors of lunar meteorites with high precision given a relatively small dataset of atomic compositions.

To further refine the accuracy of mechanical property predictions, it is important to incorporate additional variables that significantly affect a mineral’s mechanical response. Variables such as porosity, crystallographic orientation, and the degree of shock experienced by the sample region are important. These factors can cause substantial differences in mechanical responses, even among minerals with the same elemental composition. For instances Tang et al. [[41]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0205), underscored a significant influence of interphases between minerals and the presence of microcracks in defining the mechanical behavior of rocks. Peña-Asensio et al. [[27]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0135) reveal that terrestrial olivines, under nanoindentation testing, showcase elevated hardness and a greater Young’s modulus relative to their lunar counterparts. Additionally, the alignment of mineral phases along a consistent *H/E*<sub>r</sub> ratio could hint variances in local porosity or density [[42]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0210). Integrating these variables into the predictive models is anticipated to enhance the prediction of meteorite behavior under stress, offering a more comprehensive perspective on the mechanical properties of lunar material.

While the investigation of minerals’ mechanical properties at the [microscale](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/microbalance) yields valuable insights, a direct correlation to the macroscopic mechanical behavior of rocks is not straightforward. This difficulty underscores the need for techniques that can extrapolate findings from the mineral local scale to the rock macroscopic scale.

Xu et al. [[43]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0215) addressed this challenge through their research on the thermally induced microcracks in granite. Their study investigates the role of mineral heterogeneity and the impact of thermal stress on the overall mechanical properties of granite, leveraging high-temperature microscopy coupled with Accurate Grain-Based Modeling (AGBM). Tang et al. [[44]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0220) applied microscale rock mechanics and AGBM to deduce the Young’s modulus of asteroidal rocks. This method merges findings from the level of individual minerals and their interphases to reach a comprehensive understanding of rock mechanics on the macroscale. These studies are instrumental in bridging the microscale mechanical characterization and macroscale [geological phenomena](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/geological-phenomena), enhancing our capacity to predict and interpret the structural integrity and evolution of extraterrestrial rocks and minimizing damage to samples. However, due to the differing mechanical properties of terrestrial minerals compared to extraterrestrial ones [[45]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0225), [[46]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#b0230), we anticipate limitations when extrapolating our predictive models.

## 5. Conclusions

The scarcity of lunar meteorites necessitates non-destructive testing to preserve their scientific value, steering researchers towards microscale rock mechanics experiments and scanning electron microscopy for surface composition analysis. Machine learning algorithms have emerged as a pivotal tool in this realm, enabling the identification of the mineralogy and the prediction of mechanical properties from elemental compositions. In this study, we have applied novel algorithms to predict the mineralogical and mechanical characteristics of selected DHOFAR 1084, JAH 838, and NWA 11444 lunar meteorites, presented as cut and polished sections in a similar way that Lunar samples could be prepared for allowing similar routine tests performed in situ.

The clear separation of spinel clusters achieved through Principal Component Analysis suggests a new way to enhance our understanding of titanium distribution among lunar basalt minerals, addressing the challenges of characterization using telescopic or orbital data. This is important for future exploration as [ilmenite](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/ilmenite) and Ti-spinel species may be valuable sources of Ti and He-3 isotopes.

By applying a prior-data network, specifically the TabPFN model, we achieved almost perfect scores in the classification of meteorites, mineral groups, and individual minerals. The TabPFN model, designed for small and complex datasets, effectively distinguished between these categories based on elemental composition data. This outcome demonstrates the capability of this approach to improve the identification process for minerals in lunar meteorites, offering a more precise and rapid method to their analysis.

The regressor models, particularly the *K*-Neighbor model, demonstrated an outstanding degree of accuracy in estimating mechanical properties such as hardness, reduced Young’s modulus, and elastic recovery. This highlights the potential of Machine Learning techniques in geomechanical research. Nonetheless, it is important to consider additional factors like porosity, crystal orientation, and shock degree that also influence mechanical behavior. Integrating these variables into future models is expected to refine our predictions’ precision and relevance, especially for applications in [lunar exploration](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/lunar-exploration) and in-situ resource utilization.

Our study marks an initial step towards bridging the existing research gap in the scientific literature by applying advanced ML techniques to extraterrestrial minerals, particularly those in lunar meteorites. This effort highlights the potential of cutting-edge computational tools to advance the understanding and processing of lunar materials.

## Acknowledgments

EP-A and JMT-R acknowledges financial support from the project PID2021-128062NB-I00 funded by MCIN/AEI/10.13039/501100011033. The lunar samples studied here were acquired in the framework of grant PGC2018-097374-B-I00 (P.I. JMT-R). This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (No. 865657) for the project “Quantum Chemistry on Interstellar Grains” (QUANTUMGRAIN); AR acknowledges financial support from the FEDER/Ministerio de Ciencia e Innovación–Agencia Estatal de Investigación (No. PID2021-126427NB-I00). Partial financial support from the Spanish Government (No. PID2020-116844RB-C21) and the Generalitat de Catalunya (No. 2021-SGR-00651) is acknowledged. This work was supported by the LUMIO project funded by the Agenzia Spaziale Italiana (No.2024-6-HH.0).

## Appendix A. Supplementary material

The following are the Supplementary data to this article:

Supplementary Data 1.

## References

- [[1]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0005) D. Morgan, R. Jacobs Opportunities and challenges for machine learning in materials science Annu Rev Mater Res, 50 (2020), pp. 71-103 [Crossref](https://doi.org/10.1146/annurev-matsci-070218-010015) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85087867000&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Opportunities%20and%20challenges%20for%20machine%20learning%20in%20materials%20science&publication_year=2020&author=D.%20Morgan&author=R.%20Jacobs)
- [[2]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0010) J.T. McCoy, L. Auret Machine learning applications in minerals processing: A review Miner Eng, 132 (2019), pp. 95-109 [View PDF](https://www.sciencedirect.com/science/article/pii/S0892687518305430/pdfft?md5=a8e6300ff80ee69936ea984618b2b4e7&pid=1-s2.0-S0892687518305430-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0892687518305430) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85057723063&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Machine%20learning%20applications%20in%20minerals%20processing%3A%20A%20review&publication_year=2019&author=J.T.%20McCoy&author=L.%20Auret)
- [[3]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0015) O. Haavisto, J. Kaartinen, H. Hyötyniemi Optical spectrum based measurement of flotation slurry contents Int J Miner Process, 88 (3–4) (2008), pp. 80-88 [View PDF](https://www.sciencedirect.com/science/article/pii/S0301751608001026/pdfft?md5=96cacd495f522c40a27142541fabcad4&pid=1-s2.0-S0301751608001026-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0301751608001026) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-50849121061&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Optical%20spectrum%20based%20measurement%20of%20flotation%20slurry%20contents&publication_year=2008&author=O.%20Haavisto&author=J.%20Kaartinen&author=H.%20Hy%C3%B6tyniemi)
- [[4]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0020) Kewe T, Moffat N, Strobos P, Van Der Spuy D, Paine AP, Keet K. Evaluation of the Blue Cube MQi Slurry Analyser for application in an advanced control system for the optimisation of a Gold Sulphide flotation circuit. In: Proceedings of the 12 AusIMM Mill Operators’ Conference. Melbourne: The Australasian Institute of Mining and Metallurgy; 2014.p.357–62. [Google Scholar](https://scholar.google.com/scholar?q=Kewe%20T%2C%20Moffat%20N%2C%20Strobos%20P%2C%20Van%20Der%20Spuy%20D%2C%20Paine%20AP%2C%20Keet%20K.%20Evaluation%20of%20the%20Blue%20Cube%20MQi%20Slurry%20Analyser%20for%20application%20in%20an%20advanced%20control%20system%20for%20the%20optimisation%20of%20a%20Gold%20Sulphide%20flotation%20circuit.%20In%3A%20Proceedings%20of%20the%2012%20AusIMM%20Mill%20Operators%E2%80%99%20Conference.%20Melbourne%3A%20The%20Australasian%20Institute%20of%20Mining%20and%20Metallurgy%3B%202014.p.357%E2%80%9362.)
- [[5]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0025) M. Karimi, A. Dehghani, A. Nezamalhosseini, S. Talebi Prediction of hydrocyclone performance using artificial neural networks J S Afr Inst Min Metall, 110 (5) (2010), pp. 207-212 [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-77956391148&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Prediction%20of%20hydrocyclone%20performance%20using%20artificial%20neural%20networks&publication_year=2010&author=M.%20Karimi&author=A.%20Dehghani&author=A.%20Nezamalhosseini&author=S.%20Talebi)
- [[6]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0030) K. Mitra, M. Ghivari Modeling of an industrial wet grinding operation using data-driven techniques Comput Chem Eng, 30 (3) (2006), pp. 508-520 [View PDF](https://www.sciencedirect.com/science/article/pii/S0098135405002498/pdfft?md5=fd66e1026c2ac9eb103cc5ddca053646&pid=1-s2.0-S0098135405002498-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0098135405002498) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-30344443674&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Modeling%20of%20an%20industrial%20wet%20grinding%20operation%20using%20data-driven%20techniques&publication_year=2006&author=K.%20Mitra&author=M.%20Ghivari)
- [[7]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0035) A.B. Makokha, M.H. Moys Multivariate approach to on-line prediction of in-mill slurry density and ball load volume based on direct ball and slurry sensor data Miner Eng, 26 (2012), pp. 13-23 [View PDF](https://www.sciencedirect.com/science/article/pii/S0892687511003761/pdfft?md5=eab56a4d82edd49d301b9a780c481077&pid=1-s2.0-S0892687511003761-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0892687511003761) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-84856263599&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Multivariate%20approach%20to%20on-line%20prediction%20of%20in-mill%20slurry%20density%20and%20ball%20load%20volume%20based%20on%20direct%20ball%20and%20slurry%20sensor%20data&publication_year=2012&author=A.B.%20Makokha&author=M.H.%20Moys)
- [[8]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0040) S.C. Chelgani, B. Shahbazi, B. Rezai Estimation of froth flotation recovery and collision probability based on operational parameters using an artificial neural network Int J Miner Metall Mater, 17 (5) (2010), pp. 526-534 [Crossref](https://doi.org/10.1007/s12613-010-0353-1) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-78149455344&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Estimation%20of%20froth%20flotation%20recovery%20and%20collision%20probability%20based%20on%20operational%20parameters%20using%20an%20artificial%20neural%20network&publication_year=2010&author=S.C.%20Chelgani&author=B.%20Shahbazi&author=B.%20Rezai)
- [[9]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0045) A. Jahedsaravani, M.H. Marhaban, M. Massinaei, M.I. Saripan, S.B.M. Noor Froth-based modeling and control of a batch flotation process Int J Miner Process, 146 (2016), pp. 90-96 [View PDF](https://www.sciencedirect.com/science/article/pii/S0301751615300557/pdfft?md5=2fc7798a06a4bd75c996f74284736bc8&pid=1-s2.0-S0301751615300557-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0301751615300557) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-84954149696&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Froth-based%20modeling%20and%20control%20of%20a%20batch%20flotation%20process&publication_year=2016&author=A.%20Jahedsaravani&author=M.H.%20Marhaban&author=M.%20Massinaei&author=M.I.%20Saripan&author=S.B.M.%20Noor)
- [[10]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0050) K. Feng, H.B. Wang, A.J. Xu, D.F. He Endpoint temperature prediction of molten steel in RH using improved case-based reasoning Int J Miner Metall Mater, 20 (12) (2013), pp. 1148-1154 [Crossref](https://doi.org/10.1007/s12613-013-0848-7) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-84893121433&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Endpoint%20temperature%20prediction%20of%20molten%20steel%20in%20RH%20using%20improved%20case-based%20reasoning&publication_year=2013&author=K.%20Feng&author=H.B.%20Wang&author=A.J.%20Xu&author=D.F.%20He)
- [[11]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0055) F.S.V. Gomes, K.F. Côco, J.L.F. Salles Multistep forecasting models of the liquid level in a blast furnace hearth IEEE Trans Autom Sci Eng, 14 (2) (2017), pp. 1286-1296 [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85018512726&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Multistep%20forecasting%20models%20of%20the%20liquid%20level%20in%20a%20blast%20furnace%20hearth&publication_year=2017&author=F.S.V.%20Gomes&author=K.F.%20C%C3%B4co&author=J.L.F.%20Salles)
- [[12]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0060) I. Allegretta, B. Marangoni, P. Manzari, C. Porfido, R. Terzano, O. De Pascale, G.S. Senesi Macro-classification of meteorites by portable energy dispersive X-ray fluorescence spectroscopy (pED-XRF), principal component analysis (PCA) and machine learning algorithms Talanta, 212 (2020), Article 120785 [View PDF](https://www.sciencedirect.com/science/article/pii/S003991402030076X/pdfft?md5=ee558757f529267acb0090e0ec425f08&pid=1-s2.0-S003991402030076X-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S003991402030076X) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85078448027&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Macro-classification%20of%20meteorites%20by%20portable%20energy%20dispersive%20X-ray%20fluorescence%20spectroscopy%20%2C%20principal%20component%20analysis%20%20and%20machine%20learning%20algorithms&publication_year=2020&author=I.%20Allegretta&author=B.%20Marangoni&author=P.%20Manzari&author=C.%20Porfido&author=R.%20Terzano&author=O.%20De%20Pascale&author=G.S.%20Senesi)
- [[13]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0065) L.B. Breitenfeld, A.D. Rogers, T.D. Glotch, V.E. Hamilton, P.R. Christensen, D.S. Lauretta, *et al.* Machine learning mid-infrared spectral models for predicting modal mineralogy of CI/CM chondritic asteroids and bennu J Geophys Res Planets, 126 (12) (2021), p. e07035 [Google Scholar](https://scholar.google.com/scholar_lookup?title=Machine%20learning%20mid-infrared%20spectral%20models%20for%20predicting%20modal%20mineralogy%20of%20CICM%20chondritic%20asteroids%20and%20bennu&publication_year=2021&author=L.B.%20Breitenfeld&author=A.D.%20Rogers&author=T.D.%20Glotch&author=V.E.%20Hamilton&author=P.R.%20Christensen&author=D.S.%20Lauretta)
- [[14]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0070) Dyar MD, Wallace SM, Burbine TH, Sheldon DR. A machine learning classification of meteorite spectra applied to understanding asteroids. \icarus 2023;406:115718. [Google Scholar](https://scholar.google.com/scholar?q=Dyar%20MD%2C%20Wallace%20SM%2C%20Burbine%20TH%2C%20Sheldon%20DR.%20A%20machine%20learning%20classification%20of%20meteorite%20spectra%20applied%20to%20understanding%20asteroids.%20%5Cicarus%202023%3B406%3A115718.)
- [[15]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0075) E. Bruschini, C. Carli, H. Skogby, G.B. Andreozzi, A. Stojic, A. Morlok Spectroscopic characterization of impactites and a machine learning approach to determine the oxidation state of iron in glass-bearing materials JGR Planets, 128 (3) (2023) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Spectroscopic%20characterization%20of%20impactites%20and%20a%20machine%20learning%20approach%20to%20determine%20the%20oxidation%20state%20of%20iron%20in%20glass-bearing%20materials&publication_year=2023&author=E.%20Bruschini&author=C.%20Carli&author=H.%20Skogby&author=G.B.%20Andreozzi&author=A.%20Stojic&author=A.%20Morlok)
- [[16]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0080) G.R.L. Kodikara, L.J. McHenry Machine learning approaches for classifying lunar soils Icarus, 345 (2020), Article 113719 [View PDF](https://www.sciencedirect.com/science/article/pii/S001910352030110X/pdfft?md5=126dcb1d47b17abcdc97c18a78ad9ba5&pid=1-s2.0-S001910352030110X-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S001910352030110X) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85081210589&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Machine%20learning%20approaches%20for%20classifying%20lunar%20soils&publication_year=2020&author=G.R.L.%20Kodikara&author=L.J.%20McHenry)
- [[17]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0085) V. Korokhin, Y. Surkov, U. Mall, V. Kaydash, S. Velichko, Y. Velikodsky, O. Shalygina Applying machine learning to a nonlinear spectral mixing model for mapping lunar soils composition using CHANDRAYAAN-1 M3 data Planet Space Sci, 244 (2024), Article 105870 [View PDF](https://www.sciencedirect.com/science/article/pii/S0032063324000345/pdfft?md5=e940488db05f705a7e01992ff9e76691&pid=1-s2.0-S0032063324000345-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0032063324000345) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85187961682&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Applying%20machine%20learning%20to%20a%20nonlinear%20spectral%20mixing%20model%20for%20mapping%20lunar%20soils%20composition%20using%20CHANDRAYAAN-1%20M3%20data&publication_year=2024&author=V.%20Korokhin&author=Y.%20Surkov&author=U.%20Mall&author=V.%20Kaydash&author=S.%20Velichko&author=Y.%20Velikodsky&author=O.%20Shalygina)
- [[18]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0090) R.L. Korotev Lunar geochemistry as told by lunar meteorites Geochemistry, 65 (4) (2005), pp. 297-346 [View PDF](https://www.sciencedirect.com/science/article/pii/S0009281905000498/pdfft?md5=2e235c14b3fd468ae7509b3dbf4bfd0e&pid=1-s2.0-S0009281905000498-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0009281905000498) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-26944493711&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Lunar%20geochemistry%20as%20told%20by%20lunar%20meteorites&publication_year=2005&author=R.L.%20Korotev)
- [[19]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0095) K.H. Joy, J. Gross, R.L. Korotev, R.A. Zeigler, F.M. McCubbin, J.F. Snape, N.M. Curran, J.F. Pernet-Fisher, T. Arai Lunar meteorites Rev Mineral Geochem, 89 (1) (2023), pp. 509-562 [Crossref](https://doi.org/10.2138/rmg.2023.89.12) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-105031392695&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Lunar%20meteorites&publication_year=2023&author=K.H.%20Joy&author=J.%20Gross&author=R.L.%20Korotev&author=R.A.%20Zeigler&author=F.M.%20McCubbin&author=J.F.%20Snape&author=N.M.%20Curran&author=J.F.%20Pernet-Fisher&author=T.%20Arai)
- [[20]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0100) NASA. The Artemis III Science Definition Team Report. 2020. [Google Scholar](https://scholar.google.com/scholar?q=NASA.%20The%20Artemis%20III%20Science%20Definition%20Team%20Report.%202020.)
- [[21]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0105) C.E. Moyano-Cambero, J.M. Trigo-Rodríguez, E. Pellicer, M. Martínez-Jiménez, J. Llorca, N. Metres, *et al.* Chelyabinsk meteorite as a proxy for studying the properties of potentially hazardous asteroids and impact deflection strategies Assessment and Mitigation of Asteroid Impact Hazards, Springer, Cham (2017), pp. 219-241 [Crossref](https://doi.org/10.1007/978-3-319-46179-3_11) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85018650111&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Chelyabinsk%20meteorite%20as%20a%20proxy%20for%20studying%20the%20properties%20of%20potentially%20hazardous%20asteroids%20and%20impact%20deflection%20strategies&publication_year=2017&author=C.E.%20Moyano-Cambero&author=J.M.%20Trigo-Rodr%C3%ADguez&author=E.%20Pellicer&author=M.%20Mart%C3%ADnez-Jim%C3%A9nez&author=J.%20Llorca&author=N.%20Metres)
- [[22]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0110) J.M. Wheeler Mechanical phase mapping of the Taza meteorite using correlated high-speed nanoindentation and EDX J Mater Res, 36 (1) (2021), pp. 94-104 [Crossref](https://doi.org/10.1557/s43578-020-00056-7) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85101020874&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Mechanical%20phase%20mapping%20of%20the%20Taza%20meteorite%20using%20correlated%20high-speed%20nanoindentation%20and%20EDX&publication_year=2021&author=J.M.%20Wheeler)
- [[23]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0115) Zhang YH, Xu JJ, Tang XH, Paluszny A. Determining the Mechanical Property of Martian Rocks Using Accurate Grain-Based Model. In: 56th U.S. Rock Mechanics/Geomechanics Symposium. Mexico: ARMA; 2022. [Google Scholar](https://scholar.google.com/scholar?q=Zhang%20YH%2C%20Xu%20JJ%2C%20Tang%20XH%2C%20Paluszny%20A.%20Determining%20the%20Mechanical%20Property%20of%20Martian%20Rocks%20Using%20Accurate%20Grain-Based%20Model.%20In%3A%2056th%20U.S.%20Rock%20Mechanics%2FGeomechanics%20Symposium.%20Mexico%3A%20ARMA%3B%202022.)
- [[24]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0120) T.J. Huang Correlative Microscopy and Mechanical Behavior of Extraterrestrial Materials Purdue University Graduate School, West Lafayette (2023) Doctoral dissertation [Google Scholar](https://scholar.google.com/scholar_lookup?title=Correlative%20Microscopy%20and%20Mechanical%20Behavior%20of%20Extraterrestrial%20Materials&publication_year=2023&author=T.J.%20Huang)
- [[25]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0125) J.Y. Nie, Y.F. Cui, K. Senetakis, D. Guo, Y. Wang, G.D. Wang, P Feng, HY He, XH Zhang, XP Zhang, CH Li, H Zheng, WZ Hu, F Niu, Q Liu, AY. Li Predicting residual friction angle of lunar regolith based on Chang’e-5 lunar samples Sci Bull, 68 (7) (2023), pp. 730-739 [View PDF](https://www.sciencedirect.com/science/article/pii/S2095927323001810/pdfft?md5=8027a3f41efd15b0b0187044cfdc2a16&pid=1-s2.0-S2095927323001810-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S2095927323001810) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85150779313&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Predicting%20residual%20friction%20angle%20of%20lunar%20regolith%20based%20on%20Change-5%20lunar%20samples&publication_year=2023&author=J.Y.%20Nie&author=Y.F.%20Cui&author=K.%20Senetakis&author=D.%20Guo&author=Y.%20Wang&author=G.D.%20Wang&author=P%20Feng&author=HY%20He&author=XH%20Zhang&author=XP%20Zhang&author=CH%20Li&author=H%20Zheng&author=WZ%20Hu&author=F%20Niu&author=Q%20Liu&author=AY.%20Li)
- [[26]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0130) M.F. Rabbi Mechanical Behavior of Meteorites: Multiscale Characterization of the Strength and Failure Mechanism Arizona State University, Tempe (2023) Doctoral dissertation [Google Scholar](https://scholar.google.com/scholar_lookup?title=Mechanical%20Behavior%20of%20Meteorites%3A%20Multiscale%20Characterization%20of%20the%20Strength%20and%20Failure%20Mechanism&publication_year=2023&author=M.F.%20Rabbi)
- [[27]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0135) E. Peña-Asensio, J.M. Trigo-Rodríguez, J. Sort, J. Ibáñez-Insa, A. Rimola Mechanical properties of minerals in lunar and HED meteorites from nanoindentation testing: implications for space mining Meteorit Planet Sci, 59 (6) (2024), pp. 1297-1313 [Crossref](https://doi.org/10.1111/maps.14148) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85185656063&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Mechanical%20properties%20of%20minerals%20in%20lunar%20and%20HED%20meteorites%20from%20nanoindentation%20testing%3A%20implications%20for%20space%20mining&publication_year=2024&author=E.%20Pe%C3%B1a-Asensio&author=J.M.%20Trigo-Rodr%C3%ADguez&author=J.%20Sort&author=J.%20Ib%C3%A1%C3%B1ez-Insa&author=A.%20Rimola)
- [[28]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0140) Tanbakouei S, Trigo-Rodríguez JM, Sort J, Michel P, Blum J, Nakamura T, Williams I. Mechanical properties of particles from the surface of asteroid 25143 Itokawa. 2019;629:A119. [Google Scholar](https://scholar.google.com/scholar?q=Tanbakouei%20S%2C%20Trigo-Rodr%C3%ADguez%20JM%2C%20Sort%20J%2C%20Michel%20P%2C%20Blum%20J%2C%20Nakamura%20T%2C%20Williams%20I.%20Mechanical%20properties%20of%20particles%20from%20the%20surface%20of%20asteroid%2025143%20Itokawa.%202019%3B629%3AA119.)
- [[29]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0145) Russell SS, Folco L, Grady MM, Zolensky ME, Jones R, Righter K, Zipfel J, Grossman JN. The meteoritical bulletin, No. 88, 2004 July. Meteorit Planet Sci 2004;39(S8). [Google Scholar](https://scholar.google.com/scholar?q=Russell%20SS%2C%20Folco%20L%2C%20Grady%20MM%2C%20Zolensky%20ME%2C%20Jones%20R%2C%20Righter%20K%2C%20Zipfel%20J%2C%20Grossman%20JN.%20The%20meteoritical%20bulletin%2C%20No.%2088%2C%202004%20July.%20Meteorit%20Planet%20Sci%202004%3B39(S8).)
- [[30]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0150) Bouvier A, Gattacceca J, Agee C, Grossman J, Metzler K. The meteoritical bulletin, No. 104. Meteorit Planet Sci 2017;52(10):2284. [Google Scholar](https://scholar.google.com/scholar?q=Bouvier%20A%2C%20Gattacceca%20J%2C%20Agee%20C%2C%20Grossman%20J%2C%20Metzler%20K.%20The%20meteoritical%20bulletin%2C%20No.%20104.%20Meteorit%20Planet%20Sci%202017%3B52(10)%3A2284.)
- [[31]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0155) R.L. Korotev Update (2012–2017) on lunar meteorites from Oman Meteorit Planet Sci, 52 (6) (2017), pp. 1251-1256 [Crossref](https://doi.org/10.1111/maps.12869) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85017402303&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Update%20%20on%20lunar%20meteorites%20from%20Oman&publication_year=2017&author=R.L.%20Korotev)
- [[32]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0160) Gattacceca J, Bouvier A, Grossman J, Metzler K, Uehara M. The meteoritical bulletin, No. 106. Meteorit Planet Sci 2019;54(2):469–71. [Google Scholar](https://scholar.google.com/scholar?q=Gattacceca%20J%2C%20Bouvier%20A%2C%20Grossman%20J%2C%20Metzler%20K%2C%20Uehara%20M.%20The%20meteoritical%20bulletin%2C%20No.%20106.%20Meteorit%20Planet%20Sci%202019%3B54(2)%3A469%E2%80%9371.)
- [[33]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0165) Fischer-Cripps AC, Nicholson DW. Nanoindentation. mechanical engineering series. Appl Mech Rev 2004;57(2):B12. [Google Scholar](https://scholar.google.com/scholar?q=Fischer-Cripps%20AC%2C%20Nicholson%20DW.%20Nanoindentation.%20mechanical%20engineering%20series.%20Appl%20Mech%20Rev%202004%3B57(2)%3AB12.)
- [[34]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0170) W.C. Oliver, G.M. Pharr An improved technique for determining hardness and elastic modulus using load and displacement sensing indentation experiments J Mater Res, 7 (6) (1992), pp. 1564-1583 [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85140793691&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=An%20improved%20technique%20for%20determining%20hardness%20and%20elastic%20modulus%20using%20load%20and%20displacement%20sensing%20indentation%20experiments&publication_year=1992&author=W.C.%20Oliver&author=G.M.%20Pharr)
- [[35]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0175) Hollmann N, Müller S, Eggensperger K, Hutter F. TabPFN: A transformer that solves small tabular classification problems in a second. 2022:arXiv:2207.01848. [Google Scholar](https://scholar.google.com/scholar?q=Hollmann%20N%2C%20M%C3%BCller%20S%2C%20Eggensperger%20K%2C%20Hutter%20F.%20TabPFN%3A%20A%20transformer%20that%20solves%20small%20tabular%20classification%20problems%20in%20a%20second.%202022%3AarXiv%3A2207.01848.)
- [[36]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0180) Wolf T, Debut L, Sanh V, Chaumond J, Delangue C, Moi A, Cistac P, Rault T, Louf R, Morgan Funtowicz, Davison J, Shleifer S, von Platen P, Ma C, Jernite Y, Plu J, Xu CW, Scao TL, Gugger S, Drame M, Lhoest Q, Rush A. Transformers: State-of-the-Art Natural Language Processing Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. Online. Stroudsburg: Association for Computational Linguistics; 2020.p.38–45. [Google Scholar](https://scholar.google.com/scholar?q=Wolf%20T%2C%20Debut%20L%2C%20Sanh%20V%2C%20Chaumond%20J%2C%20Delangue%20C%2C%20Moi%20A%2C%20Cistac%20P%2C%20Rault%20T%2C%20Louf%20R%2C%20Morgan%20Funtowicz%2C%20Davison%20J%2C%20Shleifer%20S%2C%20von%20Platen%20P%2C%20Ma%20C%2C%20Jernite%20Y%2C%20Plu%20J%2C%20Xu%20CW%2C%20Scao%20TL%2C%20Gugger%20S%2C%20Drame%20M%2C%20Lhoest%20Q%2C%20Rush%20A.%20Transformers%3A%20State-of-the-Art%20Natural%20Language%20Processing%20Proceedings%20of%20the%202020%20Conference%20on%20Empirical%20Methods%20in%20Natural%20Language%20Processing%3A%20System%20Demonstrations.%20Online.%20Stroudsburg%3A%20Association%20for%20Computational%20Linguistics%3B%202020.p.38%E2%80%9345.)
- [[37]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0185) F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, A. Müller, J. Nothman, G. Louppe, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, É. Duchesnay Scikit-learn: Machine learning in Python J Mach Learn Res, 12 (10) (2011), pp. 2825-2830 [Google Scholar](https://scholar.google.com/scholar_lookup?title=Scikit-learn%3A%20Machine%20learning%20in%20Python&publication_year=2011&author=F.%20Pedregosa&author=G.%20Varoquaux&author=A.%20Gramfort&author=V.%20Michel&author=B.%20Thirion&author=O.%20Grisel&author=M.%20Blondel&author=A.%20M%C3%BCller&author=J.%20Nothman&author=G.%20Louppe&author=P.%20Prettenhofer&author=R.%20Weiss&author=V.%20Dubourg&author=J.%20Vanderplas&author=A.%20Passos&author=D.%20Cournapeau&author=M.%20Brucher&author=M.%20Perrot&author=%C3%89.%20Duchesnay)
- [[38]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0190) J. Musil, F. Kunc, H. Zeman, H. Poláková Relationships between hardness, Young’s modulus and elastic recovery in hard nanocomposite coatings Surf Coat Technol, 154 (2–3) (2002), pp. 304-313 [View PDF](https://www.sciencedirect.com/science/article/pii/S0257897201017145/pdfft?md5=8f85f629a35869df1267bf18e18c0fbe&pid=1-s2.0-S0257897201017145-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0257897201017145) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-0037094338&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Relationships%20between%20hardness%2C%20Youngs%20modulus%20and%20elastic%20recovery%20in%20hard%20nanocomposite%20coatings&publication_year=2002&author=J.%20Musil&author=F.%20Kunc&author=H.%20Zeman&author=H.%20Pol%C3%A1kov%C3%A1)
- [[39]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0195) E. Pellicer, A. Varea, S. Pané, B.J. Nelson, E. Menéndez, M. Estrader, S. Suriñach, M.D. Baró, J. Nogues, J. Sort Nanocrystalline electroplated Cu–Ni: metallic thin films with enhanced mechanical properties and tunable magnetic behavior Adv Funct Materials, 20 (6) (2010), pp. 983-991 [Crossref](https://doi.org/10.1002/adfm.200901732) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-77950193675&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Nanocrystalline%20electroplated%20CuNi%3A%20metallic%20thin%20films%20with%20enhanced%20mechanical%20properties%20and%20tunable%20magnetic%20behavior&publication_year=2010&author=E.%20Pellicer&author=A.%20Varea&author=S.%20Pan%C3%A9&author=B.J.%20Nelson&author=E.%20Men%C3%A9ndez&author=M.%20Estrader&author=S.%20Suri%C3%B1ach&author=M.D.%20Bar%C3%B3&author=J.%20Nogues&author=J.%20Sort)
- [[40]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0200) L.J. Wittenberg, E.N. Cameron, G.L. Kulcinski, S.H. Ott, J.F. Santarius, G. Sviatoslavsky, *et al.* A review of 3He resources and acquisition for use as fusion fuel Fusion Technol, 21 (4) (1992), pp. 2230-2253 [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-0026896721&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=A%20review%20of%203He%20resources%20and%20acquisition%20for%20use%20as%20fusion%20fuel&publication_year=1992&author=L.J.%20Wittenberg&author=E.N.%20Cameron&author=G.L.%20Kulcinski&author=S.H.%20Ott&author=J.F.%20Santarius&author=G.%20Sviatoslavsky)
- [[41]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0205) X.H. Tang, Y.H. Zhang, J.J. Xu, J. Rutqvist, M.S. Hu, Z.Z. Wang, Q. Liu Determining Young’s modulus of granite using accurate grain-based modeling with microscale rock mechanical experiments Int J Rock Mech Min Sci, 157 (2022), Article 105167 [View PDF](https://www.sciencedirect.com/science/article/pii/S1365160922001332/pdfft?md5=90dfa31df059bd7b06fc098425bb85e1&pid=1-s2.0-S1365160922001332-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S1365160922001332) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85134431045&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Determining%20Youngs%20modulus%20of%20granite%20using%20accurate%20grain-based%20modeling%20with%20microscale%20rock%20mechanical%20experiments&publication_year=2022&author=X.H.%20Tang&author=Y.H.%20Zhang&author=J.J.%20Xu&author=J.%20Rutqvist&author=M.S.%20Hu&author=Z.Z.%20Wang&author=Q.%20Liu)
- [[42]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0210) J. Luo, R. Stevens Porosity-dependence of elastic moduli and hardness of 3Y-TZP ceramics Ceram Int, 25 (3) (1999), pp. 281-286 [View PDF](https://www.sciencedirect.com/science/article/pii/S0272884298000376/pdfft?md5=da5e6de7d0c13944aa03c303275be1b3&pid=1-s2.0-S0272884298000376-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0272884298000376) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-0032663299&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Porosity-dependence%20of%20elastic%20moduli%20and%20hardness%20of%203Y-TZP%20ceramics&publication_year=1999&author=J.%20Luo&author=R.%20Stevens)
- [[43]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0215) Xu JJ, Zhang YH, Rutqvist J, Hu MS, Wang ZZ, Tang XH. Thermally induced microcracks in granite and their effect on the macroscale mechanical behavior. J Geophys Res Solid Earth 2023;128(1):e2022JB024920. [Google Scholar](https://scholar.google.com/scholar?q=Xu%20JJ%2C%20Zhang%20YH%2C%20Rutqvist%20J%2C%20Hu%20MS%2C%20Wang%20ZZ%2C%20Tang%20XH.%20Thermally%20induced%20microcracks%20in%20granite%20and%20their%20effect%20on%20the%20macroscale%20mechanical%20behavior.%20J%20Geophys%20Res%20Solid%20Earth%202023%3B128(1)%3Ae2022JB024920.)
- [[44]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0220) X.H. Tang, J.J. Xu, Y.H. Zhang, H.F. Zhao, A. Paluszny, X. Wan, ZZ. Wang The rock-forming minerals and macroscale mechanical properties of asteroid rocks Eng Geol, 321 (2023), p. 107154 [View PDF](https://www.sciencedirect.com/science/article/pii/S0013795223001722/pdfft?md5=8e143d9b4637de928a01bce0f6af31dc&pid=1-s2.0-S0013795223001722-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S0013795223001722) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85159186292&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=The%20rock-forming%20minerals%20and%20macroscale%20mechanical%20properties%20of%20asteroid%20rocks&publication_year=2023&author=X.H.%20Tang&author=J.J.%20Xu&author=Y.H.%20Zhang&author=H.F.%20Zhao&author=A.%20Paluszny&author=X.%20Wan&author=ZZ.%20Wang)
- [[45]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0225) P. Grèbol-Tomàs, J.M. Trigo-Rodríguez, J. Ibáñez-Insa, E. Peña-Asensio, R. Cuscó, I. Weber, *et al.* Nanoindentation of Lunar Basalts: Mechanical Properties of the Northwest Africa (NWA) 12008 Meteorite 55th Lunar and Planetary Science Conference, 3040, LPI Contributions, The Woodlands (2024), p. 1108 [Google Scholar](https://scholar.google.com/scholar_lookup?title=Nanoindentation%20of%20Lunar%20Basalts%3A%20Mechanical%20Properties%20of%20the%20Northwest%20Africa%20%2012008%20Meteorite&publication_year=2024&author=P.%20Gr%C3%A8bol-Tom%C3%A0s&author=J.M.%20Trigo-Rodr%C3%ADguez&author=J.%20Ib%C3%A1%C3%B1ez-Insa&author=E.%20Pe%C3%B1a-Asensio&author=R.%20Cusc%C3%B3&author=I.%20Weber)
- [[46]](https://www.sciencedirect.com/science/article/pii/S2095268624001010#bb0230) R. Li, G. Zhou, K. Yan, J. Chen, D. Chen, S. Cai, PQ. Mo Preparation and characterization of a specialized lunar regolith simulant for use in lunar low gravity simulation Int J Min Sci Technol, 32 (1) (2022), pp. 1-15 [View PDF](https://www.sciencedirect.com/science/article/pii/S2095268621001002/pdfft?md5=a89a1f8dc0b7da9fe4087b7f2f015634&pid=1-s2.0-S2095268621001002-main.pdf) [View article](https://www.sciencedirect.com/science/article/pii/S2095268621001002) [View in Scopus](https://www.scopus.com/inward/record.url?eid=2-s2.0-85117751422&partnerID=10&rel=R3.0.0) [Google Scholar](https://scholar.google.com/scholar_lookup?title=Preparation%20and%20characterization%20of%20a%20specialized%20lunar%20regolith%20simulant%20for%20use%20in%20lunar%20low%20gravity%20simulation&publication_year=2022&author=R.%20Li&author=G.%20Zhou&author=K.%20Yan&author=J.%20Chen&author=D.%20Chen&author=S.%20Cai&author=PQ.%20Mo)
