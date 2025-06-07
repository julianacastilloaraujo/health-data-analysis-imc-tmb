# Health Data Analysis: IMC & TMB

This repository contains a Jupyter notebook that performs a full analysis on health survey data collected in May 2025.

## 📊 Contents

The analysis includes:

- ✅ Calculation of **BMI (IMC)** and **BMR (TMB)** using international formulas.
- ✅ Classification of BMI into standard categories: Underweight, Normal, Overweight, Obesity.
- ✅ Descriptive statistics with up to 2 decimals.
- ✅ Histograms for all numerical variables.
- ✅ Pie chart (via histogram) of BMI category distribution.
- ✅ Scatter plot of TMB vs. IMC, segmented by gender.
- ✅ Heatmap of correlations among numerical variables.
- ✅ Qualitative and quantitative analysis summaries.

## 🛠️ How to Use

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload both of these files:
   - `analisis_encuesta_colab.ipynb`
   - `encuesta HD mayo 2025.xlsx` (raw dataset)
3. Run all cells in the notebook.
4. Visualizations and analysis will be displayed step by step.

## 📁 Files

- `analisis_encuesta_colab.ipynb`: Main notebook with all code and visualizations.
- `encuesta HD mayo 2025.xlsx`: Excel file with raw data (you must upload it yourself — not included due to privacy).

## 📚 Requirements

The notebook is ready for Google Colab and uses:

```bash
pandas
matplotlib
seaborn
