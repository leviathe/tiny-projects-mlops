import subprocess

import joblib

def transpile_simple_model(coefs, intercept):
    n = len(coefs)
    coef_str = ", ".join(f"{c:.8f}f" for c in coefs)
    code = f"""
    #include <stdio.h>
    
    float exp_approx(float x, int n_term) {{
        float sum = 1.0f;
        float x_i = 1.0f;

        for (int i = 1; i <= n_term; i++) {{
            x_i *= x / (float) i;
            sum += x_i;
        }}
        return sum;
    }}

    float sigmoid(float x) {{
        return 1.0f / (1.0f + exp_approx(-x, 10));
    }}

    float prediction(float *features, int n_feature) {{
        float coef[{n}] = {{{coef_str}}};
        float res = {intercept:.8f}f;
        for(int i = 0; i < n_feature; i++) {{
            res += coef[i] * features[i];
        }}
        return sigmoid(res);
    }}

    int main() {{
        float x[{n}] = {{1.0f, 2.0f, 3.0f}};
        float y = prediction(x, {n});
        printf("Prediction: %f\\n", y);
        return 0;
    }}
    """
    return code


def main():
    model = joblib.load("regression.joblib")
    coef = model.coef_
    intercept = model.intercept_
    code = transpile_simple_model(coef, intercept)
    print("Generate regression.c")
    with open("regression.c", "w") as f:
        f.write(code)
    print("Compilation: gcc regression.c && ./a.out")
    try:
        subprocess.run(["gcc", "regression.c"], check=True)
        print("A")
        subprocess.run(["./model_exec"], check=True)
    except Exception as e:
        print("Error", e)

main()