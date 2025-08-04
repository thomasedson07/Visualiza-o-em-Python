import plotly.express as px # type: ignore
import pandas as pd
from dash import Dash, html, dcc # type: ignore


def cria_grafico(df):

    # Histograma
    fig1 = px.histogram(df, x='Preço', nbins=30 , title='Distribuição de Preço')

    fig2 = px.pie(df, names='Gênero', color='Gênero', hole=0.2, color_discrete_sequence=px.colors.qualitative.Pastel) 
    fig2.update_layout(title='Distribuição de Gênero')

    # Grafico de bolha
    fig3 = px.scatter(df, x='Nota', y='Preço', color='Marca', hover_name='Marca', size_max=60)
    fig3.update_layout(title ='Preço vs Nota por Marca', xaxis_title='Nota', yaxis_title='Preço')


    # Grafico 3D
    fig5 = px.scatter_3d(df, x='Marca', y='Preço', z='Nota', color='Marca', title='Marcas em 3D')

    return fig1, fig2, fig3, fig5

# Cria app
def cria_app(df):
    app = Dash(__name__)

    fig1, fig2, fig3, fig5 = cria_grafico(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig5)
    ])
    return app

df = pd.read_csv('C:/Users/te742/Downloads/ecommerce_estatistica.csv')

if __name__ == '__main__':
    app = cria_app(df)
    # Executa o app
    app.run(debug=True, port=8051)
