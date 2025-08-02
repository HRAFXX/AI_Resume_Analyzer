# 🚀 AI Resume Analyzer

An **AI-powered Resume Analyzer** built with **Flask, Python, and Machine Learning** that:

- Extracts text from PDF resumes (supports **scanned and graphical resumes** with **OCR**).  
- Highlights **key skills** and **keywords**.  
- Generates **personalized AI-based job recommendations**.  
- Provides a **professional PDF report** for download.  

---

## 🌟 Features

- **📄 Resume Parsing** – Extracts text from PDF files using **PyPDF2** and **Tesseract OCR**.  
- **💡 AI Job Recommendations** – Suggests the most relevant job titles using **TF-IDF & Cosine Similarity**.  
- **🖤 Modern UI** – Clean and **black & white professional design** for landing, upload, and dashboard pages.  
- **📊 PDF Report Generation** – Generates a downloadable PDF with matched jobs and scores.  
- **⚡ Lightweight & Fast** – Handles both **text-based** and **image-based** resumes.  

---

## 🖥️ Tech Stack

**Backend:**  
- Python (Flask)  
- Machine Learning (TF-IDF, Scikit-learn)  
- OCR with PyTesseract & PDF2Image  

**Frontend:**  
- HTML5 / CSS3 (Modern Black & White Theme)  
- Bootstrap 5  
- FontAwesome Icons  

**Others:**  
- FPDF for PDF report generation  
- Git & GitHub for version control  

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
# Activate on Windows
.venv\Scripts\activate
# Activate on Mac/Linux
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python app.py
```

Then open **http://127.0.0.1:5000/** in your browser. 🎉

---

## 📁 Project Structure

```
AI_Resume_Analyzer/
│-- app.py
│-- templates/
│   │-- base.html
│   │-- landing.html
│   │-- upload.html
│   └-- dashboard.html
│-- static/
│-- uploads/           # Temporary uploaded resumes (ignored in .git)
│-- generated_pdfs/    # Generated reports (ignored in .git)
│-- temp_images/       # OCR images (ignored in .git)
│-- requirements.txt
│-- README.md
```

---

## 📸 Screenshots

### Landing Page  
> Modern black & white hero page with a **Start Now** CTA.

### Upload Page  
> Drag & Drop or click to upload your PDF resume.

### Dashboard  
> Extracted resume text with **highlighted keywords** and **AI job recommendations**.

---

## 🚀 Future Enhancements

- ✅ Multi-user authentication  
- ✅ Save reports to database (MongoDB / PostgreSQL)  
- ✅ More advanced NLP-based job recommendations using BERT or GPT  
- ✅ Cloud deployment (Heroku / Render / AWS)  

---

## 👨‍💻 Author

**Achraf Gebli**  
- 🎓 AI Engineering Student @ Euromed University of Fes  
- 🔗 [GitHub](https://github.com/HRAFXX) | [LinkedIn](https://linkedin.com/in/achraf-gebli-4aa7b5274)

---

## ⭐ Contribute

Contributions are welcome!  

1. **Fork** this repository  
2. **Create** a new branch (`feature-branch`)  
3. **Commit** your changes  
4. **Push** and **Create a Pull Request**  

If you like this project, **give it a ⭐ on GitHub**!

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use it and improve it.
