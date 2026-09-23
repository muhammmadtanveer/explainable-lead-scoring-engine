# Explainable Lead-Scoring Engine

A transparent Python decision engine that scores CRM leads and explains every routing recommendation.

## Why it matters

Automation should not be a black box. Sales teams need to know *why* a lead is prioritized, and scoring rules should avoid using protected or irrelevant personal attributes.

## Capabilities

- Scores engagement, fit, consent, and recency signals
- Returns human-readable score explanations
- Routes leads to priority sales, nurture, or review queues
- Flags incomplete/low-quality records
- Uses synthetic data and Python's standard library only

## Run

```bash
python3 app.py data/sample_leads.json
```

## Design principles

The engine intentionally excludes protected characteristics and provides reason codes alongside scores. In a production system, thresholds should be validated against outcomes, monitored for drift, and reviewed by stakeholders.
