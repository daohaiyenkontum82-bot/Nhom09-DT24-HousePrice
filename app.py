import streamlit as st
import pandas as pd
import joblib

# 1. Tải mô hình AI thật đã được huấn luyện
try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    st.error("Chưa tìm thấy file model.pkl! Vui lòng tải file mô hình lên.")

# Tiêu đề của ứng dụng web
st.title("🏡 Ứng dụng Dự đoán Giá Nhà - Nhóm 09")
st.markdown("Nhập các thông số cơ bản của ngôi nhà ở thanh công cụ bên trái để hệ thống AI dự đoán giá trị thực tế.")

# 2. Tạo form nhập liệu cho người dùng 
st.sidebar.header("Thông số đầu vào")
    
def user_input_features():
    # LƯU Ý QUAN TRỌNG: Tên các cột ở phần 'data' phải khớp 100% với tên cột lúc Trâm train model!
    area = st.sidebar.number_input('Diện tích (m2)', min_value=30, max_value=1000, value=100)
    bedrooms = st.sidebar.number_input('Số phòng ngủ', min_value=1, max_value=10, value=3)
    bathrooms = st.sidebar.number_input('Số phòng tắm', min_value=1, max_value=10, value=2)
    year_built = st.sidebar.number_input('Năm xây dựng', min_value=1900, max_value=2026, value=2010)
        
    data = {
        'Area': area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'YearBuilt': year_built
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader("Bảng thông số bạn vừa nhập:")
st.write(input_df)

# 3. Nút bấm dự đoán sử dụng mô hình thật
if st.button("Dự đoán Giá Nhà"):
    if 'model' in locals():
        # Gọi AI vào dự đoán
        prediction = model.predict(input_df)
        
        st.success(f"💰 Giá nhà dự đoán ước tính: ${int(prediction[0]):,}")
        st.info("*(Kết quả được dự đoán trực tiếp từ Trí tuệ nhân tạo của Nhóm 09)*")
