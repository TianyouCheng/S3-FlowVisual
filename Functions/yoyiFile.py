import os
import os.path as osp

def getFileSize(filePath):
    if filePath[0] not in ['C','D','E','F']:
        return 0
    fsize = osp.getsize(filePath)  # 返回的是字节大小

    if fsize < 1024:
        return f"{round(fsize, 2)}Byte"
    else:
        KBX = fsize / 1024
        if KBX < 1024:
            return f"{round(KBX, 2)}Kb"
        else:
            MBX = KBX / 1024
            if MBX < 1024:
                return f"{round(MBX, 2)}Mb"
            else:
                return f"{round(MBX/1024,2)}Gb"