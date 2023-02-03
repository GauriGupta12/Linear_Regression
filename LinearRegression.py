import streamlit as st
import sklearn
import joblib,os
import numpy as np 

# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def main():
	"""Very Simple Linear Regression App"""

	st.title("Salary Determination App")

	html_templ = """
	<div style="background-color:blue;padding:10px;">
	<h3 style="color:yellow">Linear Regression for Salary Determination</h3>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Salary Determination","About"]
	choice = st.sidebar.selectbox("Menu",activity)

# Salary Determination CHOICE
	if choice == 'Salary Determination':

		st.subheader("Salary Determination")
		experience = st.slider("Years of Experience",0,20)
		if st.button("Determination"):

			regressor = load_prediction_model("C:/Users/USER/Downloads/linear_regression_salary.pkl")
			experience_reshaped = np.array(experience).reshape(-1,1)


			predicted_salary = regressor.predict(experience_reshaped)

			st.info("Salary related to {} years of experience: {}".format(experience,(predicted_salary[0][0].round(2))))


if __name__ == '__main__':
	main()