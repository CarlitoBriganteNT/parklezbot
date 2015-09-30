import os

def convert(sound):
    cmd = 'opusenc --downmix-mono ' + str(sound) + '.wav ' + str(sound) + '.ogg'
    os.system(cmd)

print('============================')
print('    OPUS .WAV to .OGG\n\n')
print('Tool to make Telegram voice files!\n')
print('Make sure the audio file has no spaces!')
print('file.wav = correct\nfile name.wav = Incorrect!')
print('Do not write \'.wav\' in input!\n')
print('Press [ENTER] to exit.')
print('============================')

running = True
while running:
    sound = input('File name (input): ')
    if sound == '':
        running = False
        exit()
        
    elif ' ' in sound:
        print('File name can not countain spaces!!!')
    
    else:
        convert(sound)
