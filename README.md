# hERG
A robust predictor for hERG channel blockade based on deep learning meta-features
# hERG

### **Task:**

*   [x] **Prepare the data for modelling in active learning fashion in Jupyter Notebook**
*   [ ] **Choose data representation**
*   [ ] **Build starting model**
*   [ ] **Decide upon active learning strategy and apply it to improve your model**
*   [ ] **Decide when to stop labelling new data in lab as labelling compounds via lab experiments isalways additional cost**

Second task is to prepare model for production by serving the model as API and package into Docker.

*   [ ] **Organising the code**
*   [ ] **Building the REST API**
*   [ ] **Wrapping served model into Docker**
*   [ ] **Testing**
*   [ ] **Logging**
*   [ ] **Load testing of deployed model inference**

Docker Run:

Step 1: git clone https://github.com/santuchal/hERG.git
Step 2: cd hERG
Step 3: Build docker image using: docker image build -t flask_docker .
Step 4: Run newly created docker container: docker run -p 5000:5000 -d flask_docker
Step 5: Open testing API open [Postman](https://www.postman.com/)
Step 6: Chek URL http://0.0.0.0:5000/ 
Step 7: Stop all container: docker stop $(docker ps -a -q) 