# Health Data Analysis: BMI & BMR

This repository contains a full exploratory and statistical analysis of a health survey dataset collected in May 2025. The focus is on body mass index (BMI / IMC) and basal metabolic rate (BMR / TMB), along with their relationships with other variables.

## 📦 Included Files

| File                             | Description                                                   |
|----------------------------------|---------------------------------------------------------------|
| `analisis_encuesta_colab.ipynb` | Jupyter notebook to run the analysis in Google Colab.         |
| `analisis_encuesta_colab.py`    | Python script version of the notebook.                        |
| `encuesta HD mayo 2025.xlsx`    | Excel file with the raw health survey dataset.                |

## 🔍 What This Project Does

- Calculates **BMI (IMC)** and **BMR (TMB)** using the Mifflin-St Jeor formula.
- Categorizes BMI using WHO standard ranges: Underweight, Normal, Overweight, Obesity.
- Provides descriptive statistics (rounded to 2 decimals).
- Generates:
  - Histograms for all numeric variables.
  - A bar chart of BMI categories (%).
  - A scatter plot of BMR vs. BMI, colored by gender.
  - A heatmap of numerical variable correlations.
- Presents a brief qualitative and quantitative data analysis summary.

## 🚀 How to Run in Google Colab

1. Go to [Google Colab](https://colab.research.google.com/).
2. Upload the three files listed above.
3. Open `analisis_encuesta_colab.ipynb`.
4. Run all cells in order.

> Alternatively, you can run `analisis_encuesta_colab.py` in any Python environment with `pandas`, `matplotlib`, and `seaborn`.

## ✅ Requirements

The following Python libraries are used (preinstalled in Colab):

- `pandas`
- `matplotlib`
- `seaborn`

## 👩‍💻 Author

Created by **Juliana Castillo Araujo** for academic and analytical learning purposes.
