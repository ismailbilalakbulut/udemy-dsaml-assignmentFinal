import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("student_habits_performance.csv")

df = df.drop('student_id', axis=1)

df['parental_education_level'] = df['parental_education_level'].fillna('High School')


target = "exam_score"
X = df.drop(target, axis=1)
y = df[target]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


nominal_cols = ["gender"]

ordinal_cols = ["part_time_job", "diet_quality", "parental_education_level",
                "internet_quality", "extracurricular_participation"]

numerical_cols = ["age", "study_hours_per_day", "social_media_hours", "netflix_hours",
                  "attendance_percentage", "sleep_hours", "exercise_frequency", "mental_health_rating"]


ordinal_categories = [
    ["No", "Yes"],                          # part_time_job
    ["Poor", "Fair", "Good"],               # diet_quality
    ["High School", "Bachelor", "Master"],  # parental_education_level
    ["Poor", "Average", "Good"],            # internet_quality
    ["No", "Yes"]                           # extracurricular_participation
]


preprocessor = ColumnTransformer(transformers=[
    ('nominal', OneHotEncoder(drop='first', handle_unknown='ignore'), nominal_cols),
    ('ordinal', OrdinalEncoder(categories=ordinal_categories, handle_unknown='use_encoded_value', unknown_value=-1), ordinal_cols),
    ('num', StandardScaler(), numerical_cols)
])


pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor(random_state=15, n_estimators=200, max_depth=2, loss='squared_error', min_samples_split=5, min_samples_leaf=2, learning_rate=0.1))
])


print("Model eğitiliyor...")
pipeline.fit(X_train, y_train)


print("Test ediliyor...")
y_pred = pipeline.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))


print(f"R2 Score: {r2}")
print(f"RMSE: {rmse}")


joblib.dump(pipeline, 'ogrenci_basari_modeli.pkl')

print("\nBAŞARILI: Model 'ogrenci_basari_modeli.pkl' olarak kaydedildi.")
