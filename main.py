import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageTk

from fire_detection import predict_fire
from hotspot_detection import predict_hotspot

references = {'image_loaded': False}

def show_image():
    upload_file()
    img['image'] = image=references['image_ref']

def upload_file():
    references['image_path'] = tk.filedialog.askopenfilename()
    image_file = ImageTk.PhotoImage(Image.open(references['image_path']).resize((350, 350)))
    references['image_ref'] = image_file
    if references['image_loaded'] == True:
        lat_entry.delete(0, 'end')
        long_entry.delete(0, 'end')
        date_entry.delete(0, 'end')
        fire_result.pack_forget()
        hotspot_result.pack_forget()
    references['image_loaded'] = True
    lat_frame.pack()
    long_frame.pack()
    date_frame.pack()
    analyze_btn.pack(padx=20, pady=25)

def get_fire_result():
    prediction = predict_fire(image_path=references['image_path'])
    fire_result['text'] = "FIRE DETECTED" if prediction == 1 else "NO FIRE DETECTED"
    fire_result['fg'] = 'red' if prediction == 1 else 'white'
    fire_result.pack()
    return prediction

def get_hotspot_result():
    try:
        prediction = predict_hotspot(latitude=float(lat_entry.get()), longitude=float(long_entry.get()), date=date_entry.get())
        hotspot_result['text'] = "HOTSPOT DETECTED" if prediction == 1 else "NO HOTSPOT DETECTED"
        hotspot_result['fg'] = 'red' if prediction == 1 else 'white'
        hotspot_result.pack()
    except:
        pass

def get_results():
    fire_prediction = get_fire_result()
    if fire_prediction == 0:
        get_hotspot_result()

root = tk.Tk()
root.geometry('500x750')
root.title("Wildfire Detection")
root.iconbitmap('resources/icon.ico')

title = tk.Label(root, text="Wildfire Detection", font=(None, 24))
title.pack(padx=20, pady=25)

upload_btn = tk.Button(root, text="Upload File", command=show_image)
upload_btn.pack()

img = tk.Label()
img.pack(padx=20, pady=20)

lat_frame = tk.Frame()
lat_label = tk.Label(lat_frame, text="Latitude:")
lat_label.pack(side='left', padx=34)
lat_entry = tk.Entry(lat_frame)
lat_entry.pack(side='right', padx=20)

long_frame = tk.Frame()
long_label = tk.Label(long_frame, text="Longitude:")
long_label.pack(side='left', padx=29)
long_entry = tk.Entry(long_frame)
long_entry.pack(side='right', padx=20)

date_frame = tk.Frame()
date_label = tk.Label(date_frame, text="Date (YYYY-MM-DD):")
date_label.pack(side='left')
date_entry = tk.Entry(date_frame)
date_entry.pack(side='right', padx=20)

analyze_btn = tk.Button(root, text="Analyze Image", command=get_results)

fire_result = tk.Label(bg='black', font=(None, 18))
hotspot_result = tk.Label(bg='black', font=(None, 18))

root.mainloop()