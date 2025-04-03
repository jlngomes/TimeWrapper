from time import time

activated = True

def time_wrapper(met):

    if activated:
        def wrapped_method(*args, **kwargs):
            print(f'Starting method : {str(met.__name__)}')
            start_time = time()
            ret_val = met(*args, **kwargs)
            print(f'Method finished in {str(time() - start_time)} seconds.')
            return ret_val
    else:
        wrapped_method = met

    return wrapped_method