import ffmpeg
import cv2
import subprocess

ppath = "C:\\Users\\CrymeAriver\PycharmProjects\\tomwaitforitmy_v_scr\\"
file_name = 'qwe.flv'

probe = ffmpeg.probe(ppath+file_name)
video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
width = int(video_info['width']/20)
height = int(video_info['height']/8)

cap = cv2.VideoCapture(ppath+file_name)

def cutf(path, name, startframe, fps, endframe, outname):
    command = ["ffmpeg", '-i', path+name, '-ss', str(startframe/fps), '-t', str((endframe-startframe)/fps),
                '-c:v', 'libx264',
                '-c:a', 'aac',
                path+outname]
    return command

ind = 0
changed = False
counter = 0
arr = []
s_counter = 0

while(cap.isOpened()):
    start_pos = 0
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])
    # print(len(hist))
    video = gray[0:height]
    tt = []
    for i in video:
        tt.append(i[0:width])
    val = 0
    for i in tt:
        for o in i:
            val += o[2]
    x = val / (width * height)

    if x < 15 and not changed:
        print(x, ind)
        changed = True
        arr.append(ind)
        print(arr)
        if len(arr) == 2:
            a = cutf(ppath, file_name, arr[0], 30, arr[1], 'out' + str(ind) + '.flv')
            arr = []
            process = subprocess.Popen(a, stdout=subprocess.PIPE)
            output, error = process.communicate()
        arr = []

    if x > 72 and changed:
        print(x, ind)
        arr.append(ind)
        print(arr)
        changed = False

    ind += 1
    # cv2.imshow('frame', frame)
    # print(gray)
    # break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
