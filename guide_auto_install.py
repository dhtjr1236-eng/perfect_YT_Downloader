import sys
import subprocess
import threading
from tkinter import Tk, Label, Button, messagebox, Frame
import tkinter as tk

# ============================================
# CustomTkinter 자동 설치 체크
# ============================================

def check_and_install_customtkinter():
    """CustomTkinter 설치 여부 확인 및 필요시 자동 설치"""
    try:
        import customtkinter
        return True
    except ImportError:
        # CustomTkinter가 설치되지 않았으므로 기본 tkinter로 안내창 띄우기
        root = Tk()
        root.title("⚠️ CustomTkinter 설치 필요")
        root.geometry("600x300")
        root.resizable(False, False)
        
        # 중앙에 띄우기
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f"{width}x{height}+{x}+{y}")
        
        frame = Frame(root, bg="#2A2A3E")
        frame.pack(fill="both", expand=True)
        
        Label(
            frame,
            text="🛠 필수 라이브러리 설치",
            font=("Arial", 16, "bold"),
            fg="#00D4FF",
            bg="#2A2A3E"
        ).pack(pady=20)
        
        Label(
            frame,
            text="이 프로그램을 실행하기 위해서는\nCustomTkinter 라이브러리가 필요합니다.\n\n아래 버튼을 클릭하면 자동으로 설치됩니다.",
            font=("Arial", 11),
            fg="#FFFFFF",
            bg="#2A2A3E",
            justify="center"
        ).pack(pady=20)
        
        def install():
            try:
                root.destroy()
                print("[*] CustomTkinter 설치 중...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "customtkinter", "pillow"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                messagebox.showinfo(
                    "설치 완료",
                    "✅ CustomTkinter가 성공적으로 설치되었습니다!\n\n"
                    "프로그램을 다시 실행해주세요."
                )
                sys.exit(0)
            except Exception as e:
                messagebox.showerror(
                    "설치 실패",
                    f"❌ 설치 중 오류가 발생했습니다:\n\n{str(e)}\n\n"
                    f"수동으로 다음 명령어를 실행해주세요:\n"
                    f"pip install customtkinter pillow"
                )
                sys.exit(1)
        
        Button(
            frame,
            text="📥 지금 설치하기",
            command=install,
            font=("Arial", 12, "bold"),
            bg="#00D966",
            fg="white",
            padx=20,
            pady=10,
            relief="flat",
            cursor="hand2"
        ).pack(pady=15)
        
        Label(
            frame,
            text="(이 창은 설치 후 자동으로 닫힙니다)",
            font=("Arial", 9),
            fg="#808080",
            bg="#2A2A3E"
        ).pack(pady=(20, 0))
        
        root.mainloop()
        return False

# CustomTkinter 설치 확인
if not check_and_install_customtkinter():
    sys.exit(1)

# ============================================
# CustomTkinter를 이용한 메인 가이드
# ============================================

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkTextbox
from tkinter import messagebox
import subprocess, shutil, os

# ✨ CustomTkinter 설정
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ModuleAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("🛠 YouTube Downloader 설치 가이드")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        self.results = {}
        
        # 메인 프레임
        self.main_frame = CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        self.show_intro()

    def clear_frame(self):
        """프레임 초기화"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_intro(self):
        """인트로 화면"""
        self.clear_frame()
        
        # 헤더
        header_frame = CTkFrame(self.main_frame, fg_color="#1F1F2E", corner_radius=15)
        header_frame.pack(fill="x", padx=20, pady=(20, 0))
        
        CTkLabel(
            header_frame,
            text="🛠 YouTube Downloader 설치 가이드",
            font=("Segoe UI", 26, "bold"),
            text_color="#00D4FF"
        ).pack(pady=20)
        
        # 설명
        content_frame = CTkFrame(self.main_frame, fg_color="#2A2A3E", corner_radius=12)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        CTkLabel(
            content_frame,
            text="필수 환경 확인",
            font=("Segoe UI", 14, "bold"),
            text_color="#FFFFFF"
        ).pack(pady=(20, 10))
        
        CTkLabel(
            content_frame,
            text="이 프로그램을 실행하기 위해 필요한\n의존성 라이브러리와 프로그램을 점검합니다.",
            font=("Segoe UI", 12),
            text_color="#A0A0A0",
            justify="center"
        ).pack(pady=(0, 30))
        
        CTkLabel(
            content_frame,
            text="✅ CustomTkinter (UI 라이브러리)\n✓ Python 버전 확인\n✓ pip 패키지 관리자 확인\n✓ YouTube 다운로드 라이브러리 (yt-dlp)\n✓ 영상/음성 처리 도구 (ffmpeg)",
            font=("Segoe UI", 11),
            text_color="#FFFFFF",
            justify="left"
        ).pack(pady=(0, 30), anchor="w", padx=30)
        
        # 시작 버튼
        CTkButton(
            content_frame,
            text="🚀 환경 점검 시작",
            command=self.show_check,
            font=("Segoe UI", 13, "bold"),
            height=45,
            fg_color="#00D966",
            text_color="#FFFFFF",
            hover_color="#00A84D",
            corner_radius=8
        ).pack(pady=20)

    def show_check(self):
        """환경 점검 화면"""
        self.clear_frame()
        
        # 헤더
        header_frame = CTkFrame(self.main_frame, fg_color="#1F1F2E", corner_radius=15)
        header_frame.pack(fill="x", padx=20, pady=(20, 0))
        
        CTkLabel(
            header_frame,
            text="📋 환경 점검 중...",
            font=("Segoe UI", 24, "bold"),
            text_color="#00D4FF"
        ).pack(pady=20)
        
        # 체크 항목 프레임
        check_frame = CTkFrame(self.main_frame, fg_color="#2A2A3E", corner_radius=12)
        check_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # CustomTkinter 확인 (설치됨 확정)
        self.add_item(
            check_frame,
            "✨ CustomTkinter",
            True,
            "UI 라이브러리 설치됨",
            button_text="✓ 설치됨"
        )
        
        # Python 확인
        py_ok = sys.version_info >= (3, 8)
        py_version = f"Python {sys.version.split()[0]}"
        self.add_item(
            check_frame,
            "🐍 Python",
            py_ok,
            py_version,
            "3.8 이상 권장"
        )
        
        # pip 확인
        try:
            subprocess.check_output([sys.executable, "-m", "pip", "--version"], text=True)
            pip_ok = True
            pip_desc = "pip 정상 동작"
        except Exception as e:
            pip_ok = False
            pip_desc = f"pip 오류"
        
        self.add_item(check_frame, "📦 pip", pip_ok, pip_desc)
        
        # yt-dlp 확인
        try:
            __import__("yt_dlp")
            self.add_item(
                check_frame,
                "🎬 yt-dlp",
                True,
                "YouTube 다운로드 모듈 설치됨",
                button_text="✓ 설치됨"
            )
        except ImportError:
            def install_yt_dlp():
                self.install_module("yt-dlp")
            
            self.add_item(
                check_frame,
                "🎬 yt-dlp",
                False,
                "YouTube 다운로드 모듈 미설치",
                button_text="📥 설치",
                button_command=install_yt_dlp
            )
        
        # ffmpeg 확인
        if shutil.which("ffmpeg"):
            self.add_item(
                check_frame,
                "⚙️ ffmpeg",
                True,
                "ffmpeg 설치됨",
                button_text="✓ 설치됨"
            )
        else:
            def show_ffmpeg():
                self.show_ffmpeg_help()
            
            self.add_item(
                check_frame,
                "⚙️ ffmpeg",
                False,
                "ffmpeg 미설치",
                button_text="📖 가이드",
                button_command=show_ffmpeg
            )
        
        # 하단 버튼
        button_frame = CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        CTkButton(
            button_frame,
            text="🔄 다시 확인",
            command=self.show_check,
            font=("Segoe UI", 11, "bold"),
            height=40,
            fg_color="#00D4FF",
            text_color="#000000",
            hover_color="#00A8CC",
            width=150
        ).pack(side="left", padx=(0, 10))
        
        CTkButton(
            button_frame,
            text="⬅ 뒤로",
            command=self.show_intro,
            font=("Segoe UI", 11, "bold"),
            height=40,
            fg_color="#555555",
            text_color="#FFFFFF",
            hover_color="#666666"
        ).pack(side="left")

    def add_item(self, parent, name, ok, desc, sub_desc=None, button_text=None, button_command=None):
        """환경 확인 항목 추가"""
        item_frame = CTkFrame(
            parent,
            fg_color="#3A3A52" if ok else "#4A3A3A",
            corner_radius=8,
            border_width=2,
            border_color="#00D966" if ok else "#FF4444"
        )
        item_frame.pack(fill="x", pady=10, padx=15)
        
        # 좌측: 이름 및 설명
        left_frame = CTkFrame(item_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True, padx=15, pady=12)
        
        CTkLabel(
            left_frame,
            text=name,
            font=("Segoe UI", 12, "bold"),
            text_color="#00D966" if ok else "#FF6B6B"
        ).pack(anchor="w")
        
        CTkLabel(
            left_frame,
            text=desc,
            font=("Segoe UI", 10),
            text_color="#A0A0A0"
        ).pack(anchor="w", pady=(3, 0))
        
        if sub_desc:
            CTkLabel(
                left_frame,
                text=sub_desc,
                font=("Segoe UI", 9),
                text_color="#808080"
            ).pack(anchor="w", pady=(2, 0))
        
        # 우측: 버튼 또는 상태
        right_frame = CTkFrame(item_frame, fg_color="transparent")
        right_frame.pack(side="right", padx=15, pady=12)
        
        if button_command:
            CTkButton(
                right_frame,
                text=button_text or "작업",
                command=button_command,
                font=("Segoe UI", 10, "bold"),
                height=32,
                fg_color="#00D4FF" if ok else "#FF9800",
                text_color="#000000",
                hover_color="#00A8CC" if ok else "#E67E22",
                width=100
            ).pack()
        else:
            CTkLabel(
                right_frame,
                text=button_text or ("✅ 완료" if ok else "⚠️ 필요"),
                font=("Segoe UI", 11, "bold"),
                text_color="#00D966" if ok else "#FF6B6B"
            ).pack()

    def install_module(self, pip_name):
        """패키지 설치"""
        answer = messagebox.askyesno(
            "설치 확인",
            f"📦 '{pip_name}' 패키지를 설치하시겠습니까?\n\n"
            f"(관리자 권한이 필요할 수 있습니다)"
        )
        if not answer:
            return
        
        def worker():
            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", pip_name],
                    check=True
                )
                messagebox.showinfo(
                    "설치 완료",
                    f"✅ '{pip_name}' 설치가 완료되었습니다!\n\n"
                    f"다시 환경을 확인해주세요."
                )
                self.show_check()
            except Exception as e:
                messagebox.showerror(
                    "설치 실패",
                    f"❌ 오류 발생:\n\n{str(e)}"
                )
        
        threading.Thread(target=worker, daemon=True).start()

    def show_ffmpeg_help(self):
        """ffmpeg 설치 가이드"""
        guide = ctk.CTkToplevel(self.root)
        guide.title("🎬 ffmpeg 설치 가이드")
        guide.geometry("750x700")
        guide.resizable(False, False)
        
        # 헤더
        header = CTkFrame(guide, fg_color="#1F1F2E", corner_radius=12)
        header.pack(fill="x", padx=15, pady=(15, 0))
        
        CTkLabel(
            header,
            text="🎬 ffmpeg 설치 방법",
            font=("Segoe UI", 20, "bold"),
            text_color="#00D4FF"
        ).pack(pady=15)
        
        # 컨텐츠
        content = CTkFrame(guide, fg_color="#2A2A3E", corner_radius=12)
        content.pack(fill="both", expand=True, padx=15, pady=15)
        
        guide_text = """ffmpeg는 동영상/음성 병합을 위해 필수적인 프로그램입니다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📥 1단계: ffmpeg 다운로드
   • 아래 링크를 브라우저에서 열어주세요:
   • https://www.gyan.dev/ffmpeg/builds/
   • 'ffmpeg-release-essentials.zip' 파일을 다운로드합니다

