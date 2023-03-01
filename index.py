# imports
from rich.console import Console
from rich.progress import Progress
import dns.resolver
import re

# global variables
console = Console()

# Banner for introduction:
def banner():
    banner = """
        ███████╗██████╗ ███████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
        ██╔════╝██╔══██╗██╔════╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
        ███████╗██████╔╝█████╗  ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
        ╚════██║██╔═══╝ ██╔══╝  ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ███████║██║     ██║     ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
        ╚══════╝╚═╝     ╚═╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   
    """
    _info = """
        [cyan bold]Name[/cyan bold]:       [green bold]Spf Checker[/green bold]
        [cyan bold]Author[/cyan bold]:     [green bold]XARGAI[/green bold]
        [cyan bold]version[/cyan bold]:    [green bold]0.1[/green bold]
    """
    console.print(f"\t\t\t[blue bold]{banner}[/blue bold]" + f"\t{_info}")
    console.print(f"[blue bold]=[/blue bold]" * 80 + "\n")



# SPF Record Handler:
def get_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        # print("1",answers)
        for rdata in answers:
            # print("2",rdata)
            for txt_string in rdata.strings:
                # print("3")
                if txt_string.startswith(b'v=spf1'):
                    return txt_string.decode()
    except:
        return None

# reading file content Handler :
def read_file(filename):
 try:
    with open(filename) as f:
      contents = f.read()
      return contents
 except Exception as e:
    print('\033[93m Error reading file :',e)    

# writing to file 
def write_file(domain):
 try:
     with open('no_spf.txt') as f:
       contents = f.read()
       if domain in contents:
         pass  #  already domains saved:
       else:
            f = open('no_spf.txt', 'a') 
            f.write(domain)  
            f.write('\n')  
            f.close()
 except Exception as e:
    print('\033[93m Error writing file :',e)    

def main():
    # banner for script execution:
    banner()
    # regex for extracting domains from txt file:
    regex = '([A-Za-z_0-9.-]+).*' 
    # reading file content from 'domain.txt' file:
    content = read_file('domains.txt')
    # finding domains from content using regex:
    domains = re.findall(regex,content)
    print('\033[94m Domains found in file:',len(domains))
    # filtering duplicate records:
    domains = list(dict.fromkeys(domains))
    print('\033[94m Total domains to process :',len(domains),'\n')  
    with Progress() as progress:
        task1 = progress.add_task("[cyan]Processing...", total=len(domains))
        for index, domain in enumerate(domains):
                progress.update(task1, advance=1)
                spf_record = get_spf_record(domain)
                if spf_record:
                        print('\033[92m',domain, '==> found' ) 
                else:
                    write_file(domain)
                    print('\033[91m',domain, ' ==> not found' ) 
        
    console.log(f'[blue]Please check no_spf.txt file for results.')
    console.log(f'[bold][blue]Process Completed Successfully!\n')


# Executing Main Function:
main()
