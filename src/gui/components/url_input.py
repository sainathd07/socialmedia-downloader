"""URL input component with validation feedback"""
import customtkinter as ctk
from tkinter import END
from typing import Callable, Optional
from ...core.validator import URLValidator


class URLInput(ctk.CTkFrame):
    """URL input field with real-time validation"""
    
    def __init__(self, parent, on_change: Optional[Callable[[str, bool], None]] = None, **kwargs):
        """
        Initialize URL input component
        
        Args:
            parent: Parent widget
            on_change: Callback function called when URL changes (url, is_valid)
        """
        super().__init__(parent, **kwargs)
        self.on_change = on_change
        
        # Label
        self.label = ctk.CTkLabel(
            self,
            text="Paste Video URL:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label.pack(pady=(0, 8), anchor="w")
        
        # Input frame (to hold entry and validation icon)
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(fill="x")
        
        # Entry field
        self.entry = ctk.CTkEntry(
            self.input_frame,
            placeholder_text="https://youtube.com/watch?v=... or https://instagram.com/p/...",
            height=40,
            font=ctk.CTkFont(size=13)
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.entry.bind("<KeyRelease>", self._on_entry_change)
        
        # Validation indicator
        self.validation_label = ctk.CTkLabel(
            self.input_frame,
            text="",
            width=30,
            font=ctk.CTkFont(size=20)
        )
        self.validation_label.pack(side="right")
        
        # Error message label
        self.error_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=11),
            text_color="#e74c3c",
            wraplength=500
        )
        self.error_label.pack(pady=(4, 0), anchor="w")
        self.error_label.pack_forget()  # Hide initially
    
    def _on_entry_change(self, event=None):
        """Handle entry change event"""
        url = self.get_url()
        
        if not url:
            # Empty - hide validation
            self.validation_label.configure(text="")
            self.error_label.pack_forget()
            if self.on_change:
                self.on_change("", False)
            return
        
        # Validate URL
        is_valid, platform, error_msg = URLValidator.validate(url)
        
        if is_valid:
            self.validation_label.configure(text="✓", text_color="#2fa572")
            self.error_label.pack_forget()
        else:
            self.validation_label.configure(text="✗", text_color="#e74c3c")
            if error_msg:
                self.error_label.configure(text=error_msg)
                self.error_label.pack(pady=(4, 0), anchor="w")
        
        if self.on_change:
            self.on_change(url, is_valid)
    
    def get_url(self) -> str:
        """Get current URL from entry"""
        return self.entry.get().strip()
    
    def set_url(self, url: str):
        """Set URL in entry field"""
        self.entry.delete(0, END)
        self.entry.insert(0, url)
        self._on_entry_change()
    
    def clear(self):
        """Clear the entry field"""
        self.entry.delete(0, END)
        self.validation_label.configure(text="")
        self.error_label.pack_forget()
    
    def set_enabled(self, enabled: bool):
        """Enable or disable the input"""
        state = "normal" if enabled else "disabled"
        self.entry.configure(state=state)