📂 2단계: 폴더 생성 및 압축 해제
   • C:\ffmpeg 폴더를 생성합니다
   • 다운로드한 zip 파일을 C:\ffmpeg에 압축 해제합니다

⚙️ 3단계: 환경 변수 설정
   • Windows 검색창에서 "환경 변수" 검색
   • "시스템 환경 변수 편집" 클릭
   • "환경 변수" 버튼 클릭
   • "Path" 선택 후 "편집" 클릭
   • "새로 만들기"에서 C:\\ffmpeg\\bin 추가

✅ 4단계: 설치 확인
   • 새로운 CMD/PowerShell 창 열기
   • ffmpeg -version 입력
   • 버전 정보가 나오면 성공!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ 설치를 완료했다면 "환경 점검"으로 돌아가서
   "다시 확인" 버튼을 눌러주세요!"""
        
        text_box = CTkTextbox(
            content,
            font=("Consolas", 10),
            fg_color="#1F1F2E",
            text_color="#00D4FF",
            border_color="#00D4FF",
            border_width=1,
            activate_scrollbars=True
        )
        text_box.pack(fill="both", expand=True, padx=15, pady=15)
        text_box.insert("0.0", guide_text)
        text_box.configure(state="disabled")
        
        # 하단 버튼
        button_frame = CTkFrame(guide, fg_color="transparent")
        button_frame.pack(fill="x", padx=15, pady=15)
        
        CTkButton(
            button_frame,
            text="🔗 ffmpeg 다운로드 링크 열기",
            command=lambda: os.system("start https://www.gyan.dev/ffmpeg/builds/"),
            font=("Segoe UI", 11, "bold"),
            height=40,
            fg_color="#00D4FF",
            text_color="#000000",
            hover_color="#00A8CC"
        ).pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        CTkButton(
            button_frame,
            text="✓ 닫기",
            command=guide.destroy,
            font=("Segoe UI", 11, "bold"),
            height=40,
            fg_color="#555555",
            text_color="#FFFFFF",
            hover_color="#666666",
            width=80
        ).pack(side="right")


if __name__ == "__main__":
    root = ctk.CTk()
    app = ModuleAdmin(root)
    root.mainloop()
