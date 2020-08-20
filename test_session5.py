import inspect
import os
import re

import pytest

import session5

README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"
        
def test_neg_zero_repeat_time_it():
    with pytest.raises(ValueError) as e_info:
         session5.time_it(print, 'a', 'b', 'c', sep='-', end= ' ***\n', repetitions=0)  
    with pytest.raises(ValueError) as e_info:
         session5.time_it(print, 'a', 'b', 'c', sep='-', end= ' ***\n', repetitions=-1)  
         
def test_any_args_print():
    output, avg_time = session5.time_it(print, 'a', 'b', 'c', 'd', sep='-', end= ' ***\n', repetitions=100)
    assert avg_time > 0, 'Average time should be > 0'    
    
def test_any_kwargs_print():
    output, avg_time = session5.time_it(print, 'a', 'b', 'c', 'd', sep='-', xyz='anil', end= ' ***\n', repetitions=100)
    assert avg_time > 0, 'Average time should be > 0'        

def test_pos_number_squared():
    output, avg_time = session5.time_it(squared_power_list, 2, start=0, end=5, repetitons=100) 
    assert output == [1, 2, 4, 8, 16], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'

def test_neg_number_squared():
    output, avg_time = session5.time_it(squared_power_list, -2, start=0, end=5, repetitons=100) 
    assert output == [1, -2, 4, -8, 16], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'    

def test_zero_squared():
    output, avg_time = session5.time_it(squared_power_list, 0, start=0, end=5, repetitons=100) 
    assert output == [1, 0, 0, 0, 0], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'  

def test_pos_decimal_squared():
    output, avg_time = session5.time_it(squared_power_list, 1.5, start=0, end=5, repetitons=100) 
    assert output == [1.0, 1.5, 2.25, 3.375, 5.0625], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'

def test_neg_decimal_squared():
    output, avg_time = session5.time_it(squared_power_list, -1.5, start=0, end=5, repetitons=100) 
    assert output == [1.0, -1.5, 2.25, -3.375, 5.0625], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'    
             
def test_same_start_end_squared():
    with pytest.raises(ValueError) as e_info:
         session5.time_it(squared_power_list, 1.5, start=2,end=2,repetitions=1000)
         
def test_start_lt_end_squared():
    with pytest.raises(ValueError) as e_info:
         session5.time_it(squared_power_list, 1.5, start=-2,end=2,repetitions=1000)  

def test_neg_start_squared():
    output, avg_time = session5.time_it(squared_power_list, 2, start=-2,end=2,repetitions=1000)
    assert output == [0.25, 0.5, 1, 2], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'  

def test_neg_start_end_squared():
    output, avg_time = session5.time_it(squared_power_list, 2, start=-2,end=-1,repetitions=1000)
    assert output == [0.25], 'Square List incorrect'
    assert avg_time > 0, 'Average time should be > 0'  

def test_invalid_sides_polygon():
    with pytest.raises(ValueError) as e_info:
         session5.time_it(polygon_area, 4, sides=-5,repetitions=100000)
    with pytest.raises(ValueError) as e_info:
         session5.time_it(polygon_area, 4, sides=0,repetitions=100000)
    with pytest.raises(ValueError) as e_info:
         session5.time_it(polygon_area, 4, sides=8,repetitions=100000)     

def test_triangle_polygon():
    output, avg_time = session5.time_it(polygon_area, 4, sides=3,repetitions=1000)
    assert round(output,2) == 6.93, 'Incorrect Area'
    assert avg_time > 0, 'Average time should be > 0'          
 
def test_square_polygon():
    output, avg_time = session5.time_it(polygon_area, 4, sides=4,repetitions=1000)
    assert round(output,2) == 16, 'Incorrect Area'
    assert avg_time > 0, 'Average time should be > 0'      
    
def test_pentagon_polygon():
    output, avg_time = session5.time_it(polygon_area, 4, sides=5,repetitions=1000)
    assert round(output,2) == 27.53, 'Incorrect Area'
    assert avg_time > 0, 'Average time should be > 0'     

def test_hexagon_polygon():
    output, avg_time = session5.time_it(polygon_area, 4, sides=6,repetitions=1000)
    assert round(output,2) == 41.57, 'Incorrect Area'
    assert avg_time > 0, 'Average time should be > 0'   

def test_invalid_sidelength_polygon():
    with pytest.raises(ValueError) as e_info:
         session5.time_it(polygon_area, -4, sides=4,repetitions=100000)
    with pytest.raises(ValueError) as e_info:
         session5.time_it(polygon_area, 0, sides=4,repetitions=100000) 

