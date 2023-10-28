# Prediccion-Precio-Casas-Modelo-Ridge-Regressor
Os dejo un modelo de regresión lineal Ridge, entrenado para predecir el precio de casas a partir de un set de datos obtenido mediante web scraping. En primer lugar os adjunto el archivo de web scraping a idealista.com (WebScraping BeautifulSoap y Selenium Idealista_1.ipynb), para obtener el dataset que utilizaremos en el modelo Ridge. En segundo lugar, os adjunto el archivo donde realizo el análisis exploratorio, y el ajuste del modelo Ridge (ADE y Ajuste modelo regresión lineal Casas Idealista_2.ipynb). Y en tercer lugar, os adjunto también un tercer archivo donde creo un pipeline, en el cual hago un procesado de los datos antes de pasárselos al modelo, incluyendo una transformación logarítmica, para obetener mejores resultados en el ajuste del mismo (Pipeline Ridge con transformación Casas Idealista_3.ipynb). Finalmente, os dejo el archivo que he creado con Shiny para que el usuario pueda interactuar facilmente con el modelo predictivo (app.py).
Here you have Ridge linear regression model, trained to predict the price of houses from a data set obtained through web scraping. First of all, I attach the web scraping file to idealista.com (WebScraping BeautifulSoap y Selenium Idealista_1.ipynb), to obtain the dataset that we will use in the Ridge model. Secondly, I attach the file where I realise the exploratory analysis, and the adjustment of the Ridge model (ADE y Ajuste modelo regresión lineal Casas Idealista_2.ipynb). And thirdly, I also attach a third file where I create a pipeline, to process the data before passing it to the model, including a logarithmic transformation, to obtain better results in its adjustment (Pipeline Ridge con transformación Casas Idealista_3.ipynb). Finally, here you have the file that I have created with Shiny (app.py), for a better and easier use of the predict model by the user.
