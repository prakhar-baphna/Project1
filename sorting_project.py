import os,shutil
folders={
    'video':['.mp4','.mov'],
    'audio':['.wav','.mp3'],
    'images':['.jpg','.png','.jpeg','.JPG'],
    'documents':['.doc','.docm','.docx','.dot','.dotm','.dotx','.htm','.html','.docm','.odt','.pdf','.rft','.txt','wps','.xml','.xps','.dbf','.dif','.xlsx','.xls','.pdf','.zip','.rar','.csv','.prn','.slk','.xla','.xlam','.ppt','.pptx','.pptm'],
    'subtitles':['.srt'],
}        
def create_move(ext,file_name):
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder_name))
            shutil.move(os.path.join(directory,file_name),os.path.join(directory,folder_name))
            break
         
directory=input('enter the location:')
all_files=os.listdir(directory)
for i in all_files:
    if os.path.isfile(os.path.join(directory,i))==True:
        create_move(i.split(".")[-1],i)
