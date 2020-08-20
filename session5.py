import math
import random
import time

def time_it(*time_it_args, **time_it_kwargs): 
    fn        = time_it_args[0]
    repeat    = time_it_kwargs['repetitions']   
 
    if repeat <= 0:        
       Error = ValueError('Repeat should be positive')
       raise Error       
    
    if fn == print:
        sep = str(time_it_kwargs['sep'])
        end = str(time_it_kwargs['end'])
        x   = 0
        start     = time.time()
        while x < repeat:
            string = ''
            for i in range(1,len(time_it_args)):
                string += str(time_it_args[i]) + sep
            string += end
            x += 1
        end       = time.time() 
        avg_time  = round((end-start)/(60*repeat), 10)
        return string, avg_time
        
    start     = time.time() 
    for i in range(repeat):
        fn_op = fn(*time_it_args[1:],**time_it_kwargs)          
    end       = time.time() 
    avg_time  = round((end-start)/(60*repeat), 10)
    return fn_op, avg_time
    
def squared_power_list(*fn_args, **fn_kwargs):
    num     = fn_args[0]
    fn_dict = fn_kwargs
    start   = fn_kwargs['start']
    end     = fn_kwargs['end']
    
    if start == end:
        Error = ValueError('Squared Power Error - Start and end needs to be different')
        raise Error       
    elif start < end:
        Error = ValueError('Squared Power Error - Start cannot be smaller than end')
        raise Error           
        
    lst     = []
    for i in range(start,end, 1):
        lst.append(num**i)
    return lst       
    
def polygon_area(*fn_args, **fn_kwargs):
    side      = int(fn_args[0])
    fn_dict   = fn_kwargs
    num_sides = int(fn_kwargs['sides'])
    
    if num_sides in [0,1,2]:
        Error = ValueError('Poly Area - Can calculate area only for ploygons with sides >=3')
        raise Error
    elif num_sides > 6:
        Error = ValueError('Poly Area - Area calculation supported only for polygons with sides 3 to 6')
        raise Error
    elif side <= 0:
        Error = ValueError('Poly Area - Side length needs to be greater than 0')
        raise Error       
        
    if num_sides == 3:
        area = 1/4 * (math.sqrt(3) * side**2)
    elif num_sides == 4:
        area = side**2
    elif num_sides == 5:
        area = 1/4 * math.sqrt((5 * (5 + 2* math.sqrt(5)))) * side**2
    elif num_sides == 6:
        area = 1/2 * (3 * math.sqrt(3) * side**2)     
                               
    return area                           
    
def temp_converter(*fn_args, **fn_kwargs):
    temp_in  = fn_args[0]
    in_scale = fn_kwargs['temp_given_in']
    
    if str(in_scale).lower() not in ['f','c']:
        Error = ValueError('Temp Convert - Give Valid Scale, Only c/C and k/K allowed')
        raise Error
    
    if in_scale == 'f':
        temp_out = 5/9 * (temp_in - 32)
    else:
        temp_out = (9/5 * temp_in) + 32
     
    return round(temp_out,2)
    
def speed_converter(*fn_args, **fn_kwargs):
    speed = fn_args[0]
    dist  = fn_kwargs['dist']
    time  = fn_kwargs['time']
    
    if float(speed) < 0:
        Error = ValueError('Speed Convert - Speed cant be negative')
        raise Error       
    elif str(dist).lower() not in ['km','m','yrd','ft']:
        Error = ValueError('Speed Convert - Distance should be in km/m/ft/yrd')
        raise Error 
    elif str(time).lower() not in ['day','hr','min','s','ms']:   
        Error = ValueError('Speed Convert - Time should be in ms/s/min/hr/day')
        raise Error          
        
    dist_dict = {'km':1,'m':1000,'yrd':1093.61,'ft':3280.84}
    time_dict = {'day':0.4167,'hr':1,'min':60,'s':3600,'ms':3.6e+6}    
    dist_convert = dist_dict.get(dist)
    time_convert = time_dict.get(time)
    speed_convert = speed * (dist_convert / time_convert)
    
    return round(speed_convert,4)    