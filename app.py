from flask import Flask, request, render_template, send_file
import pandas as pd
import joblib
import io

app = Flask(__name__)
MODEL_PATH = "best_model.pkl"

model = joblib.load(MODEL_PATH)

last_results = None

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        has_results=False,
        model_name=type(model).__name__,
        threshold=0.5,
        columns=[],
        rows=[]
    )

@app.route("/predict", methods=["POST"])
def predict():
    global last_results
    try:
        file = request.files["file"]
        threshold = float(request.form.get("threshold", 0.5))

        df = pd.read_csv(file)

        #gerekli sütunların kontrolü
        required = {"type", "amount", "step"}
        if not required.issubset(df.columns):
            return render_template(
                "index.html",
                error=f"Gerekli kolonlar eksik: {required}",
                has_results=False,
                model_name=type(model).__name__,
                threshold=threshold,
                columns=[],
                rows=[]
            )

        
        type_map = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
        if df["type"].dtype == object:
            df["type"] = df["type"].astype(str).str.strip().str.upper().map(type_map)

        
        X = df[["type", "amount", "step"]]

        # Olasılık ve tahmin
        probs = model.predict_proba(X)[:, 1]
        df["Fraud_Prob"] = probs
        df["Prediction"] = (probs >= threshold).astype(int)

        
        last_results = df.copy()

        
        df_view = df.copy()

        
        columns = list(df_view.columns)
        rows = df_view.to_dict(orient="records")

        return render_template(
            "index.html",
            has_results=True,
            model_name=type(model).__name__,
            threshold=threshold,
            columns=columns,
            rows=rows
        )
    except Exception as e:
        return render_template(
            "index.html",
            error=str(e),
            has_results=False,
            model_name=type(model).__name__,
            threshold=0.5,
            columns=[],
            rows=[]
        )

@app.route("/download")
def download():
    global last_results
    if last_results is None:
        return "Henüz sonuç yok!"
    buf = io.BytesIO()
    last_results.to_csv(buf, index=False)
    buf.seek(0)
    return send_file(buf, mimetype="text/csv", as_attachment=True, download_name="predictions.csv")

if __name__ == "__main__":
    app.run(debug=True)
