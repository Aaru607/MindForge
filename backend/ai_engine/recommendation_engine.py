import datetime
import logging
logger = logging.getLogger(__name__)

async def generate_career_recommendations(user_id, assessment_data):
    """
    Main function to calculate career matches. 
    It takes the user's test scores and compares them against our database.
    """
    if not assessment_data:
        logger.error(f"No assessment data found for user {user_id}")
        return []
    try:
        user_profile = await mongo_client.get_user_profile(user_id)
        top_category = assessment_data.get('aptitude_scores', {}).get('primary')
        career_candidates = await db_client.fetch_careers_by_category(top_category)
    except Exception as e:
        logger.error(f"Database error: {e}")
        return []
    recommendations = []
    for career in career_candidates:
        aptitude_score = assessment_data['aptitude_scores'].get(career.required_field, 0)
        interest_score = assessment_data['interest_profiles'].get(career.type, 0)
        base_score = (aptitude_score * 0.5) + (interest_score * 0.3) + (50 * 0.2)
        if career.demand == "High":
            base_score += 10
        elif career.demand == "Low":
            base_score -= 10
        recommendations.append({
            "career_id": career.id,
            "title": career.title,
            "match_percent": round(base_score, 2),
            "reasoning": f"Matches your interest in {career.type} and high aptitude scores.",
            "salary": career.salary_range,
            "created_at": datetime.datetime.now().isoformat()
        })
    recommendations.sort(key=lambda x: x['match_percent'], reverse=True)
    cache_key = f"user_rec_{user_id}"
    await redis_cache.set(cache_key, recommendations, expire=3600)
    return recommendations[:5]
