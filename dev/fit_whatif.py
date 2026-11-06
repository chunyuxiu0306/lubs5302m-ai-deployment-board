#!/usr/bin/env python3
"""Reproduce the small, separate, synthetic logistic model used in the what-if sandbox.

Developer-only. Browser students do not need Python or these packages.
The main Lab 3 model comparison numbers are authored classroom values,
not scores for this logistic model.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression

rng = np.random.default_rng(5302)
n = 7000
sessions = rng.integers(0, 13, n)
complaints = np.minimum(rng.poisson(1.25, n), 5)
tenure = rng.integers(3, 61, n)
price = rng.choice([18, 28, 42], n, p=[.30, .48, .22])
logit = (
    -.7 + .52 * (complaints - 1) - .24 * (sessions - 5)
    + .18 * ((price - 30) / 10) - .018 * (tenure - 24)
)
labels = rng.binomial(1, 1 / (1 + np.exp(-logit)))
features = np.column_stack([sessions, complaints, tenure, price])
model = LogisticRegression(max_iter=1000, solver="lbfgs")
model.fit(features, labels)

print("Feature order: sessions, complaints, tenure, monthly price")
print("Intercept:", repr(float(model.intercept_[0])))
print("Coefficients:", [repr(float(c)) for c in model.coef_[0]])
print("Synthetic positive cases:", int(labels.sum()), "/", n)
