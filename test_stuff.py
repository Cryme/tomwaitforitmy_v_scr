import subprocess
import os
def cutf(path, name, startframe, fps, endframe, outname):
    command = ["ffmpeg", '-i', path+name, '-ss', str(startframe/fps), '-t', str((endframe-startframe)/fps),
                '-c:v', 'libx264',
                '-c:a', 'aac',
                path+outname]
    return command

ppath = "C:\\Users\\CrymeAriver\PycharmProjects\\tomwaitforitmy_v_scr\\"

a = cutf(ppath, 'qwe.flv', 8089, 30, 8989, 'out' + str(1) + '.flv')
print(a)
process = subprocess.Popen(a, stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)

# threading.Thread(target=os.system(cutf(ppath, 'qwe.flv', 8089, 30, 8989, 'out' + str(1) + '.flv')))
