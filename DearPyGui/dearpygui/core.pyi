from typing import List, Any, Callable
from dearpygui.core import *

##########################################################
# This file is generated automatically by mvPythonParser #
##########################################################

# ~ Dear PyGui Version: master
def add_2d_histogram_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, xbins: int =-1, ybins: int =-1, xmin_range: float =0.0, xmax_range: float =1.0, ymin_range: float =0.0, ymax_range: float =1.0, density: bool =False, outliers: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_3d_slider(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[float] =(0.0, 0.0, 0.0, 0.0), max_x: float =100.0, max_y: float =100.0, max_z: float =100.0, min_x: float =0.0, min_y: float =0.0, min_z: float =0.0, scale: float =1.0) -> str:
	"""Undocumented function"""
	...

def add_activated_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_active_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_area_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, fill: List[int] =(0, 0, 0, -255), contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_bar_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, weight: float =1.0, horizontal: bool =False, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_button(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, small: bool =False, arrow: bool =False, direction: int =0) -> str:
	"""Undocumented function"""
	...

def add_candle_series(dates : List[float], opens : List[float], closes : List[float], lows : List[float], highs : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, bull_color: List[int] =(0, 255, 113, 255), bear_color: List[int] =(218, 13, 79, 255), weight: int =0.25, contribute_to_bounds: bool =True, tooltip: bool =True) -> str:
	"""Undocumented function"""
	...

def add_checkbox(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: bool =False) -> str:
	"""Undocumented function"""
	...

def add_child(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, border: bool =True, autosize_x: bool =False, autosize_y: bool =False, no_scrollbar: bool =False, horizontal_scrollbar: bool =False, menubar: bool =False) -> str:
	"""Undocumented function"""
	...

def add_clicked_handler(parent : str, button : int, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_clipper(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_collapsing_header(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, closable: bool =False, default_open: bool =False, open_on_double_click: bool =False, open_on_arrow: bool =False, leaf: bool =False, bullet: bool =False) -> str:
	"""Undocumented function"""
	...

def add_color_button(default_value : List[int] =(0, 0, 0, 255), *, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, no_alpha: bool =False, no_border: bool =False, no_drag_drop: bool =False) -> str:
	"""Undocumented function"""
	...

def add_color_edit(default_value : List[int] =(0, 0, 0, 255), *, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, no_alpha: bool =False, no_picker: bool =False, no_options: bool =False, no_small_preview: bool =False, no_inputs: bool =False, no_tooltip: bool =False, no_label: bool =False, no_drag_drop: bool =False, alpha_bar: bool =False, alpha_preview: bool =False, alpha_preview_half: bool =False, display_rgb: bool =False, display_hsv: bool =False, display_hex: bool =False, uint8: bool =False, floats: bool =False, input_rgb: bool =False, input_hsv: bool =False, m_3component: bool =False) -> str:
	"""Undocumented function"""
	...

def add_color_picker(default_value : List[int] =(0, 0, 0, 255), *, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, no_alpha: bool =False, no_picker: bool =False, no_side_preview: bool =False, no_small_preview: bool =False, no_inputs: bool =False, no_tooltip: bool =False, no_label: bool =False, alpha_bar: bool =False, alpha_preview: bool =False, alpha_preview_half: bool =False, display_rgb: bool =False, display_hsv: bool =False, display_hex: bool =False, uint8: bool =False, floats: bool =False, input_rgb: bool =False, input_hsv: bool =False, picker_hue_bar: bool =False, picker_hue_wheel: bool =False) -> str:
	"""Undocumented function"""
	...

def add_colormap_scale(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, pos: List[int] =[], default_value: int =0, min_scale: float =0.0, max_scale: float =1.0) -> str:
	"""Undocumented function"""
	...

def add_combo(items : List[str] =(), *, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: str ='', popup_align_left: bool =False, height_small: bool =False, height_regular: bool =False, height_large: bool =False, height_largest: bool =False, no_arrow_button: bool =False, no_preview: bool =False) -> str:
	"""Undocumented function"""
	...

def add_date_picker(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: dict ={'month_day': 14, 'year':20, 'month':5}, level: int =0) -> str:
	"""Undocumented function"""
	...

def add_deactivated_after_edit_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_deactivated_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_drag_float(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: float =0.0, size: int =4, format: str ='%0.3f', speed: float =1.0, min_value: float =0.0, max_value: float =100.0, no_input: bool =False, clamped: bool =False) -> str:
	"""Undocumented function"""
	...

def add_drag_floatx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[float] =(0.0, 0.0, 0.0, 0.0), size: int =4, format: str ='%0.3f', speed: float =1.0, min_value: float =0.0, max_value: float =100.0, no_input: bool =False, clamped: bool =False) -> str:
	"""Undocumented function"""
	...

def add_drag_int(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: int =0, size: int =4, format: str ='%d', speed: float =1.0, min_value: int =0, max_value: int =100, no_input: bool =False, clamped: bool =False) -> str:
	"""Undocumented function"""
	...

def add_drag_intx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[int] =(0, 0, 0, 0), size: int =4, format: str ='%d', speed: float =1.0, min_value: int =0, max_value: int =100, no_input: bool =False, clamped: bool =False) -> str:
	"""Undocumented function"""
	...

