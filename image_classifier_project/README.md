# Deep Learning Image Classification – Hidden Message Decoder

This project required me to develop a deep learning image classifier capable of distinguishing between extremely similar 64x64 grayscale images across 26 classes (A–Z, encoded as labels 0–25). The broader goal was to demonstrate how neural networks can detect patterns imperceptible to the human eye and to apply this trained model to decode a hidden message from a sequence of classified images.

---

## 📁 Project Structure

- `train/` – Contains labeled training images and a `labels.csv` file mapping each image to its class (0–25).
- `test/` – Contains test images without labels; used for performance evaluation via F1 score.
- `message/` – Contains 21 images that, once classified in the correct order, reveal a hidden message.

---

## 🧠 Task Summary

### 🔹 Part 1: Image Classification (90 marks)
- Trained a deep learning model to classify the training set into one of 26 image categories.
- Built and validated a convolutional neural network (CNN) using PyTorch.
- Evaluated model performance on the test set via macro F1 score.
- Ensured that predictions on the test set came from a saved and reloadable model checkpoint.

### 🔹 Part 2: Decoding a Message (10 marks)
- Used the trained model to predict classes of the 21 images in the `message/` folder.
- Translated predicted labels (0–25) into corresponding letters (A–Z).
- Decoded the hidden message based on the ordered image predictions.

---

## 🛠️ Technologies Used

- **Python** and **PyTorch**
- **NumPy**, **Pandas**, **Matplotlib** for data handling and visualization
- **torchvision** for image preprocessing
- Jupyter Notebooks for experimentation and reproducibility


