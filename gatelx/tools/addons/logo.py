"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """

░██████╗░░█████╗░████████╗███████╗██╗░░░░░██╗░░██╗
██╔════╝░██╔══██╗╚══██╔══╝██╔════╝██║░░░░░╚██╗██╔╝
██║░░██╗░███████║░░░██║░░░█████╗░░██║░░░░░░╚███╔╝░
██║░░╚██╗██╔══██║░░░██║░░░██╔══╝░░██║░░░░░░██╔██╗░
╚██████╔╝██║░░██║░░░██║░░░███████╗███████╗██╔╝╚██╗
░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚═╝                                 ░     
  """

    print(f"{F.WHITE}{logo}")
    print(" ")
    print(" $===============INFO===============$")
    print(" ├ • Created  : Mr.Cypher4x         |")
    print(" ├ • Name     : GATELX - DOS TOOL   |")
    print(" ├ • Date     : 05 - 10 - 2024      |")
    print(" ├ • Telegram : @kingepepp          |")
    print(" ├ • Team     : UNDERGROUND-NET     |")
    print(" $==================================$")
    print(" ")
    print("├─── DOS TOOL")
    print("├─── AVAILABLE METHODS")
    print("├─── LAYER 7: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── LAYER 4: SYN-FLOOD")
        print("├─── LAYER 2: ARP-SPOOF | DISCONNECT")
    print("├───┐")
