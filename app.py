import numpy as np
import pandas as pd
import tensorflow as tf
import keras
import streamlit as st
from PIL import Image


classifier = tf.keras.models.load_model('model.h5')
classifier.summary()

def welcome():
    return "Welcome All"

def diabetic_predict(c,g,a,d,f,BMI,e,b):
    
    prediction=classifier.predict([[c,g,a,d,f,BMI,e,b]])
    print(prediction)
    return prediction
    
def main():
    # st.title("@Travelify")
  
    html_temp = """
    <div style="background-color:Orange;padding:10px">
    <h1 style="color:white;text-align:center;"><em>Diabeticsica
</em> </h1>
    </div>
    <hr>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.write('''
    # Procedure to use this App:
    ### Input the following.
    * Enter your Age, Height, Weight.
    * Diastolic blood pressure (in mm Hg).
    * Pregnancy Count
    * Tricep Skinfold Thickness (in millimeters), using your Skinfold Caliper. If you do not know how to use Caliper, click on "Know" button below
    * Then Proceed to Diabetic Pedigree function.
    
''')
    b = st.number_input("Enter is your Age (yr)",step=1.0,max_value=150.0)
    
    
    height= st.slider(label='Enter is your Height(in centimeter)?',min_value=30,max_value=200,step=1)
    weight= st.slider(label='Enter is your Weight(in Kg)?',min_value=5,max_value=150,step=1)
    BMI= 0 #Input to model
    if height>0:
        BMI= weight/((height/100)**2)
    st.write('Your BMI',BMI)
    a = st.slider("Enter Your Blood Pressure (mm Hg)",0.0,122.0,step=1.0)
    
    c= st.number_input(label='How many number of times you have been pregnent?',min_value=0.0,step=1.0) 
    d = st.number_input(label="Enter Your Tricep Skinfold Thickness (in mm)",min_value=0.0)
    if st.button('To know Skinfold Thinkness'):
        st.image("1.jpg")
        st.write('''
        #### Ideal Tricep Skinfold Thickness is around 20.0 mm
    ''')
    e = st.number_input("Diabetic Pedigree Function",min_value=0.0,max_value=1.0)
    if st.button("Know Pedigree Function"):
        st.write('''
                 * Diabetes pedigree function (a function which scores likelihood of diabetes based on family history) 
                 * Age: Age (years) 
                 * Outcome: Class variable (0 if non-diabetic, 1 if diabetic)
                 
                 #### Tip:
                     *Average Diabetic Pedigree Function score for a person from Diabetic family is < 0.5
                     *Average Diabetic Pedigree Function score for a person from non-Diabetic family is > 0.5
                 
                 ''')
    f = st.number_input("Insulin",min_value=0.0)
    g = st.number_input("Glucose",min_value=0.0)
    # h = st.number_input("h")
   
    if st.button("Predict"):
        if b<=0:
            st.write('''
            #### Please Enter Your Age(yr)
            ''')
        elif a<=0:
            st.write('''
            
            #### Please Enter Your Blood Pressure (mm Hg)
            ''')
        
        elif d<=0:
            st.write('''
            #### Please Enter Your Tricep Skinfold Thickness (in mm)
            ''')

        elif e<=0:
            st.write('''
            #### Please Enter Diabetic Pedigree Function
            ''')
        
        elif height<=30:
            st.write('''
            #### Please Enter Your Height
            ''')

        elif weight<5:
            st.write('''
            #### Please Enter Your weight
            ''')

        else:
            result=diabetic_predict(c,g,a,d,f,BMI,e,b)
        
            if(result<=0.75):
                st.write('''
                ## Congratulations....!!!! 
                ''')
                
                html_temp1 = """
                <div style="background-color:Yellow;padding:10px">
                <h2 style="color:Black;text-align:center;"><em>You are not Diabetic
                </em> </h2>
                </div>
                <hr>
                            """
        
                st.markdown(html_temp1,unsafe_allow_html=True)
                st.image('https://banner2.cleanpng.com/20180928/zgk/kisspng-megadeth-dave-tumblr-5bae41dad049e2.5155379115381467788532.jpg',width=500)
                
                
            elif(result >0.75):
                st.write('''
                ### Calm Down.. 
                ## you are a Diabetic
                ## Please visit your nearest lab for Glucose Tolerance Test
                ''')
            
            
        
        
        
    html_temp3='''
    <hr>
    '''

    st.markdown(html_temp3,unsafe_allow_html=True)
    if st.button("About"):
        
        
        st.warning('''
        ### Developed By Rahul Gowlapalli
        ''')
      
        
if __name__=='__main__':
    main()
