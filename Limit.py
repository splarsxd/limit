import os, speedtest, rich, time, sys

prefix = "Limit b3 by splars#1252"
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout -1 >nul" if os.name == "nt" else time.sleep(5))
os.system("title %s" % prefix if os.name == "nt" else "pass")
cls()

dotnmbr = -6
dot = [".","..","...","....",".....","......"]

while True:
    if dotnmbr >= 6:
        break
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                     {dot[dotnmbr]}")
    os.system("color c")
    os.system("color e")
    os.system("color a")
    os.system("color b")
    os.system("color d")
    os.system("color 5")
    cls()

    dotnmbr += 1
    continue

os.system("color 0f" if os.name == "nt" else "pass")
print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                Please, wait patiently!")

super = speedtest.Speedtest()
latency = super.get_best_server()
down = super.download() / 1000 / 1000
up = super.upload() / 1000 / 1000
cls()

def pinger(ping):
    if ping <= 32:
        return "green3"
    elif ping < 70:
        return "orange3"
    else:
        return "red3"

rich.print(f"""\n\n\n\n\n\n\n\n\n\n
                                    [bold grey]——————————————————————————————————————————————————[/bold grey]
                                        [bold white]Host:[/bold white] [bold cyan]{latency['host']}[/bold cyan]
                                        [bold white]Country: {latency['country']} {latency['cc']}[/bold white]

                                        [bold white]Ping:[/bold white] [{pinger(latency['latency'])}]{latency['latency']} ms[/{pinger(latency['latency'])}]
                                        [bold white]Download:[/bold white] [deep_sky_blue4]{down:.2f} Mb/s[/deep_sky_blue4] | [deep_sky_blue4]{down / 8:.2f} MB/s[/deep_sky_blue4]
                                        [bold white]Upload:[/bold white] [dark_magenta]{up:.2f} Mb/s[/dark_magenta] | [dark_magenta]{up / 8:.2f} MB/s[/dark_magenta]
                                    [bold grey]——————————————————————————————————————————————————[/bold grey]
""")

sleep()
sys.exit()