def add_drag_line(*, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', callback: Callable =None, show: bool =True, default_value: Any =(0.0, 0.0, 0.0, 0.0), color: List[int] =(0, 0, 0, -255), thickness: float =1.0, show_label: bool =True, vertical: bool =True) -> str:
	"""Undocumented function"""
	...

def add_drag_payload(*, id: str =..., parent: str ='', show: bool =True, drag_data: Any =None, payload_type: str ='$$DPG_PAYLOAD') -> str:
	"""Undocumented function"""
	...

def add_drag_point(*, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', callback: Callable =None, show: bool =True, default_value: Any =(0.0, 0.0, 0.0, 0.0), color: List[int] =(0, 0, 0, -255), thickness: float =1.0, show_label: bool =True) -> str:
	"""Undocumented function"""
	...

def add_draw_layer(*, id: str =..., parent: str ='', before: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_drawlist(*, id: str =..., width: int =0, height: int =0, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5) -> str:
	"""Undocumented function"""
	...

def add_dummy(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', show: bool =True, pos: List[int] =[]) -> str:
	"""Undocumented function"""
	...

def add_dynamic_texture(width : int, height : int, default_value : List[float], *, id: str =..., parent: str ='') -> str:
	"""Undocumented function"""
	...

def add_edited_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_error_series(x : List[float], y : List[float], negative : List[float], positive : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True, horizontal: bool =False) -> str:
	"""Undocumented function"""
	...

def add_file_dialog(*, id: str =..., width: int =0, height: int =0, label: str ='', callback: Callable =None, show: bool =True, default_path: str ='', default_filename: str ='.', file_count: int =0, modal: bool =False, directory_selector: bool =False) -> str:
	"""Undocumented function"""
	...

def add_file_extension(extension : str, *, id: str =..., width: int =0, height: int =0, parent: str ='', before: str ='', label: str ='', custom_text: str ='', color: List[float] =(-255, 0, 0, 255)) -> str:
	"""Undocumented function"""
	...

def add_filter_set(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_focus_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_font(font : str, file : str, size : float, glyph_ranges : str ='', *, custom_glyph_chars: List[int] =[], custom_glyph_ranges: Any =[[]], char_remaps: Any =[[]]) -> None:
	"""Undocumented function"""
	...

def add_group(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, horizontal: bool =False, horizontal_spacing: float =-1) -> str:
	"""Undocumented function"""
	...

def add_handler_registry(*, id: str =..., show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_heat_series(x : List[float], rows : int, cols : int, *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, scale_min: float =0.0, scale_max: float =1.0, bounds_min: Any =(0.0, 0.0), bounds_max: Any =(1.0, 1.0), format: str ='%0.1f', contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_histogram_series(x : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, bins: int =-1, bar_scale: float =1.0, min_range: float =0.0, max_range: float =1.0, cumlative: bool =False, density: bool =False, outliers: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_hline_series(x : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_hover_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_image(default_value : str, *, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, tint_color: List[float] =(255, 255, 255, 255), border_color: List[float] =(0, 0, 0, 0), uv_min: List[float] =(0.0, 0.0), uv_max: List[float] =(1.0, 1.0)) -> str:
	"""Undocumented function"""
	...

def add_image_button(default_value : str, *, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, frame_padding: int =-1, tint_color: List[float] =(255, 255, 255, 255), background_color: List[float] =(0, 0, 0, 0), uv_min: List[float] =(0.0, 0.0), uv_max: List[float] =(1.0, 1.0)) -> str:
	"""Undocumented function"""
	...

def add_image_series(value : str, bounds_min : List[float], bounds_max : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, uv_min: List[float] =(0.0, 0.0), uv_max: List[float] =(1.0, 1.0), tint_color: List[int] =(255, 255, 255, 255), contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_input_float(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: float =0.0, format: str ='%.3f', min_value: float =0.0, max_value: float =100.0, step: float =0.1, step_fast: float =1.0, size: int =4, min_clamped: bool =False, max_clamped: bool =False, on_enter: bool =False, readonly: bool =False) -> str:
	"""Undocumented function"""
	...

def add_input_floatx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[float] =(0.0, 0.0, 0.0, 0.0), format: str ='%.3f', min_value: float =0.0, max_value: float =100.0, size: int =4, min_clamped: bool =False, max_clamped: bool =False, on_enter: bool =False, readonly: bool =False) -> str:
	"""Undocumented function"""
	...

def add_input_int(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[int] =(0, 0, 0, 0), min_value: int =0, max_value: int =100, size: int =4, step: int =1, step_fast: int =100, min_clamped: bool =False, max_clamped: bool =False, on_enter: bool =False, readonly: bool =False) -> str:
	"""Undocumented function"""
	...

def add_input_intx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[int] =(0, 0, 0, 0), min_value: int =0, max_value: int =100, size: int =4, min_clamped: bool =False, max_clamped: bool =False, on_enter: bool =False, readonly: bool =False) -> str:
	"""Undocumented function"""
	...

def add_input_text(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: str ='', hint: str ='', multiline: bool =False, no_spaces: bool =False, uppercase: bool =False, tab_input: bool =False, decimal: bool =False, hexadecimal: bool =False, readonly: bool =False, password: bool =False, scientific: bool =False, on_enter: bool =False) -> str:
	"""Undocumented function"""
	...

def add_key_down_handler(key : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_key_press_handler(key : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_key_release_handler(key : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_knob_float(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: float =0.0, min_value: float =0.0, max_value: float =100.0) -> str:
	"""Undocumented function"""
	...

def add_line_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_listbox(items : List[str] =(), *, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: str ='', num_items: int =3) -> str:
	"""Undocumented function"""
	...

def add_loading_indicator(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', show: bool =True, pos: List[int] =[], style: int =0) -> str:
	"""Undocumented function"""
	...

def add_menu(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, enabled: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5) -> str:
	"""Undocumented function"""
	...

def add_menu_bar(*, id: str =..., indent: int =-1, parent: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_menu_item(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: bool =False, shortcut: str ='', check: bool =False) -> str:
	"""Undocumented function"""
	...

def add_mouse_click_handler(button : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_double_click_handler(button : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_down_handler(button : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_drag_handler(button : int, threshold : float, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_move_handler(*, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_release_handler(button : int, *, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_mouse_wheel_handler(*, id: str =..., parent: str ='', callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_node(*, id: str =..., parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, draggable: bool =True) -> str:
	"""Undocumented function"""
	...

def add_node_attribute(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, output: bool =False, static: bool =False, shape: int =54010) -> str:
	"""Undocumented function"""
	...

def add_node_editor(*, id: str =..., parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, delink_callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_node_link(node_1 : str, node_2 : str, *, id: str =..., parent: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_pie_series(x : float, y : float, radius : float, values : List[float], labels : List[str], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, format: str ='%0.2f', angle: float =90.0, normalize: bool =False, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_plot(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, query_callback: Callable =None, x_axis_name: str ='', no_title: bool =False, no_menus: bool =False, no_box_select: bool =False, no_mouse_pos: bool =False, no_highlight: bool =False, no_child: bool =False, query: bool =False, crosshairs: bool =False, anti_aliased: bool =False, equal_aspects: bool =False, xaxis_no_gridlines: bool =False, xaxis_no_tick_marks: bool =False, xaxis_no_tick_labels: bool =False, xaxis_log_scale: bool =False, xaxis_time: bool =False, xaxis_invert: bool =False, xaxis_lock_min: bool =False, xaxis_lock_max: bool =False) -> str:
	"""Undocumented function"""
	...

def add_plot_annotation(*, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, default_value: Any =(0.0, 0.0), offset: List[float] =(0.0, 0.0), color: List[int] =(0, 0, 0, -255), clamped: bool =True) -> str:
	"""Undocumented function"""
	...

def add_plot_legend(*, id: str =..., parent: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_plot_yaxis(*, id: str =..., parent: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, yaxis_no_gridlines: bool =False, yaxis_no_tick_marks: bool =False, yaxis_no_tick_labels: bool =False, yaxis_log_scale: bool =False, yaxis_invert: bool =False, yaxis_lock_min: bool =False, yaxis_lock_max: bool =False) -> str:
	"""Undocumented function"""
	...

def add_popup(*, id: str =..., width: int =0, height: int =0, parent: str ='', show: bool =True, pos: List[int] =[], mousebutton: int =1, modal: bool =False) -> str:
	"""Undocumented function"""
	...

def add_progress_bar(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, overlay: str ='', default_value: float =0.0) -> str:
	"""Undocumented function"""
	...

def add_radio_button(items : int =(), *, id: str =..., indent: int =-1, parent: str ='', before: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: str ='', horizontal: bool =False) -> str:
	"""Undocumented function"""
	...

def add_same_line(*, id: str =..., parent: str ='', before: str ='', show: bool =True, xoffset: float =0.0, spacing: float =-1.0) -> str:
	"""Undocumented function"""
	...

def add_scatter_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_selectable(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: bool =False, span_columns: bool =False) -> str:
	"""Undocumented function"""
	...

def add_separator(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', show: bool =True, pos: List[int] =[]) -> str:
	"""Undocumented function"""
	...

def add_shade_series(x : List[float], y1 : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, y2: Any =[], contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_simple_plot(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[float] =(), overlay: str ='', histogram: bool =False, autosize: bool =True, min_scale: float =0.0, max_scale: float =0.0) -> str:
	"""Undocumented function"""
	...

def add_slider_float(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: float =0.0, size: int =4, vertical: bool =False, no_input: bool =False, clamped: bool =False, min_value: float =0.0, max_value: float =100.0, format: str ='%.3f') -> str:
	"""Undocumented function"""
	...

def add_slider_floatx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[float] =(0.0, 0.0, 0.0, 0.0), size: int =4, no_input: bool =False, clamped: bool =False, min_value: float =0.0, max_value: float =100.0, format: str ='%.3f') -> str:
	"""Undocumented function"""
	...

def add_slider_int(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: int =0, size: int =4, vertical: bool =False, no_input: bool =False, clamped: bool =False, min_value: int =0, max_value: int =100, format: str ='%d') -> str:
	"""Undocumented function"""
	...

def add_slider_intx(*, id: str =..., width: int =0, indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, enabled: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: List[int] =(0, 0, 0, 0), size: int =4, no_input: bool =False, clamped: bool =False, min_value: int =0, max_value: int =100, format: str ='%d') -> str:
	"""Undocumented function"""
	...

def add_spacing(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', show: bool =True, pos: List[int] =[], count: int =1) -> str:
	"""Undocumented function"""
	...

def add_staging_container(*, id: str =...) -> str:
	"""Undocumented function"""
	...

def add_stair_series(x : List[float], y : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_static_texture(width : int, height : int, default_value : List[float], *, id: str =..., parent: str ='', file: str ='') -> str:
	"""Undocumented function"""
	...

def add_stem_series(x : List[float], y : List[float], *, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_tab(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, closable: bool =False, no_reorder: bool =False, leading: bool =False, trailing: bool =False, no_tooltip: bool =False) -> str:
	"""Undocumented function"""
	...

def add_tab_bar(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, reorderable: bool =False) -> str:
	"""Undocumented function"""
	...

def add_tab_button(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, filter_key: str ='', tracked: bool =False, track_offset: float =0.5, no_reorder: bool =False, leading: bool =False, trailing: bool =False, no_tooltip: bool =False) -> str:
	"""Undocumented function"""
	...

def add_table(*, id: str =..., width: int =0, height: int =0, indent: int =-1, parent: str ='', before: str ='', source: str ='', callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', header_row: bool =True, inner_width: int =0, policy: int =0, freeze_rows: int =0, freeze_columns: int =0, sort_multi: bool =False, sort_tristate: bool =False, resizable: bool =False, reorderable: bool =False, hideable: bool =False, sortable: bool =False, context_menu_in_body: bool =False, row_background: bool =False, borders_innerH: bool =False, borders_outerH: bool =False, borders_innerV: bool =False, borders_outerV: bool =False, no_host_extendX: bool =False, no_host_extendY: bool =False, no_keep_columns_visible: bool =False, precise_widths: bool =False, no_clip: bool =False, pad_outerX: bool =False, no_pad_outerX: bool =False, no_pad_innerX: bool =False, scrollX: bool =False, scrollY: bool =False) -> str:
	"""Undocumented function"""
	...

def add_table_column(*, id: str =..., parent: str ='', before: str ='', show: bool =True, init_width_or_weight: bool =0.0, default_hide: bool =False, default_sort: bool =False, width_stretch: bool =False, width_fixed: bool =False, no_resize: bool =False, no_reorder: bool =False, no_hide: bool =False, no_clip: bool =False, no_sort: bool =False, no_sort_ascending: bool =False, no_sort_descending: bool =False, no_header_width: bool =False, prefer_sort_ascending: bool =False, prefer_sort_descending: bool =False, indent_enable: bool =False, indent_disable: bool =False) -> str:
	"""Undocumented function"""
	...

def add_table_next_column(*, id: str =..., parent: str ='', before: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_table_row(*, id: str =..., parent: str ='', before: str ='', show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_text(default_value : str ='', *, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', source: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, wrap: int =-1, bullet: bool =False, color: List[float] =(-1, -1, -1, -1), show_label: bool =False) -> str:
	"""Undocumented function"""
	...

def add_text_point(x : float, y : float, *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, x_offset: int =..., y_offset: int =..., contribute_to_bounds: bool =True, vertical: bool =False) -> str:
	"""Undocumented function"""
	...

def add_texture_container(*, id: str =..., show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_time_picker(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', payload_type: str ='$$DPG_PAYLOAD', callback: Callable =None, drag_callback: Callable =None, user_data: Any =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_value: dict ={'hour': 14, 'min': 32, 'sec': 23}, hour24: bool =False) -> str:
	"""Undocumented function"""
	...

def add_toggled_open_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_tooltip(*, id: str =..., show: bool =True) -> str:
	"""Undocumented function"""
	...

def add_tree_node(*, id: str =..., indent: int =-1, parent: str ='', before: str ='', label: str ='', payload_type: str ='$$DPG_PAYLOAD', drag_callback: Callable =None, show: bool =True, pos: List[int] =[], filter_key: str ='', tracked: bool =False, track_offset: float =0.5, default_open: bool =False, open_on_double_click: bool =False, open_on_arrow: bool =False, leaf: bool =False, bullet: bool =False, selectable: bool =False) -> str:
	"""Undocumented function"""
	...

def add_viewport_drawlist(*, id: str =..., show: bool =True, filter_key: str ='', front: bool =True) -> str:
	"""Undocumented function"""
	...

def add_visible_handler(parent : str, *, id: str =..., callback: Callable =None) -> str:
	"""Undocumented function"""
	...

def add_vline_series(x : List[float], *, id: str =..., parent: str ='', before: str ='', label: str ='', source: str ='', show: bool =True, contribute_to_bounds: bool =True) -> str:
	"""Undocumented function"""
	...

def add_window(*, id: str =..., width: int =0, height: int =0, indent: int =-1, label: str ='', show: bool =True, min_size: List[int] =[32, 32], max_size: List[int] =[30000, 30000], menubar: bool =False, collapsed: bool =False, autosize: bool =False, no_resize: bool =False, no_title_bar: bool =False, no_move: bool =False, no_scrollbar: bool =False, no_collapse: bool =False, horizontal_scrollbar: bool =False, no_focus_on_appearing: bool =False, no_bring_to_front_on_focus: bool =False, no_close: bool =False, no_background: bool =False, modal: bool =False, popup: bool =False, on_close: Callable =None) -> str:
	"""Undocumented function"""
	...

def cleanup_dearpygui() -> None:
	"""Undocumented function"""
	...

def clear_selected_links(node_editor : str) -> None:
	"""Undocumented function"""
	...

def clear_selected_nodes(node_editor : str) -> None:
	"""Undocumented function"""
	...

def close_popup(item : str) -> None:
	"""Undocumented function"""
	...

def configure_item(item : str, **kwargs) -> None:
	"""Undocumented function"""
	...

def configure_viewport() -> None:
	"""Undocumented function"""
	...

def create_viewport(*, title: str ='Dear PyGui', small_icon: str ='', large_icon: str ='', width: str =1280, height: str =800, x_pos: str =100, y_pos: str =100, min_width: str =250, max_width: str =10000, min_height: str =250, max_height: str =10000, resizable: bool =True, vsync: bool =True, always_on_top: bool =False, maximized_box: bool =True, minimized_box: bool =True, border: bool =True, caption: bool =True, overlapped: bool =True, clear_color: List[float] =(0, 0, 0, 255)) -> str:
	"""Undocumented function"""
	...

def delete_item(item : str, *, children_only: bool =False) -> None:
	"""Undocumented function"""
	...

def does_item_exist(item : str) -> bool:
	"""Undocumented function"""
	...

def draw_arrow(p1 : List[float], p2 : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), thickness: float =1.0, size: int =4) -> str:
	"""Undocumented function"""
	...

def draw_bezier_curve(p1 : List[float], p2 : List[float], p3 : List[float], p4 : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), thickness: float =1.0, size: int =4, segments: int =0) -> str:
	"""Undocumented function"""
	...

def draw_circle(center : List[float], radius : float, *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), thickness: float =1.0, segments: int =0) -> str:
	"""Undocumented function"""
	...

def draw_ellipse(pmin : List[float], pmax : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), thickness: float =1.0, segments: int =3) -> str:
	"""Undocumented function"""
	...

def draw_image(file : str, pmin : List[float], pmax : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, uv_min: List[float] =(0.0, 0.0), uv_max: List[float] =(1.0, 1.0), color: List[int] =(255, 255, 255, 255)) -> str:
	"""Undocumented function"""
	...

def draw_line(p1 : List[float], p2 : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def draw_polygon(points : List[List[float]], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def draw_polyline(points : List[List[float]], *, id: str =..., parent: str ='', before: str ='', show: bool =True, closed: bool =False, color: List[int] =(255, 255, 255, 255), thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def draw_quad(p1 : List[float], p2 : List[float], p3 : List[float], p4 : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def draw_rectangle(pmin : List[float], pmax : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), rounding: float =0.0, thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def draw_text(pos : List[float], text : str, *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), size: int =10) -> str:
	"""Undocumented function"""
	...

def draw_triangle(p1 : List[float], p2 : List[float], p3 : List[float], *, id: str =..., parent: str ='', before: str ='', show: bool =True, color: List[int] =(255, 255, 255, 255), fill: List[int] =(0, 0, 0, -255), thickness: float =1.0) -> str:
	"""Undocumented function"""
	...

def empty_container_stack() -> str:
	"""Undocumented function"""
	...

def enable_docking(*, dock_space: bool =False) -> None:
	"""Undocumented function"""
	...

def focus_item(item : str) -> None:
	"""Undocumented function"""
	...

def get_active_window() -> str:
	"""Undocumented function"""
	...

def get_all_items() -> List[str]:
	"""Undocumented function"""
	...

def get_dearpygui_version() -> str:
	"""Undocumented function"""
	...

def get_delta_time() -> float:
	"""Undocumented function"""
	...

def get_drawing_mouse_pos() -> List[int]:
	"""Undocumented function"""
	...

def get_file_dialog_info(file_dialog : str) -> dict:
	"""Undocumented function"""
	...

def get_global_font_scale() -> float:
	"""Undocumented function"""
	...

def get_item_configuration(item : str) -> dict:
	"""Undocumented function"""
	...

def get_item_info(item : str) -> dict:
	"""Undocumented function"""
	...

def get_item_state(item : str) -> dict:
	"""Undocumented function"""
	...

def get_links(node_editor : str) -> List[List[str]]:
	"""Undocumented function"""
	...

def get_mouse_drag_delta() -> float:
	"""Undocumented function"""
	...

def get_mouse_pos(*, local: bool =True) -> List[int]:
	"""Undocumented function"""
	...

def get_plot_mouse_pos() -> List[int]:
	"""Undocumented function"""
	...

def get_plot_query_area(plot : str) -> List[float]:
	"""Undocumented function"""
	...

def get_plot_xlimits(plot : str) -> List[float]:
	"""Undocumented function"""
	...

def get_plot_ylimits(plot : str) -> List[float]:
	"""Undocumented function"""
	...

def get_selected_links(node_editor : str) -> List[List[str]]:
	"""Undocumented function"""
	...

def get_selected_nodes(node_editor : str) -> List[str]:
	"""Undocumented function"""
	...

def get_total_time() -> float:
	"""Undocumented function"""
	...

def get_value(item : str) -> Any:
	"""Undocumented function"""
	...

def get_values(items : List[str]) -> Any:
	"""Undocumented function"""
	...

def get_windows() -> List[str]:
	"""Undocumented function"""
	...

def get_x_scroll(item : str) -> float:
	"""Undocumented function"""
	...

def get_x_scroll_max(item : str) -> float:
	"""Undocumented function"""
	...

def get_y_scroll(item : str) -> float:
	"""Undocumented function"""
	...

def get_y_scroll_max(item : str) -> float:
	"""Undocumented function"""
	...

def is_dearpygui_running() -> bool:
	"""Undocumented function"""
	...

def is_key_down() -> bool:
	"""Undocumented function"""
	...

def is_key_pressed() -> bool:
	"""Undocumented function"""
	...

def is_key_released() -> bool:
	"""Undocumented function"""
	...

def is_mouse_button_clicked(button : int) -> bool:
	"""Undocumented function"""
	...

def is_mouse_button_double_clicked(button : int) -> bool:
	"""Undocumented function"""
	...

def is_mouse_button_down(button : int) -> bool:
	"""Undocumented function"""
	...

def is_mouse_button_dragging(button : int, threshold : float) -> bool:
	"""Undocumented function"""
	...

def is_mouse_button_released(button : int) -> bool:
	"""Undocumented function"""
	...

def is_plot_queried(plot : str) -> bool:
	"""Undocumented function"""
	...

def maximize_viewport() -> None:
	"""Undocumented function"""
	...

def minimize_viewport() -> None:
	"""Undocumented function"""
	...

def move_item(item : str, *, parent: str ='', before: str ='') -> None:
	"""Undocumented function"""
	...

def move_item_down(item : str) -> None:
	"""Undocumented function"""
	...

def move_item_up(item : str) -> None:
	"""Undocumented function"""
	...

def pop_container_stack() -> str:
	"""Undocumented function"""
	...

def push_container_stack(item : str) -> bool:
	"""Undocumented function"""
	...

def render_dearpygui_frame() -> None:
	"""Undocumented function"""
	...

def reorder_items(container : str, slot : int, new_order : List[str]) -> None:
	"""Undocumented function"""
	...

def reset_pos(item : str) -> None:
	"""Undocumented function"""
	...

def reset_xticks(plot : str) -> None:
	"""Undocumented function"""
	...

def reset_yticks(plot : str) -> None:
	"""Undocumented function"""
	...

def set_exit_callback(callback : Callable) -> str:
	"""Undocumented function"""
	...

def set_font(font : str, size : float, *, item: str ='') -> None:
	"""Undocumented function"""
	...

def set_global_font_scale(scale : float) -> None:
	"""Undocumented function"""
	...

def set_item_pos(item : str, x : float, y : float) -> None:
	"""Undocumented function"""
	...

def set_plot_xlimits(plot : str, xmin : float, xmax : float) -> None:
	"""Undocumented function"""
	...

def set_plot_xlimits_auto(plot : str) -> None:
	"""Undocumented function"""
	...

def set_plot_ylimits(plot : str, ymin : float, ymax : float) -> None:
	"""Undocumented function"""
	...

def set_primary_window(window : str, value : bool) -> None:
	"""Undocumented function"""
	...

def set_resize_callback(callback : Callable, *, handler: str ='') -> str:
	"""Undocumented function"""
	...

def set_staging_mode(mode : bool) -> None:
	"""Undocumented function"""
	...

def set_start_callback(callback : Callable) -> str:
	"""Undocumented function"""
	...

def set_theme_color(constant : int, color : List[float], *, item: str ='') -> str:
	"""Undocumented function"""
	...

def set_theme_color_disabled(constant : int, color : List[float], *, item: str ='') -> str:
	"""Undocumented function"""
	...

def set_theme_style(constant : int, style : float, *, item: str ='') -> str:
	"""Undocumented function"""
	...

def set_value(item : str, value : Any) -> None:
	"""Undocumented function"""
	...

def set_x_scroll(item : str, value : float) -> None:
	"""Undocumented function"""
	...

def set_xticks(plot : str, label_pairs : Any) -> None:
	"""Undocumented function"""
	...

def set_y_scroll(item : str, value : float) -> None:
	"""Undocumented function"""
	...

def set_yticks(plot : str, label_pairs : Any) -> None:
	"""Undocumented function"""
	...

def setup_dearpygui(*, viewport: str ='') -> None:
	"""Undocumented function"""
	...

def show_tool(tool : str) -> str:
	"""Undocumented function"""
	...

def show_viewport(viewport : str, *, minimized: bool =False, maximized: bool =False) -> None:
	"""Undocumented function"""
	...

def stage_items(items : List[str]) -> None:
	"""Undocumented function"""
	...

def stop_dearpygui() -> None:
	"""Undocumented function"""
	...

def top_container_stack() -> str:
	"""Undocumented function"""
	...

def unstage_items(items : List[str]) -> None:
	"""Undocumented function"""
	...

