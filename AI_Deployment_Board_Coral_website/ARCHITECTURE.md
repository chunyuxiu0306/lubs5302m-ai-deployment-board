# Architecture

- **Delivery:** one self-contained static `index.html` file (HTML/CSS/vanilla JS; no runtime dependencies, no remote fonts, no backend).
- **Stages:** six `screens[]` render functions. Navigation renders the selected stage into `#stageContent`; delegated event handlers handle inputs / buttons.
- **State:** `defaultState()`, `hydrate()`, `save()`. Browser `localStorage` key `northstar_ai_board_lab_v2`, read-only migration source `v1`; JSON import/export.
- **Case data:** `RESULTS` defines authored, arithmetically consistent model confusion matrices; `CUSTOMERS` defines illustrative local predictions/explanation bars.
- **Cost analysis:** editable `costContact` and `costMissed`; `assumedCost(result)` recalculates FP×cost+FN×cost. Inputs are assumptions; the decision stores a snapshot at submission.
- **What-if:** `WHAT_IF_MODEL` stores four fitted coefficients plus intercept, three fixed profiles, and two editable features per profile. `whatIfPredict()` computes log-odds, sigmoid probability and per-feature terms. No browser ML library. The source of coefficients is `dev/fit_whatif.py` (reproducible synthetic logistic regression trained offline).
- **Pedagogical separation:** Stage 2 and the case explanations are authored fixed teaching illustrations. Stage 3's What-if is separately fitted, calculated, synthetic and intentionally *not numerically equal* to the case forest.
- **Reports:** `reportHTML()` creates the in-app printable board report. `reportStandalone()` wraps the report in an independent HTML document for download; native browser printing provides PDF.
- **Privacy:** browser-only. No API, tracking or student uploads. Final Minerva upload happens outside this static app.
- **Security:** user-written free text is HTML-escaped when inserted in report. Imported session fields are hydrated and bounded; there is no authentication.
- **Responsiveness:** the desktop sidebar becomes a compact six-stage navigation on smaller screens. Cost tables horizontally scroll within their card.
- **Dependencies:** no client runtime dependencies. `dev/requirements.txt` is only for reproducing the fitted synthetic what-if parameters.
