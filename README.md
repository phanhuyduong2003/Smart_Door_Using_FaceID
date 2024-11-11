# Thiết kế khóa cửa thông minh FaceID (Môi trường giả lập)

## Bước 1: Cài đặt và truy cập vào môi trường ảo

### Bước 1.1: Cài đặt môi trường ảo

Chạy lệnh sau:

```
source python -m venv pj_env
```

Cấu trúc thư mục của môi trường ảo như sau:

```
pj_env/
├─ Include/
├─ Lib/
├─ Scripts/
├─ pyvenv.cfg

```

### Bước 1.2: Truy cập môi trường ảo

Để truy cập môi trường ảo, chạy lệnh sau:

```
source ./pj_env/Scripts/activate
```

## Bước 2: Cài đặt thư viện cần thiết

### Bước 2.1: Kiểm tra phiên bản Python (hỗ trợ từ phiên bản 3.7 - 3.12)

Chạy lệnh sau:

```
python -V
```

### Bước 2.2: Cài đặt thư viện dlib

-   Python phiên bản 3.7 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.22.99-cp37-cp37m-win_amd64.whl
```

-   Python phiên bản 3.8 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.22.99-cp38-cp38-win_amd64.whl
```

-   Python phiên bản 3.9 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.22.99-cp39-cp39-win_amd64.whl
```

-   Python phiên bản 3.10 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.22.99-cp310-cp310-win_amd64.whl
```

-   Python phiên bản 3.11 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.24.1-cp311-cp311-win_amd64.whl
```

-   Python phiên bản 3.12 chạy lệnh sau:

```
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/refs/heads/main/dlib-19.24.99-cp312-cp312-win_amd64.whl
```

### Bước 2.3: Cài đặt thư viện còn lại

Chạy lệnh sau:

```
pip install -r requirements.txt
```

## Bước 3: Chụp ảnh khuôn mặt để lưu trữ dữ liệu cho việc huấn luyện mô hình

Chạy lệnh sau:

```
python face_shot.py
```

Chụp khuôn mặt của người cần lưu trữ vào để huấn luyện mô hình, ấn phím `Esc` để thoát quá trình chụp, dữ liệu sẽ tự động được lưu vào

## Bước 4: Huấn luyện mô hình để nhận diện khuôn mặt

Chạy lệnh sau:

```
python train_model_py
```

## Bước 5: Kiểm thử nhận diện khuôn mặt (Có thể bỏ qua bước này và chuyển đến bước 6)

Chạy lệnh sau:

```
python face_rec.py
```

Cửa sổ nhận diện khuôn mặt sẽ hiện ra, để thoát cửa sổ ấn phím `Esc`

## Bước 6: Chạy hệ thống khoá/mở khoá cửa sử dụng FaceID

Chạy lệnh sau:

```
python setup_system.py
```

# Ghi chú:

-   Nếu đã có thư mục pj_env được tạo trước đó, mỗi lần vào lại dự án chỉ cần chạy lệnh ở [Bước 1.2](#Bước-12-Truy-cập-môi-trường-ảo)
-   Chương trình chạy trên môi trường giả lập vì không có thiết bị cần thiết như Raspberry Pi, động cơ bước,... nên vẫn mang tính viết chương trình phần mềm hơn là viết chương trình cho hệ thống nhúng để tương tác thật hơn
