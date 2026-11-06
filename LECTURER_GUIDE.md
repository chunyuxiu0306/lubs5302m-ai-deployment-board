# Lecturer Guide — Computer Lab 3

**Module:** LUBS5302M Foundations of Machine Learning in Business  
**Duration:** 60 minutes, one shared laptop per board group.

| Time | Stage | Prompt |
|---|---|---|
| 0–5 min | Board briefing | What can the board approve, and on what evidence? |
| 5–15 min | Model comparison | What business costs could attach to false positives and false negatives? Change the *assumed* costs. |
| 15–30 min | Explanation / What-if | Contrast global/local *illustrations* with the separate **calculated logistic what-if**. Which input changes influence its prediction? Why is that not causal? |
| 30–40 min | Data audit | On Day 1, was the account closure request known? What changes when we remove leaked data? |
| 40–50 min | Board resolution | Which valid model and deployment policy, with review triggers and pilot evidence? |
| 50–60 min | Report / debrief | How did assumptions, explanation and data audit change your decision? Export one report and follow Minerva instructions. |

## Important distinctions

1. **Fixed A/B/C case metrics** are authored teaching examples, NOT results from an actual tree or forest fit. The audit correction is an authored time-valid simulation; it is *not* retraining performed in the browser.
2. **What-if logistic model** is independently fitted to reproducible synthetic data and evaluated in JS. Its probabilities will not match the fixed case-study RF scores. Its coefficients and attribution bars are in log-odds units and are not SHAP.
3. **Input changes are not causal treatments.** Modifying simulated usage is not proof that increasing usage prevents churn. Ask students what controlled test would support a retention intervention.
4. **Business costs are illustrative assumptions** (£ per unnecessary contact and £ per missed churner). They are not actual operational loss, savings or ROI. Students should question what evidence supports the chosen assumptions.
5. **Original forest uses a future-recorded account closure field.** The correct response is to identify lack of valid early-warning evidence; students still must make a justified deployment choice among valid evidence, pilot, or deferral.
6. **No winning score** and no automatic credit for conservative decisions.

## Session and submission

Use one shared device. Encourage session JSON export if classroom browser storage is unreliable. At the end, a team may download standalone HTML or print to PDF. The app provides general Minerva steps; lecturers should supply the *actual module assignment/submission link* and clarify submission deadline and acceptable file type. Neither the simulation nor GitHub Pages submits work or collects student entries.

## Before the class

- Confirm University brand/logo use is authorised for the chosen hosting domain.
- Test on the actual classroom browser / GitHub Pages URL.
- Confirm Minerva hand-in instructions and whether HTML/PDF is accepted.
- If updating the synthetic model, re-run `dev/fit_whatif.py` and update the coefficients in HTML together.
- Keep the label “synthetic logistic demonstrator” if discussing the new What-if activity; do not present it as a causal experiment.
