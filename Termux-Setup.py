#Root Jahid
#VIP Members 
import os
import time
import sys
import requests
import threading
from termcolor import colored, cprint
from pyfiglet import Figlet
from tqdm import tqdm
import subprocess

# Voice announcement function using termux-tts-speak
def speak(text):
    try:
        subprocess.run(["termux-tts-speak", text])
    except:
        pass  # Continue silently if voice fails

# Clear screen with animation
def clear_screen():
    os.system('clear')
    for i in range(5):
        print("\n" * i)
        time.sleep(0.1)
    os.system('clear')

# Display animated ASCII art
def show_ascii_art():
    custom_fig = Figlet(font='slant')
    ascii_art = custom_fig.renderText('T-Setup')
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    
    for i in range(3):  # Animation loop
        for color in colors:
            print(colored(ascii_art, color))
            time.sleep(0.2)
            if i < 2:
                os.system('clear')

# Display colorful banner
def show_banner():
    clear_screen()
    show_ascii_art()
    print(colored("="*60, 'cyan'))
    print(colored("Termux Professional Setup Tool".center(60), 'yellow'))
    print(colored("Created by RootJahid".center(60), 'magenta'))
    print(colored("="*60, 'cyan'))
    print("\n")

# Open Telegram channel
def open_telegram():
    speak("Welcome to Root Jahid Termux Setup Tool")
    speak("Please join our Telegram channel for updates and support")
    print(colored("\nOpening Telegram channel...", 'yellow'))
    time.sleep(2)
    os.system("xdg-open https://t.me/RootJahid")
    time.sleep(5)

# Install packages with progress bar
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
    
    speak("Starting Termux setup process")
    print(colored("\nUpdating packages...", 'cyan'))
    os.system("pkg update -y")
    
    print(colored("\nUpgrading packages...", 'cyan'))
    os.system("pkg upgrade -y")
    
    print(colored("\nInstalling required packages...", 'cyan'))
    
    # Animated progress bar for package installation
    with tqdm(total=len(packages), ncols=70, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        for pkg in packages:
            pbar.set_description(f"Installing {pkg}")
            os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
            pbar.update(1)
            time.sleep(0.5)
    
    print(colored("\nInstalling Python packages...", 'cyan'))
    os.system("pip install --upgrade pip")
    os.system("pip install requests bs4 colorama")
    
    # Final animation
    for i in range(3):
        for color in ['green', 'yellow', 'cyan']:
            print(colored("\nSetup completed successfully!", color))
            time.sleep(0.3)
            os.system('clear')
    
    speak("Termux setup has been completed successfully")
    time.sleep(2)

# Main menu
def main_menu():
    while True:
        show_banner()
        print(colored("Choose an option:\n", 'yellow'))
        print(colored("1. Set-up My Termux", 'green'))
        print(colored("2. Exit", 'red'))
        
        choice = input(colored("\nEnter your choice (1-2): ", 'cyan'))
        
        if choice == '1':
            print(colored("\nStarting Termux setup...", 'magenta'))
            speak("Starting Termux setup process. Please wait...")
            install_packages()
            input(colored("\nPress Enter to return to main menu...", 'yellow'))
        elif choice == '2':
            speak("Thanks for using our tools. Goodbye!")
            print(colored("\nThanks for using our tools. Goodbye!\n", 'green'))
            
            # Exit animation
            for i in range(5, 0, -1):
                print(colored(f"Exiting in {i} seconds...", 'red'))
                time.sleep(1)
                os.system('clear')
            break
        else:
            print(colored("\nInvalid choice! Please try again.", 'red'))
            time.sleep(1)

# Main function
def main():
    try:
        # Initial setup
        threading.Thread(target=speak, args=("Welcome to Root Jahid Termux Setup Tool",)).start()
        open_telegram()
        main_menu()
    except KeyboardInterrupt:
        speak("Setup process cancelled")
        print(colored("\n\nSetup cancelled by user!", 'red'))
        sys.exit()
    except Exception as e:
        print(colored(f"\nError occurred: {str(e)}", 'red'))
        sys.exit()

if __name__ == "__main__":
    # Check if termux-tts-speak is installed
    if os.system("command -v termux-tts-speak > /dev/null") != 0:
        print(colored("Installing termux-tts-speak for voice announcements...", 'yellow'))
        os.system("pkg install termux-tts-speak -y")
    
    # Check if pyfiglet is installed
    if os.system("pip show pyfiglet > /dev/null") != 0:
        print(colored("Installing pyfiglet for ASCII art...", 'yellow'))
        os.system("pip install pyfiglet")
    
    # Check if termcolor is installed
    if os.system("pip show termcolor > /dev/null") != 0:
        print(colored("Installing termcolor for colored output...", 'yellow'))
        os.system("pip install termcolor")
    
    # Check if tqdm is installed
    if os.system("pip show tqdm > /dev/null") != 0:
        print(colored("Installing tqdm for progress bars...", 'yellow'))
        os.system("pip install tqdm")
    
    main()
