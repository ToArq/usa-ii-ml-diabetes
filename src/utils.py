from sklearn.pipeline import Pipeline
#Automation libraries
from joblib import dump
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def update_model (model: Pipeline) -> None:
    dump(model, "model/model.pkl")
    dump(model, 'model/model.joblib')


def save_simple_metric_report(accuracy_train_score: float, accuracy_test_score: float , model: Pipeline) -> None:
    with open('report.txt', 'w') as report_file:

        report_file.write("# Model Pipeline Description"+"\n")

        for k,v in model.named_steps.items():
            report_file.write(f'### {k}:{v.__repr__()}'+"\n")

        report_file.write("## Accuracy train score: {accuracy_train_score}"+"\n")
        report_file.write("## Accuracy test score: {accuracy_test_score}"+"\n")


def get_model_performance_test_set(y_real: pd.Series, y_pred: pd.Series) -> None:
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x=y_pred, y=y_real, ax = ax)
    ax.set_xlabel("Predicted diabetes hospital readmitted")
    ax.set_ylabel("Y")
    ax.set_title("Behavior of model prediction")
