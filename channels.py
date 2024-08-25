# Seznam kanálů s pevnými URL adresami pro každý stream
# Navod :
# "name": "ČT1" = tvg-name="ČT1" nazev Tv programu

# "group": "Česke" =  group-title="Česke" 

# "epg": "" = tvg-id="" tv stanice oznacena v epg

# "tvg_logo": "ct1" = nazev ikony bez .png nazev ikon si muzete dohledat na mych strankach https://github.com/michalba77/ikony

# "id": "" = tady se dava cast url ze streamu ktera je na kazdy stream jina . napr. pokud je stream http://IP adresa/a02o/index.m3u8 a nasledna je http://IP adresa/a03o/index.m3u8 tak zapis bude "id": "a02o"

# "base_url": "one" = tady je zapis staticke url ktera se nemeni, tu uvedeme do souboru url.py 

# "kodi_group": "group1" = zde je vyber kodiprop ktery jsme si nastavili v souboru kodiprop.py

# vse zapisujeme mezi zavorky

# "catchup": True = zde uvadime zapnuti a vypnuti catchup ( True - zapnuto , False - vypnuto ) jestlize je uvedeno False neni catchup pridan do playlistu

 

channels = [   
    {"name": "",
    "group": "",
    "epg": "",
    "tvg_logo": "",
    "id": "",
    "base_url": "",
    "kodi_group": "",
    "catchup": True},
    
    {"name": "",
    "group": "",
    "epg": "",
    "tvg_logo": "",
    "id": "",
    "base_url": "",
    "kodi_group": "",
    "catchup": False},
       
]