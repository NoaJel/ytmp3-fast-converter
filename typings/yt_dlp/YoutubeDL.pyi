from typing import Any, Iterable, Optional, Self

from yt_dlp_manager import VideoInfo


class YoutubeDL:
    def __init__(self, params: Optional[dict[str, Any]] = None, auto_init: bool = True) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, *args: Any) -> None:
        ...

    def download(self, url_list: Iterable[str]) -> int:
        ...

    def extract_info(self, url: str, download: bool = True, ie_key: Any = None, extra_info: Any = None,
                     process: bool = True, force_generic_extractor: bool = False) -> VideoInfo:
        ...
