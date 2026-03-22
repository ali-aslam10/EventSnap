# 📸 EventSnap – Face Recognition-Based Event Photo Retrieval

**EventSnap** is a Google Colab-compatible notebook that enables users to automatically detect, enhance, and match faces in event photos deep learning.

It helps event participants quickly retrieve their photos by simply uploading a reference image.

---

## 🚀 Model Variant: EventSnap_L

**EventSnap_L** is the core pipeline used in this project, combining:

- 🔍 **Face Detection & Recognition**: InsightFace (`buffalo_l`)
- 🧖‍♂️ **Face Enhancement**: GFPGAN
- 🧠 **Face Matching**: Cosine similarity on embeddings

---

## 🎯 Project Highlights

- 🔍 High-accuracy **face detection & recognition** using `buffalo_l`
- 🧖‍♂️ Automatic **face enhancement** for low-resolution faces
- 🗃️ **Event-wise embedding storage** using Pickle
- 📥 Fast **participant image matching** via cosine similarity
- ⚡ Optimized pipeline (**EventSnap_L**) for better results
- ✅ Fully executable in **Google Colab**
- 📽️ Includes a full working **demo video**

---

## 🧠 Technologies Used

- **Python 3.11**
- InsightFace (`buffalo_l`)
- GFPGAN (Face Restoration)
- OpenCV, NumPy, Pickle
- Google Colab (for execution)

---

## 🔧 Setup Instructions (Google Colab)

1. **Mount Google Drive**  
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Install Required Packages**  
   ```bash
   !pip install -U insightface onnxruntime
   !pip install -r requirements.txt
   ```

3. **Fix TorchVision Compatibility (Colab only)**  
   ```bash
   !sed -i "s/from torchvision.transforms.functional_tensor import rgb_to_grayscale/from torchvision.transforms.functional import rgb_to_grayscale/" /usr/local/lib/python3.11/dist-packages/basicsr/data/degradations.py
   ```

4. **Change to GFPGAN directory**  
   ```python
   %cd "/content/drive/MyDrive/model"
   ```

---

## ✅ How It Works

### 👤 Organizer Side

- Upload group event photos
- Faces are detected using InsightFace
- Faces below a resolution threshold are enhanced using GFPGAN
- Embeddings for each detected face are computed and saved

### 🧍 Participant Side

- Upload a reference image
- Face is detected and its embedding is computed
- Matching is performed against stored event embeddings
- Matching images are retrieved and displayed

---


## 🎥 Demo Video

Watch the full system in action:  
📺 [Demo Video Link](https://drive.google.com/file/d/1QKeqIkf4YfGsZ3QoGThzJO4vZOxitvPt/view?usp=drive_link)

---

## 📌 Notes

- GFPGAN is only used if the detected face resolution is below the defined threshold (default: 128 pixels).
- The system works best when faces are clear and forward-facing.
- Embeddings are stored per event using Pickle files and can be reused for faster matching.

---
