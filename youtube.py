from pytube import YouTube

def downLoad(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        ytObject.download()
        print("successful!")
    except:
        print("something gone wrong!")

link = input("Enter Link:  ")
downLoad(link)
