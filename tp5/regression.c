
    #include <stdio.h>
    
    float exp_approx(float x, int n_term) {
        float sum = 1.0f;
        float x_i = 1.0f;

        for (int i = 1; i <= n_term; i++) {
            x_i *= x / (float) i;
            sum += x_i;
        }
        return sum;
    }

    float sigmoid(float x) {
        return 1.0f / (1.0f + exp_approx(-x, 10));
    }

    float prediction(float *features, int n_feature) {
        float coef[3] = {717.25836971f, 36824.19597426f, 101571.84002157f};
        float res = -8152.93771016f;
        for(int i = 0; i < n_feature; i++) {
            res += coef[i] * features[i];
        }
        return sigmoid(res);
    }

    int main() {
        float x[3] = {1.0f, 2.0f, 3.0f};
        float y = prediction(x, 3);
        printf("Prediction: %f\n", y);
        return 0;
    }
    