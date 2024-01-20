# ✨ VNULIB DOWNLOADER ✨

<pre align="center">
██╗   ██╗███╗   ██╗██╗   ██╗██╗     ██╗██████╗ 
██║   ██║████╗  ██║██║   ██║██║     ██║██╔══██╗
██║   ██║██╔██╗ ██║██║   ██║██║     ██║██████╔╝
╚██╗ ██╔╝██║╚██╗██║██║   ██║██║     ██║██╔══██╗
 ╚████╔╝ ██║ ╚████║╚██████╔╝███████╗██║██████╔╝
  ╚═══╝  ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ 

██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

Python CLI tool download sách từ <strong>VNULIB</strong>
</pre>

[![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/KevinNitroG/VNULIB-Downloader?style=for-the-badge&color=CAEDFF)](../../commits/main)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/KevinNitroG/VNULIB-Downloader/release.yml?style=for-the-badge&label=RELEASE)
![GitHub issues](https://img.shields.io/github/issues-raw/KevinNitroG/VNULIB-Downloader?style=for-the-badge&color=ffadad)
![GitHub closed issues](https://img.shields.io/github/issues-closed/KevinNitroG/VNULIB-Downloader?style=for-the-badge&color=%23ffc6ff)
![GitHub repo size](https://img.shields.io/github/repo-size/KevinNitroG/VNULIB-Downloader?style=for-the-badge&color=D8B4F8)
[![GitHub contributors](https://img.shields.io/github/contributors/KevinNitroG/VNULIB-Downloader?style=for-the-badge&color=FBF0B2)](../../graphs/contributors)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/KevinNitroG/VNULIB-Downloader?style=for-the-badge)](https://www.codefactor.io/repository/github/kevinnitrog/VNULIB-Downloader)
[![wakatime](https://wakatime.com/badge/user/018b410d-fa7b-44ba-a5de-f025fcbeb499/project/018d034e-ab72-4111-95fa-bd5dc58c6ae7.svg?style=for-the-badge)](https://wakatime.com/badge/user/018b410d-fa7b-44ba-a5de-f025fcbeb499/project/018d034e-ab72-4111-95fa-bd5dc58c6ae7)

[![DeepSource](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader.svg/?label=code+coverage&show_trend=true&token=CudEDrOLrCKS4df1IaYBoP-G)](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader/)
[![DeepSource](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader.svg/?label=active+issues&show_trend=true&token=CudEDrOLrCKS4df1IaYBoP-G)](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader/)
[![DeepSource](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader.svg/?label=resolved+issues&show_trend=true&token=CudEDrOLrCKS4df1IaYBoP-G)](https://app.deepsource.com/gh/KevinNitroG/VNULIB-Downloader/)

> [!CAUTION]
>
> **WORK IN PROGRESS**

---

- [✨ VNULIB DOWNLOADER ✨](#-vnulib-downloader-)
  - [🎆 CHỨC NĂNG](#-chức-năng)
  - [🥂 DEMO](#-demo)
  - [🪴 HƯỚNG DẪN SỬ DỤNG](#-hướng-dẫn-sử-dụng)
    - [1️⃣ Tải tool _(file thực thi)_](#1️⃣-tải-tool-file-thực-thi)
    - [2️⃣ Lấy link trang sách](#2️⃣-lấy-link-trang-sách)
    - [3️⃣ Mở lên và sử dụng](#3️⃣-mở-lên-và-sử-dụng)
  - [⚙️ NÂNG CAO](#️-nâng-cao)
    - [🗃️ Thiết lập giá trị biến trước](#️-thiết-lập-giá-trị-biến-trước)
    - [⛏️ Pass by arguments](#️-pass-by-arguments)
    - [🤐 Python](#-python)
  - [📝 LICENSE](#-license)
  - [😌 CREDIT](#-credit)
  - [🤥 DISCLAIMER](#-disclaimer)
  - [⭐ STAR GRAPH](#-star-graph)

---

## 🎆 CHỨC NĂNG

- Tải sách free _(có thể đọc preview online)_ trên [vnulib](https://vnulib.edu.vn/) (HCM)
- Tải một lúc nhiều sách
- Merge ảnh của các trang sách đã tải thành file PDF

---

## 🥂 DEMO

- Hong be oi

---

## 🪴 HƯỚNG DẪN SỬ DỤNG

### 1️⃣ Tải tool _(file thực thi)_

- [![Windows](https://img.shields.io/badge/Windows-a0c4ff?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-windows.exe)
- [![Mac OS](https://img.shields.io/badge/MAC_OS-bdb2ff?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-macos)
- [![Ubuntu](https://img.shields.io/badge/Ubuntu-ffadad?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-ubuntu)

### 2️⃣ Lấy link trang sách

- Vào preview sách
- Lấy link ảnh trang sác của một trang bất kì

> [!NOTE]
>
> Có thể F12 để lấy link ảnh trang sách nếu chuột phải không có option `Copy image address`...
>
> ![Lấy link ảnh trang sách bằng F12](../asset/video/huong_dan_get_link_anh_trang_sach.mp4)

### 3️⃣ Mở lên và sử dụng

1. Mở tool
2. Nhập các user input

| **VARIABLE**     | **GIÁ TRỊ**                 | **MẶC ĐỊNH** | **MÔ TẢ**                                                             | **VÍ DỤ**       |
| ---------------- | --------------------------- | ------------ | --------------------------------------------------------------------- | --------------- |
| `LINKS`          | `string string ...`         |              | Link ảnh trang sách _(Có thể nhiều sách, cách nhau bằng khoảng cách)_ | `link_1 link_2` |
| `OVERWRITE_BOOK` | `Yes`, `Y`, `y`, `1`, `...` | `N`          | Xoá các sách cũ đã tải về                                             | `n`             |
| `CREATE_PDF`     | `Yes`, `Y`, `y`, `1`, `...` | `Y`          | Tạo file PDF từ các ảnh đã tải về                                     | `y`             |
| `KEEP_IMGS`      | `Yes`, `Y`, `y`, `1`, `...` | `Y`          | Giữ lại các ảnh đã tải về sau khi tạo file PDF                        | `y`             |
| `LOG`            | `Yes`, `Y`, `y`, `1`, `...` | `N`          | Ghi log sách đã tải vào folder `./logs`                               | `y`             |

3. Ảnh và sách sẽ được tải về thư mục `./downloaded_books`

---

## ⚙️ NÂNG CAO

> [!NOTE]
>
> Thứ tự ưu tiên giá trị biến: `arguments` > `config.yml` > `user input`

### 🗃️ Thiết lập giá trị biến trước

1. Tạo file `config.yml` trong directory chứa file thực thi bằng các cách:
   - Copy nội dung của file [`config.yml.example`](../config-sample.yml) và paste vào file `config.yml`
   - Chạy trước tool 1 lần sẽ tự tạo file `config.yml`
2. Chỉnh các giá trị biến trong file `config.yml`

### ⛏️ Pass by arguments

**Ví dụ**

- Windows:

  ```.ps1
  .\VNULIB-Downloader-windows.exe --help

  .\VNULIB-Downloader-windows.exe "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=119407993845809379459430067212192785232&format=jpg&page=1&subfolder=11/94/07/" "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=12946732106750219640246592834&format=jpg&page=11&subfolder=13/12/06/" --overwrite-book --create-pdf --log
  ```

- Mac OS:

  ```sh
  ./VNULIB-Downloader-macos --help

  ./VNULIB-Downloader-macos "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=119407993845809379459430067212192785232&format=jpg&page=1&subfolder=11/94/07/" "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=12946732106750219640246592834&format=jpg&page=11&subfolder=13/12/06/" --overwrite-book --create-pdf --log
  ```

- Ubuntu:

  ```sh
  ./VNULIB-Downloader-ubuntu --help

  ./VNULIB-Downloader-ubuntu "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=119407993845809379459430067212192785232&format=jpg&page=1&subfolder=11/94/07/" "https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=12946732106750219640246592834&format=jpg&page=11&subfolder=13/12/06/" --overwrite-book --create-pdf --log
  ```

### 🤐 Python

- Cài đặt các thư viện cần thiết

  ```sh
  pip install -r requirements.txt
  ```

- Chắc không cần phải nói thêm đâu ha 🤐

---

## 📝 LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-9bf6ff?style=for-the-badge)](./LICENSE)

---

## 😌 CREDIT

- Inspired by [vnulib_downloader](https://github.com/tlatonf/vnulib_downloader/)

## 🤥 DISCLAIMER

Dự án này không liên quan đến [VNULIB](https://vnulib.edu.vn/) hay bất kì tổ chức nào khác. Dự án chỉ mang tính học tập _(thực hành, làm việc nhóm, sử dụng ngôn ngữ lập trình, tổ chức một dự án, sử dụng Git, Github, CI/CD)_, không có mục đích thương mại. Chúng tôi không chịu trách nhiệm cho bất kì kết quả và hậu quả nào của việc sử dụng tool.

---

## ⭐ STAR GRAPH

<a href="https://star-history.com/#KevinNitroG/VNULIB-Downloader&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline" />
  </picture>
</a>
