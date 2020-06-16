from django.shortcuts import render

def home(request):
	return render(request,'index.html')

def fac(request):
	num1=request.POST.get('num')
	if num1=='':
		result1='ENTER SOMETHING'
	else:
		num1=int(num1)
		if num1==1 or num1==0:
			result1='1'
		elif num1<0:
			result1="NOT DEFINED"
		else:
			temp=num1
			result1=1
			while temp>1:
				result1=result1*temp
				temp-=1

	params={'number1':num1,'result2':result1}
	return render(request,'result.html',params)