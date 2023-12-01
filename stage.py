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


def stage_update(o):
    match stage_num:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass