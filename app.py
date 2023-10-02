import streamlit as st
from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        title = yt.title
        st.write("Video Title:", title)
        st.write("Downloading...")
        yt.streams.first().download()
        st.write("Download completed!!")
    except Exception as e:
        st.write("Error:", e)

# Streamlit app
def main():
    st.title("YouTube Video Downloader")

    # User input for YouTube URL
    url = st.text_input("Enter YouTube Video Link:")

    # Display video title
    title = ""
    if url:
        try:
            yt = YouTube(url)
            title = yt.title
        except:
            title = "Invalid URL"

    st.write("Video Title:", title)

    # Download button
    if st.button("Download"):
        if url and title != "Invalid URL":
            download_video(url)

# Run the Streamlit app
if __name__ == "__main__":
    main()
