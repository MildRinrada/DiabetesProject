# Import libraries
from model import DataModel
import pandas as pd
from sklearn.linear_model import LogisticRegression

def calculate_result(pregnancies, glucose, skin_thickness, BMI, age):
    # อ่านข้อมูลจากไฟล์ csv
    df = pd.read_csv('diabetes_training_data.csv')

    # กำหนดตัวแปร target และ features
    target = 'Outcome'
    features = list(df.columns)
    features.remove(target)

    # สร้างโมเดล logistic regression
    model = LogisticRegression()

    # ฝึกโมเดลด้วยข้อมูลทั้งหมด
    X = df[features]
    y = df[target]
    model.fit(X, y)

    # ตอนรับค่า แปลงตัวเลขก่อน ป้องกัน error
    sample = [int(pregnancies), float(glucose), float(skin_thickness), float(BMI), int(age)]
    sample = pd.DataFrame([sample], columns=['Pregnancies', 'Glucose', 'SkinThickness', 'BMI', 'Age'])
    sample = sample.astype({'Pregnancies': 'int', 'Glucose': 'float', 'SkinThickness': 'float', 'BMI': 'float', 'Age': 'int'})
    
    # ทำนายแล้วรับคำตอบเป็นความน่าจะเป็น
    probabilities = model.predict_proba(sample)[0]
    # ใช้ฟังก์ชัน predict_proba เพื่อคำนวณค่าเปอร์เซ็นต์
    percentage = probabilities[1] * 100
    # ได้ output เป็น เปอร์เซ็น เช่น 10%
    result = f"{percentage:.2f}%"
    
     # ตรวจสอบเงื่อนไขและกำหนดข้อความที่จะแสดงผล
    if percentage >= 75:
        message = "มีโอกาสเป็นเบาหวานสูง"
    elif percentage >= 50:
        message = "มีโอกาสเป็นเบาหวานปานกลาง"
    elif percentage >= 25:
        message = "มีโอกาสเป็นเบาหวานต่ำ"
    else:
        message = "มีโอกาสเป็นเบาหวานต่ำมาก"
    

    # สร้าง instance ของ DataModel และเรียกใช้เมทอด insert()
    data = DataModel(None, int(pregnancies), float(glucose), float(skin_thickness), float(BMI), int(age), result)
    last_insert_id = data.insert(result)
    return result, last_insert_id, message
