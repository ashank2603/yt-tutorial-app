# yt-tutorial-app

A one stop place to store and access all your youtube tutorials!!

## Demo Screenshot:
![image](https://user-images.githubusercontent.com/61231703/194314888-6f662e92-594e-4076-b76a-37f7580854ea.png)

### How to run:
- Set up a harperDB account and create a free instance.
- In the instance, create a new schema called "workouts" and then two tables: tutorials (hash: video_id) and tutorial_today (hash: id).
- Copy the username, password and url of the instance.
- Clone this repo and create a virtualenv in the directory. Activate it.
- Install streamlit, harperdb, youtube_dl using pip.
- Paste the copied content in the respective placeholders in database_service.py.
- Run "streamlit run app.py" in the terminal to access the app.
