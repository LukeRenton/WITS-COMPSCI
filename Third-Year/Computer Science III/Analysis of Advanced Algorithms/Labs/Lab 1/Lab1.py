import random
import time

def random_distinct_integers(n):
    lower = -1 * n
    upper = n
    # Sample ensures unique values
    return random.sample(range(lower, upper), n)
    
def sort_array_asc(n):
    arr = random_distinct_integers(n)
    return sorted(arr)

def sort_array_desc(n):
    arr = random_distinct_integers(n)
    return sorted(arr, reverse=True)

def measure_time(func, *args, repeats=5):
    total_time = 0
    # Benchmarks the function by running it multiple times on the same input size and averaging the time taken
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / repeats

def write_results_to_file(times_taken : dict, filename):
    with open(filename, 'w') as f:
        f.write("input,time\n")
        for key, value in times_taken.items():
            f.write(f'{key},{value}\n')
            
def run_benchmark():
    time_taken_asc = {}
    time_taken_desc = {}
    time_taken_random = {}
    # These seemed to be the most significant samples to test
    for n in [100, 1000, 10000, 100000, 250000, 500000, 1000000]:
        time_taken_random[n] = measure_time(random_distinct_integers, n) 
        time_taken_asc[n] = measure_time(sort_array_asc, n)
        time_taken_desc[n] = measure_time(sort_array_desc, n)
    write_results_to_file(time_taken_random, 'random.csv')
    write_results_to_file(time_taken_asc, 'ascending.csv')
    write_results_to_file(time_taken_desc, 'descending.csv')

if __name__ == '__main__':
    run_benchmark()