def test_invalid_scale_temp():
    with pytest.raises(ValueError) as e_info:    
         session5.time_it(temp_converter, 100, temp_given_in = 'X',repetitions=1000)

def test_posc_temp():
    output, avg_time = session5.time_it(temp_converter, 100, temp_given_in = 'C',repetitions=1000)
    assert round(output,2) == 212.0, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0' 

def test_negc_temp():
    output, avg_time = session5.time_it(temp_converter, -100, temp_given_in = 'C',repetitions=1000)
    assert round(output,2) == -148.0, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0' 
    
def test_0c_temp():
    output, avg_time = session5.time_it(temp_converter, 0, temp_given_in = 'c',repetitions=1000)
    assert round(output,2) == 32.0, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_posf_temp():
    output, avg_time = session5.time_it(temp_converter, 100, temp_given_in = 'f',repetitions=1000)
    assert round(output,2) == 37.78, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0' 

def test_negf_temp():
    output, avg_time = session5.time_it(temp_converter, -100, temp_given_in = 'f',repetitions=1000)
    assert round(output,2) == -73.33, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0' 
    
def test_0f_temp():
    output, avg_time = session5.time_it(temp_converter, 0, temp_given_in = 'F',repetitions=1000)
    assert round(output,2) == -17.78, 'Incorrect Temp'  
    assert avg_time > 0, 'Average time should be > 0'  
    
def test_invalid_dist_speed():
    with pytest.raises(ValueError) as e_info:    
         session5.time_it(speed_converter, 100, dist='miles', time='ms',repetitions=1000)
         
def test_invalid_time_speed():         
    with pytest.raises(ValueError) as e_info:    
         session5.time_it(speed_converter, 100, dist='m', time='minutes',repetitions=1000)  

def test_invalid_speed():         
    with pytest.raises(ValueError) as e_info:    
         session5.time_it(speed_converter, -100, dist='m', time='s',repetitions=1000)            
    
def test_kmhr_kmday_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='km', time='day',repetitions=1000) 
    assert round(output,2) == 239.98, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'  

def test_kmhr_kmhr_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='km', time='hr',repetitions=1000) 
    assert round(output,2) == 100.0, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'     

def test_kmhr_kmmin_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='km', time='min',repetitions=1000) 
    assert round(output,2) == 1.67, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'      

def test_kmhr_kms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='km', time='s',repetitions=1000) 
    assert round(output,4) == 0.0278, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'     

def test_kmhr_kmms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='km', time='ms',repetitions=1000) 
    assert round(output,4) == 0.0, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'      
    
def test_kmhr_mday_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='m', time='day',repetitions=1000) 
    assert round(output,2) == 239980.8, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'      
    
def test_kmhr_mhr_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='m', time='hr',repetitions=1000) 
    assert round(output,2) == 100000.0, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0' 

def test_kmhr_mmin_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='m', time='min',repetitions=1000) 
    assert round(output,2) == 1666.67, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_kmhr_ms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='m', time='s',repetitions=1000) 
    assert round(output,2) == 27.78, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'      
    
def test_kmhr_mms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='m', time='ms',repetitions=1000) 
    assert round(output,4) == 0.0278, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_kmhr_ftday_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='ft', time='day',repetitions=1000) 
    assert round(output,2) == 787338.61, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'    

def test_kmhr_fthr_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='ft', time='hr',repetitions=1000) 
    assert round(output,2) == 328084.0, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'

def test_kmhr_ftmin_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='ft', time='min',repetitions=1000) 
    assert round(output,2) == 5468.07, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0' 

def test_kmhr_fts_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='ft', time='s',repetitions=1000) 
    assert round(output,2) == 91.13, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'

def test_kmhr_ftms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='ft', time='ms',repetitions=1000) 
    assert round(output,4) == 0.0911, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_kmhr_yrdday_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='yrd', time='day',repetitions=1000) 
    assert round(output,2) == 262445.4, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'  

def test_kmhr_yrdhr_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='yrd', time='hr',repetitions=1000) 
    assert round(output,2) == 109361.0, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'       

def test_kmhr_yrdmin_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='yrd', time='min',repetitions=1000) 
    assert round(output,2) == 1822.68, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_kmhr_yrds_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='yrd', time='s',repetitions=1000) 
    assert round(output,2) == 30.38, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'   

def test_kmhr_yrdms_dist():
    output, avg_time = session5.time_it(speed_converter, 100, dist='yrd', time='ms',repetitions=1000) 
    assert round(output,4) == 0.0304, 'Incorrect Speed'  
    assert avg_time > 0, 'Average time should be > 0'          