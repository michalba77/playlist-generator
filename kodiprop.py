# Funkce pro přidání KODI properties na základě zvolené skupiny

def add_kodi_properties(kodi_group):
    if kodi_group == "group1":
        return """#KODIPROP:inputstreamaddon=inputstream.adaptive
#KODIPROP:inputstream.adaptive.license_type=com.widevine.alpha
#KODIPROP:inputstream.adaptive.stream_buffer_size=30
#KODIPROP:inputstream.adaptive.live_delay=5
#KODIPROP:inputstream.ffmpegdirect.stream_mode=timeshift
#KODIPROP:inputstream.ffmpegdirect.is_realtime_stream=true
#KODIPROP:inputstream.adaptive.manifest_type=mpd\n"""
    
    elif kodi_group == "group2":   # tento group2 je vhodny na widewine a drm. zde je potreba doplnit dalsi informace ke kontrole klicu 
        return """#KODIPROP:inputstreamaddon=inputstream.adaptive
#KODIPROP:inputstream.adaptive.license_type=com.widevine.alpha
#KODIPROP:inputstream.adaptive.stream_buffer_size=30
#KODIPROP:inputstream.adaptive.live_delay=4
#KODIPROP:inputstream.ffmpegdirect.stream_mode=timeshift
#KODIPROP:inputstream.ffmpegdirect.is_realtime_stream=true
#KODIPROP:inputstream.adaptive.stream_headers=User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0
#KODIPROP:inputstream.adaptive.license_key=  
#KODIPROP:inputstream.adaptive.manifest_type=mpd\n"""
    
    elif kodi_group == "group3":
        return """#KODIPROP:inputstreamaddon=inputstream.adaptive
#KODIPROP:mimetype=application/x-mpegURL
#KODIPROP:inputstream.ffmpegdirect.stream_mode=timeshift
#KODIPROP:inputstream.ffmpegdirect.is_realtime_stream=true\n"""

    elif kodi_group == "group4":
        return """#KODIPROP:inputstream=inputstream.ffmpegdirect
#KODIPROP:inputstream.ffmpegdirect.stream_mode=timeshift
#KODIPROP:inputstream.adaptive.max_resolution_width=1920
#KODIPROP:inputstream.adaptive.max_resolution_height=1080
#KODIPROP:inputstream.ffmpegdirect.is_realtime_stream=true\n"""
    
    return "#KODIPROP:inputstreamaddon=inputstream.adaptive\n"