from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse
#from django.views.decorators import gzip
from django.views.decorators.gzip import gzip_page
import cv2
import numpy as np
import threading
from .forms import ImageForm
from .models import Image
from django.conf import settings
import cv2,os,urllib.request
from django.http import JsonResponse
import json  
from django.template import RequestContext


def trick(request):
    product=request.POST.GET.get('something')
    print(product)

def decent(request):
    #global useful
    #useful= #ajax data import code
    #return JsonResponse('Item found',safe=False)
    #body_unicode = request.body.decode('utf-8').replace('\0', '')
    #print(repr(body_unicode))
       #dataa=json.loads(request.body)
    #dataa=simplejson.loads(request.raw_post_data)
    #dataa=dataa.json()
    #dataa=json.loads(body_unicode)
    #producturl=dataa[namee]
       #producturl=dataa['imagebaato']
    #print('haha:',producturl)
       #return JsonResponse('Item found',safe=False)
    #return JsonResponse(producturl,safe=False)
    #formss=lala(request.POST)
    #print(formss)
    #global catt
    #catt=request.GET.get('cat')
    #print(catt)
    #path='"/imageuploader/imageuploader/" + catt'
    #os.system('echo'+ path)
    #os.system() some opencv code

    #alternative

    img = Image.objects.all()
    return render(request, 'myapp/test.html',{'img':img})

        #pass

def cutie(request):
    return render(request,'myapp/first.html')


def cute(request):
    return render(request,'myapp/sandu.html')

    


# Create your views here.

def home(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 return render(request, 'myapp/home.html', {'img':img, 'form':form})

def next(request):
    img = Image.objects.all()
    return render(request, 'myapp/test.html',{'img':img})

#def nice(a):
 #   return a

#def wow(request):
  #  img = Image.objects.all()
   # return render(request, 'myapp/home.html',{'img':img})  

#def old(object):
 #   return object         


def pro(request):
  img = Image.objects.all()
  return render(request, 'myapp/test.html',{'img':img})

#def awes(self,request,id):
 #   self.post_id=request.GET.get('ss') 



  






class VideoCamera(object):



    #def save_content(self,request):
    #    if request.method == 'POST':
     #       if 'URL' in request.POST:
     #           self.file_data = request.POST['URL']
    


    #def request_page(self,request):
    #    self.so=request.GET.get('{{x.photo.url}}')


    def __init__(self):
        self.video=cv2.VideoCapture(0)
        (self.grabbed,self.frame)=self.video.read()
        threading.Thread(target=self.update,args=()).start()


    def __del__(self):
        self.video.release()

    def get_frame(self):
        x=0
        y=0
        h=0
        w=0

        x_user=0
        y_user=0
        z_user=0
        l_img=0
        crop=0
        #path="/imageuploader/ + self.post_id"
        shoo="pant"
        noo="shirt"


        #use=str(catt.split('/')[0:-1])
        #use=str(use)
        cattt=catt + "/"
        dog=cattt.split('/')[:-1]
        lionn=dog[-1]
        lion=str(lionn)

        #sub=str('h'.join(use.split('.')[0:]))
        #sub=str(sub)



        face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

        img=self.frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #_,jpeg=cv2.imencode('.jpg',gray)
        poww="/imageuploader" + catt
        #path='"/imageuploader/imageuploader/" + catt'
        #path=str(poww)
        #s_img = cv2.imread("/imageuploader/media/myimage/1_JZoBjTL.png")
        #s_img = cv2.imread("\\media\\myimage\\1_JZoBjTL.png")
           #s_img=cv2.imread("/imageuploader/media/myimage/1_JZoBjTL.png")
        s_img=cv2.imread(poww)   
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            flag=1
            l_img = img
            x_onset = 3.2*w/s_img.shape[0]+z_user
            y_onset = 2.5*h/s_img.shape[1]+z_user
            x_offset = int(x - x_onset*200)+x_user
            y_offset = int(y + h + 15)+y_user
            u_offset=y_offset
            d_offset=2*u_offset

            if shoo in lion:
                y_offset=d_offset

            elif noo in lion:
                y_offset=u_offset    




            if x_offset<=0:
                xcut=abs(x_offset)
                x_offset=0
            else:
                xcut=0
            s_img = cv2.resize(s_img,(0,0),fx=x_onset,fy=y_onset)
            crop=s_img[0:l_img.shape[0]-y_offset,xcut:l_img.shape[1]-x_offset]
            #l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1]] = crop
            for c in range(0,3):
                l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1], c] = crop[:,:,c] * (crop[:,:,2]/255.0) +  l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1], c] * (1.0 - crop[:,:,2]/255.0)
            # cv2.putText(l_img,"a - Move left",(10,10),FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
            #cv2.imshow('img',l_img)
        _,jpeg=cv2.imencode('.jpg',l_img)    
        return jpeg.tobytes() 

    def update(self):
        while True:
            (self.grabbed,self.frame)=self.video.read()



def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@gzip_page
def house(request):
    global catt
    #catt=request.GET.get('cat')
    #catt=str(catt)
    #catts=catt.replace("\\","//")
    catt=request.GET.get('zara')
    catt=str(catt)
    #catt=catt.replace("\\","/")
    try:
        cam=VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")

    except:
        pass    
    #return render(request,'app1.html')        

  

#face_detection_videocam = cv2.CascadeClassifier(os.path.join(
 #   settings.BASE_DIR,'haarcascade_frontalface_default.xml'))  


def qq(request):
    #global ssss
    #ssss=request.GET.get('value')
    #ssss=str(ssss)
    os.system('"echo shubs"')

#def hello(request):
#    res = os.system('ls')
    #return render('myapp/nothing.html', {'res':res}, context_instance=RequestContext(request))   
#    return render(request,'myapp/nothing.html', {'res':res})   


def hello(request):
    global ssss
    ssss=request.GET.get('zara')
    ssss=str(ssss)
    res = os.system('echo ' + ssss)
    #return render('myapp/nothing.html', {'res':res}, context_instance=RequestContext(request))   
    return render(request,'myapp/nothing.html', {'res':res})       
