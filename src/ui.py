from .utils import *

def print_banner():
    banner = f"""{MAGENTA}{BRIGHT}
██╗      █████╗ ██████╗ ██████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██║     ██╔══██╗██╔══██╗██╔══██╗   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██║     ███████║██████╔╝██████╔╝   ██║     ███████║█████╗  ██║     █████╔╝ 
██║     ██╔══██║██╔══██╗██╔═══╝    ██║     ██║  ██║██╔══╝  ██║     ██╔═██╗ 
███████╗██║  ██║██║  ██║██║        ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
{RESET}
    {CYAN}[ {RED}Legitimacy and Repository Plagiarism ${CYAN}Checker ]{RESET}
    {MAGENTA}// {RED}Verify the truth{MAGENTA}. {CYAN}Expose the lies{MAGENTA}. //{RESET}
    """
    print(banner)

def print_menu():
    menu = f"""
{MAGENTA}╔═══════════════════════════════════════════╗
║             {RED}$ELECT YOUR PATH{MAGENTA}              ║
╠═══════════════════════════════════════════╣
║  {CYAN}[{RED}1{CYAN}]{RESET} {MAGENTA}INITIATE REPOSITORY ANALYSIS        {MAGENTA} ║
║  {CYAN}[{RED}2{CYAN}]{RESET} {MAGENTA}ABOUT LARP ${CYAN}CHECK                 {MAGENTA}   ║
║  {CYAN}[{RED}3{CYAN}]{RESET} {MAGENTA}TERMINATE                          {MAGENTA}  ║
╚═══════════════════════════════════════════╝{RESET}
"""
    print(menu)

def print_report(report):
    """Print the analysis report with fancy formatting"""
    print(f"\n{MAGENTA}╔{'═' * 60}╗")
    print(f"║{' ' * 20}{RED}ANALYSIS REPORT{MAGENTA}{' ' * 25}║")
    print(f"╠{'═' * 60}╣{RESET}")
    
    # Repository Info
    print(f"{MAGENTA}║{RESET} {CYAN}Repository:{RESET} {BRIGHT}{report['repository']['name']}{RESET}")
    print(f"{MAGENTA}║{RESET} {CYAN}URL:{RESET} {report['repository']['url']}")
    print(f"{MAGENTA}║{RESET} {CYAN}Stars:{RESET} {BRIGHT}{report['repository']['stars']}{RESET}")
    print(f"{MAGENTA}║{RESET} {CYAN}Last Updated:{RESET} {report['repository']['last_updated']}")
    
    # Features Analysis
    print(f"{MAGENTA}╠{'═' * 60}╣")
    print(f"║{' ' * 20}{RED}FEATURE SCAN{MAGENTA}{' ' * 27}║{RESET}")
    for feature, implemented in report['features_analysis']:
        status = f"{GREEN}[✓]{RESET}" if implemented else f"{RED}[✗]{RESET}"
        feature_text = feature[:45] + '...' if len(feature) > 45 else feature
        print(f"{MAGENTA}║{RESET} {status} {CYAN}{feature_text}{RESET}")
    
    # Similar Repositories
    print(f"{MAGENTA}╠{'═' * 60}╣")
    print(f"║{' ' * 18}{RED}SIMILAR REPOS FOUND{MAGENTA}{' ' * 22}║{RESET}")
    if report['similar_repositories']:
        for repo in report['similar_repositories']:
            similarity_color = RED if repo['similarity'] > 0.9 else YELLOW if repo['similarity'] > 0.85 else GREEN
            print(f"{MAGENTA}║{RESET} {similarity_color}■{RESET} {CYAN}{repo['repo']}{RESET}")
            print(f"{MAGENTA}║{RESET}   {similarity_color}↳ Similarity: {repo['similarity']:.2%}{RESET}")
            print(f"{MAGENTA}║{RESET}   {CYAN}URL: {repo['url']}{RESET}")
    else:
        print(f"{MAGENTA}║{RESET} {GREEN}No similar repositories detected{RESET}")
    
    # Health Checks
    print(f"{MAGENTA}╠{'═' * 60}╣")
    print(f"║{' ' * 20}{RED}HEALTH STATUS{MAGENTA}{' ' * 25}║{RESET}")
    for check, status in report['health_checks'].items():
        status_symbol = f"{GREEN}[PASS]{RESET}" if status else f"{RED}[FAIL]{RESET}"
        check_name = check.replace('_', ' ').title()
        print(f"{MAGENTA}║{RESET} {status_symbol} {CYAN}{check_name}{RESET}")
    
    print(f"{MAGENTA}╚{'═' * 60}╝{RESET}")

def print_about():
    about_text = f"""
{MAGENTA}╔═════════════════════════════════════════════════════════════╗
║     {RED} ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗{MAGENTA}                ║
║     {RED}██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝{MAGENTA}                ║
║     {RED}██║     ███████║█████╗  ██║     █████╔╝{MAGENTA}                 ║
║     {RED}██║     ██╔══██║██╔══╝  ██║     ██╔═██╗{MAGENTA}                 ║
║     {RED}╚██████╗██║  ██║███████╗╚██████╗██║  ██╗{MAGENTA}                ║
║     {RED} ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝{MAGENTA}                ║
╠═════════════════════════════════════════════════════════════╣
║                                                             ║
║                  {RED}[ {CYAN}SYSTEM OVERVIEW{RED} ]{MAGENTA}                        ║
╠═════════════════════════════════════════════════════════════╣{RESET}

{CYAN}LARP ${RED}CHECK{RESET} is a {RED}cyberpunk-inspired{RESET} tool designed to expose the 
{RED}truth{RESET} in the digital underground. Operating in the shadows of the 
{CYAN}repository matrix{RESET}, it hunts for {RED}deception{RESET} and {RED}plagiarism{RESET}.

{MAGENTA}╔═════════════════════════════════════════════════════════════╗
║                  {RED}[ {CYAN}CORE FUNCTIONS{RED} ]{MAGENTA}                         ║
╠═════════════════════════════════════════════════════════════╣{RESET}

{CYAN}▓▓▒▒░░ {RED}>{RESET} Deep analysis of repository claims vs. reality
{CYAN}▓▓▒▒░░ {RED}>{RESET} Advanced plagiarism detection algorithms
{CYAN}▓▓▒▒░░ {RED}>{RESET} Comprehensive health and authenticity scanning
{CYAN}▓▓▒▒░░ {RED}>{RESET} Detailed reporting with threat assessment

{MAGENTA}╔═════════════════════════════════════════════════════════════╗
║                   {RED}[ {CYAN}DIRECTIVE{RED} ]{MAGENTA}                             ║
╠═════════════════════════════════════════════════════════════╣{RESET}

Maintain integrity in the {CYAN}digital realm{RESET} by exposing {RED}copycats{RESET}
and verifying the {CYAN}authenticity{RESET} of open-source repositories.

{MAGENTA}╔═════════════════════════════════════════════════════════════╗
║                   {RED}[ {CYAN}PROTOCOL{RED} ]{MAGENTA}                              ║
╠═════════════════════════════════════════════════════════════╣{RESET}

{RED}[ {CYAN}Remember{RED} ]{RESET} In cyberspace, trust is a vulnerability.
{RED}[ {CYAN}Solution{RED} ]{RESET} Verify everything. Trust nothing.

{MAGENTA}╚═════════════════════════════════════════════════════════════╝{RESET}
"""
    print(about_text)
