import time
import requests
from colorama import init, Fore, Style
from channels import*
from URL import*
from kodiprop import*

init(autoreset=True)
def test_stream(url):
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return True  
        else:
            return False  
    except requests.RequestException:
        return False  
def generate_playlist(channels):
    playlist = "#EXTM3U\n"  
    tvg_chno = 1  
    total_channels = len(channels)
    for i, channel in enumerate(channels, start=1):  
        print(f"Generování kanálu {i}/{total_channels}: {channel['name']}") 
        if channel["base_url"] == "one":
            stream_url = f"{one_base_url}{channel['id']}{end_base_url}"
        elif channel["base_url"] == "two":
            stream_url = f"{two_base_url}{channel['id']}"
        elif channel["base_url"] == "three":
            stream_url = f"{three_base_url}{channel['id']}"
        elif channel["base_url"] == "four":
            stream_url = f"{four_base_url}{channel['id']}{end_base_url}"
        elif channel["base_url"] == "five":
            stream_url = f"{five_base_url}"    
        else:
            stream_url = f"{one_base_url}{channel['id']}"                 
        if test_stream(stream_url):
            print(f"Stream {channel['name']}: {Fore.GREEN}OK{Style.RESET_ALL}")
            stream_status = "OK"
        else:
            print(f"Stream {channel['name']}: {Fore.RED}OFF{Style.RESET_ALL}")
            stream_status = "OFF"              
        if stream_status == "OFF":
            continue              
        icon_url = f"{icon_base_url}{channel['tvg_logo']}.png"             
        if channel["catchup"]:
            extinf_line = f'#EXTINF:-1 $ExtFilter="TV" tvg-name="{channel["name"]}" tvg-chno="{tvg_chno}" tvg-id="{channel["epg"]}" group-title="{channel["group"]}" tvg-logo="{icon_url}" catchup="append" catchup-days="7" catchup-source="{stream_url}?offset=-${{offset}}",{channel["name"]}\n'
        else:
            extinf_line = f'#EXTINF:-1 $ExtFilter="TV"  tvg-name="{channel["name"]}" tvg-chno="{tvg_chno}" tvg-id="{channel["epg"]}" group-title="{channel["group"]}" tvg-logo="{icon_url}",{channel["name"]}\n'                
        playlist += extinf_line              
        playlist += add_kodi_properties(channel["kodi_group"])            
        playlist += f"{stream_url}\n\n"               
        tvg_chno += 1               
        time.sleep(0.1)   
    return playlist
playlist_content = generate_playlist(channels)
with open("playlist.m3u8", "w") as file:
    file.write(playlist_content)
print("Playlist byl úspěšně vygenerován.\n")
input("Generování dokončeno. Stiskněte libovolnou klávesu pro ukončení...")