# For some extra marks, here's Tom that I made (https://github.com/LukeRenton/ImageToASCII)
'''

                                              __                   _.,---------,_  
                                    ...,,,..__...._            _.----------------_  
                   ..,--------,.._..,,--,,...,---,.,,,.____.,------------,,,,,.,--,_  
__     _______.,-------------------,,--------------------------------,.=++++-_   _,--._  
..,.......,-,..-=++++++++++=-,-------------------------------------,,=++++++.       _.,--,._  
,,.............,+++++++++++,=++,---------------------------------,,++=.,+++=_  
__................=+++++++++-,,-------,,---====-----,------------,---,,,-++-_  
_________...........+++:++=.-,==--,._,---=----------,.---------------.-++++.  
         ___________.=:++++=,==-._,;;,-==========----._,=----=---------.++-_  
                     _-++++,=-_.:c;ccc-=========-=====,__.-====-----===-,-_  
                      =,,=+,--c;+--++ba-======,.,:cc;c;+.__-====-------=,  
                    =ba!!!;-,=:acbcca!!c,==,+aacccc==ccc;..==-=+=b!!!!!+b+,  
                  .c?!!b;b,=,+ca!+._=bb;,=-aa;c-,bc;a;-cc;.=-!!!!a=!!!!?+!a,  
                 +!????b,---;:=;caccccb=====;ab-.;aa;cb;-;-==!!??!b+!!!?:!!;.  
                 :??a+-==-;:-+;:=:bab=-=====,.-:cbc:;;+-=,===?!???!+!!!;a!!:.  
                 ..,-======-,,,,.+;+----+c!c-,,---=++=-==-=-;!??!!!:!!!!!!a,  
              ,,=======-,,,-=-:!==-.__-b!?!;??b-,,--,,,===-b??????!c???!!b,  
              .....a??+-=,=;a!?abb?aa?b!?b!????!ba+-c!?b-a???????????!!;-=====  
             _,,.==,c??c+;?!:=:bb;=;a!!???aa?+b???;+?c:????????????!:-========-,  
              .-====-.b:!00?!aa??ac?a??b:::;:+++???b;???????????!:-=============-,  
            .-====--===-a??0??0?b+;!????cb????!b;?!;0?0????????:-=================,  
          _,=====,=======-!???00000;bac,,-----==,,=:??????????+====================.  
         .======-=========-:????????0?;-++=======,=,+;+;;:!;cc--====================,_  
       .-======-=======-,-=====:!??a--===========,==-,==========,-===,,==============,_  
     _,============,,-===========..=============;=;+==,===========,,-=,-==============._  
    .=========,,-=+============.-.====;bb;====:bb+;b:==,-============-,.===============.  
  .-====+=,,=======+=========.=:-,===+bbbbc++cbbb;:bb;==-,===============-,-============.  
_.=====-,=======+====+++===,-+:+=.===:bbbbbbbbbbbc=bbbc===--=================-,-=========.  
.-==================++++=-.+:++++,-+++cbbbbbbbbbbb=bbbbb:===,-===================,=======,  
 .================+++===,-========.=+=:bbbbbbbbbbbb+cbbbbb:===,-==========================_  
 ,====================-_____......_,+==cbbbbbbbbbbbbbbbbbbbb:===,-========================,_  
 _==================-__.........,,,.-==:bbbbbbbbbbbbbbbbbbbbbc+===.-======================-_  
  -================._....______....__-+=cbbbbbbbbbbbbbbbbbbbbbb;====,,====================-.  
   -=============.___________________.==:bbbbbbbbbbbbbbbbbbbbbbbc+====-,-=================__  
    _,-=======-.-==-,...,,,,,,,,,,,,,.-=+bbbbbbbbbbbbbbbbbbbbbbbbb+=======,,-============.._  
       _..,.,-=====++====..,,,,,......-=:bbbbbbbbbbbbbbbbbbbbbbbbbc+==========-,.,----,....  
       -====================,.-=--,,,,==cbbbbbbbbbbbbbbbbbbbbbbbbbbc=======,,-============..  
      -.-======================-.,--.==:bbbbbbbbbbbbbbbbbbbbbbbbbbbb:===-.-================-.  
      ..===========================,-=+cbbbbbbbbbbbbbbbbbbbbbbbcccccc=-.====================,.  
       _==========================-,==cbbbbbbbbbbbbbbbbbbbccccccccccc--======================,  
        ,=========================,==+cccccccccccccccccccccccccccccc:,=======================-,  
         .=======================-,==:cccccccccccccccccccccccccccccc--========================,  
          .-=====================,-==:ccccccccccccccccccccccccccccc;,=========================,  
            ,-===================,-==+ccccccccccccccccccccccccccccc;,=========----------=====-,  
              .,=================-,===;cccccccccccc;;;;;;;;;;;;;;;;;,=======------------------,  
                 ,-===============,-=-:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-==-------------------,--,  
                    ,--------------.--=;;;;;;;;;;;;;;;;;;;;;;;;;;;;;=--------------------.---.  
                      _,------------.--=;;;;;;;;;;;;;;;;;;;;;;;;;;;;+-------------------.---,.  
                         .-----------.--+;;;;;;;;;;;;;;;;;;;;;;;;;;;:,-----------------.---,.  
                           .----------.--+;;;;;;;;;;;;;;;;;::;;;;;:;:,----------------.,--,.     ..,  
                            .,---------.,-=:::::::::::::::::::::::::+,---------------.,--,_.,-------  
         ______            _..----------,.--+:::::::::::::::::::::::=,--------------.,--,.----------  
   .:cbbbbbabababbaabb;:+=--,-+:=---,,,,--,,,-+:::::::::::::::::::::,-------------,.,--.,-----------  
 +cbbbbbbbbbbbbbbbbbbbbbbbbbbbb;=:bbbbbbbbbbbbbc=,+::::::::::::::::-,------------..--,.,,,,,,,,,,,,,  
cbbbb;=:cbbbbbc;;cbbbbbbbbbbb:+bbc:+++++;bbbbbbcccb;--+:::::::::::=.------------.,,,.,,,,,,,,,,,,,,,  
ccc:+cbccbc=;cbbbbbbbbbbbbbb;=c=;cccccccc;;cccccccccccc:-,=+::::+,,-,-,,,,,,,,,.,,..,,,,,,,,,,,,,,,,  
:c;-ccccc+:cccccccccccccccccc--;cccc++;cccccccccccccccccccccc;::;;cc;=---,,,,,.,..,,,,,,,,,,,,,,,,..  
    _=+;;=;cccccccccccc;;;:+=-,,;;;=ccccc;cccccccccccccc;;;;;;;;;;;;;;;;;;;;=..,,,,,,,,,,,..__  
                                ...-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:, ...  
                                    ._.-+:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:-  
                                    
'''
