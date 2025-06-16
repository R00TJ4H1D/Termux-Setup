import os
import time
import subprocess
from termcolor import colored
from pyfiglet import Figlet

# 🔊 ভয়েস ফাংশন
def speak(text):
    try:
        subprocess.run(["termux-tts-speak", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# 🧼 স্ক্রিন ক্লিয়ার
def clear_screen():
    os.system("clear")

# 🎨 ASCII Banner একবার দেখায়
def show_banner():
    clear_screen()
    figlet = Figlet(font="slant")
    banner = figlet.renderText("T-Setup")
    for line in banner.splitlines():
        print(colored(f"❯❯ {line}", "cyan"))
    print(colored("❯❯ " + "=" * 60, "green"))
    print(colored("❯❯ TERMUX PROFESSIONAL SETUP TOOL".center(60), "yellow"))
    print(colored("❯❯ CREATED BY ROOTJAHID".center(60), "magenta"))
    print(colored("❯❯ " + "=" * 60, "green"))
    print("\n")

# 🔧 প্যাকেজ ইনস্টল ফাংশন
def install_package(pkg):
    speak(f"Installing {pkg}")
    print(colored(f"❯❯ 📦 INSTALLING: {pkg.upper()}", "yellow"))
    os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
    print(colored(f"❯❯ ✅ {pkg.upper()} INSTALLED SUCCESSFULLY", "green"))
    speak(f"{pkg} installed successfully")
    time.sleep(0.5)

# 📦 সমস্ত প্যাকেজ ইনস্টল
def install_all_packages():
    packages = [
        "python", "git", "curl", "wget", "nano", "vim", "zip", "unzip", "tar",
        "clang", "make", "nodejs", "php", "ruby", "bash", "fish", "net-tools",
        "tmux", "figlet", "toilet", "cowsay", "termux-api", "dnsutils", "jq",
        "coreutils", "util-linux", "tsu", "proot", "man", "neofetch", "htop",
        "tree", "grep", "sed", "nmap", "cmatrix", "lolcat", "openssl",
        "libffi", "ndk-sysroot", "termux-exec", "python3-pip"
    ]

    print(colored("❯❯ 🔁 UPDATING PACKAGE LIST", "cyan"))
    speak("Updating package list")
    os.system("pkg update -y")

    print(colored("❯❯ ⬆️ UPGRADING EXISTING PACKAGES", "cyan"))
    speak("Upgrading packages")
    os.system("pkg upgrade -y")

    for pkg in packages:
        install_package(pkg)

    print(colored("\n❯❯ 🎉 ALL PACKAGES INSTALLED SUCCESSFULLY!", "yellow"))
    speak("All packages installed successfully")

# 🐍 পাইথন প্যাকেজ ইনস্টল
def install_python_libraries():
    speak("Installing python libraries")
    print(colored("❯❯ 🐍 INSTALLING PYTHON LIBRARIES", "magenta"))
    os.system("pip install --upgrade pip")
    os.system("pip install requests bs4 colorama pyfiglet termcolor tqdm")
    speak("Python libraries installed")

# 📋 মেইন মেনু
def main_menu():
    while True:
        show_banner()
        print(colored("❯❯ 1. SETUP MY TERMUX", "green"))
        print(colored("❯❯ 2. EXIT", "red"))

        choice = input(colored("\n❯❯ ENTER YOUR CHOICE (1-2): ", "cyan"))

        if choice == "1":
            print(colored("❯❯ 🔧 STARTING SETUP...\n", "yellow"))
            speak("Starting Termux setup")
            install_all_packages()
            install_python_libraries()
            input(colored("\n❯❯ PRESS ENTER TO RETURN TO MAIN MENU...", "cyan"))
        elif choice == "2":
            speak("Thanks for using. Goodbye!")
            print(colored("\n❯❯ 👋 THANK YOU FOR USING THIS TOOL. GOODBYE!\n", "green"))
            break
        else:
            print(colored("❯❯ ❌ INVALID CHOICE! TRY AGAIN.", "red"))
            time.sleep(1)

# ▶️ MAIN RUN
if __name__ == "__main__":
    main_menu()
