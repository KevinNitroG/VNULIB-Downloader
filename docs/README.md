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
[![wakatime of KevinNitroG](https://wakatime.com/badge/github/KevinNitroG/VNULIB-Downloader.svg?style=for-the-badge)](https://wakatime.com/badge/github/KevinNitroG/VNULIB-Downloader)

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
    - [2️⃣ Sử dụng](#2️⃣-sử-dụng)
  - [⚙️ NÂNG CAO](#️-nâng-cao)
    - [🗃️ Pre-config](#️-pre-config)
    - [⛏️ Pass by arguments](#️-pass-by-arguments)
    - [🤐 Python](#-python)
  - [🤔 NOTES](#-notes)
    - [Giải thích thuật ngữ](#giải-thích-thuật-ngữ)
    - [Cách lấy page link](#cách-lấy-page-link)
  - [📝 LICENSE](#-license)
  - [🤥 DISCLAIMER](#-disclaimer)
  - [😌 CREDIT](#-credit)
  - [⭐ STARGAZER](#-stargazer)

---

## 🎆 CHỨC NĂNG

- Tải sách _(có thể đọc preview online)_ trên [VNULIB](https://vnulib.edu.vn/) _(HCM)_
  > Ví dụ: https://ir.vnulib.edu.vn/handle/VNUHCM/8108
- Hỗ trợ link: `book`, `preview`, `page` [<sup>giải thích</sup>](#giải-thích-thuật-ngữ)
- Tải một lúc nhiều sách _(lần lượt từng sách)_
- Sử dụng multi thread _(đa luồng)_ để tải sách [<sup>lưu ý</sup>]()
- Merge ảnh của các trang sách đã tải thành file PDF

---

## 🥂 DEMO

- Hong be oi

---

## 🪴 HƯỚNG DẪN SỬ DỤNG

### 1️⃣ Tải tool

- [![Windows](https://img.shields.io/badge/Windows-a0c4ff?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-windows.exe)
- [![Mac OS](https://img.shields.io/badge/MAC_OS-bdb2ff?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-macos)
- [![Linux](https://img.shields.io/badge/Linux-ffc6ff?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/KevinNitroG/VNULIB-Downloader/releases/download/latest/VNULIB-Downloader-ubuntu)

### 2️⃣ Sử dụng

1. Mở tool
2. Input

| **VARIABLE**                                    | **VALUE**                                   | **DEFAULT** | **DESCRIPTION**                                                              | **EXAMPLE**     |
| ----------------------------------------------- | ------------------------------------------- | ----------- | ---------------------------------------------------------------------------- | --------------- |
| `USERNAME`                                      | `string`                                    |             | Username tài khoản                                                           | `1500023520000` |
| `PASSWORD`                                      | `string`                                    |             | Password tài khoản                                                           | `examplePass`   |
| `LINKS`                                         | `string string ...`                         |             | Link ảnh trang sách<br>_(Có thể nhiều sách, cách nhau bằng khoảng cách)_     | `link_1 link_2` |
| `TIMEOUT`                                       | `int`                                       | `20`        | Timeout _(s)_ khi sử dụng Selenium và request lấy mỗi ảnh từ server          | `20`            |
| `BROWSER`                                       | `chrome`,<br> `path/to/local/chrome_driver` | `chrome`    | Trình duyệt để sử dụng Selenium Webdriver khi có cần xử lý `book`, `preview` | `chrome`        |
| `HEADLESS`[<sup>?</sup>](#giải-thích-thuật-ngữ) | `y`, `n`, ...                               | `y`         | Selenium Webdriver headless mode                                             | `y`             |
| `CREATE_PDF`                                    | `y`, `n`, ...                               | `y`         | Tạo file PDF từ các ảnh đã tải về                                            | `y`             |
| `CLEAN_IMG`                                     | `y`, `n`, ...                               | `y`         | Xoá ảnh sau khi đã tạo PDF                                                   | `y`             |

4. Ảnh và sách sẽ được tải về thư mục `./VNULIB-Downloader/Downloads/`

> [!IMPORTANT]
>
> - Nếu trong tương lai việc sử dụng link `book` hay `preview` không được, hãy thử link `page` _(vì các phần tử trang web
>   có thể thay đổi)_
> - Nếu dùng để tải nhiều sách _(sử dụng multi threading)_ có thể khiến server bị quá tải, dẫn đến download fail

> [!NOTE]
>
> - `preview` link của mỗi tài khoản là khác nhau _(dựa trên query `uid`)_
> - Khi có >= 1 link là `book` / `preview`: Tool sẽ sử dụng Selenium Webdriver để xử lý, cần phải dùng tài khoản thư viện để login
> - Trái lại, khi toàn bộ link là `page`: Tool không cần dùng Selenium Webdriver, nên `USERNAME`, `PASSWORD`, `BROSWER`, `HEADLESS` không còn quan trọng _(nhập bừa / để trống)_
> - `page` link: Trong link có query `&page=`:
>   - `1`: Tool sẽ tự động check và tải trang sách đến khi đạt giới hạn _(không dùng multi threading)_
>   - > `1`: Tool tự nhận đấy là limit của file sách hoặc chủ đích sử dụng tải tới trang đấy, dùng multi threading

---

## ⚙️ NÂNG CAO

- Có thể chạy tool theo các cách:
  - [Pre config](#🗃️-pre-config): Để không phải nhập input mỗi lần chạy
  - [Pass by arguments](#⛏️-pass-by-arguments)
  - [Python](#🤐-python): Clone cả repo về chạy python

> [!NOTE]
>
> Thứ tự ưu tiên giá trị biến: `arguments` > `config.yml` > `user input`

### 🗃️ Pre-config

1. Tạo file `config.yml` trong đường dẫn `./VNULIB-Downloader/` bằng 1 trong 2 cách:
   - Chạy trước tool 1 lần sẽ tự tạo file `config.yml`
   - Copy nội dung của file [`config-sample.yml`](../VNULIB-Downloader/config-sample.yml) và paste vào
     file `config.yml`
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
- Ví dụ _(Windows)_:
  ```.ps1
  .\VNULIB-Downloader-windows.exe --link "link1" "link2" --username "1500023520000" --password "examplePass" --browser "~/chrome_driver.exe" --headless --create-pdf --clean-imgs
  ```

### 🤐 Python

1. Install [Python](https://www.python.org/downloads/)
2. Create virtual environment _(optional)_
3. Install requirements
   ```ps1
   pip install -r requirements.txt
   ```
4. Run tool
   ```ps1
   python main.py
   ```

> [!NOTE]
>
> **Linux** / **Mac** hãy thử `pip3` và `python3` nếu `pip` và `python` không chạy

---

## 🤔 NOTES

### Giải thích thuật ngữ

| **TERM**             | **EXPLANTION**                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `book`               | Link của sách<br>Ex: `https://ir.vnulib.edu.vn/handle/VNUHCM/8108`                                                                                                                                           |
| `preview`            | Preview link của sách<br>Ex: `https://ir.vnulib.edu.vn/flowpaper/simple_document.php?subfolder=11/94/07/&doc=914783209473971&bitsid=c3558fcc-95bb-4a92-a492-46f61eccfadc&uid=237ys-b676-45b0-855b-12iuiwdT5` |
| `page`               | Link ảnh của 1 trang sách<br>Ex: `https://ir.vnulib.edu.vn/flowpaper/services/view.php?doc=914783209473971&format=jpg&page=1&subfolder=11/94/07/_                                                            |
| `Selenium Webdriver` | Hỗ trợ automation bằng trình duyệt                                                                                                                                                                           |
| `headless`           | Khi chạy trình duyệt sẽ không hiện ra thành cửa sổ, chỉ ẩn dưới nền                                                                                                                                          |

### Cách lấy page link

- Vào `preview` sách
- Lấy link ảnh trang sác của một trang bất kì
  > Có thể F12 để lấy link ảnh trang sách nếu chuột phải không có option `Copy image address`, ...
  > ![Lấy link ảnh trang sách bằng F12](../asset/video/huong_dan_get_link_anh_trang_sach.mp4)

---

## 📝 LICENSE

[![License: MIT](https://img.shields.io/badge/License-MIT-9bf6ff?style=for-the-badge)](./LICENSE)

---

## 🤥 DISCLAIMER

Dự án không dưới quyền [VNULIB](https://vnulib.edu.vn/) hay bất kì tổ chức nào khác. Dự án chỉ mang tính học tập
_(thực hành, làm việc nhóm, sử dụng ngôn ngữ lập trình, tổ chức một dự án, sử dụng Git, Github, CI/CD)_, không có mục
đích thương mại, phá hoại _(DDOS,...)_. Chúng tôi không chịu trách nhiệm cho bất kì kết quả và hậu quả nào của việc sử dụng tool.

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
