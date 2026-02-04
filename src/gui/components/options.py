"""Download options component (type and quality selector)"""
import customtkinter as ctk
from typing import Callable, Optional


class DownloadOptions(ctk.CTkFrame):
    """Download type and quality selector"""
    
    QUALITY_OPTIONS = [
        "Best Available",
        "2160p (4K)",
        "1440p (2K)",
        "1080p (Full HD)",
        "720p (HD)",
        "480p",
        "360p",
    ]
    
    def __init__(
        self,
        parent,
        on_type_change: Optional[Callable[[str], None]] = None,
        on_quality_change: Optional[Callable[[str], None]] = None,
        **kwargs
    ):
        """
        Initialize download options component
        
        Args:
            parent: Parent widget
            on_type_change: Callback when download type changes
            on_quality_change: Callback when quality changes
        """
        super().__init__(parent, **kwargs)
        self.on_type_change = on_type_change
        self.on_quality_change = on_quality_change
        
        # Download Type Section
        self.type_label = ctk.CTkLabel(
            self,
            text="Download Type:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.type_label.pack(pady=(0, 8), anchor="w")
        
        # Radio button frame
        self.type_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.type_frame.pack(fill="x", pady=(0, 16))
        
        self.type_var = ctk.StringVar(value="video")
        
        self.video_radio = ctk.CTkRadioButton(
            self.type_frame,
            text="Video",
            variable=self.type_var,
            value="video",
            command=self._on_type_change,
            font=ctk.CTkFont(size=13)
        )
        self.video_radio.pack(side="left", padx=(0, 24))
        
        self.audio_radio = ctk.CTkRadioButton(
            self.type_frame,
            text="Audio Only (MP3)",
            variable=self.type_var,
            value="audio",
            command=self._on_type_change,
            font=ctk.CTkFont(size=13)
        )
        self.audio_radio.pack(side="left")
        
        # Quality Section
        self.quality_label = ctk.CTkLabel(
            self,
            text="Quality:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.quality_label.pack(pady=(0, 8), anchor="w")
        
        self.quality_dropdown = ctk.CTkComboBox(
            self,
            values=self.QUALITY_OPTIONS,
            command=self._on_quality_change,
            height=35,
            font=ctk.CTkFont(size=13),
            dropdown_font=ctk.CTkFont(size=12),
            state="readonly"
        )
        self.quality_dropdown.set("Best Available")
        self.quality_dropdown.pack(fill="x")
    
    def _on_type_change(self):
        """Handle download type change"""
        download_type = self.type_var.get()
        
        # Disable quality selector for audio
        if download_type == "audio":
            self.quality_dropdown.configure(state="disabled")
            self.quality_label.configure(text_color="gray50")
        else:
            self.quality_dropdown.configure(state="readonly")
            self.quality_label.configure(text_color=("gray10", "gray90"))
        
        if self.on_type_change:
            self.on_type_change(download_type)
    
    def _on_quality_change(self, choice):
        """Handle quality selection change"""
        if self.on_quality_change:
            self.on_quality_change(choice)
    
    def get_download_type(self) -> str:
        """Get selected download type"""
        return self.type_var.get()
    
    def get_quality(self) -> str:
        """Get selected quality"""
        return self.quality_dropdown.get()
    
    def set_download_type(self, download_type: str):
        """Set download type"""
        self.type_var.set(download_type)
        self._on_type_change()
    
    def set_quality(self, quality: str):
        """Set quality selection"""
        if quality in self.QUALITY_OPTIONS:
            self.quality_dropdown.set(quality)
    
    def set_enabled(self, enabled: bool):
        """Enable or disable the options"""
        state = "normal" if enabled else "disabled"
        self.video_radio.configure(state=state)
        self.audio_radio.configure(state=state)
        
        if enabled and self.get_download_type() == "video":
            self.quality_dropdown.configure(state="readonly")
        else:
            self.quality_dropdown.configure(state="disabled")
