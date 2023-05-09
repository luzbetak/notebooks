Convert Jupyter and Databricks Notebooks
========================================

## Convert files using Jupyter
- Open a terminal or command prompt, and navigate to the directory containing the .ipynb file.
- Run the following command:

Replace `example.ipynb` with the name of your file.
- This will create a new .py file with the same name in the same directory, containing the code cells from the original notebook. Note that markdown cells and outputs will be commented out.

You have now successfully converted your Databricks .ipynb file into a Python (.py) file.

```python
$ pip install jupyter
$ jupyter nbconvert --to script example.ipynb
```

---


## How to Convert Databricks .ipynb Files into Python (.py) Files

Follow the steps below to convert a Databricks .ipynb file, such as `example.ipynb`, into a Python (.py) file:

### 1. Export the Databricks notebook as an .ipynb file

- In Databricks, open the notebook you want to convert.
- Click on the **File** menu and select **Export** > **IPython Notebook** or **Export** > **Download as** > **IPython Notebook (.ipynb)**.
- Save the file to your local machine.

### 2. Convert the .ipynb file to a .py file using Jupyter

- Make sure you have Jupyter Notebook or JupyterLab installed. If not, you can install it using the following command:

---

## How to Open a Python (.py) File in a Databricks Notebook

Follow the steps below to open a Python (.py) file, such as `example.py`, in a Databricks notebook:

### 1. Create a new Databricks notebook

- In Databricks, click on the **Workspace** tab.
- Navigate to the desired folder, or stay in the **Users** folder.
- Right-click the folder and select **Create** > **Notebook**.
- Provide a name for the new notebook and select **Python** as the language.
- Click **Create**.

### 2. Import the .py file into the new Databricks notebook

- Open the newly created notebook.
- Click on the **File** menu, then select **Import**.
- In the **Import Notebook** window, click on **Upload** and choose the .py file (e.g., `example.py`) from your local machine.
- Click **Open** to upload the file. The contents of the .py file will be loaded into the notebook as code cells.

**Note:** The conversion from a .py file to a Databricks notebook might not be perfect, and you might need to adjust some formatting or cell breaks in the notebook. However, the code should be functional, and you can run the cells as you normally would in a Databricks notebook.


