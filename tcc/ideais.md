# ideas

## one shot ideias

- sentinel tem resoulução melhor 10m contra 30m do landsat, talvez dropar landsat

After reading a paper on the multiple reasons as to why creating a ml model for raw ore identification on the surface of the earth is almost unfeasible, i decided to take a naive aproach of pretending that these problems dont exist

ja que aparentemente é impossivel crir um dataset é melhor:

4.4. Philosophical differences in exploration
Mineral exploration poses unique challenges for the application of machine learning (ML), differing fundamentally from its use in more conventional contexts. Unlike traditional applications, where ML models aim to identify patterns with high accuracy, mineral exploration requires searching a finite space for subtle variations that may signal undiscovered ore deposits. This process involves training models to recognise patterns derived from known orebodies, to predict the locations of undiscovered orebodies. However, contrary to conventional applications of ML, an emphasis on achieving high accuracy may paradoxically hinder success.[https://www.sciencedirect.com/science/article/pii/S2772883825000111]

A significant limitation arises from the scarcity of training data, since only a small number of known ore deposits are available, and these deposits are unlikely to perfectly resemble those yet to be discovered. Since mining involves sampling without replacement, undiscovered deposits will likely exhibit variations that diverge from the training dataset. Consequently, a different philosophical approach is necessary. Instead of prioritising model accuracy, practitioners are encouraged to adopt an exploratory mindset when applying ML in mineral exploration.[https://www.sciencedirect.com/science/article/pii/S2772883825000111]

segundo [https://www.sciencedirect.com/science/article/pii/S2666544123000059#sec2.1], utilizar multispectral é melhor pois tem menos bandas e consequentemente diminui o numero de features do dataset, uma dimensionalidade maior pode ser erroneamente associada a uma melhora no treinamento de um modelo de IA, hyperspectral possuem mais bandas conseguentemente mais features, so que essas features possui um co-linearidade muito alta entre features proximas oq acaba não melhorando o modelo e sim piorando

se eu for fazer analise das imagens, [https://www.sciencedirect.com/science/article/pii/S2666544123000059#sec2.1] diz que "For mineral exploration and lithological classification, radiometric correction is important to minimize pixel error in spectral data (Rajendran and Nasir, 2014; examples in Cooley et al., 2002; Salem et al., 2016). Radiometric calibration optimized remote sensing images for best radiance, reflectance or brightness temperatures."
