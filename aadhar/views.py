from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import aadhar_model,pdf
from .serializers import aadhar_modelSerializer
from django.http import JsonResponse
from .forms import pdfForm
from django.contrib import messages

@api_view(['GET', 'POST'])
def homepage(request,number):

    if request.method == 'GET':
        aadhar_data = aadhar_model.objects.filter(aadhar_number=number)
        if aadhar_data:
            serializer = aadhar_modelSerializer(aadhar_data, many=True)
            return JsonResponse(serializer.data,safe=False)
        else:
            voter_data=aadhar_model.objects.filter(voter_id=number)    
            serializer = aadhar_modelSerializer(voter_data, many=True)
            return JsonResponse(serializer.data,safe=False)

    # elif request.method == 'POST':
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




def getstatus(request):
    aadharobj=aadhar_model.objects.all()
    return JsonResponse({'total':len(aadharobj),'aadhar_number':[aadhar.aadhar_number if aadhar.aadhar_number !="" else aadhar.voter_id for aadhar in aadharobj]},safe=False)


#extract data from pdf
    
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal
def get_aadhar_details(path , password):
    i = 0
    try:
        for page_layout in extract_pages(path, password):
            for element in page_layout:
                if isinstance(element , LTTextBoxHorizontal):
                    i+=1
                    if i==2:
                        addr = element.get_text()
                    elif i == 24:
                        aadhar_no = element.get_text()
                        
        addr_list=addr.splitlines()
        num_list=aadhar_no.splitlines()
        #name
        # print(addr_list[2])
        # #mobile number
        # print(addr_list[-1])
        # #aadhar number
        aadhar=num_list[0]
        splitted_aadhar_with_space=aadhar.split(' ')
        aadhar="".join(splitted_aadhar_with_space)
        return(addr_list[2],addr_list[-1],aadhar)
    except:
        return False    




def add_detais(request):
    return_response={}
    form=pdfForm() 
    flag=False
    if request.method== "POST":
        form = pdfForm(request.POST or None,request.FILES)
        if form.is_valid():
            details = form.save(commit=True)
            try:
                name,mobile,aadhar=get_aadhar_details(details.pdf_file.path , details.password)
                flag=True
            except:
                pdf.objects.filter(pdf_file=str(details.pdf_file)).delete()  
                messages.error(request, 'WRONG PASSWORD or WRONG FILE please enter correct password or check if you are uploading aadhar file')
                return redirect('/add-deatils/')
            if flag :
                aadhar_obj=aadhar_model.objects.filter(aadhar_number=aadhar)
                # print(aadhar_obj)
                if len(aadhar_obj) != 0:
                    pdf.objects.filter(pdf_file=str(details.pdf_file)).delete()  
                    messages.warning(request, 'Data already present in the database..')
                    return redirect('/add-deatils/')
                else:
                    pdf.objects.filter(pdf_file=str(details.pdf_file)).delete()   
                    aadhar_model.objects.create(aadhar_number=aadhar,name=name,phone_number=mobile)
                    messages.success(request,"Successfully added the data!")
                    return redirect('/add-deatils/')        
    return_response['form']=form
    return render(request,'addfiles.html',return_response)          