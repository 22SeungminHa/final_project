import stage_list_mode
import thema_list
import thema_list_mode

thema_num = -1
stage_num = -1

def init():
    global thema_num
    global stage_num

    thema_num = thema_list_mode.thema_list.select
    stage_num = stage_list_mode.stage_list.select
