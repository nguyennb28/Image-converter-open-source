# 🖼️ Modern Image Converter

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Ứng dụng chuyển đổi định dạng ảnh hiện đại với giao diện đồ họa đẹp mắt**

Hỗ trợ WebP, AVIF, JPEG, PNG với chất lượng cao và tốc độ xử lý nhanh

[Tính năng](#-tính-năng) • [Cài đặt](#-cài-đặt) • [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng) • [Build Executable](#-build-executable)

</div>

---

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng](#-tính-năng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
  - [Windows](#windows)
  - [Linux](#linux)
  - [macOS](#macos)
- [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [Build Executable](#-build-executable)
- [Xử lý lỗi thường gặp](#-xử-lý-lỗi-thường-gặp)
- [Đóng góp](#-đóng-góp)
- [License](#-license)

---

## 🎯 Giới thiệu

**Modern Image Converter** là ứng dụng chuyển đổi định dạng ảnh mạnh mẽ và dễ sử dụng, được phát triển bằng Python với giao diện PyQt6. Ứng dụng giúp bạn chuyển đổi hàng loạt ảnh sang các định dạng hiện đại như WebP và AVIF, tiết kiệm dung lượng lưu trữ đến 70% mà vẫn giữ được chất lượng ảnh cao.

### 🌟 Tại sao nên dùng?

- 💾 **Tiết kiệm dung lượng**: WebP nhỏ hơn JPEG ~30%, AVIF nhỏ hơn ~50%
- 🎨 **Giao diện đẹp**: Dark theme hiện đại, dễ nhìn, dễ dùng
- ⚡ **Xử lý nhanh**: Multi-threading, không lag UI
- 🔄 **Batch conversion**: Chuyển đổi nhiều ảnh cùng lúc
- 🖱️ **Drag & Drop**: Kéo thả ảnh trực tiếp vào app
- 🎚️ **Tùy chỉnh quality**: Điều chỉnh chất lượng từ 1-100

---

## ✨ Tính năng

| Tính năng | Mô tả |
|-----------|-------|
| **Multiple Format Support** | WebP, AVIF, JPEG, PNG |
| **Batch Conversion** | Chuyển đổi nhiều ảnh cùng lúc |
| **Drag & Drop** | Kéo thả ảnh trực tiếp vào app |
| **Quality Control** | Slider điều chỉnh quality 1-100 |
| **Custom Output Directory** | Chọn thư mục lưu file output |
| **Progress Tracking** | Progress bar real-time |
| **Multi-threading** | UI không bị block khi convert |
| **Auto RGBA→RGB** | Tự động convert cho JPEG |
| **Cross-platform** | Windows, Linux, macOS |
| **Modern UI** | Dark theme, responsive |

---

## 💻 Yêu cầu hệ thống

### Phần mềm cần thiết:

- **Python**: 3.8 hoặc cao hơn
- **pip**: Package manager của Python
- **OS**: Windows 10+, Ubuntu 20.04+, macOS 10.15+

### Dependencies:

```
PyQt6 >= 6.6.0
Pillow >= 10.0.0
pillow-avif-plugin >= 1.3.1
```

---

## 📥 Cài đặt

### Windows

#### Cách 1: Cài đặt từ source (Khuyên dùng cho developer)

1. **Cài Python**
   - Download Python từ [python.org](https://www.python.org/downloads/)
   - Khi cài, **CHECK ☑️ "Add Python to PATH"**
   - Verify: Mở Command Prompt và chạy
   ```cmd
   python --version
   ```

2. **Clone hoặc Download project**
   ```cmd
   git clone https://github.com/nguyennb28/Image-converter-open-source.git
   cd image-converter
   ```

   Hoặc download ZIP từ GitHub và giải nén

3. **Tạo Virtual Environment (Optional nhưng khuyên dùng)**
   ```cmd
   python -m venv venv
   venv\Scriptsctivate
   ```

4. **Cài đặt dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Chạy ứng dụng**
   ```cmd
   python image_converter.py
   ```

#### Cách 2: Dùng file .exe (Đơn giản nhất cho end-user)

1. Download file `Image Converter.exe` từ [Releases](https://github.com/nguyennb28/image-converter/releases)
2. Double-click file `.exe` để chạy
3. **Không cần cài Python!**

---

### Linux

#### Ubuntu/Debian

1. **Cài Python và pip**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Verify Python**
   ```bash
   python3 --version
   pip3 --version
   ```

3. **Clone project**
   ```bash
   git clone https://github.com/nguyennb28/Image-converter-open-source.git
   cd image-converter
   ```

4. **Tạo Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Cài dependencies**
   ```bash
   pip install -r requirements.txt
   ```

6. **Chạy ứng dụng**
   ```bash
   python3 image_converter.py
   ```

#### Fedora/RHEL/CentOS

```bash
# Cài Python
sudo dnf install python3 python3-pip

# Follow các bước 3-6 giống Ubuntu
```

#### Arch Linux

```bash
# Cài Python
sudo pacman -S python python-pip

# Follow các bước 3-6 giống Ubuntu
```

---

### macOS

#### Cách 1: Từ source

1. **Cài Homebrew (nếu chưa có)**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Cài Python**
   ```bash
   brew install python@3.11
   ```

3. **Verify Python**
   ```bash
   python3 --version
   ```

4. **Clone project**
   ```bash
   git clone https://github.com/nguyennb28/image-converter.git
   cd image-converter
   ```

5. **Tạo Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

6. **Cài dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Chạy ứng dụng**
   ```bash
   python3 image_converter.py
   ```

#### Cách 2: Dùng file .app

1. Download `Image Converter.app` từ [Releases](https://github.com/nguyennb28/image-converter/releases)
2. Kéo vào thư mục Applications
3. Right-click → Open (lần đầu tiên để bypass Gatekeeper)

---

## 🚀 Hướng dẫn sử dụng

### Giao diện chính

```
┌─────────────────────────────────────┐
│  🖼️ Modern Image Converter          │
├─────────────────────────────────────┤
│  📁 Select Images                   │
│  ┌─────────────┬─────────────────┐  │
│  │ Select Files│  Clear All      │  │
│  └─────────────┴─────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │ • image1.jpg                  │  │
│  │ • image2.png                  │  │
│  │ • image3.bmp                  │  │
│  └───────────────────────────────┘  │
│  💡 Drag & drop images here         │
├─────────────────────────────────────┤
│  ⚙️ Conversion Settings             │
│  Output Format: [WebP ▼]            │
│  Quality: 85  ░░░░█░░░░░░░          │
├─────────────────────────────────────┤
│  📂 Output Directory                │
│  Same as source  [Change Output]    │
├─────────────────────────────────────┤
│  ▓▓▓▓▓▓▓▓░░░░░░ 50%                │
├─────────────────────────────────────┤
│      🚀 Convert Images              │
├─────────────────────────────────────┤
│  Ready to convert                   │
└─────────────────────────────────────┘
```

### Các bước sử dụng

#### 1️⃣ Chọn ảnh để convert

**Cách 1: Button "Select Files"**
- Click button "Select Files"
- Chọn 1 hoặc nhiều ảnh
- Hỗ trợ: PNG, JPG, JPEG, BMP, GIF, TIFF, WebP, AVIF

**Cách 2: Drag & Drop**
- Kéo ảnh từ File Explorer/Finder
- Thả vào cửa sổ app
- Ảnh sẽ được thêm vào list tự động

#### 2️⃣ Chọn định dạng output

Click dropdown "Output Format" và chọn:
- **WebP**: Recommended cho web, balance tốt giữa size và quality
- **AVIF**: File nhỏ nhất, chất lượng tốt nhất, decode chậm hơn
- **JPEG**: Universal format, tương thích rộng
- **PNG**: Lossless, cho ảnh cần transparency

#### 3️⃣ Điều chỉnh Quality (Optional)

- Di chuyển slider để chọn quality: 1-100
- **Recommended**:
  - WebP/AVIF: 85-90
  - JPEG: 85-92
  - PNG: Không ảnh hưởng (lossless)

#### 4️⃣ Chọn thư mục output (Optional)

- Mặc định: Lưu cùng folder với ảnh gốc
- Click "Change Output Dir" để chọn folder khác

#### 5️⃣ Convert

- Click button "🚀 Convert Images"
- Đợi progress bar chạy
- Thông báo "Successfully converted X/Y images"

#### 6️⃣ Xem kết quả

- File output được lưu trong folder đã chọn
- Tên file: `tên_gốc.webp` / `.avif` / `.jpg` / `.png`

---

## 🔨 Build Executable

### Cài PyInstaller

```bash
pip install pyinstaller
```

### Build cho từng platform

#### Windows

```cmd
pyinstaller --onefile --windowed --name "Image Converter" --icon=icon.ico image_converter.py
```

Hoặc chạy script có sẵn:
```cmd
build_windows.bat
```

**Output**: `dist/Image Converter.exe`

#### Linux

```bash
pyinstaller --onefile --windowed --name "ImageConverter" image_converter.py
```

Hoặc chạy script có sẵn:
```bash
chmod +x build_linux.sh
./build_linux.sh
```

**Output**: `dist/ImageConverter`

#### macOS

```bash
pyinstaller --onefile --windowed --name "Image Converter" --icon=icon.icns image_converter.py
```

Hoặc chạy script có sẵn:
```bash
chmod +x build_macos.sh
./build_macos.sh
```

**Output**: `dist/Image Converter.app`

### Build options nâng cao

```bash
# Thêm hidden imports nếu gặp lỗi
pyinstaller --onefile --windowed --hidden-import=pillow_avif image_converter.py

# UPX compression để giảm size
pyinstaller --onefile --windowed --upx-dir=./upx image_converter.py

# Debug mode
pyinstaller --onefile --windowed --debug=all image_converter.py
```

---

## 🐛 Xử lý lỗi thường gặp

### Windows

#### Lỗi: "python is not recognized as an internal or external command"

**Nguyên nhân**: Python chưa được add vào PATH

**Giải pháp**:
1. Cài lại Python, nhớ check ☑️ "Add Python to PATH"
2. Hoặc add manually:
   - Windows + R → `sysdm.cpl` → Advanced → Environment Variables
   - Thêm `C:\Python311` và `C:\Python311\Scripts` vào PATH

#### Lỗi: "No module named 'PyQt6'"

**Giải pháp**:
```cmd
pip install PyQt6
```

#### Lỗi: File .exe bị Windows Defender block

**Giải pháp**:
- Click "More info" → "Run anyway"
- Hoặc add exception trong Windows Security

---

### Linux

#### Lỗi: "ModuleNotFoundError: No module named 'PyQt6'"

**Giải pháp Ubuntu/Debian**:
```bash
sudo apt install python3-pyqt6
# hoặc
pip install PyQt6
```

#### Lỗi: "qt.qpa.plugin: Could not load the Qt platform plugin"

**Giải pháp**:
```bash
sudo apt install libxcb-xinerama0 libxcb-cursor0
```

#### Lỗi: Permission denied khi chạy

**Giải pháp**:
```bash
chmod +x image_converter.py
./image_converter.py
```

---

### macOS

#### Lỗi: "image_converter.py can't be opened because it is from an unidentified developer"

**Giải pháp**:
1. Right-click → Open
2. Click "Open" trong dialog
3. Hoặc: System Preferences → Security & Privacy → "Open Anyway"

#### Lỗi: "No module named 'PyQt6'"

**Giải pháp**:
```bash
pip3 install PyQt6
```

#### Lỗi: "zsh: command not found: python"

**Giải pháp**:
```bash
# Dùng python3 thay vì python
python3 image_converter.py

# Hoặc tạo alias
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

---

### Lỗi chung

#### Lỗi: "Failed to execute script" khi chạy .exe

**Giải pháp**:
- Build lại với `--debug=all` để xem lỗi chi tiết
- Check missing modules, thêm `--hidden-import`
- Chạy từ Command Prompt để xem error message

#### Lỗi: "pillow_avif not found"

**Giải pháp**:
```bash
pip install pillow-avif-plugin
```

#### App chạy chậm khi convert

**Giải pháp**:
- Giảm quality xuống 75-80
- Convert ít ảnh hơn trong 1 lần
- Check CPU/RAM usage

---

## 📊 So sánh định dạng

| Format | Size vs JPEG | Quality | Decode Speed | Browser Support | Use Case |
|--------|-------------|---------|--------------|-----------------|----------|
| **WebP** | -30% | Excellent | Fast | 96%+ | Best for web |
| **AVIF** | -50% | Best | Slow | 90%+ | High-quality images |
| **JPEG** | Baseline | Good | Fastest | 100% | Universal |
| **PNG** | +50% | Lossless | Fast | 100% | Transparency needed |

### Recommendations

- **Cho website**: WebP (balance tốt nhất)
- **Cho photography**: AVIF (chất lượng cao nhất)
- **Cho compatibility**: JPEG (mọi thiết bị đều chạy)
- **Cho logos/graphics**: PNG (lossless, transparency)

---

## 📁 Cấu trúc project

```
image-converter/
├── image_converter.py      # Main application file
├── requirements.txt        # Python dependencies
├── build_windows.bat       # Windows build script
├── build_linux.sh         # Linux build script
├── build_macos.sh         # macOS build script
├── README.md              # This file
├── LICENSE                # MIT License
└── assets/
    ├── icon.ico           # Windows icon
    ├── icon.icns          # macOS icon
    └── screenshots/       # App screenshots
```

---

## 🤝 Đóng góp

Contributions are welcome! Mọi đóng góp đều được đánh giá cao.

### Cách contribute:

1. **Fork repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open Pull Request**

### Ideas for contribution:

- [ ] Thêm batch resize images
- [ ] Thêm watermark feature
- [ ] Export settings presets
- [ ] Undo/Redo functionality
- [ ] Image preview before conversion
- [ ] Multi-language support (EN, VI, etc.)
- [ ] Dark/Light theme toggle

---

## 📝 Changelog

### Version 1.0.0 (2026-01-26)

- ✨ Initial release
- ✨ Support WebP, AVIF, JPEG, PNG
- ✨ Batch conversion
- ✨ Drag & Drop
- ✨ Quality control slider
- ✨ Dark theme UI
- ✨ Multi-threading
- ✨ Cross-platform support

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 nguyennb28

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

**nguyennb28**
- GitHub: [@nguyennb28](https://github.com/nguyennb28)
- Email: nguyennb.coding@gmail.com

---

## 🙏 Acknowledgments

- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) - GUI framework
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Image processing library
- [PyInstaller](https://www.pyinstaller.org/) - Packaging tool
- [pillow-avif-plugin](https://github.com/fdintino/pillow-avif-plugin) - AVIF support

---

## 📞 Support

Nếu gặp vấn đề hoặc có câu hỏi:

1. **Check [Issues](https://github.com/nguyennb28/Image-converter-open-source/issues)** - có thể đã có người gặp vấn đề tương tự
2. **Create new Issue** - mô tả chi tiết vấn đề, kèm screenshots nếu có
3. **Email**: nguyennb.coding@gmail.com

---

## ⭐ Star History

Nếu project này hữu ích, đừng quên star ⭐ để support nhé!

[![Star History Chart](https://api.star-history.com/svg?repos=nguyennb28/image-converter&type=Date)](https://star-history.com/#nguyennb28/image-converter&Date)

---

<div align="center">

**Made with ❤️ and ☕ by [nguyennb28]**

[⬆ Back to top](#-modern-image-converter)

</div>
