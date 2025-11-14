# 📓 Jupyter Notebook Guide - Inline Visualization

## What's the Difference?

You now have **TWO versions** of the analysis:

### 1. **Python Script** (`car_price_analysis.py`)
- ✅ Runs from command line
- ✅ Saves graphs to PNG files
- ❌ Does NOT show graphs inline

### 2. **Jupyter Notebook** (`Car_Price_Analysis_COMPLETE.ipynb`) ⭐ NEW!
- ✅ Runs in Jupyter notebook
- ✅ **SHOWS graphs inline** (like your example file)
- ✅ Also saves graphs to PNG files
- ✅ Interactive cell-by-cell execution

---

## 🚀 How to Use the Jupyter Notebook

### Step 1: Open Jupyter Notebook
```bash
# In your terminal or command prompt:
jupyter notebook
```

### Step 2: Navigate to the File
- Browse to `/mnt/user-data/outputs/`
- Click on `Car_Price_Analysis_COMPLETE.ipynb`

### Step 3: Run the Cells
- Click on first cell
- Press **Shift + Enter** to run each cell
- Or use **Cell → Run All** to run everything

### Step 4: See Graphs Inline! 📊
- Each visualization will **display directly** in the notebook
- No need to open separate PNG files
- Interactive viewing experience

---

## 🎯 Key Feature: `plt.show()`

The magic that makes graphs appear inline is:

```python
plt.figure(figsize=(12, 6))
# ... plotting code ...
plt.show()  # 👈 THIS LINE DISPLAYS THE GRAPH INLINE!
```

**Without `plt.show()`:** Graph is only saved to file
**With `plt.show()`:** Graph appears in notebook AND saves to file

---

## 📋 What's Included in the Notebook

### ✅ Task 1: Data Ingestion & Quality Profiling
- Load and inspect dataset
- Data structure analysis
- **2 inline visualizations:**
  - Missing values bar chart
  - Missing values heatmap

### ✅ Task 2: Data Frames Queries (2.1-2.12)
- All 12 queries with results
- Interactive DataFrames
- Summary statistics

### ✅ Task 3: Visualizations (3.1-3.7)
- **8 inline visualizations:**
  1. Correlation matrix
  2. Price by year (line graph)
  3. Price by odometer (scatter plot)
  4. Cars by state (bar chart)
  5. Price by condition ranges (bar chart)
  6. Cars by condition ranges (bar chart)
  7. Price by color WITH outliers (box plot)
  8. Price by color WITHOUT outliers (box plot)

**Total: 10 visualizations displayed inline!**

---

## 💡 Pro Tips

### Cell Execution
- **Run current cell:** Shift + Enter
- **Run all cells:** Cell → Run All
- **Restart kernel:** Kernel → Restart & Clear Output

### Viewing Results
- Scroll through the notebook to see all outputs
- Graphs appear right below their code cells
- No need to switch between windows!

### Saving Your Work
- **Save notebook:** Ctrl + S (or Cmd + S on Mac)
- **Export to HTML:** File → Download as → HTML
- **Export to PDF:** File → Download as → PDF

### Troubleshooting
If graphs don't appear:
1. Make sure you have `%matplotlib inline` at the top
2. Check that `plt.show()` is included after each graph
3. Restart kernel and run all cells again

---

## 📁 File Locations

### Input Data
```
/home/claude/car_prices_decompressed.csv
```
Or update to:
```
/mnt/user-data/outputs/car_prices_cleaned.csv
```

### Output Files
All PNG graphs are saved to:
```
/mnt/user-data/outputs/
```

---

## 🎨 Customization Options

### Change Figure Size
```python
plt.figure(figsize=(14, 8))  # Width, Height in inches
```

### Change Colors
```python
color='#E74C3C'  # Hex color code
palette='Set2'    # Seaborn palette name
```

### Adjust DPI (Resolution)
```python
plt.rcParams['figure.dpi'] = 150  # Higher = better quality
```

---

## ✨ Benefits of Jupyter Notebook Version

1. **Interactive Experience**
   - Run cells individually
   - Modify and re-run without starting over
   - See immediate results

2. **Inline Visualizations**
   - Graphs appear directly in notebook
   - Easy comparison and analysis
   - No file switching needed

3. **Better Documentation**
   - Markdown cells for explanations
   - Code and output together
   - Professional presentation

4. **Easy Sharing**
   - Export to HTML for viewing without Jupyter
   - Share entire analysis in one file
   - Reproducible results

---

## 🔧 Technical Requirements

### Required Libraries
```bash
pip install pandas numpy matplotlib seaborn scipy jupyter
```

### Python Version
- Python 3.7 or higher

### Jupyter Installation
```bash
pip install jupyter notebook
# OR
pip install jupyterlab  # Modern interface
```

---

## 📊 Comparison: Script vs Notebook

| Feature | Python Script | Jupyter Notebook |
|---------|--------------|------------------|
| Inline Graphs | ❌ No | ✅ Yes |
| Interactive | ❌ No | ✅ Yes |
| Cell-by-Cell | ❌ No | ✅ Yes |
| Save to Files | ✅ Yes | ✅ Yes |
| Command Line | ✅ Yes | ❌ No |
| Documentation | Limited | ✅ Rich |

---

## 🎯 Quick Start Checklist

- [ ] Install Jupyter: `pip install jupyter`
- [ ] Open notebook: `jupyter notebook`
- [ ] Navigate to file: `Car_Price_Analysis_COMPLETE.ipynb`
- [ ] Update file path if needed (cell 3)
- [ ] Run all cells: Cell → Run All
- [ ] Enjoy inline visualizations! 🎉

---

## 📞 Need Help?

### Common Issues

**Issue:** Graphs not showing
**Solution:** Add `%matplotlib inline` at the beginning

**Issue:** Can't find file
**Solution:** Check file path in load cell, update if needed

**Issue:** Module not found
**Solution:** Install missing library with `pip install <library-name>`

---

## 🌟 Example: What You'll See

Instead of:
```python
plt.savefig('graph.png')
# [Graph saved to file]
```

You get:
```python
plt.show()
# [GRAPH DISPLAYS HERE IN NOTEBOOK!]
# AND also saves to file
```

---

## 📝 Summary

**The Jupyter Notebook version is EXACTLY what you wanted:**

✅ All graphs display inline in the notebook
✅ Graphs also save to PNG files for backup
✅ Professional presentation format
✅ Easy to run cell-by-cell
✅ Interactive and user-friendly

**Just open it in Jupyter and run!** 🚀

---

**Created by:** Sukesh Singla
**Date:** November 13, 2025
**Assignment:** Hero Vired - Python Programming

**File:** `Car_Price_Analysis_COMPLETE.ipynb`
**Location:** `/mnt/user-data/outputs/`

