# Testing record — Computer Lab 3 coral revision (5 November 2026)

## Executed checks

- [x] Static JavaScript syntax check: `node --check` passed.
- [x] Chromium (Playwright `set_content`) rendered all pages without page errors in tested flow.
- [x] Landing-page heading, university wordmark, module identity and all six stage links render.
- [x] Group name and initial model recommendation saved in active page state.
- [x] Business-cost sliders updated row totals immediately (e.g. £20 contact -> £60 altered Model A cost from £6,560 to £9,600 with FN cost unchanged at £60).
- [x] What-if sessions/complaints sliders recalculated risk AND log-odds contributions (Customer C: 34% baseline -> 49% when sessions 5→9 and complaints 1→4).
- [x] Saved what-if insight and customer explanation, and checked prediction-vs-causation prompt.
- [x] Requested data audit, removed future-recorded field and displayed corrected case metrics.
- [x] Submitted limited pilot using corrected Model B, a human review rule and monitoring plan.
- [x] Board report contained team label, cost snapshot, saved what-if calculation, monitoring plan and Minerva submission notice.
- [x] Downloaded self-contained HTML board report; browser produced the named download.
- [x] 390px-wide mobile rendering had no document-level horizontal overflow in briefing, cost comparison or what-if pages.
- [x] Captured desktop and mobile screenshots, inspected layout and confirmed coral/brick-red/warm-brown theme.
- [x] Reproduced synthetic logistic-regression coefficients with `dev/fit_whatif.py` and checked exact agreement with embedded JS values.

## Not fully testable here

- Browser navigation to `file://` and `http://127.0.0.1` was blocked by this execution environment's administrator settings, so interactive tests were executed with Playwright `page.set_content()` instead. Under an opaque origin, localStorage was unavailable, so **reload-based persistence and the published GitHub Pages deployment still need a pre-class manual check**.
- Print-to-PDF pagination, actual Minerva submission, Safari/Firefox, screen-reader navigation and formal accessibility audit are **not** claimed as completed.
- Live hosting, university logo authorisation and intervention cost realism are outside this local test.

## Pre-class acceptance checklist

1. Open `index.html` locally, set a team name, refresh, check that it persists (if the browser permits localStorage).
2. Change costs, set a What-if, save JSON; open on the *same and another* origin and confirm import works.
3. Run a complete audit and board resolution, export report, confirm printed PDF fits classroom expectations.
4. Test keyboard-only navigation and browser zoom at 200%.
5. Confirm lecturer-provided Minerva submission instructions and logo permission.
