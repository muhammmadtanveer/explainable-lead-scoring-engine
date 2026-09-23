import json, sys
from pathlib import Path

def score(lead):
    points, reasons = 0, []
    if lead.get("consent") is not True:
        return {"id": lead.get("id"), "score": 0, "route": "data-review", "reasons": ["missing marketing consent"]}
    if lead.get("email_opened"): points += 10; reasons.append("opened email (+10)")
    if lead.get("clicked_offer"): points += 20; reasons.append("clicked offer (+20)")
    if lead.get("demo_requested"): points += 40; reasons.append("requested demo (+40)")
    if lead.get("company_size", 0) >= 20: points += 15; reasons.append("team-size fit (+15)")
    if lead.get("days_since_activity", 999) <= 7: points += 15; reasons.append("recent activity (+15)")
    if not lead.get("email"): reasons.append("missing email; record quality risk")
    route = "priority-sales" if points >= 60 else "nurture" if points >= 25 else "education"
    return {"id": lead.get("id"), "score": points, "route": route, "reasons": reasons}

if __name__ == "__main__":
    if len(sys.argv) != 2: raise SystemExit("Usage: python3 app.py data/leads.json")
    leads = json.loads(Path(sys.argv[1]).read_text())
    decisions = [score(lead) for lead in leads]
    print(json.dumps({"decisions": decisions, "summary": {"priority_sales": sum(x["route"]=="priority-sales" for x in decisions)}}, indent=2))
