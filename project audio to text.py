import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            txtSpeech.insert(tk.END, "Listening...\n")
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, text + "\n")

        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Could not understand audio\n")

        except sr.RequestError as e:
            txtSpeech.insert(tk.END, "Error: {0}\n".format(e))

        except OSError as e:
            txtSpeech.insert(tk.END, "Microphone access error: {0}\n".format(e))

        except Exception as e:
            txtSpeech.insert(tk.END, "An unexpected error occurred: {0}\n".format(e))
            
        finally:
            txtSpeech.insert(tk.END, "Ready for next input\n")

def reset_txtSpeech():
    txtSpeech.delete("1.0", tk.END)

def Exit_Speech():
    iExit = messagebox.askquestion("Exit", "Confirm if you want to exit?")
    if iExit == 'yes':
        messagebox.showinfo("Goodbye", "Goodbye")
        root.destroy()

root = tk.Tk()
root.title("Speech to Text")

RootFrame = tk.Frame(root, width=700, height=500, bd=10, bg='cadet blue')
RootFrame.pack()

MainFrame = tk.Frame(RootFrame, bd=10, width=780, height=380)
MainFrame.pack()

lblTitle = tk.Label(MainFrame, font=('arial', 70, 'bold'), text="Speech To Text", width=17)
lblTitle.pack()

txtSpeech = tk.Text(MainFrame, font=('arial', 25, 'bold'), width=50, height=11)
txtSpeech.pack()

btnConvert = tk.Button(MainFrame, font=('arial', 25, 'bold'), text="Convert", width=17, height=2, command=Speech_to_Text)
btnConvert.pack(side=tk.LEFT, padx=10)

btnReset = tk.Button(MainFrame, font=('arial', 25, 'bold'), text="Reset", width=17, height=2, command=reset_txtSpeech)
btnReset.pack(side=tk.LEFT, padx=10)

btnExit = tk.Button(MainFrame, font=('arial', 25, 'bold'), text="Exit", width=17, height=2, command=Exit_Speech)
btnExit.pack(side=tk.LEFT, padx=10)

root.mainloop()
