from enum import Enum


class TikTokSignLiveClient(str, Enum):
    GOTIKTOK_LIVE = "gotiktok_live"
    INTERNAL = "internal"
    TTLIVE_CLOUDFLARE = "ttlive-cloudflare"
    TTLIVE_JAVA = "ttlive-java"
    TTLIVE_NET = "ttlive-net"
    TTLIVE_NODE = "ttlive-node"
    TTLIVE_OTHER = "ttlive-other"
    TTLIVE_PYTHON = "ttlive-python"
    TTLIVE_RUST = "ttlive-rust"

    def __str__(self) -> str:
        return str(self.value)
