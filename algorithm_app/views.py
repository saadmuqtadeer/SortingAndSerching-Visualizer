
from asyncio.constants import ACCEPT_RETRY_DELAY
from django.shortcuts import render
import json
from .forms import Data,Search_Data,BFSForm
import random
from collections import deque
import matplotlib.pyplot as plt

# Create your views here.
def home(request):
    return render(request,'home.html')
####################################################################################################
#####################################################################################################

def bubble(request):
    return render(request,"bubble.html")

def selection(request):
    return render(request,"selection.html")

def insertion(request):
    return render(request,"insertion.html")

def quick(request):
    return render(request,"quick.html")

def oddeven(request):
    return render(request,"oddeven.html")

def cocktail(request):
    return render(request,"cocktail.html")

def shell(request):
    return render(request,"shell.html")

def pancake(request):
    return render(request,"pancake.html")

def comb(request):
    return render(request,"comb.html")

def bogo(request):
    return render(request,"bogo.html")

####################################################################################################
#####################################################################################################
def bubble_sort(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]
            list_data=data.split(",") 
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        for i in range(len(list_data)):
            for j in range(len(list_data)-i-1):
                if list_data[j]>list_data[j+1]:
                    list_data[j],list_data[j+1]=list_data[j+1],list_data[j]
                    copy_list=list_data.copy()
                    extra_list.append(copy_list)                 
    else:
          form=Data()
    return render(request,'bubble_sort.html',{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})



