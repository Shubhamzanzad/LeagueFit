import streamlit as st
import requests

def main():
    st.title("LeagueFit")
    st.header("Enter Player Attributes")
    col1, col2 = st.columns(2)
    with col1:
        overall = col1.slider("Overall", 0.0, 100.0, 50.0)
        potential = col1.slider("Potential", 0.0, 100.0, 50.0)
        age = col1.slider("Age", 0.0, 40.0, 20.0)
        height = col1.slider("Height", 15.0, 40.0, 20.0)    
        weight = col1.slider("Weight", 50.0, 120.0, 70.0)
        reputation = col1.slider("International Reputation", 1.0, 5.0, 2.0)
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
        
    attribute = [age,attack,dribbling,goal_keeping,height,reputation,mentality,movement,overall,pace,passing,physic,potential,power,shooting,skill,weight] 
    
    if st.button("Get Recommendations"):
        try:
            response = requests.post("http://backend:8000/recommend", json={
                "numbers": attribute
            })
            recommendations = response.json()
            st.write("Top 5 Recommended Players:")
            for ind, i in enumerate(recommendations):
                st.write("Team Name: ", i['team_name'])
                st.write("Average Wage in Euros: ", i['wage_eur'])
                # st.write("Recommendation Number:", ind + 1)
                if st.button("Accept Recommendation", key=f"accept_{ind}", help=str(ind)):
                    request = requests.post("http://backend:8000/append", json={
                        "dataToAppend": recommendations[ind]
                    })
        except ValueError as e:
            st.error("Error: Unable to decode JSON. No recommendations available.")
            

if __name__ == "__main__":
    main()
