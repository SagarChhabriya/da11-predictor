# da11-predictor

ML Project

1. Create a GitHub repo
	- Title, public, README.md, .gitignore: python
	- Clone the repo
		- In case of multiple GitHub accounts
			- instead of `git clone https://example.com/open-source/library.git`, run:
			- git clone https://contrib123@example.com/open-source/library.git	
		https://github.com/SagarChhabriya/income-predictor.git
	- open this repo in vs code
	
	- https://SagarChhabriya@github.com/SagarChhabriya/AI16-predictor.git

	https://SagarChhabriya@github.com/SagarChhabriya/da11-predictor.git


	
2. create virtual env
	- activate the env, in case you get a command not recognized error
		- Execute this command in the VS Code PowerShell instance: Set-ExecutionPolicy RemoteSigned -Scope Process
	- install the required libraries: pip install Jupyter ipykernel numpy pandas matplotlib seaborn scikit-learn 
 

3. Data Gathering and Model Training (model.ipynb)
	- select the kernel
	- Load Data and import libraries
	- preprocessing + train test split
	- model training
	- Model evaluation
	- Testing on new instances
	- Model serialization

4. app.py (streamlit UI)
	- import libraries
	- page, title, doc title
		- run file: streamlit run app.py
	- load model
	- define input fields: st.number_input()
	- make prediction: st.success

5. requirements.txt
	- module.__version__
	- don't do pip freeze

6. streamlit community cloud
	- connect / continue with GitHub
	- utilize default CI/CD
	