def bubble_sort_string(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]
            list_data=list(data)
        for i in range(len(list_data)):
            for j in range(len(list_data)-i-1):
                if list_data[j]>list_data[j+1]:
                    list_data[j],list_data[j+1]=list_data[j+1],list_data[j]
                    copy_list=list_data.copy()
                    extra_list.append(copy_list)                 
    else:
          form=Data()
    return render(request,'bubble_sort_string.html',{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

#####################################################################################################
def selection_sort(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        n=len(list_data)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if list_data[j]<list_data[min_index]:
                    min_index=j
            list_data[i],list_data[min_index]=list_data[min_index],list_data[i]
            copy_list=list_data.copy()
            print(copy_list)
            extra_list.append(copy_list)
    else:
          form=Data()
    return render(request,"selection_sort.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

def selection_sort_string(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
        n=len(list_data)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if list_data[j]<list_data[min_index]:
                    min_index=j
            list_data[i],list_data[min_index]=list_data[min_index],list_data[i]
            copy_list=list_data.copy()
            extra_list.append(copy_list)
    else:
          form=Data()
    return render(request,"selection_sort_string.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

#####################################################################################################

def insertion_sort(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        n=len(list_data)
        for i in range(1,n):
            key=list_data[i]
            j=i-1
            while j>=0 and key<list_data[j]:
                list_data[j+1]=list_data[j]
                j-=1
            list_data[j+1]=key
            copy_list=list_data.copy()
            extra_list.append(copy_list)
    else:
          form=Data()
    return render(request,"insertion_sort.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

def insertion_sort_string(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        n=len(list_data)
        for i in range(1,n):
            key=list_data[i]
            j=i-1
            while j>=0 and key<list_data[j]:
                list_data[j+1]=list_data[j]
                j-=1
            list_data[j+1]=key
            copy_list=list_data.copy()
            extra_list.append(copy_list)
    else:
          form=Data()
    return render(request,"insertion_sort_string.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

#####################################################################################################

def quick_sort1(arr):
    stack = [(0, len(arr) - 1)]
    copy_list = [arr.copy()]  
    while stack:
        low, high = stack.pop()
        pivot_index = partition(arr, low, high, copy_list)

        if pivot_index - 1 > low:
            stack.append((low, pivot_index - 1))

        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

    return copy_list  

def partition(arr, low, high, copy_list):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            copy_list.append(arr.copy())  

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    copy_list.append(arr.copy()) 
    return i + 1

def quick_sort(request):
    list_data = []
    extra_list = []
    data = []
    copy_list = []

    if request.method == "POST":
        form = Data(request.POST)
        if form.is_valid():
            data = form.cleaned_data["Enter_Character"]
            list_data = data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
            copy_list = quick_sort1(list_data)
        extra_list=copy_list
    else:
        form = Data()

    return render(request, "quick_sort.html", {"form": form, "list_data": list_data, "extra_list": extra_list, "data": data, "copy_list": copy_list})

def quick_sort_string(request):
    list_data = []
    extra_list = []
    data = []
    copy_list = []

    if request.method == "POST":
        form = Data(request.POST)
        if form.is_valid():
            data = form.cleaned_data["Enter_Character"]
            list_data = list(data)
            copy_list = quick_sort1(list_data)
        extra_list=copy_list
    else:
        form = Data()

    return render(request, "quick_sort_string.html", {"form": form, "list_data": list_data, "extra_list": extra_list, "data": data, "copy_list": copy_list})

#####################################################################################################

def odd_even(request):
    extra_list = []
    data = []
    list_data = []
    copy_list = []

    if request.method == "POST":
        form = Data(request.POST) 
        if form.is_valid():
            data = form.cleaned_data["Enter_Character"]
            list_data = data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
            n = len(list_data)
            sorted = False

            while not sorted:
                sorted = True

                # Odd phase
                for i in range(1, n - 1, 2):
                    if list_data[i] > list_data[i + 1]:
                        list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
                        sorted = False

                # Even phase
                for i in range(0, n - 1, 2):
                    if list_data[i] > list_data[i + 1]:
                        list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
                        sorted = False

                copy_list = list_data.copy()
                extra_list.append(copy_list)
    else:
        form = Data()

    return render(request, "odd_even.html", {"form": form, "list_data": list_data, "extra_list": extra_list, "data": data, "copy_list": copy_list})

def odd_even_string(request):
    extra_list = []
    data = []
    list_data = []
    copy_list = []

    if request.method == "POST":
        form = Data(request.POST) 
        if form.is_valid():
            data = form.cleaned_data["Enter_Character"]
            list_data = list(data)
            n = len(list_data)
            sorted = False

            while not sorted:
                sorted = True

                # Odd phase
                for i in range(1, n - 1, 2):
                    if list_data[i] > list_data[i + 1]:
                        list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
                        sorted = False

                # Even phase
                for i in range(0, n - 1, 2):
                    if list_data[i] > list_data[i + 1]:
                        list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
                        sorted = False

                copy_list = list_data.copy()
                extra_list.append(copy_list)
    else:
        form = Data()

    return render(request, "odd_even_string.html", {"form": form, "list_data": list_data, "extra_list": extra_list, "data": data, "copy_list": copy_list})

#####################################################################################################

def cocktail_sort(request):
    extra_list = []
    data = []
    list_data = []
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]            
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        extra_list=(cocktail_sort_algorithm(list_data))
    else:
          form=Data()
    return render(request,"cocktail_sort.html",{"form":form,"data":data,"extra_list":extra_list})


def cocktail_sort_string(request):
    extra_list = []
    data = []
    list_data = []
    if request.method=="POST":
        form=Data(request.POST)
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]            
            list_data=list(data)
        extra_list=(cocktail_sort_algorithm(list_data))
    else:
          form=Data()
    return render(request,"cocktail_sort_string.html",{"form":form,"data":data,"extra_list":extra_list})

def cocktail_sort_algorithm(arr):
    extra_list=[]
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Loop from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                copy_list=arr.copy()
                swapped = True
                extra_list.append(copy_list)  # Capture the state of the list

        # If nothing moved, array is sorted
        if not swapped:
            break

        swapped = False

        # Move the end point back by one
        end = end - 1

        # Loop from right to left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                copy_list=arr.copy()
                swapped = True
                extra_list.append(copy_list)  # Capture the state of the list
        start = start + 1
    return extra_list

#####################################################################################################

def shell_sort_algorithm(arr):
    n = len(arr)
    gap = n // 2
    extra_list=[]
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

            extra_list.append(arr.copy())  # Capture the state of the list

        gap //= 2
    return extra_list



def shell_sort(request):
    extra_list=[]
    data=[]
    list_data=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        extra_list=shell_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"shell_sort.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

def shell_sort_string(request):
    extra_list=[]
    data=[]
    list_data=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
        extra_list=shell_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"shell_sort_string.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

#####################################################################################################

def pancake_sort_algorithm(arr):
    n = len(arr)
    extra_list=[]
    for current_size in range(n, 1, -1):
        max_index = arr.index(max(arr[:current_size]))

        if max_index != current_size - 1:
            arr[:max_index + 1] = reversed(arr[:max_index + 1])
            extra_list.append(arr.copy())
            arr[:current_size] = reversed(arr[:current_size])
            extra_list.append(arr.copy())
    return extra_list

def pancake_sort(request):
    data=[]
    extra_list=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
            extra_list=pancake_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"pancake_sort.html",{"form":form,"data":data,"extra_list":extra_list})

def pancake_sort_string(request):
    data=[]
    extra_list=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
            extra_list=pancake_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"pancake_sort_string.html",{"form":form,"data":data,"extra_list":extra_list})

#####################################################################################################

def com_sort_algorithm(arr):
    extra_list=[]
    n = len(arr)
    gap = n
    shrink_factor = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False

        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
                extra_list.append(arr.copy())
    return extra_list

def comb_sort(request):
    data=[]
    extra_list=[]
    list_data=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
        extra_list=com_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"comb_sort.html",{"form":form,"data":data,"extra_list":extra_list})

def comb_sort_string(request):
    data=[]
    extra_list=[]
    list_data=[]
    if request.method=="POST":
        form=Data(request.POST) 
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
        extra_list=com_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"comb_sort_string.html",{"form":form,"data":data,"extra_list":extra_list})

#####################################################################################################

def bogo_sort_algorithm(arr):
    extra_list=[]
    while not is_sorted(arr):
        random.shuffle(arr)
        extra_list.append(arr.copy())
    return extra_list

def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)  
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
            extra_list=bogo_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"bogo_sort.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

def bogo_sort_string(request):
    list_data=[]
    extra_list=[]
    data=[]
    if request.method=="POST":
        form=Data(request.POST)  
        if form.is_valid():
            data=form.cleaned_data["Enter_Character"]           
            list_data=list(data)
            extra_list=bogo_sort_algorithm(list_data)
    else:
          form=Data()
    return render(request,"bogo_sort_string.html",{"form":form,"list_data":list_data,"extra_list":extra_list,"data":data})

##############################################################################################################################
##############################################################################################################################

def linear(request):
    return render(request,"linear.html")
def linear_search(request):
    return render(request,"linear_search.html")

def linear_search_string(request):
    return render(request,"linear_search_string.html")

def linear_search_algorithm(arr,target):
    d={}
    for i in arr:
        if i==target:
            d[i]="found"
            break
        else:
            d[i]="not found"
    return d

def binary(request):
    return render(request,"binary.html")    

def binary_search(request):
    return render(request,"binary_search.html")


def binary_search_string(request):
    return render(request,"binary_search_string.html")


def binary_search_algorithm(arr,target):
    arr=sorted(arr)
    low, high = 0, len(arr) - 1
    steps_list = []

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        steps_list.append((("low position",low),("high position", high),("mid position",mid),("mid value position", mid_value)))  

        if mid_value == target:
            steps_list.append((("low position",low),("high position", high),("mid position",mid),("mid value position", mid_value)))
            return mid, steps_list 
            
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1, steps_list

############################################################################################################



def breadth_first_search(request):
    return render(request, 'breadth_first_search.html')
    
def breadth_first_search_string(request):
    return render(request, 'breadth_first_search_string.html')

def construct_graph(start_nodes, end_nodes):
    graph = {}
    start_list = start_nodes.split(',')
    end_list = end_nodes.split(',')
    
    # Ensure the number of start nodes matches the number of end nodes
    if len(start_list) != len(end_list):
        return None
    
    # Construct the graph dictionary
    for i in range(len(start_list)):
        start_node = start_list[i].strip()
        end_node = end_list[i].strip()
        graph[start_node] = end_node.split(',')
    
    return graph


def depth_first_search(request):
    return render(request,"depth_first_search.html")

def depth_first_search_string(request):
    return render(request,"depth_first_search_string.html")

def a_star(request):
    if request.method=="POST":
        form=Search_Data(request.POST)   
        if form.is_valid():
            data=form.cleaned_data["Enter_number_or_string"]
            search=form.cleaned_data["Enter_number_or_string_to_search"]            
            list_data=data.split(",")
            list_data=[int(i) if i.isdigit() else i for i in list_data]
    else:
          form=Data()
    return render(request,"a_star.html",{"form":form})

def a_star_algorithm(arr,target):
    pass