---

# Multi-Dataset Classifier

This project is designed to load, preprocess, and classify datasets stored in ARFF format using various machine learning models. The project uses popular classification algorithms, including Logistic Regression, Random Forest, Support Vector Machines (SVM), and Gradient Boosting, to evaluate and compare their performance on the datasets.

## Features

- **Load Multiple Datasets:** Load and combine multiple ARFF files into a single dataset.
- **Preprocessing:** Normalize features using standard scaling and encode target variables.
- **Model Training:** Train multiple machine learning models on the processed dataset.
- **Model Evaluation:** Evaluate models using classification reports, including precision, recall, and F1-score.
- **Flexible Extension:** Easily add more ARFF datasets for analysis.

## Requirements

Before running the script, ensure that you have the following Python packages installed:

- `scipy`
- `pandas`
- `scikit-learn`

You can install these packages using pip:

```bash
pip install scipy pandas scikit-learn
```

## How to Use

### 1. Load and Preprocess Datasets

The script loads ARFF files from specified paths, preprocesses the data by normalizing features and encoding the target variable, and combines multiple datasets into a single DataFrame.

```python
X, y, label_encoder = load_and_preprocess_datasets(file_paths)
```

### 2. Train-Test Split

Split the dataset into training and testing sets:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### 3. Model Training and Evaluation

Train multiple machine learning models and evaluate their performance:

```python
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
    results[name] = report
```

### 4. View Results

Print the classification report for each model:

```python
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    print(metrics)
    print("\n")
```

### Example

Here's how to execute the script step by step:

1. **Specify the ARFF file paths:**
    ```python
    file_paths = [
        'path/to/dataset1.arff',
        'path/to/dataset2.arff',
        'path/to/dataset3.arff'
    ]
    ```

2. **Load and preprocess the datasets:**
    ```python
    X, y, label_encoder = load_and_preprocess_datasets(file_paths)
    ```

3. **Split the dataset and train the models:**
    ```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    ```

4. **Evaluate and print the results:**
    ```python
    for model_name, metrics in results.items():
        print(f"Model: {model_name}")
        print(metrics)
        print("\n")
    ```

## Customization

- **Add More Datasets:** To add more ARFF datasets, simply include their file paths in the `file_paths` list.
- **Adjust Test Size:** You can change the `test_size` parameter in `train_test_split` to alter the proportion of the dataset used for testing.

---
