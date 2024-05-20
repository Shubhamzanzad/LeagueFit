import streamlit as st
import requests
import random

def handle_click(attribute, recommend):
    try:
        response = requests.post("http://backend:8000/addPlayer", json={
            "overall": attribute[10],
            "potential": attribute[14],
            "wage_eur": recommend['wage_eur'],
            "age": attribute[0],
            "height_cm": attribute[6],
            "weight_kg": attribute[18],
            "international_reputation": attribute[7],
            "pace": attribute[11],
            "shooting": attribute[16],
            "passing": attribute[12],
            "dribbling": attribute[4],
            "defending":attribute[3],
            "physic": attribute[13],
            "contribution_type": attribute[2], 
            "league_name": "xyz",
            "club_name": recommend['club_name'],
            "name": 'Rolando'+str(random.randint(100,999)),
            "attacking": attribute[1],
            "skill": attribute[17],
            "power": attribute[15],
            "mentality": attribute[8],
            "goalkeeping": attribute[5],
            "movement": attribute[9]
        })
        if response.status_code == 200:
            st.success(f"Successfully added player to {recommend['club_name']}!")
        else:
            st.error("Failed to add player.")
    except Exception as e:
        st.error(f"Failed to add player: {e}")


def main():
    st.title("LeagueFit")
    st.header("Enter Player Attributes")

    col1, col2 = st.columns(2)
    with col1:
        overall = col1.slider("Overall", 0.0, 100.0, 76.0)
        potential = col1.slider("Potential", 0.0, 100.0, 80.0)
        age = col1.slider("Age", 20.0, 40.0, 26.0)
        height = col1.slider("Height", 150.0, 200.0, 182.0)    
        weight = col1.slider("Weight", 50.0, 100.0, 70.0)
        reputation = col1.slider("International Reputation", 1.0, 5.0, 1.7)
        pace = col1.slider("Pace", 0.0, 100.0, 71.0)
        shooting = col1.slider("Shooting", 0.0, 100.0, 60.0)    
        passing = col1.slider("Passing", 0.0, 100.0, 67.0)

    with col2:
        dribbling = col2.slider("Dribbling", 0.0, 100.0, 72.0)
        defence = col2.slider("Defence", 0.0, 100.0, 58.0)
        physic = col2.slider("Physic", 0.0, 100.0, 72.0)
        contribution= col2.slider("Contribution", 0.0, 1.0, step=1.0)
        attack = col2.slider("Attack", 0.0, 100.0, 59.0)
        skill = col2.slider("Skill", 0.0, 100.0, 61.0)
        movement = col2.slider("Movement", 0.0, 100.0, 69.0)
        power = col2.slider("Power", 0.0, 100.0, 67.0)
        mentality = col2.slider("Mentality", 0.0, 100.0, 62.0)
        goal_keeping = col2.slider("Goal Keeping", 0.0, 100.0, 21.0)
        
    attribute = [age,attack,contribution,defence,dribbling,goal_keeping,height,reputation,mentality,movement,overall,pace,passing,physic,potential,power,shooting,skill,weight] 
    
    if st.button("Get Recommendations"):
        try:
            response = requests.post("http://backend:8000/recommend", json={
                "numbers": attribute
            })
            recommendations = response.json()
            st.session_state['recommendations'] = recommendations

            if 'recommendations' in st.session_state:  
                st.header("Top 5 Recommended Players:")
                for ind, recommend in enumerate(st.session_state['recommendations']):
                    with st.container():
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(
                                f"""
                                    **Team Name**: {str(recommend['club_name'])}\n
                                    **Average Salary**(in euros): {recommend['wage_eur']}
                                """
                            )
                        with col2:
                            st.button("Accept Recommendation", key=f"btn_{ind}", on_click=handle_click,args=(attribute,recommend))
        except ValueError as e:
            st.error("Error: Unable to decode JSON. No recommendations available.")
            

if __name__ == "__main__":
    main()
