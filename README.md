# The AI Deployment Board — Computer Lab 3

LUBS5302M **Foundations of Machine Learning in Business** · Leeds University Business School  
60-minute group activity · Northstar Retail fictional churn case · no login, backend, API or internet needed.

## Open the app

Open `index.html` in a modern browser (Chrome, Edge, Firefox or Safari). All student-facing HTML, CSS and JavaScript are embedded in this one file.

## Six-stage exercise

1. **Board briefing (5 min):** group name, roles and CEO brief.
2. **Compare the models (10 min):** confusion matrices, recall/precision and editable *assumed business costs* (£ per false positive contact and £ per false negative missed churner). Record initial recommendation.
3. **Explain a prediction (15 min):** three example customers, global/local classroom illustrations, a **calculated What-if Analysis** using a separate synthetic logistic-regression demonstrator and the causation question. Record one what-if insight.
4. **Challenge the evidence (10 min):** inspect Day 1 feature availability; identify future-recorded closure-request leakage; show the authored time-valid correction.
5. **Make the board decision (10 min):** choose model, deployment scope, review controls, rationale and next evidence. Cost assumptions are snapshotted at board submission.
6. **Report & debrief (10 min):** download a standalone HTML report or use browser Print / Save as PDF, export/import JSON session, follow **Minerva** upload instructions.

**No single deployment option is marked correct.** Students should reason from evidence, including how predictive accuracy differs from operational impact.

## What the two new interactions mean

### 1. Cost assumptions (Stage 2)

`Assumed loss = FP × assumed cost per unnecessary contact + FN × assumed opportunity cost per missed churner`.

Defaults: **£20** per unnecessary contact, **£60** per missed churner, applied to the fictional 1,000-customer test sample. These assumptions are adjustable; they **are not observed costs** and do not establish the value of any intervention. Original Model B is labelled invalid for prospective deployment until its leakage is addressed. Once corrected in Stage 4, the cost comparison uses corrected Model B's confusion matrix.

### 2. What-if calculations (Stage 3)

Students change **weekly app sessions** (0–12) and **previous-month complaints** (0–5). The app recomputes probabilities and additive **log-odds** feature terms with a small logistic regression trained offline on 7,000 reproducible synthetic examples. Tenure and monthly fee remain fixed within each customer file. `dev/fit_whatif.py` produces the coefficients shown in `index.html`.

This logistic model is **separate from** the authored Decision Tree / Random Forest case. Its probabilities are not supposed to equal the fixed customer case-study predictions; its terms are not SHAP. The what-if exercise shows the model's sensitivity to inputs, **not** whether changing those inputs changes real-world churn.

See `MODEL_CARD.md`.

## Saving work / student privacy

- Browser localStorage autosaves when permitted; save-state key `northstar_ai_board_lab_v2`.
- Existing browser data under the previous `northstar_ai_board_lab_v1` key is read as a migration source and not deleted.
- New JSON export uses version 2. The importer accepts version 1 or 2 and fills missing new fields with defaults.
- Save session JSON if browser storage is disabled, a device changes, or work must move from a local file to GitHub Pages. Local sessions do not synchronise between origins.
- No student responses leave this app. **Downloading a report is not submission**. Upload one final group PDF or HTML report using the **Minerva submission link provided by the lecturer**.

Do not enter personal or sensitive data. The University brand and the fictional case do not imply a University-run submission service.

## GitHub Pages

1. Create a GitHub repository (e.g. `lubs5302m-lab3`).
2. Upload `index.html` at the repository root, plus the documentation if desired.
3. Commit and push to `main`.
4. Open **Settings → Pages → Deploy from a branch**.
5. Select **main** and **/(root)**, save.
6. Open the generated `https://<account>.github.io/<repository>/` URL.
7. Test a complete audit, board decision, PDF export and session import *on the published URL* before teaching.

All runtime code is in one HTML file; there are no runtime dependencies. GitHub Pages serves the static files and cannot receive student submissions.

## Developer model reproduction (optional)

```bash
python -m pip install -r dev/requirements.txt
python dev/fit_whatif.py
```

The app does not need Python at runtime. Synthetic model coefficients were generated with NumPy 2.3.5 and scikit-learn 1.8.0. Model regenerations should be reviewed and copied into the HTML only with an explicit version update.

## Customise

- UI and copy: `index.html`, including `briefing`, `compare`, `explanations`, `audit`, `board`, `report`.
- Colour palette: last CSS section in `index.html`; inspired by the **colleague's executive-simulation reference**, not the previous vivid-orange/black variant.
- Synthetic case/metrics: `RESULTS` and `CUSTOMERS` constants (changing these demands rechecking every cited figure).
- What-if: `WHAT_IF_MODEL` and `dev/fit_whatif.py` together (keep coefficients in sync).
- Default costs: `defaultState().costContact` and `.costMissed`.
- Minerva instructions: in `report()`; keep them generic unless a confirmed course submission URL is supplied.

## Known limitations

- Original RF/decision-tree metrics and their explanatory bars are **authored classroom examples**, not empirical validation. The separate what-if logistic regression **is fitted and calculated**, but on intentionally synthetic records.
- The business cost model omits intervention effectiveness, treatment costs for true positives, uncertainty and distribution shifts. Costs are assumptions, not operational evidence.
- No live data, calibrated churn model, fairness audit, causal trial, authenticated submissions, or cross-device synchronisation.
- University branding is shown for preview and may require permission before publishing to third-party GitHub Pages; see `BRANDING.md`.
- Browser restrictions can disable localStorage. The app should remain usable but the JSON download is then necessary to persist work.

See `ARCHITECTURE.md`, `LECTURER_GUIDE.md`, `MODEL_CARD.md`, `TESTING.md` and `BRANDING.md`.
