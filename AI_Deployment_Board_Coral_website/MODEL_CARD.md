# MODEL CARD — The AI Deployment Board (Lab 3)

## Scope

**Status:** All organisations and customer cases are fictional. The A/B/C metrics below are **authored teaching scenarios**; only the clearly separated what-if logistic model is fitted to synthetic records and numerically evaluated by code.

Northstar Retail wants to flag existing subscribers who might cancel within 30 days. Prediction is at **Day 1** of each month. Students decide which evidence can justify a pilot, a full rollout or deferral.

## Fixed teaching case: comparison models

The hold-out scenario has **1,000 fictional customers** (200 churners, 800 non-churners) and a 50% contact threshold.

| Case | TP | FN | FP | TN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Model A: small decision tree | 116 | 84 | 76 | 724 | 84.0% | 60.4% | 58.0% |
| Model B: original random forest | 170 | 30 | 104 | 696 | 86.6% | 62.0% | 85.0% |
| Corrected Model B: time-valid forest | 142 | 58 | 110 | 690 | 83.2% | 56.3% | 71.0% |

TP = churner flagged, FN = churner missed, FP = non-churner flagged, TN = non-churner not flagged. Values are arithmetically consistent and scenario-authored. In the original fictional historical data, “account closure request” appears **after Day 1**, causing temporal leakage. The corrected forest scenario is an authored before/after teaching comparison; the app does **not** retrain that random forest.

Original global and local explanation bars are *illustrative*, not SHAP. Case-study customer probabilities are illustrative, not calibrated.

## Separate computed What-if sandbox (Stage 3)

A logistic regression was fitted offline to 7,000 reproducible synthetic examples using `dev/fit_whatif.py`. Feature order:
- Weekly app sessions before Day 1 (0–12)
- Complaints before Day 1 (0–5)
- Account tenure (3–60 months in synthetic data)
- Monthly subscription fee (£18/£28/£42 in synthetic data)

Generation: NumPy RNG seed **5302**, feature distributions and logistic label-generating process in the script. The positive outcome is sampled Bernoulli from a logistic data-generating process. Fitting used `sklearn.linear_model.LogisticRegression(max_iter=1000, solver="lbfgs")`, NumPy 2.3.5, scikit-learn 1.8.0.

Saved fitted parameters (full precision):

```
intercept   -0.1697464171327536
sessions    -0.22931069096916337
complaints  +0.5039852062405663
tenure      -0.019043489980805167
price       +0.01929682453534369
```

Calculations run in the browser:

```
z = intercept + sessions*w_sessions + complaints*w_complaints
              + tenure*w_tenure + price*w_price
probability = 1/(1 + exp(-z))
```

The per-feature bars show each **coefficient × raw feature value** in **log-odds units**, with the intercept stated separately. These bars are not percentage-point contributions, SHAP values or causal effects.

Three fictional customer baselines:

| Customer | Weekly sessions | Recent complaints | Tenure months | Fee (£) |
|---|---:|---:|---:|---:|
| A | 3 | 3 | 14 | 28 |
| B | 8 | 0 | 42 | 42 |
| C | 5 | 1 | 20 | 28 |

Students may change only sessions and complaints; the other two terms remain fixed. The model's displayed probability recalculates after each change. Its numbers **intentionally differ** from the separate fixed random-forest example.

**Important:** A counterfactual *input adjustment* is not a causal intervention. This fitted synthetic surrogate does not predict whether changing a customer's experience or offering a discount actually reduces churn.

## Business cost analysis

Stage 2 lets students vary two hypothetical values:
- £0–£100 per unnecessary outreach to a non-churner (`FP`)
- £0–£200 per missed churner (`FN`)

Displayed simplified scenario cost per 1,000 cases:

`FP * assumed FP cost + FN * assumed FN cost`

This is not a net-profit estimate. It excludes treatment efficacy, handling costs when a churner is contacted, customers who opt out, customer lifetime value uncertainty, and distribution changes. Original Model B should never be approved because a lower apparent cost cannot repair leakage.

## Limits and intended use

The app is for teaching managerial interpretation, audit and deployment decisions, not customer treatment or production prediction. No real customer data, empirically validated RF, real SHAP computations, calibration, sensitivity analyses, fairness measurement, intervention experiment or production deployment plan is supplied.
