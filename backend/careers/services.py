def generate_recommendations(interests, skill_level):
    recommendations = []
    if "Technology" in interests:
        recommendations.append("Software Engineering")

    if "Science" in interests:
        recommendations.append("Data Science")

    if skill_level in ["Advanced", "Expert"]:
        recommendations.append("AI / ML Engineer")

    return recommendations
