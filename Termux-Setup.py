from termcolor import colored
from pyfiglet import Figlet
import subprocess
import time
import os
import sys

# Function to speak a message using termux-tts-speak
def speak(message):
    try:
        subprocess.run(["termux-tts-speak", message], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

# Clear the screen
def clear_screen():
    os.system("clear")

# Display the ASCII banner only once with multi-color
def show_ascii_art_once():
    fig = Figlet(font="slant")
    ascii_art = fig.renderText("T-Setup")
    gradient = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    lines = ascii_art.splitlines()
    for i, line in enumerate(lines):
        print(colored(line, gradient[i % len(gradient)]))

# Show banner
def show_banner():
    clear_screen()
    show_ascii_art_once()
    print(colored("❯❯ " + "=" * 60, 'cyan'))
    print(colored("❯❯ TERMUX PROFESSIONAL SETUP TOOL".center(60), 'yellow'))
    print(colored("❯❯ CREATED BY ROOTJAHID".center(60), 'magenta'))
    print(colored("❯❯ " + "=" * 60, 'cyan'))
    print("\n")

# Install a single package with voice and styled output
def install_single_package(pkg_name):
    message = f"INSTALLING PACKAGE {pkg_name.upper()}"
    speak(message)
    print(colored(f"❯❯ 📦 INSTALLING: {pkg_name.upper()}", 'green'))
    print(colored("❯❯ " + "=" * (12 + len(pkg_name)), 'cyan'))
    time.sleep(0.5)
    os.system(f"pkg install {pkg_name} -y")
    print(colored(f"❯❯ ✅ {pkg_name.upper()} INSTALLED SUCCESSFULLY.\n", 'green'))
    speak(f"{pkg_name.upper()} INSTALLED SUCCESSFULLY")
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

    speak("UPDATING PACKAGE LIST")
    print(colored("\n❯❯ 🔄 UPDATING PACKAGE LIST...", 'cyan'))
    os.system("pkg update -y")

    speak("UPGRADING PACKAGES")
    print(colored("\n❯❯ ⏫ UPGRADING INSTALLED PACKAGES...", 'cyan'))
    os.system("pkg upgrade -y")

    for pkg in packages:
        install_single_package(pkg)

    speak("ALL PACKAGES INSTALLED SUCCESSFULLY")
    print(colored("\n❯❯ 🎉 ALL PACKAGES INSTALLED SUCCESSFULLY!", 'yellow'))

# Install Python libraries
def install_python_modules():
    speak("INSTALLING PYTHON LIBRARIES")
    print(colored("\n❯❯ 🐍 INSTALLING PYTHON LIBRARIES...", 'magenta'))
    os.system("pip install --upgrade pip")
    os.system("pip install requests bs4 colorama termcolor pyfiglet tqdm")
    speak("PYTHON LIBRARIES INSTALLED")

# Menu
def main_menu():
    while True:
        show_banner()
        print(colored("❯❯ 📋 CHOOSE AN OPTION:\n", 'yellow'))
        print(colored("❯❯ 1. SET-UP MY TERMUX", 'green'))
        print(colored("❯❯ 2. EXIT", 'red'))

        choice = input(colored("\n❯❯ ENTER YOUR CHOICE (1-2): ", 'cyan'))

        if choice == '1':
            speak("STARTING TERMUX SETUP")
            print(colored("\n❯❯ 🚀 STARTING TERMUX SETUP...\n", 'magenta'))
            install_packages()
            install_python_modules()
            input(colored("\n❯❯ PRESS ENTER TO RETURN TO MAIN MENU...", 'yellow'))
        elif choice == '2':
            speak("THANKS FOR USING THE TOOL. GOODBYE")
            print(colored("\n❯❯ 👋 THANKS FOR USING THE TOOL. GOODBYE!\n", 'green'))
            break
        else:
            print(colored("❯❯ ❌ INVALID CHOICE! TRY AGAIN.", 'red'))
            time.sleep(1)

# Run
def main():
    clear_screen()
    speak("WELCOME TO ROOT JAHID TERMUX SETUP TOOL")
    main_menu()

if __name__ == "__main__":
    main()
