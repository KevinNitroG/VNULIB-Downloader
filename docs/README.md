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
[![wakatime of KevinNitroG](https://wakatime.com/badge/user/018b410d-fa7b-44ba-a5de-f025fcbeb499/project/018d747b-a2e0-42a1-8363-a1cc4bcbbb6c.svg?style=for-the-badge)](https://wakatime.com/badge/user/018b410d-fa7b-44ba-a5de-f025fcbeb499/project/018d747b-a2e0-42a1-8363-a1cc4bcbbb6c)

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
    - [1️⃣ Tải tool](#1️⃣-tải-tool)
    - [3️⃣ Sử dụng](#3️⃣-sử-dụng)
  - [⚙️ NÂNG CAO](#️-nâng-cao)
    - [🗃️ Pre-config](#️-pre-config)
    - [⛏️ Pass by arguments](#️-pass-by-arguments)
    - [🤐 Python](#-python)
    - [🤔 More notes](#-more-notes)
  - [📝 LICENSE](#-license)
  - [🤥 DISCLAIMER](#-disclaimer)
  - [😌 CREDIT](#-credit)
  - [⭐ STARGAZER](#-stargazer)

---

## 🎆 CHỨC NĂNG

- Tải sách _(có thể đọc preview online)_ trên [VNULIB](https://vnulib.edu.vn/) _(HCM)_
- Hỗ trợ link: `Sách`, `Preview sách`, `Link trang sách`
- Tải một lúc nhiều sách
- Sử dụng multi thread để tải sách
- Merge ảnh của các trang sách đã tải thành file PDF

---

## 🥂 DEMO

- Hong be oi

---

## 🪴 HƯỚNG DẪN SỬ DỤNG

### 1️⃣ Tải tool

- [![Windows](https://img.shields.io/badge/Windows-a0c4ff?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-windows.exe)
- [![Mac OS](https://img.shields.io/badge/MAC_OS-bdb2ff?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-macos)
- [![Linux](https://img.shields.io/badge/Linux-ffadad?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-ubuntu)

### 3️⃣ Sử dụng

1. Mở tool
2. Input

| **VARIABLE** | **VALUE**                 | **DEFAULT** | **DESCRIPTION**                                                        | **EXAMPLE**     |
| ------------ | ------------------------- | ----------- | ---------------------------------------------------------------------- | --------------- |
| `USERNAME`   | `string`                  |             | Username tài khoản                                                     | `1500023520000` |
| `PASSWORD`   | `string`                  |             | Password tài khoản                                                     | `examplePass`   |
| `LINKS`      | `string string ...`       |             | Link ảnh trang sách _(Có thể nhiều sách, cách nhau bằng khoảng cách)_  | `link_1 link_2` |
| `BROWSER`    | `chrome`, `path/to/local` | `chrome`    | Trình duyệt để sử dụng Selenium khi có cần xử lý Book, Preview website | `chrome`        |
| `HEADLESS`   | `Yes`, `Y`, `y`, `1`, ... | `Y`         | Khi sử dụng Selenium, chạy trình duyệt ẩn                              | `y`             |
| `CREATE_PDF` | `Yes`, `Y`, `y`, `1`, ... | `Y`         | Tạo file PDF từ các ảnh đã tải về                                      | `y`             |
| `CLEAN_IMGS` | `Yes`, `Y`, `y`, `1`, ... | `Y`         | Xoá ảnh sau khi đã tạo PDF                                             | `y`             |

3. Ảnh và sách sẽ được tải về thư mục `./VNULIB-Downloader/Downloads/`

> [!NOTE]
>
> Khi có hơn 1 link là `book`, `preview`: Tool sẽ sử dụng Selenium để xử lý, cần phải dùng tài khoản thư viện để login
>
> Khi toàn bộ link là `page`: Tool không cần dùng Selenium, nhập bừa tài khoản 😏

---

## ⚙️ NÂNG CAO

> [!NOTE]
>
> Thứ tự ưu tiên giá trị biến: `arguments` > `config.yml` > `user input`

### 🗃️ Pre-config

1. Tạo file `config.yml` trong directory `VNULIB-Downloader` bằng 1 trong 2 cách:
   - Chạy trước tool 1 lần sẽ tự tạo file `config.yml`
   - Copy nội dung của file [`config-sample.yml`](../config-sample.yml) và paste vào file `config.yml`
2. Chỉnh các giá trị biến trong file `config.yml`

### ⛏️ Pass by arguments

- Windows:

  ```.ps1
  .\VNULIB-Downloader-windows.exe --help
  ```

- Mac OS:

  ```sh
  ./VNULIB-Downloader-macos --help
  ```

- Linux:

  ```sh
  ./VNULIB-Downloader-ubuntu --help
  ```

> [!NOTE]
>
> Ví dụ _(Windows)_:
>
> `.\VNULIB-Downloader-windows.exe --link "link1" "link2" --username 1500023520000 --password examplePass --browser chrome --headless --create-pdf --clean-imgs`

### 🤐 Python

1. Create virtual environment _(optional)_

2. Install requirements

```sh
pip install -r requirements.txt
```

3. Run tool

```sh
python main.py
```

> [!NOTE]
>
> Linux / Mac hãy thử pip/pip3 và python/python3 trong lệnh

### 🤔 More notes

- Lấy link trang sách:
  - Vào preview sách
  - Lấy link ảnh trang sác của một trang bất kì
    > Có thể F12 để lấy link ảnh trang sách nếu chuột phải không có option `Copy image address`, ...
    > ![Lấy link ảnh trang sách bằng F12](../asset/video/huong_dan_get_link_anh_trang_sach.mp4)

---

## 📝 LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-9bf6ff?style=for-the-badge)](./LICENSE)

---

## 🤥 DISCLAIMER

Dự án này không liên quan đến [VNULIB](https://vnulib.edu.vn/) hay bất kì tổ chức nào khác. Dự án chỉ mang tính học tập _(thực hành, làm việc nhóm, sử dụng ngôn ngữ lập trình, tổ chức một dự án, sử dụng Git, Github, CI/CD)_, không có mục đích thương mại. Chúng tôi không chịu trách nhiệm cho bất kì kết quả và hậu quả nào của việc sử dụng tool.

---

## 😌 CREDIT

- Inspired by [vnulib_downloader](https://github.com/tlatonf/vnulib_downloader/)

---

## ⭐ STARGAZER

<a href="https://star-history.com/#KevinNitroG/VNULIB-Downloader&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=KevinNitroG/VNULIB-Downloader&type=Timeline" />
  </picture>
</a>
