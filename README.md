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

## Bước 3: Chạy hệ thống khoá/mở khoá cửa sử dụng FaceID:

Chạy lệnh sau:

```
python setup_system.py
```

Trên cửa sổ GPIO giả lập, nhấn nút `GPIO22` để chạy chương trình khoá/mở khoá cửa, nếu muốn thêm khuôn mặt cần nhấn phím `Esc` để thoát chương trình và chuyển đến [Bước 4](#Bước-4-Chụp-ảnh-khuôn-mặt-để-lưu-trữ-dữ-liệu-cho-việc-huấn-luyện-mô-hình)

## Bước 4: Chụp ảnh khuôn mặt để lưu trữ dữ liệu cho việc huấn luyện mô hình

-   Trên cửa sổ GPIO giả lập hiện lên, nhấn nút `GPIO17`
-   Cửa sổ nhập tên hiện lên, nhập tên người cần thêm và nhấn phím `Enter` trên bàn phím hoặc nút `OK` trên cửa sổ
-   Cửa sổ chụp ảnh khuôn mặt hiện lên, nhấn chuột vào cửa sổ này và ấn phím `Space` để chụp
-   Ấn phím `Esc` để thoát quá trình chụp, dữ liệu sẽ tự động được lưu.
-   Việc huấn luyện sẽ được thực hiện ngay sau khi ấn phím `Esc`, cửa sổ hiển thị tiến trình huấn luyện sẽ được hiện ra và sẽ tự đóng khi huấn luyện xong

# Ghi chú:

-   Nếu đã có thư mục pj_env được tạo trước đó, mỗi lần vào lại dự án chỉ cần chạy lệnh ở [Bước 1.2](#Bước-12-Truy-cập-môi-trường-ảo)
-   Chương trình chạy trên môi trường giả lập vì không có thiết bị cần thiết như Raspberry Pi, động cơ bước,... nên vẫn mang tính viết chương trình phần mềm hơn là viết chương trình cho hệ thống nhúng để tương tác thật hơn
