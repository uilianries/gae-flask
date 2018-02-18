# gae-flask

Just another Google App Engine Flask example

### Instructions
* Mount this project on Google Cloud SDK container
      docker run --rm -ti ${PWD}:/root/project google/cloud-sdk

* Move to project directory
      cd /root/project

* Install dependencies in `lib/`
      pip install -r requirements.txt -t lib
* Login on Google cloud account
      gcloud auth login
* Set current project id
      gcloud config set project $PROJECT_ID
* Deploy
      gcloud app deploy
* Visit the application in the web browser:
      gcloud app browse
* Enjoy!

To get more information, visit [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)

#### NOTE
* Do not forget to enable [Cloud SQL Admin API](https://console.developers.google.com/apis/api/sqladmin.googleapis.com/overview)

#### LICENSE
[MIT](LICENSE)
