
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
file_path = 'encuesta HD mayo 2025.xlsx'
df = pd.read_excel(file_path)

# Limpiar nombres de columnas
df.columns = df.columns.str.strip().str.replace(r'\s+\[.*?\]', '', regex=True).str.lower()

# Calcular IMC y TMB
df['imc'] = df['peso'] / (df['altura'] ** 2)
df['altura_cm'] = df['altura'] * 100
df['tmb'] = df.apply(lambda row: (
    10 * row['peso'] + 6.25 * row['altura_cm'] - 5 * row['edad'] + (5 if row['sexo'] == 'Hombre' else -161)
), axis=1)

# Categorizar IMC
def categorizar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 <= imc < 25:
        return 'Normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

df['categoria_imc'] = df['imc'].apply(categorizar_imc)

# Estadísticas descriptivas
desc_stats = df.describe().round(2)

# Histogramas de variables numéricas
num_cols = ['peso', 'altura', 'edad', 'imc', 'tmb']
for col in num_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], bins=10, color='orange', edgecolor='black')
    plt.title(f'Histograma de {col}')
    plt.xlabel(col)
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

# Histograma de categorías de IMC (porcentaje)
plt.figure(figsize=(8, 6))
sns.histplot(df['categoria_imc'], stat='percent', shrink=0.8, color='orange', edgecolor='black')
plt.title('Distribución porcentual de categorías de IMC')
plt.xlabel('Categoría IMC')
plt.ylabel('Porcentaje')
plt.tight_layout()
plt.show()

# Dispersión TMB vs IMC diferenciando por Sexo
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='imc', y='tmb', hue='sexo', palette='autumn')
plt.title('Dispersión TMB vs IMC diferenciando por Sexo')
plt.tight_layout()
plt.show()

# Mapa de calor de correlaciones
plt.figure(figsize=(8, 6))
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de calor de correlaciones')
plt.tight_layout()
plt.show()

# Análisis cualitativo y cuantitativo
print("\nResumen cualitativo (categorías IMC):")
print(df['categoria_imc'].value_counts(normalize=True).round(2))

print("\nEstadísticas descriptivas:")
print(desc_stats)
