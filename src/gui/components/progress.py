"""Progress display component"""
import customtkinter as ctk
from ...utils.helpers import format_speed, format_eta


class ProgressDisplay(ctk.CTkFrame):
    """Download progress display with status updates"""
    
    def __init__(self, parent, **kwargs):
        """
        Initialize progress display component
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent, **kwargs)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            self,
            height=20,
            corner_radius=10
        )
        self.progress_bar.pack(fill="x", pady=(0, 8))
        self.progress_bar.set(0)
        
        # Stats frame (speed and ETA)
        self.stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 4))
        
        # Percentage label
        self.percentage_label = ctk.CTkLabel(
            self.stats_frame,
            text="0%",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.percentage_label.pack(side="left")
        
        # Speed label
        self.speed_label = ctk.CTkLabel(
            self.stats_frame,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.speed_label.pack(side="left", padx=(16, 0))
        
        # ETA label
        self.eta_label = ctk.CTkLabel(
            self.stats_frame,
            text="",
            font=ctk.CTkFont(size=12)
        )
        self.eta_label.pack(side="left", padx=(16, 0))
        
        # Status message
        self.status_label = ctk.CTkLabel(
            self,
            text="Ready to download",
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        self.status_label.pack(fill="x")
        
        self.hide()
    
    def update_progress(
        self,
        percentage: float,
        speed: float = 0,
        eta: float = None,
        status: str = ""
    ):
        """
        Update progress display
        
        Args:
            percentage: Progress percentage (0-100)
            speed: Download speed in bytes per second
            eta: Estimated time remaining in seconds
            status: Status message
        """
        # Update progress bar
        self.progress_bar.set(percentage / 100)
        
        # Update percentage
        self.percentage_label.configure(text=f"{int(percentage)}%")
        
        # Update speed
        if speed > 0:
            self.speed_label.configure(text=f"Speed: {format_speed(speed)}")
        else:
            self.speed_label.configure(text="")
        
        # Update ETA
        if eta is not None and eta > 0:
            self.eta_label.configure(text=f"ETA: {format_eta(eta)}")
        else:
            self.eta_label.configure(text="")
        
        # Update status
        if status:
            self.status_label.configure(text=status)
    
    def set_status(self, status: str, color: str = None):
        """
        Set status message with optional color
        
        Args:
            status: Status message
            color: Text color (optional)
        """
        self.status_label.configure(text=status)
        if color:
            self.status_label.configure(text_color=color)
    
    def show_success(self, message: str):
        """Show success message"""
        self.progress_bar.set(1.0)
        self.percentage_label.configure(text="100%")
        self.speed_label.configure(text="")
        self.eta_label.configure(text="")
        self.status_label.configure(text=message, text_color="#2fa572")
    
    def show_error(self, message: str):
        """Show error message"""
        self.progress_bar.set(0)
        self.percentage_label.configure(text="0%")
        self.speed_label.configure(text="")
        self.eta_label.configure(text="")
        self.status_label.configure(text=message, text_color="#e74c3c")
    
    def reset(self):
        """Reset progress display"""
        self.progress_bar.set(0)
        self.percentage_label.configure(text="0%")
        self.speed_label.configure(text="")
        self.eta_label.configure(text="")
        self.status_label.configure(text="Ready to download", text_color=("gray10", "gray90"))
    
    def show(self):
        """Show the progress display"""
        self.pack(fill="x", pady=(16, 0))
    
    def hide(self):
        """Hide the progress display"""
        self.pack_forget()
