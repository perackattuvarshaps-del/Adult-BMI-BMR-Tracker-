
import streamlit as st

st.set_page_config(page_title="Adult BMI BMR Tracker",layout="wide")

st.sidebar.title("About BMI and BMR")

st.sidebar.subheader("BMI(Body Mass Index)")
st.sidebar.write("A measure of weight related to height.")

st.sidebar.markdown("""

           BMI Categories
            -------------
           Underweight  : < 18.5
                      
           Normal  : 18.5 - 24.9
                    
           Overweight  : 25 - 29.9
                    
           Obese class I  : 30 - 34.9
                    
           Obese class II  : 35 - 39.9
                    
           Obese class III : > 39.9                                                   
                    
"""
                   )

st.sidebar.subheader("BMR(Basal Metabolic Rate)")

st.sidebar.write("The calories your body needs to keep you alive.")

st .sidebar.caption("⚠️This Tracker is for adults only(19+ years).For children, please use a child specific calculator.")

st.title("Adult BMI BMR Tracker")

tab1,tab2=st.tabs(["BMI Calculator","BMR Calculator"])


with tab1:
    st.header("BMI Calculator")

    weight=st.number_input("Weight(Kg)",min_value =30,max_value=300,value=55)

    height=st.number_input("Height(cm)",min_value=120,max_value=200,value= 150)

    age=st.number_input("Age",min_value=1,max_value=120,value=25)


    adult_age = age >=19

    if not adult_age:

       st.warning("This Tracker is for adults only (19+ years)")

    calculate =st.button("Calculate BMI",disabled=not adult_age)  
     

    
    if  calculate and adult_age:
              
       height_m=height/100

       bmi = weight/(height_m **2)

       st.metric("BMI (kg/m²)",round(bmi,2))

       if bmi < 18.5:
                   category = "Underweight"

                   advice= """

                   Weight is less than the normal recommended weight ,
                            Eat more nutritious food with adequate exercise"""
                   
       elif bmi>18.5 and bmi<=24.9:

                    category="Normal"
                    
                    advice="""

                             Weight is within the normal recommended range,
                             Maintain your weight with adequate exercise."""
            

       elif bmi>=25 and bmi<=29.9:

                    category= "Overweight"

                    advice="""

                             Weight is more than the normal recommended weight,
                             Follow a balanced diet and bring down your weight with more exercise."""
            
       elif bmi>=30 and bmi<=34.9:

                     category = "Obese class I"

                     advice="""

                            An early stage of obesity,consult a doctor first,
                            follow a balanced diet, stay active daily,get enough sleep,
                            Aim for gradual weight loss."""
           

       elif bmi>=35 and bmi<=39.9:

                     category="Obese class II"

                     advice="""

                            Moderate obesity,Consult a doctor, follow a balanced diet,
                             Exercise regularly,improve sleep,manage stress,
                             Aim gradual and steady weight loss under medical supervision."""
            
       else:
                     category="Obese class III"

                     advice="""

                             Follow a strict balanced diet,
                             Engage in safe physical activity,improve sleep,manage stress,
                             Aim for steady and medically supervised weight loss."""
                     

       st.success(f" Category : {category}")
       st.markdown(f"Advice : {advice} ")   


with tab2:
    st.header("BMR Calculator")

    gender=st.radio("Gender",["Male","Female"])

    weight_bmr=st.number_input("Weight(Kg)",min_value =30,max_value=300,value=55,key="bmr_weight")

    height_bmr=st.number_input("Height(cm)",min_value=120,max_value=200,value= 150,key="bmr_height")

    age_bmr=st.number_input("Age",min_value=1,max_value=120,value=25,key="bmr_age")

    adult_age_bmr = age_bmr >=19

    if not adult_age_bmr:

       st.warning("This Tracker is for adults only (19+ years)")

           
                 
    finding_bmr=  st.button("Calculate BMR",disabled=not adult_age_bmr) 

    

    if finding_bmr and adult_age_bmr:
            
            if gender=="Male":
                     
              bmr = (10*weight_bmr)+(6.25*height_bmr)-(5*age_bmr)+5

            else:
             
              bmr = (10*weight_bmr)+(6.25*height_bmr)-(5*age_bmr)-161  


            st.success(f"BMR(Kcal/day) : {round(bmr,2)}")

    