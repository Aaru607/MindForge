import json
import logging
logger = logging.getLogger(__name__)

def generate_career_recommendation(user_profile, llm_client):
    """
    Main function to take user data and get career advice from the AI.
    Handles the prompt building and basic parsing of the AI's response.
    """
    if not user_profile.get("skills") or not user_profile.get("career_goal"):
        logger.error("User profile is missing key data")
        return {"error": "Incomplete profile"}
    skills_list = ", ".join(user_profile["skills"])
    interest_list = ", ".join(user_profile.get("interests", ["General Development"]))
    system_msg = (
        "You are a career coach. Based on the user's data, provide exactly 3 career paths. "
        "Return the response in a valid JSON format with keys: 'role', 'why', and 'steps'."
    )
    
    user_msg = f"""
    Here is my profile:
    - Skills: {skills_list}
    - Interests: {interest_list}
    - Goal: {user_profile['career_goal']}
    - Level: {user_profile.get('experience_level', 'Entry-level')}
    
    Please give me specific, non-generic advice.
    """

    try:
        raw_response = llm_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_msg}
            ],
            temperature=0.7 
        )
        
        content = raw_response.choices[0].message.content
        
        try:
            structured_data = json.loads(content)
        except json.JSONDecodeError:
            logger.warning("AI didn't return perfect JSON. Attempting to clean string.")
            content = content.replace("```json", "").replace("```", "").strip()
            structured_data = json.loads(content)

        return {
            "status": "success",
            "data": structured_data,
            "version": "v1.2"
        }

    except Exception as e:
        logger.exception("Something went wrong with the LLM call")
        return {"status": "error", "message": str(e)}
