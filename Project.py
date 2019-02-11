from tkinter import Tk, Label, Button
from PIL import Image
import pytesseract
import io
import speech_recognition as sr

root = Tk()
#root.attributes('-fullscreen',True)

root.geometry("400x400+800+300") #You want the size of the app to be 400x400
root.resizable(0, 0)

msg = Label(root, text = "EXTRACT TEXT USING OCR",background = 'lightblue',foreground='darkblue')
msg.config(font = ('georgia',20,' bold underline'))
msg.grid(row = 5, column = 10)

def my_callback1():
    im = Image.open("text.jpg")
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text)

    text_file = open("Output1.txt", "w")
    text_file.write(text)
    text_file.close()

label1 = Label(root, text = "EXTRACT TEXT FROM IMAGE", background = 'yellow',foreground='red')
label1.config(font = ('callibri',10,' bold underline'))
label1.grid(row = 50,column = 10,ipadx = 20,ipady=10)

msg_button1 = Button(root, text = 'Image to Text', command = my_callback1).grid(row = 150,column = 10,ipadx = 20,ipady=10)

def my_callback2():
    from wand.image import Image as wi
    pdf = wi(filename = "sample.pdf", resolution = 300)
    pdfImage = pdf.convert('jpeg')

    imageBlobs = []

    for img in pdfImage.sequence:
        imgPage = wi(image = img)
        imageBlobs.append(imgPage.make_blob('jpeg'))

    recognized_text = []

    for imgBlob in imageBlobs:
        im = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(im, lang = 'eng')
        recognized_text.append(text)

    print(recognized_text)
    text_file = open("Output2.txt", "w")
    text_file.write(text)
    text_file.close()

label2 = Label(root, text = "EXTRACT TEXT FROM PDF", background = 'yellow',foreground='red')
label2.config(font = ('callibri',10,' bold underline'))
label2.grid(row = 250,column = 10,ipadx = 20,ipady=10)

msg_button2 = Button(root, text = 'PDF to Text', command = my_callback2).grid(row = 350,column = 10,ipadx = 20,ipady=10)



def my_callback3():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry, could not recognize what you said.")
    

label3 = Label(root, text = "SPEECH RECOGNITION", background = 'yellow',foreground='red')
label3.config(font = ('callibri',10,' bold underline'))
label3.grid(row = 450,column = 10,ipadx = 20,ipady=10)

msg_button3 = Button(root, text = 'Audio to Text', command = my_callback3).grid(row = 550,column = 10,ipadx = 20,ipady=10)

label4 = Label(root, text = "EXIT PROGRAM", background = 'yellow',foreground='red')
label4.config(font = ('callibri',10,' bold underline'))
label4.grid(row = 650,column = 10,ipadx = 60,ipady=10)

exit_button = Button(root, text = 'Exit Program', command = root.destroy).grid(row = 750,column = 10,ipadx = 20,ipady=10)

root.mainloop()

