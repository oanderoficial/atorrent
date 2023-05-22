import os
from colorama import Fore, Style

while True:
    print(Fore.GREEN + """
                                      
   (         )                               )  
   )\     ( /(      (    (      (         ( /(  
((((_)(   )\()) (   )(   )(    ))\  (     )\()) 
 )\ _ )\ (_))/  )\ (()\ (()\  /((_) )\ ) (_))/  
 (_)_\(_)| |_  ((_) ((_) ((_)(_))  _(_/( | |_   
  / _ \  |  _|/ _ \| '_|| '_|/ -_)| ' \))|  _|  
 /_/ \_\  \__|\___/|_|  |_|  \___||_||_|  \__|  

    """ + Style.RESET_ALL)
    print(Fore.GREEN + "1. Download Torrent (link magnético)\n" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Download de BitTorrent:\n" + Style.RESET_ALL)
    print(Fore.GREEN + "3. Streaming de Torrents: \n" + Style.RESET_ALL)
    print(Fore.GREEN + "0 - Sair \n" + Style.RESET_ALL)
    opcao = input(Fore.RED + "\nATORRENT>> " + Style.RESET_ALL)

    if opcao == "1":
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)
        link = input(Fore.GREEN + "Digite o link magnético: " + Style.RESET_ALL)
        os.system(f"aria2c {link}")
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)

    elif opcao == "2":
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)
        bittorrent = input(Fore.GREEN + "Digite o link BitTorrent: " + Style.RESET_ALL)
        os.system(f"aria2c {bittorrent}")
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)

    elif opcao == "3":
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)
        streaming = input(Fore.GREEN + "Digite o link magnético: " + Style.RESET_ALL)
        os.system(f"webtorrent {streaming} 0 1")
        print(Fore.RED + "-----------------------------\n" + Style.RESET_ALL)

    elif opcao == "0":
        print("Saindo do programa...\n")
        break

    else:
        print(Fore.RED + "Opção inválida.\n" + Style.RESET_ALL)
