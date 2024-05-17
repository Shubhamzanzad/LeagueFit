import streamlit as st
import requests
import pandas as pd
import io

def handle_click(attribute, recommend, contribution):
    try:
        response = requests.post("http://backend:8000/addPlayer", json={
            "overall": attribute[8],
            "potential": attribute[12],
            "wage_eur": recommend['wage_eur'],
            "age": attribute[0],
            "height_cm": attribute[4],
            "weight_kg": attribute[16],
            "international_reputation": attribute[5],
            "pace": attribute[9],
            "shooting": attribute[14],
            "passing": attribute[10],
            "dribbling": attribute[2],
            "physic": attribute[11],
            "contribution_type": contribution, 
            "league_name": "xyz",
            "club_name": recommend['team_name'],
            "attacking": attribute[1],
            "skill": attribute[15],
            "power": attribute[13],
            "mentality": attribute[6],
            "goalkeeping": attribute[3],
            "movement": attribute[7]
        })
        if response.status_code == 200:
            st.success(f"Successfully added player to {recommend['team_name']}!")
        else:
            st.error("Failed to add player.")
    except Exception as e:
        st.error(f"Failed to add player: {e}")


def main():
    response = requests.get("http://dataset:8008/getDf")
    if response.status_code == 200:
        df = pd.read_csv(io.StringIO(response.text))
        st.title("LeagueFit")
        st.header("Enter Player Attributes")
        col1, col2 = st.columns(2)
        with col1:
            overall = col1.slider("Overall", 0.0, 100.0, 50.0)
            potential = col1.slider("Potential", 0.0, 100.0, 50.0)
            age = col1.slider("Age", 0.0, 40.0, 20.0,step=1.0)
            height = col1.slider("Height", 160.0, 240.0, 180.0)    
            weight = col1.slider("Weight", 50.0, 120.0, 70.0)
            reputation = col1.slider("International Reputation", 1.0, 5.0, 2.0,step=1.0)
            pace = col1.slider("Pace", 0.0, 100.0, 50.0)
            shooting = col1.slider("Shooting", 0.0, 100.0, 50.0)    
            movement = col1.slider("Movement", 0.0, 100.0, 50.0)
        
        with col2:
            passing = col2.slider("Passing", 0.0, 100.0, 50.0)
            dribbling = col2.slider("Dribbling", 0.0, 100.0, 50.0)
            physic = col2.slider("Physic", 0.0, 100.0, 50.0)
            attack = col2.slider("Attack", 0.0, 100.0, 50.0)
            skill = col2.slider("Skill", 0.0, 100.0, 50.0)
            power = col2.slider("Power", 0.0, 100.0, 50.0)
            mentality = col2.slider("Mentality", 0.0, 100.0, 50.0)
            goal_keeping = col2.slider("Goal Keeping", 0.0, 100.0, 50.0)
            contribution = col2.slider("Contribution Type",0.0,1.0,step=1.0)
            
        attribute = [age,attack,dribbling,goal_keeping,height,reputation,mentality,movement,overall,pace,passing,physic,potential,power,shooting,skill,weight] 

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
                                        **Team Name**: {str(recommend['team_name'])}\n
                                        **Median Salary**(in euros): {recommend['wage_eur']}
                                    """
                                )
                            with col2:
                                st.button("Accept Recommendation", key=f"btn_{ind}", on_click=handle_click,args=(attribute,recommend,contribution))
            except ValueError as e:
                st.error("Error: Unable to decode JSON. No recommendations available.")
        

if __name__ == "__main__":
    main()
