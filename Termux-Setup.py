from termcolor import colored
from pyfiglet import Figlet
import subprocess
import time
import os
import sys

# Voice announcement using termux-tts-speak
def speak(text):
    try:
        subprocess.run(["termux-tts-speak", text], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# Clear screen
def clear_screen():
    os.system("clear")

# Show ASCII banner once with gradient color
def show_ascii_art_once():
    fig = Figlet(font="slant")
    ascii_art = fig.renderText("T-Setup")
    gradient = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for i, line in enumerate(ascii_art.splitlines()):
        color = gradient[i % len(gradient)]
        print(colored(line, color))

# Show banner
def show_banner():
    clear_screen()
    show_ascii_art_once()
    print(colored("=" * 60, 'cyan'))
    print(colored("Termux Professional Setup Tool".center(60), 'yellow'))
    print(colored("Created by RootJahid".center(60), 'magenta'))
    print(colored("=" * 60, 'cyan'))
    print("\n")

# Install single package with announcement and styling
def install_single_package(pkg_name):
    speak(f"Installing {pkg_name}")
    print(colored(f"\n📦 Installing: {pkg_name}", 'green'))
    print(colored("=" * (12 + len(pkg_name)), 'cyan'))
    time.sleep(1)
    os.system(f"pkg install {pkg_name} -y > /dev/null 2>&1")
    print(colored(f"✅ {pkg_name} installed successfully.\n", 'green'))
    speak(f"{pkg_name} installed successfully")
    time.sleep(0.5)

# Install all packages one by one
def install_packages():
    packages = [
        "python", "python2", "git", "curl", "wget", "openssh",
        "nano", "vim", "zip", "unzip", "tar", "clang", "make",
        "nodejs", "php", "ruby", "bash", "fish", "net-tools",
        "tmux", "figlet", "toilet", "cowsay", "termux-api",
        "dnsutils", "jq", "coreutils", "util-linux", "tsu",
        "proot", "man", "neofetch", "htop", "tree", "grep",
        "sed", "nmap", "cmatrix", "lolcat", "openssl", "libffi",
        "ndk-sysroot", "termux-exec", "python3-pip", "rust",
        "busybox", "libxml2", "libxslt", "binutils", "gdb", "fftw"
    ]

    speak("Updating packages")
    print(colored("\n🔄 Updating packages...", 'cyan'))
    os.system("pkg update -y > /dev/null 2>&1")

    speak("Upgrading packages")
    print(colored("\n⏫ Upgrading packages...", 'cyan'))
    os.system("pkg upgrade -y > /dev/null 2>&1")

    for pkg in packages:
        install_single_package(pkg)

    print(colored("\n🎉 All packages installed successfully!\n", 'yellow'))
    speak("All packages installed successfully")

# Install required Python modules
def install_python_modules():
    speak("Installing required python packages")
    print(colored("\n🐍 Installing Python packages...\n", 'magenta'))
    os.system("pip install --upgrade pip")
    os.system("pip install requests bs4 colorama termcolor pyfiglet tqdm > /dev/null 2>&1")
    speak("Python packages installed")

# Main menu
def main_menu():
    while True:
        show_banner()
        print(colored("📋 Choose an option:\n", 'yellow'))
        print(colored("1. Set-up My Termux", 'green'))
        print(colored("2. Exit", 'red'))

        choice = input(colored("\nEnter your choice (1-2): ", 'cyan'))

        if choice == '1':
            speak("Starting Termux setup")
            print(colored("\n🚀 Starting Termux setup...\n", 'magenta'))
            install_packages()
            install_python_modules()
            input(colored("\nPress Enter to return to main menu...", 'yellow'))
        elif choice == '2':
            speak("Thanks for using the tool. Goodbye")
            print(colored("\n👋 Thanks for using the tool. Goodbye!\n", 'green'))
            break
        else:
            print(colored("\n❌ Invalid choice! Try again.", 'red'))
            time.sleep(1)

# Initial dependency check and run
def main():
    clear_screen()
    speak("Welcome to Root Jahid Termux Setup Tool")
    main_menu()

if __name__ == "__main__":
    main()
