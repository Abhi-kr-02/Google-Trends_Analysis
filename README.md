# 📊 Google Trends Analysis Tool

A beginner-friendly web application for analyzing Google Trends data with an interactive interface.

## 🚀 Features

- **Regional Interest Analysis**: See which countries search for your keywords most
- **Time Series Analysis**: Track search interest over time
- **Keyword Comparison**: Compare multiple keywords side by side
- **Interactive Charts**: Beautiful, interactive visualizations
- **Easy to Use**: Simple web interface - no coding required!

## 📋 Requirements

- Python 3.8 or higher
- Internet connection (to fetch Google Trends data)

## 🛠️ Installation

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Enter a keyword** you want to analyze (e.g., "AI/ML", "Python", "Data Science")
2. **Select a time period** (last 12 months, 5 years, etc.)
3. **Choose analysis type:**
   - **Regional Interest**: See which countries search for your keyword
   - **Time Series**: Track interest over time
   - **Keyword Comparison**: Compare multiple keywords
   - **All Analyses**: Run everything at once
4. **Click "Run Analysis"** and wait for the results
5. **Explore the interactive charts** - hover, zoom, and interact!

## 🎯 Example Keywords to Try

- "AI/ML"
- "Data Science"
- "Cloud Computing"
- "Web Development"
- "Python"
- "Machine Learning"
- "JavaScript"

## 📊 What You'll See

- **Bar charts** showing top countries by search interest
- **World maps** with color-coded interest levels
- **Line charts** showing trends over time
- **Comparison charts** for multiple keywords

## 🔧 Tips

- Leave the country field empty for worldwide analysis
- Try different time periods to see how trends change
- Use the keyword comparison to see which topics are more popular
- The charts are interactive - you can zoom, pan, and hover for details

## 🐛 Troubleshooting

- **"Error fetching data"**: Check your internet connection
- **No results**: Try a different keyword or time period
- **Slow loading**: Some analyses may take a few seconds to load

## 📝 Note

This tool uses Google Trends data, which provides relative search interest (0-100 scale) rather than absolute search volumes.

---

**Happy analyzing! 🎉** 