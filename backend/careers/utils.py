import csv
from io import TextIOWrapper
from .models import CareerMaster

def process_career_csv(file):
    reader = csv.DictReader(TextIOWrapper(file, encoding="utf-8"))
    count = 0
    for row in reader:
        CareerMaster.objects.update_or_create(
            title=row["title"],
            defaults={
                "category": row["category"],
                "description": row["description"],
                "required_skills": row["required_skills"].split(","),
                "growth_score": int(row["growth_score"]),
            }
        )
        count += 1
    return count
