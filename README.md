#  Face Recognition with Live Webcam Greeting

A simple, interactive Python project that uses your webcam to recognize your face and greet you on screen.

Built using OpenCV and the `face_recognition` library, this project is great for learning about computer vision, or just having a little fun when your computer knows who you are!

---

## ✨ What It Does

- Uses your webcam to detect faces in real-time
- Compares detected faces to a reference photo of you
- If it recognizes you:
  - ✅ It draws a green box around your face
  - ✅ Displays a greeting: `"HI MR SIDDARTH SREENIVAS"`
- If not:
  - ❌ It shows `"Unknown"` and prints that you're not recognized

All of this happens privately, right on your machine.

---

## 🛠 Tech Stack

- `Python` 3.10+
- [`face_recognition`](https://github.com/ageitgey/face_recognition) (built on dlib)
- `OpenCV` for video capture and drawing

---

## 📸 How to Use It

### 1. Clone the project

```bash
https://github.com/SIDDARTH-SREENIVAS/MINI-PROJECTS/blob/33711032dc410943fd7f42791cd769bdddf4e84b/face_recognition01.py
```
### 2.Create and activate a Conda environment

```python
conda create -n faceenv python=3.10
conda activate faceenv
conda install -c conda-forge face_recognition opencv dlib
```
### 3.Add your image
Place a clear, front-facing photo of yourself in the project folder and name it: "yourname.jpg"
here I have used "siddarth.jpg"

### 4.Run

```bash
python face_recognition01.py
```
•	It will open your webcam.
•	If your face matches siddarth.jpg, it will greet you on screen.
•	If not, it will label you as "Unknown".
Press q to quit.

made by SIDDARTH SREENIVAS

THIS IS THE RESULT WHICH I GOT
<img width="1280" alt="Screenshot 2025-06-21 at 12 14 31 PM" src="https://github.com/user-attachments/assets/ff2af694-9cd4-45a1-a4a2-f53edf77b3ea" />
