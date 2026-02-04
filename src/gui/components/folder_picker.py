"""Folder picker component for output directory selection"""
import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path
from typing import Callable, Optional
from ...utils.helpers import truncate_path


class FolderPicker(ctk.CTkFrame):
    """Output folder selection component"""
    
    def __init__(
        self,
        parent,
        default_folder: Path,
        on_folder_change: Optional[Callable[[Path], None]] = None,
        **kwargs
    ):
        """
        Initialize folder picker component
        
        Args:
            parent: Parent widget
            default_folder: Default folder path
            on_folder_change: Callback when folder changes
        """
        super().__init__(parent, **kwargs)
        self.current_folder = default_folder
        self.on_folder_change = on_folder_change
        
        # Label
        self.label = ctk.CTkLabel(
            self,
            text="Save to:",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label.pack(pady=(0, 8), anchor="w")
        
        # Folder display and button frame
        self.folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.folder_frame.pack(fill="x")
        
        # Folder path display
        self.path_label = ctk.CTkLabel(
            self.folder_frame,
            text=str(default_folder),
            font=ctk.CTkFont(size=12),
            anchor="w",
            fg_color=("gray85", "gray25"),
            corner_radius=6,
            padx=12,
            pady=10
        )
        self.path_label.pack(side="left", fill="x", expand=True, padx=(0, 8))
        
        # Browse button
        self.browse_button = ctk.CTkButton(
            self.folder_frame,
            text="Browse",
            command=self._browse_folder,
            width=100,
            height=35,
            font=ctk.CTkFont(size=13)
        )
        self.browse_button.pack(side="right")
        
        # Update display
        self._update_display()
    
    def _browse_folder(self):
        """Open folder selection dialog"""
        folder = filedialog.askdirectory(
            title="Select Download Folder",
            initialdir=str(self.current_folder)
        )
        
        if folder:
            self.set_folder(Path(folder))
    
    def _update_display(self):
        """Update the folder path display"""
        # Truncate long paths
        display_path = str(self.current_folder)
        if len(display_path) > 50:
            display_path = truncate_path(display_path, 50)
        
        self.path_label.configure(text=display_path)
        
        # Set tooltip with full path
        self._set_tooltip(str(self.current_folder))
    
    def _set_tooltip(self, text: str):
        """Set tooltip text (simplified - full path on hover would need additional library)"""
        # For now, just ensure full path is accessible
        # Could be enhanced with a proper tooltip library
        pass
    
    def get_folder(self) -> Path:
        """Get current folder path"""
        return self.current_folder
    
    def set_folder(self, folder: Path):
        """Set folder path"""
        self.current_folder = folder
        self._update_display()
        
        if self.on_folder_change:
            self.on_folder_change(folder)
    
    def set_enabled(self, enabled: bool):
        """Enable or disable the browse button"""
        state = "normal" if enabled else "disabled"
        self.browse_button.configure(state=state)
