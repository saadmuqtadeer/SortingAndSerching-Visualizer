from django.contrib import admin
from django.urls import path
from algorithm_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    ############################################
    path("bubble",views.bubble,name="bubble"),
    path("selection",views.selection,name="selection"),
    path("insertion",views.insertion,name="insertion"),
    path("quick",views.quick,name="quick"),
    path("oddeven",views.oddeven,name="oddeven"),
    path("cocktail",views.cocktail,name="cocktail"),
    path("shell",views.shell,name="shell"),
    path("pancake",views.pancake,name="pancake"),
    path("comb",views.comb,name="comb"),
    path("bogo",views.bogo,name="bogo"),
    #########################################
    path("bubble_sort",views.bubble_sort,name="bubble_sort"),
    path("selection_sort",views.selection_sort,name="selection_sort"),
    path("insertion_sort",views.insertion_sort,name="insertion_sort"),
    path("quick_sort",views.quick_sort,name="quick_sort"),
    path("odd_even",views.odd_even,name="odd_even"),
    path("cocktail_sort",views.cocktail_sort,name="cocktail_sort"),
    path("shell_sort",views.shell_sort,name="shell_sort"),
    path("pancake_sort",views.pancake_sort,name="pancake_sort"),
    path("comb_sort",views.comb_sort,name="comb_sort"),
    path("bogo_sort",views.bogo_sort,name="bogo_sort"),
    
    path("bogo_sort_string",views.bogo_sort_string,name="bogo_sort_string"),
    path("bubble_sort_string",views.bubble_sort_string,name="bubble_sort_string"),
    path("selection_sort_string",views.selection_sort_string,name="selection_sort_string"),
    path("insertion_sort_string",views.insertion_sort_string,name="insertion_sort_string"),
    path("quick_sort_string",views.quick_sort_string,name="quick_sort_string"),
    path("odd_even_string",views.odd_even_string,name="odd_even_string"),
    path("cocktail_sort_string",views.cocktail_sort_string,name="cocktail_sort_string"),
    path("shell_sort_string",views.shell_sort_string,name="shell_sort_string"),
    path("pancake_sort_string",views.pancake_sort_string,name="pancake_sort_string"),
    path("comb_sort_string",views.comb_sort_string,name="comb_sort_string"),
#################################################################################################
    path("linear",views.linear,name="linear"),
    path("linear_search",views.linear_search,name="linear_search"),
    path("linear_search_string",views.linear_search_string,name="linear_search_string"),
    path("binary",views.binary,name="binary"),
    path("binary_search",views.binary_search,name="binary_search"),
    path("binary_search_string",views.binary_search_string,name="binary_search_string"),
    path("breadth_first_search",views.breadth_first_search,name="breadth_first_search"),
    path("breadth_first_search_string",views.breadth_first_search_string,name="breadth_first_search_string"),
    path("depth_first_search",views.depth_first_search,name="depth_first_search"),
    path("depth_first_search_string",views.depth_first_search_string,name="depth_first_search_string"),
    path("a_star",views.a_star,name="a_star"),
]
