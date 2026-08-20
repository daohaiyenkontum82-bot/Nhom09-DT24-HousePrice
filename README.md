<div align="center">
  
  # 🏡 ESTATE ANALYTICS
  ### Hệ thống Ứng dụng AI Dự đoán Giá Bất Động Sản (House Price Prediction)
  
  *Bài tập lớn học phần :  Lập trình Python cho phân tích dữ liệu - Giảng viên hướng dẫn: Thầy Nguyễn Hoàng Hải*

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
  ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) 
  ![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## 📖 Giới thiệu dự án
Chào mừng đến với kho mã nguồn của **Nhóm 09**! 

**Estate Analytics** là dự án ứng dụng các kỹ thuật Học máy (Machine Learning) để giải quyết bài toán định giá bất động sản dựa trên bộ dữ liệu House Prices từ Kaggle. Thay vì chỉ dừng lại ở các dòng code khô khan trên Jupyter Notebook, nhóm đã phát triển hoàn thiện một ứng dụng Web trực quan, giúp người dùng dễ dàng tương tác, nhập thông số và nhận về kết quả định giá ngay lập tức.

## ✨ Tính năng nổi bật & Kỹ thuật áp dụng
- **Phân tích EDA chuyên sâu:** Trực quan hóa dữ liệu với 5 loại biểu đồ đa dạng (Heatmap, Scatter, Boxplot...) và giải quyết 5 câu hỏi phân tích trọng tâm.
- **Huấn luyện mô hình kép:** Áp dụng và so sánh hai thuật toán Linear Regression và Random Forest, đánh giá qua các chỉ số RMSE, MAE, R².
- **Tự động quy đổi thông minh:** Hệ thống tự động đọc cấu hình tỷ giá từ file JSON (có xử lý ngoại lệ Try-Except), quy đổi đơn vị nhập liệu từ Mét vuông (m²) sang Feet vuông (sq ft) để khớp với dữ liệu AI chuẩn Mỹ.
- **Giao diện Glassmorphism:** Thiết kế web hiện đại, tối ưu trải nghiệm người dùng (UX/UI).

---

## 👥 Đội ngũ phát triển (Nhóm 09)

| STT | Thành viên | Vai trò | Chi tiết công việc |
| :---: | :--- | :---: | :--- |
| **1** | **Đào Hải Yến** | Trưởng nhóm | Setup dự án; Lập trình Web Streamlit & Xử lý đọc file JSON quy đổi; Tổng hợp báo cáo. |
| **2** | **Lê Bảo Trâm** | Thành viên | Huấn luyện mô hình (Linear Regression & Random Forest); Đánh giá chỉ số; Định dạng báo cáo. |
| **3** | **Lê Bảo Ngọc** | Thành viên | Làm sạch dữ liệu; Trực quan hóa EDA (5 loại biểu đồ); Dựng video thuyết trình AI. |

---

## 🛠 Công cụ & Thư viện sử dụng

- **Xử lý dữ liệu & Nguồn Data:** `pandas`, `numpy`, `json` (Đọc dữ liệu CSV và JSON)
- **Trực quan hóa dữ liệu:** `matplotlib`, `seaborn`
- **Xây dựng & Huấn luyện Model:** `scikit-learn` (Linear Regression, Random Forest Regressor)
- **Triển khai Web App:** `streamlit`

---

## 🚀 Hướng dẫn cài đặt và chạy ứng dụng

**1. Clone kho lưu trữ này về máy:**
```bash
git clone [https://github.com/daohaiyenkontum82-bot/Nhom09-HousePrice.git](https://github.com/daohaiyenkontum82-bot/Nhom09-HousePrice.git)
