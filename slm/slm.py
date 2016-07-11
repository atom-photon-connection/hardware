

import os
from ctypes import *
from scipy import misc
from time import sleep

# Load the DLL
slm_lib = CDLL("Blink_SDK_C")
path = os.path.dirname(__file__)

# Blink_SDK_C.h
#
# void* Create_SDK(unsigned int SLM_bit_depth, unsigned int SLM_resolution, unsigned int* n_boards_found, int *constructed_ok, int is_nematic_type, int RAM_write_enable, int use_GPU_if_available, int max_transient_frames, char* static_regional_lut_file);
slm_lib.Create_SDK.argtypes = (c_uint, c_uint, POINTER(c_uint), POINTER(c_bool), c_bool, c_bool, c_bool, c_uint, c_char_p)
slm_lib.Create_SDK.restype = c_void_p
# void Delete_SDK(void *sdk);
slm_lib.Delete_SDK.argtypes = (c_void_p,)
# const char* Get_last_error_message(void *sdk);
slm_lib.Get_last_error_message.argtypes = (c_void_p,)
slm_lib.Get_last_error_message.restype = c_char_p
# const char* Get_version_info(void *sdk);
slm_lib.Get_version_info.argtypes = (c_void_p,)
slm_lib.Get_version_info.restype = c_char_p
# int Load_linear_LUT(void *sdk, int board);
slm_lib.Load_linear_LUT.argtypes = (c_void_p, c_int)
slm_lib.Load_linear_LUT.restype = c_int
# int Load_LUT_file(void *sdk, int board, char* LUT_file);
slm_lib.Load_LUT_file.argtypes = (c_void_p, c_int, c_char_p)
slm_lib.Load_LUT_file.restype = c_int
# int Load_overdrive_LUT_file(void *sdk, char* static_regional_lut_file);
slm_lib.Load_overdrive_LUT_file.argtypes = (c_void_p, c_char_p)
slm_lib.Load_overdrive_LUT_file.restype = c_int
# void Set_true_frames(void *sdk, int true_frames);
slm_lib.Set_true_frames.argtypes = (c_void_p, c_int)
# void SLM_power(void *sdk, int power_state);
slm_lib.SLM_power.argtypes = (c_void_p, c_int)
# bool Write_cal_buffer(void *sdk, int board, const unsigned char* buffer);
slm_lib.Write_cal_buffer.argtypes = (c_void_p, c_int, POINTER(c_ubyte))
slm_lib.Write_cal_buffer.restype = c_int
# int Write_image(void *sdk, int board, unsigned char* image, unsigned int image_size, int wait_for_trigger, int external_pulse);
slm_lib.Write_image.argtypes = (c_void_p, c_int, POINTER(c_ubyte), c_uint, c_bool, c_bool)
slm_lib.Write_image.restype = c_int

# Basic parameters for calling Create_SDK
bit_depth           = 8
slm_resolution      = 512
num_boards_found    = c_uint()
constructed_okay    = c_bool()
is_nematic_type     = 1
RAM_write_enable    = 1
use_GPU             = 1
max_transients      = 20
true_frames         = 3
board               = 1

# OverDrive Plus parameters
lut_file = os.path.join(path, "slm3995_regional.txt")

sdk = slm_lib.Create_SDK(bit_depth, slm_resolution, byref(num_boards_found), 
                         byref(constructed_okay), is_nematic_type, 
                         RAM_write_enable, use_GPU, max_transients, lut_file)

if not constructed_okay:
    print "Blink SDK was not successfully constructed"
    print slm_lib.Get_last_error_message(sdk)
    slm_lib.Delete_SDK(sdk)
else:
    print "Blink SDK was successfully constructed"
    print "Found %s SLM controller(s)" % num_boards_found.value
    
    slm_lib.Load_linear_LUT(sdk, board)
    # When using Write_overdrive_image, you need to load the overdrive
    # LUT file "slm3995_regional.txt" and set the normal LUT to be linear.

def lut(filename=None):
    """Load a LUT (look-up table) file.
    
    Omitting the filename loads a linear look-up table.
    """
    if filename == None:
        slm_lib.Load_linear_LUT(sdk, board)
        print 'Loaded linear LUT'
    else:
        if slm_lib.Load_LUT_file(sdk, board, filename):
            print 'Loaded LUT file', filename
        else:
            print slm_lib.Get_last_error_message(sdk)

def show(image):
    """Display an image on the SLM.
    
    - image must be 512x512 ndarray with dtype=uint8
    """
    # int Write_image(void *sdk, int board, unsigned char* image, unsigned int image_size, int wait_for_trigger, int external_pulse);
    return slm_lib.Write_image(sdk, board, image.ctypes.data_as(POINTER(c_ubyte)), 512, 0, 0)

def overdrive(image):
    """Display an image on the SLM using Overdrive Plus.
    
    - image must be 512x512 ndarray with dtype=uint8
    - must be called with a linear look-up table
    """
    slm_lib.Write_overdrive_image(sdk, 1, image.ctypes.data_as(POINTER(c_ubyte)), 0, 0)

def kill():
    """Close the SLM library."""
    slm_lib.Delete_SDK(sdk)