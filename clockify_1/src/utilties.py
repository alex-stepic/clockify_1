import os
def avatar_set():
    src_dir = os.listdir(str(os.path.dirname(__file__)).replace("\\", "/")+"/avatar_pictures")
    return [f for f in src_dir]
def bad_avatar_set():
    src_dir = os.listdir(str(os.path.dirname(__file__)).replace("\\", "/")+"/bad_avatar_pictures")
    return [f for f in src_dir]
def avatar_full(xavatar):
    return str(os.path.dirname(__file__)).replace("\\", "/")+"/avatar_pictures/"+xavatar
def avatar_full_neg(xavatar):
    return str(os.path.dirname(__file__)).replace("\\", "/")+"/bad_avatar_pictures/"+xavatar
def global_par():
    return str(os.path.dirname(__file__)).replace("\\", "/")+"/global.json"