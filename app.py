from shiny import App, render, ui, reactive
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler
# Configuro la ruta del modelo y lo cargo con joblib
model_path = 'C:/Users/danal/Documents/Python/ridge_model_idealista.pkl'
model = joblib.load(model_path)
# Configuro todos los botones, sliders y seleccionables gráficos del front off
app_ui = ui.page_fluid(
    ui.markdown(
        """
        # Predicción inmuebles Valencia
        """
    ),
    ui.layout_sidebar(
        ui.panel_sidebar(ui.input_select("localizacion", "Localización", {"Patraix": "Patraix", "Safranar": "Safranar", "Vara de Quart": "Vara de Quart", "Sant Isidre": "San Isidre", "Barrio de Favara": "Barrio de Favara"}),
                         ui.input_numeric("metros_cuadrados", "Metros cuadrados", value=100),
                         ui.input_slider("habitaciones", "Habitaciones", 1, 6, 1),
                         ui.input_slider("baños", "Baños", 1, 4, 1),
                         ui.input_select("ascensor", "Ascensor", {0:'No', 1:'Si'}),
                         ui.input_numeric("año", "Año de construcción", value=2000),
                         ui.input_select("trastero", "Trastero", {0:'No', 1:'Si'}),
                         ui.input_select("condicion", "Condición", {"Segunda mano/para reformar": "Segunda mano/para reformar", "Segunda mano/buen estado": "Segunda mano/buen estado", "Promoción de obra nueva": "Promoción de obra nueva"}),
                         ui.input_select("armarios_empotrados", "Armarios empotrados", {0:'No', 1:'Si'}),
                         ui.input_select("terraza", "Terraza", {0:'No', 1:'Si'}),
                         ui.input_select("balcon", "Balcón", {0:'No', 1:'Si'}),
                         ui.input_select("jardin", "Jardín", {0:'No', 1:'Si'}),
                         ui.input_select("garaje", "Garaje", {0:'No', 1:'Si'}),
                         ui.input_select("calefaccion", "Calefacción", {0:'No', 1:'Si'}),
                         ui.input_select("aire_acondicionado", "Aire acondicionado", {0:'No', 1:'Si'}),
                         ui.input_select("altura_piso", "Altura piso", {"PLANTA BAJA": "Planta Baja", "PISOS BAJOS": "Pisos Bajos < 3º", "PISOS MEDIOS": "Pisos Medios 3º > < 6º", "PISOS ALTOS": "Pisos Altos > 6º"}),
                         ui.input_action_button('btn','Calcular', class_="btn-primary")),
        ui.panel_main(
            ui.markdown(
                """
                ## Predicción del modelo
                """
            ),
            ui.output_text_verbatim("txt", placeholder=True)
        )
    )
)
# Activo en el server el boton de calcular con 'reactive'
def server(input, output, session):
    # Define una función reactiva para calcular la predicción
    @reactive.Effect
    @reactive.event(input.btn)
    def calculate_prediction():
        test_df = pd.DataFrame([[input.localizacion(), input.metros_cuadrados(), input.habitaciones(), input.baños(), input.ascensor(), input.año(), input.trastero(), 
                input.condicion(), input.armarios_empotrados(), input.terraza(), input.balcon(), input.jardin(), input.garaje(), 
                input.calefaccion(), input.aire_acondicionado(), input.altura_piso()]],
                columns=['localizacion', 'metros_cuadrados', 'habitaciones', 'baños', 'ascensor', 'año', 'trastero', 'condicion', 
                'armarios_empotrados', 'terraza', 'balcon', 'jardin', 'garaje', 'calefaccion', 'aire_acondicionado', 'altura_piso'])
        prediction = int(model.predict(test_df)[0])
        @output
        @render.text
        def txt():
            return f"El precio del inmueble es de: {prediction}"

# Crea la aplicación Shiny
app = App(app_ui, server)

# Inicia la aplicación
if __name__ == "__main__":
    app.run()
