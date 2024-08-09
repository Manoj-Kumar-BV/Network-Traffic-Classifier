from scipy.io import arff
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Function to load and preprocess multiple datasets
def load_and_preprocess_datasets(file_paths):
    # List to hold DataFrames
    dataframes = []

    # Load each ARFF file and convert to DataFrame
    for file_path in file_paths:
        data, meta = arff.loadarff(file_path)
        df = pd.DataFrame(data)
        df['class1'] = df['class1'].str.decode('utf-8')
        dataframes.append(df)

    # Concatenate all DataFrames
    df_all = pd.concat(dataframes, ignore_index=True)

    # Separate features and target variable
    X = df_all.drop('class1', axis=1)
    y = df_all['class1']

    # Normalize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Encode the target variable
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    return X_scaled, y_encoded, label_encoder

# List of ARFF file paths
file_paths = [
    'D:/4th semester/CN_EL/ELFinal/Scenario B-ARFF/TimeBasedFeatures-Dataset-15s-AllinOne.arff',
    'D:/4th semester/CN_EL/ELFinal/Scenario B-ARFF/TimeBasedFeatures-Dataset-30s-AllinOne.arff',
    'D:/4th semester/CN_EL/ELFinal/Scenario B-ARFF/TimeBasedFeatures-Dataset-120s-AllinOne.arff'  # Add more paths as needed
    # 'path/to/your/third_dataset.arff'
]

# Load and preprocess the datasets
X, y, label_encoder = load_and_preprocess_datasets(file_paths)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the models
log_reg = LogisticRegression(max_iter=1000, random_state=42)
random_forest = RandomForestClassifier(random_state=42)
svm = SVC(random_state=42)
gradient_boost = GradientBoostingClassifier(random_state=42)

# Train and evaluate each model
models = {'Logistic Regression': log_reg, 'Random Forest': random_forest, 'SVM': svm, 'Gradient Boosting': gradient_boost}
results = {}

for name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
    # Make predictions
    y_pred = model.predict(X_test)
    # Evaluate the model
    report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
    results[name] = report

# Print the results
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    print(metrics)
    print("\n")
