# 🏡 Đồ án: Dự đoán Giá Nhà (House Price Prediction)
*Thực hiện bởi Nhóm 09* 👋

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)]()

Chào mừng mọi người đến với kho mã nguồn của Nhóm 09! Trong dự án này, tụi mình áp dụng các kỹ thuật Machine Learning để xây dựng mô hình dự đoán giá nhà dựa trên bộ dữ liệu từ Kaggle. Thay vì chỉ chạy file code khô khan, nhóm còn thiết kế thêm một giao diện web trực quan để ai cũng có thể nhập số liệu và xem thử giá nhà.

## 👥 Thành viên nhóm 09
*   **Đào Hải Yến** - Trưởng nhóm *(Setup GitHub, Deploy giao diện Streamlit & Tổng hợp báo cáo)*
*   **Lê Bảo Trâm** - Thành viên *(Xử lý code Machine Learning, Huấn luyện mô hình & Vẽ biểu đồ)*
*   **Lê Bảo Ngọc** - Thành viên *(Nghiên cứu dữ liệu, Tiền xử lý Data & Viết cơ sở lý thuyết)*

## 🛠️ Công cụ & Thư viện sử dụng
*   **Xử lý dữ liệu:** `pandas`, `numpy`
*   **Trực quan hoá:** `matplotlib`, `seaborn`
*   **Huấn luyện AI:** `scikit-learn` (Dùng thuật toán Hồi quy tuyến tính & Rừng ngẫu nhiên)
*   **Xây dựng UI Web:** `streamlit`

## 📂 Sơ đồ cấu trúc dự án
```text
Nhom09-DT24-HousePrice/
│
├── data/                     # Thư mục chứa data gốc (train.csv, zone_info.json)
├── Nhom09_DT24.ipynb         # Code chính (Tiền xử lý, train & đánh giá mô hình)
├── app.py                    # File giao diện web dự đoán giá nhà
├── requirements.txt          # Danh sách các thư viện môi trường cần cài đặt
└── README.md                 # Tài liệu giới thiệu dự án bạn đang đọc
