# cs5412-dairy-project
Estrus and Pregnancy Prediction CS 5412 Final Project

Initial version of our web demo at https://cow-dashboard.herokuapp.com/

## The Problem We Are Solving
(Cow) Estrus and pregnancy prediction based on the combination of behavioral and physiological features collected by automated sensors (Smartbow) with cow health, production, and reproductive performance data. Ultimately, we want to develop models to predict the outcome of an insemination using sensor and non-sensor data collected before insemination. 

## Our Approach

- First, we use Azure Cosmos DB table to store a portion of the dataset provided by ANSC students.

- We use Azure ML and other Azure App services to train a supervised learning model to predict desired variables.

- We use Azure IoT hub to simulate receiving live streams of data from sensors.

- We then connect our backend to a frontend dashboard to demo our cloud system.

- Finally, we evaluate our system on performance, scalability and fault-tolerance.


## Final Deliverables
We will demo our data management and analytics system on a public hosted **web dashboard** where users can **monitor continuous streams of IoT data**, and **view real-time predictions and other insights**.


## Get Started
```bash
git clone https://github.com/ZiweiGu/cs5412-dairy-project.git
cd cs5412-dairy-project
# # Create a new python3 virtualenv named venv.
virtualenv -p python3 venv 
# Activate venv
source venv/bin/activate
# Install all requirements
pip install -r requirements.txt
# Set environment
source .env
# Run the app in localhost!
python3 app.py
# Push to heroku (after changes are made)
heroku update
heroku auth:login
git push heroku main
```
