import nltk
import time
from src import (
    LARPChecker,
    print_banner,
    print_menu,
    print_report,
    print_about,
    clear_screen,
    CYAN,
    RED,
    RESET
)

def main():
    # Download required NLTK data
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        choice = input(f"{CYAN}[{RED}?{CYAN}]{RESET} Enter your choice: ")
        
        if choice == '1':
            repo_url = input(f"\n{CYAN}[{RED}?{CYAN}]{RESET} Enter target repository URL: ")
            
            try:
                checker = LARPChecker(repo_url)
                checker.analyze_features()
                checker.check_code_similarity()
                report = checker.generate_report()
                print_report(report)
                input(f"\n{CYAN}[{RED}*{CYAN}]{RESET} Press Enter to continue...")
            except Exception as e:
                print(f"\n{RED}[!] Error:{RESET} {str(e)}")
                input(f"\n{CYAN}[{RED}*{CYAN}]{RESET} Press Enter to continue...")
                
        elif choice == '2':
            print_about()
            input(f"\n{CYAN}[{RED}*{CYAN}]{RESET} Press Enter to continue...")
            
        elif choice == '3':
            print(f"\n{CYAN}[{RED}*{CYAN}]{RESET} Terminating LARP ${CYAN}CHECK{RESET}...")
            time.sleep(1)
            break
            
        else:
            print(f"\n{RED}[!] Invalid choice. Recalibrate and try again.{RESET}")
            input(f"\n{CYAN}[{RED}*{CYAN}]{RESET} Press Enter to continue...")

if __name__ == "__main__":
    main()
