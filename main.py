import tkinter as tk

#master variable maybe this is for a window
window = tk.Tk()
window.title('o ye')

#the amazing label to let the users know we need a sentence
tk.Label(window, text="Sentence: ", width = 15).grid(column = 0)

#the input field itself
userInput = tk.Entry(window, width = 45)

userInput.grid(row=0, column=1)

tk.Button(window, text='Quit', command = window.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
                                    

window.mainloop()
