from tkinter import *
import speedtest

root = Tk()
root.title("Speedy McTesterton")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg= "#1a212d")


def speed_check():
    '''
    Run an internet speed test including ping, 
    upload, and download speed. Output the different
    values to pre - determined locations on the GUI.
    '''
    server_names = []
    x = 0
    for x in range(0, 2):
        test = speedtest.Speedtest()
        test.get_servers(server_names)
        test.get_best_server()

        uploading = round(test.upload() / (1000*1000), 2)
        upload.config(text= uploading)

        downloading = round(test.download() / (1000*1000), 2)
        download.config(text= downloading)
        center_download.config(text= downloading)

        ping.config(text= test.results.ping)
    
    return

'Add the tiny icon at the top left of the window.'
image_icon = PhotoImage(file= "assets/bolt_icon.png")
root.iconphoto(False, image_icon)

'Pack the top graphic in the window.'
top = PhotoImage(file= "assets/top_rings.png")
Label(root, image= top, bg= "#1a212d").pack()

'Pack the large middle graphic.'
main = PhotoImage(file= "assets/speed_dial.png")
Label(root, image= main, bg= "#1a212d").pack(pady= (40, 0))

'Pack the button.'
button = PhotoImage(file= "assets/start_button.png")
start_button = Button(root, image= button, bg= "#1a212d", bd= 0, activebackground= "#1a212d", cursor= "hand2", command= speed_check)
start_button.pack(pady= 10)

"Place the ping, up, and down labels in the window."
Label(root, text= "PING", font= "arial 10 bold", bg= "#384056").place(x= 45, y= 0)
Label(root, text= "DOWNLOAD", font= "arial 10 bold", bg= "#384056").place(x= 140, y= 0)
Label(root, text= "UPLOAD", font= "arial 10 bold", bg= "#384056").place(x= 267.5, y= 0)

'Place labels for the ping, up, and down labels.'
Label(root, text= "ms", font= "arial 7 bold", bg= "#384056", fg= "white").place(x= 55, y= 80)
Label(root, text= "mbps", font= "arial 7 bold", bg= "#384056", fg= "white").place(x= 165, y= 80)
Label(root, text= "mbps", font= "arial 7 bold", bg= "#384056", fg= "white").place(x= 282.5, y= 80)

'Place center labels.'
Label(root, text= "Download", font= "arial 15 bold", bg= "#384056", fg= "white").place(x= 130, y= 240)
Label(root, text= "mbps", font= "arial 15 bold", bg= "#384056", fg= "white").place(x= 150, y= 455)

'Place number holders throuought the window.'
ping = Label(root, text= "00", font= "arial 13 bold", bg= "#384056", fg= "white")
ping.place(x= 65, y= 60, anchor= "center")

download = Label(root, text= "00", font= "arial 13 bold", bg= "#384056", fg= "white")
download.place(x= 181, y= 60, anchor= "center")

upload = Label(root, text= "00", font= "arial 13 bold", bg= "#384056", fg= "white")
upload.place(x= 299, y= 60, anchor= "center")

center_download = Label(root, text= "00", font= "arial 22 bold", bg= "#384056")
center_download.place(x= 181, y= 400, anchor= "center")

root.mainloop()