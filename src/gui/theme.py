"""Custom theme configuration for CustomTkinter"""
import customtkinter as ctk


# Color schemes
LIGHT_THEME = {
    "primary": "#1f6aa5",
    "primary_hover": "#1a5a8e",
    "background": "#f5f5f5",
    "surface": "#ffffff",
    "text": "#1a1a1a",
    "text_secondary": "#666666",
    "success": "#2fa572",
    "error": "#e74c3c",
    "border": "#d0d0d0",
}

DARK_THEME = {
    "primary": "#3b8ed0",
    "primary_hover": "#4a9fd9",
    "background": "#1a1a1a",
    "surface": "#2b2b2b",
    "text": "#f5f5f5",
    "text_secondary": "#a0a0a0",
    "success": "#2fa572",
    "error": "#e74c3c",
    "border": "#3a3a3a",
}


def apply_theme(theme_name: str = "dark") -> None:
    """
    Apply theme to the application
    
    Args:
        theme_name: "dark" or "light"
    """
    ctk.set_appearance_mode(theme_name)
    
    # Set color theme
    if theme_name == "dark":
        ctk.set_default_color_theme("blue")
    else:
        ctk.set_default_color_theme("blue")


def get_theme_colors(theme_name: str = "dark") -> dict:
    """
    Get color dictionary for current theme
    
    Args:
        theme_name: "dark" or "light"
        
    Returns:
        Dictionary of theme colors
    """
    return DARK_THEME if theme_name == "dark" else LIGHT_THEME
