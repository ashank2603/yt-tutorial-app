import random
import streamlit as st

from yt_extractor import get_info
import database_service as dbs


@st.cache(allow_output_mutation=True)
def get_tutorials():
    return dbs.get_all_tutorials()

def get_duration_text(duration_s):
    seconds = duration_s % 60
    minutes = int((duration_s / 60) % 60)
    hours = int((duration_s / (60*60)) % 24)
    text = ''
    if hours > 0:
        text += f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    else:
        text += f'{minutes:02d}:{seconds:02d}'
    return text

st.title("Tutorial App")

menu_options = ("Today's tutorials", "All tutorials", "Add tutorial")
selection = st.sidebar.selectbox("Menu", menu_options)

if selection == "All tutorials":
    st.markdown(f"## All tutorials")
    
    tutorials = get_tutorials()
    for tuts in tutorials:
        url = "https://youtu.be/" + tuts["video_id"]
        st.text(tuts['title'])
        st.text(f"{tuts['channel']} - {get_duration_text(tuts['duration'])}")
        
        ok = st.button('Delete tutorial', key=tuts["video_id"])
        if ok:
            dbs.delete_tutorial(tuts["video_id"])
            # st.legacy_caching.clear_cache()
            st.experimental_rerun()
            
        st.video(url)
    else:
        st.text("No tutorials in Database!")
elif selection == "Add tutorial":
    st.markdown(f"## Add tutorial")
    
    url = st.text_input('Please enter the video url')
    if url:
        tutorial_data = get_info(url)
        if tutorial_data is None:
            st.text("Could not find video")
        else:
            st.text(tutorial_data['title'])
            st.text(tutorial_data['channel'])
            st.video(url)
            if st.button("Add tutorial"):
                dbs.insert_tutorial(tutorial_data)
                st.text("Added tutorial!")
                # st.legacy_caching.clear_cache()
else:
    st.markdown(f"## Today's tutorial")
    
    tutorials = get_tutorials()
    if not tutorials:
        st.text("No tutorials in Database!")
    else:
        tuts = dbs.get_tutorial_today()
        
        if not tuts:
            # not yet defined
            tutorials = get_tutorials()
            n = len(tutorials)
            idx = random.randint(0, n-1)
            tuts = tutorials[idx]
            dbs.update_tutorial_today(tuts, insert=True)
        else:
            # first item in list
            tuts = tuts[0]
        
        if st.button("Choose another tutorial"):
            tutorials = get_tutorials()
            n = len(tutorials)
            if n > 1:
                idx = random.randint(0, n-1)
                tut_new = tutorials[idx]
                while tut_new['video_id'] == tut['video_id']:
                    idx = random.randint(0, n-1)
                    tut_new = tutorials[idx]
                tut = tut_new
                dbs.update_tutorial_today(tut)
        
        url = "https://youtu.be/" + tuts["video_id"]
        st.text(tuts['title'])
        st.text(f"{tuts['channel']} - {get_duration_text(tuts['duration'])}")
        st.video(url)
    
