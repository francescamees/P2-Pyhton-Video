# create outer class
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import sys


class exercises:
    def __init__(self):
        self.name = 'Exercise'


    def show(self):
        print('In outer class')
        print('Name:', self.name)

    # create a 1st Inner class
    class ex1:
        def __init__(self, name_):
            self.name = 'Exercise 1: parse the BBB video '
            self.file_name = name_


        def parse_video(self):
            str = "ffmpeg -i "+self.file_name
            print(str)
            os.system(str)

        def parse_video_stream(self):
            str = "ffmpeg -i "+self.file_name+" 2>&1 | grep Stream"
            print(str)
            os.system(str)

        def display(self):
            print("Name:", self.name)


    # create a 2nd Inner class
    class ex2:
        def __init__(self, name_):
            self.name = 'Exercise 2:  create a new BBB container'
            self.file_name = name_


        def crop2(self):
            start = 0.0
            end = 60.0
            input = self.file_name
            output = 'BBB_1min.mp4'
            ffmpeg_extract_subclip(input, start, end, targetname=output)

        def extract_audio(self):
            str = "ffmpeg -i BBB_1min.mp4 -map 0 -map -0:a BBB_1min_everything_except_audio.mp4"
            print(str)
            os.system(str)

        def mp4_to_mp3(self):
            str = "ffmpeg -i BBB_1min.mp4 BBB_1min_audio.mp3"
            print(str)
            os.system(str)
        def mp3_to_acc(self):
            str = "ffmpeg -i BBB_1min_audio.mp3 -c:a aac -b:a 128k BBB_1min.aac"
            print(str)
            os.system(str)

        def merge(self):
            str = "ffmpeg -i BBB_1min_everything_except_audio.MP4 -i BBB_1min_audio.mp3 -i BBB_1min.aac -map 0 -map 1 -map 2 -codec copy new_BBB.mp4"
            print(str)
            os.system(str)

        def display(self):
            print("Name:", self.name)


     # create a 3st Inner class
    class ex3:
        def __init__(self, name, size):
            self.name = 'Exercise 3: resize (resolution change) of any input given'
            self.file_name= name
            self.file_size = size


        def compress_image(self):
            str = 'ffmpeg -i '+self.name+' -vf scale='+self.size+' output.png'
            print(str)
            os.system(str)
        def compress_video(self):
            str = 'ffmpeg -i '+self.name+' -vf scale='+self.size+' output.mp4'
            print(str)
            os.system(str)
        def compress_audio(self):
            str = 'ffmpeg -i '+self.name+' -b:a '+self.size+'k -map a output.mp3'
            print(str)
            os.system(str)


        def display(self):
            print("Name:", self.name)

    # create a 4th Inner class
    class ex4:
        def __init__(self, name):
            self.name = 'Exercise 4: check the audio tracks of the video'
            self.file_name= name

        def display(self):
            print("Name:", self.name)

        def check_audio_track(self):
            str = 'ffprobe -v error -select_streams a:0 -show_entries stream=codec_type,codec_name -of default=noprint_wrappers=1 ' + self.name + '> SomeFile.txt'
            print(str)
            os.system(str)
            l = []
            with open('SomeFile.txt') as f:
                for line in f:
                    l.append(line.strip().split('=')[1])
                    print(l[0])
                    break;
            f.close()
            if (l[0]=='ac3'):
                print( 'The broadcasting standard the video can fit are: DVB, ATSC and DTMB')
            if (l[0]=='aac'):
                print('The broadcasting standard the video can fit are: DVB, ISDB and DTMB')
            if (l[0]=='mp3'):
                print('The broadcasting standard the video can fit are: DVB and DTMB')
            if (l[0]=='mp2' or l[0]=='dra'):
                print('The broadcasting standard the video can fit is DTMB')



# create a object
# of outer class
outer = exercises()
outer.show()

# create a object
# of 1st inner class
e1 = outer.ex1('')
# create a object
# of 2nd inner class
e2 = outer.ex2('')
# create a object
# of 3r inner class
e3 = outer.ex3('','')
# create a object
# of 4th inner class
e4 = outer.ex4('')


def print_menu(): # function that prints the menu
    print('''
    
    Choose the exercise you want to do:
    
            1) Parse the ‘ffmpeg–i BBB.mp4’ file, which can mark at least 3 relevant data from the container 
            2) Create a new BBB container
            3) Resize (resolution change) of any input given
            4) Check the audio tracks of the video and which broadcasting standard the video can fit
    ''')
print_menu()


def print_menu2():  # function that prints the menu
    print('''

    Choose the input type (1-3):

            1) Image
            2) Video
            3) Audio
    ''')

def main_loop():
    try:
        choice=int(input())
        if choice == 1:
            try:
                name = input('Enter the name of the video file you want to parse (BBB.mp4): ')
                e1.file_name = name
                e1.parse_video_stream()
                main_loop()
            except:
                print('Enter number, try again')
        if choice == 2:
            try:
                name = input('Enter the name of the video file you want to create a new container (BBB.mp4): ')
                e2.file_name = name
                e2.crop2()
                e2.extract_audio()
                e2.mp4_to_mp3()
                e2.mp3_to_acc()
                e2.merge()
                main_loop()
            except:
                print('Enter number, try again')
        if choice == 3:
            print_menu2()
            try:
                choice2 = int(input())
                if choice2 == 1:
                    try:
                        name = input('Enter the name of the image file you want to resize (Lenna.png): ')
                        size = input('Enter size you want to resize the image for example(150:150): ')
                        e3.size = size
                        e3.name = name
                        e3.compress_image()
                        main_loop()
                    except:
                        print('Enter number, try again')
                if choice2 == 2:
                    try:
                        name = input('Enter the name of the video file you want to resize (BBB_1min.mp4): ')
                        size = input('Enter size you want to resize the video for example(1080:-1): ')
                        e3.size = size
                        e3.name = name
                        e3.compress_video()
                        main_loop()
                    except:
                        print('Enter number, try again')
                if choice2 == 3:
                    try:
                        name = input('Enter the name of the audio file you want to resize (BBB_1min_audio.mp3): ')
                        size = input('Enter size you want to resize the audio for example(96)kb: ')
                        e3.size = size
                        e3.name = name
                        e3.compress_audio()
                        main_loop()
                    except:
                        print('Enter number, try again')
                main_loop()
            except:
                print('Enter number, try again')
        if choice == 4:
            try:
                name = input('Enter the name of the video you want to know the broadcasting standard (new_BBB.mp4): ')
                e4.name = name
                e4.check_audio_track()
                main_loop()
            except:
                print('Enter number, try again')
    except ValueError:
        print("The value introduced is incorrect, enter a digit from 1-4")
        main_loop()
main_loop()





