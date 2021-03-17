import os
import math
import warnings

warnings.filterwarnings('ignore')
os.system("cls")

class colors:
    GREEN = "\033[92m"
    BLUE = "\u001b[34;1m"
    RED = "\u001b[31;1m"
    CYAN = "\u001b[36;1m"
    YELLOW = "\u001b[33m"
    GRAY = "\033[90m"
    ENDC = "\033[0m"

print(f"┌────────────────────────────────────────────────────────────────────────────────────────────────────┐")
print(f"│ ██████╗   ██╗ ███╗    ██╗   ██████╗  ███╗    ███╗ ██╗     ████╗     ██╗       {colors.GREEN}██████╗  ██╗     ██╗{colors.ENDC} │")
print(f"│ ██╔══██╗  ██║ ████╗   ██║  ██╔═══██╗ ████╗  ████║ ██║    ██╔═██╗    ██║       {colors.GREEN}██╔══██╗  ██╗   ██╔╝{colors.ENDC} │")
print(f"│ ██║   ██╗ ██║ ██║██╗  ██║  ██║   ██║ ██║██╗██║██║ ██║   ██╔╝  ██╗   ██║       {colors.GREEN}██║  ██║   ██╗ ██╔╝{colors.ENDC}  │")
print(f"│ ███████╔╝ ██║ ██║ ██╗ ██║  ██║   ██║ ██║ ███╔╝██║ ██║   ████████║   ██║       {colors.GREEN}██████╔╝    ████╔╝{colors.ENDC}   │")
print(f"│ ██╔═══██╗ ██║ ██║  ██╗██║  ██║   ██║ ██║ ╚══╝ ██║ ██║  ██╔═════██╗  ██║       {colors.GREEN}██╔═══╝      ██╔╝{colors.ENDC}    │")
print(f"│ ██║  ██╔╝ ██║ ██║   ████║  ██║   ██║ ██║      ██║ ██║  ██║     ██║  ██║       {colors.GREEN}██║          ██║{colors.ENDC}     │")
print(f"│ ██████╔╝  ██║ ██║    ███║   ██████╔╝ ██║      ██║ ██║ ██╔╝      ██╗ ████████╗ {colors.GREEN}██║          ██║{colors.ENDC}     │")
print(f"│ ╚═════╝   ╚═╝ ╚═╝    ╚══╝   ╚═════╝  ╚═╝      ╚═╝ ╚═╝ ╚═╝       ╚═╝ ╚═══════╝ {colors.GREEN}╚═╝          ╚═╝{colors.ENDC}     │")
print(f"└────────────────────────────────────────────────────────────────────────────────────────────────────┘\n")

def set_n():
    print(f"[{colors.YELLOW}SET VALUE{colors.ENDC}] n = ", end='')
    set_n.n = int(input())
    if set_n.n <= 0:
        print(f"[{colors.RED}ERROR{colors.ENDC}] n > {colors.CYAN}0{colors.ENDC}")
        set_n()

def set_p():
    print(f"[{colors.YELLOW}SET VALUE{colors.ENDC}] p = ", end='')
    set_p.p = float(input())
    if set_p.p <= 0 or set_p.p > 1:
        print(f"[{colors.RED}ERROR{colors.ENDC}] {colors.CYAN}0{colors.ENDC} > p <= {colors.CYAN}1{colors.ENDC}")
        set_p()

set_n()
set_p()

n = set_n.n
p = set_p.p

def set_k():
    print(f"[{colors.YELLOW}SET VALUE{colors.ENDC}] k = ", end='')
    set_k.k = float(input())
    if set_k.k < 0 or set_k.k > n:
        print(f"[{colors.RED}ERROR{colors.ENDC}] {colors.CYAN}0{colors.ENDC} >= k <= {colors.CYAN} {n} {colors.ENDC}")
        set_k()

set_k()

k = set_k.k

def set_r():
    print(f"[{colors.YELLOW}SET VALUE{colors.ENDC}] r = ", end='')
    set_r.r = int(input())
    if set_r.r < -1:
        print(f"[{colors.RED}ERROR{colors.ENDC}] r >= {colors.CYAN}0{colors.ENDC}")
        set_r()

set_r()
r = set_r.r

def pdfORcdf():
    print(f"[{colors.BLUE}INFO{colors.ENDC}] Do you want to calculate the Binomialpdf({colors.BLUE}pdf{colors.ENDC}) or Binomialcdf({colors.BLUE}cdf{colors.ENDC})?: ", end='')
    pdfORcdf.answer = str(input())
    if pdfORcdf.answer == "pdf" or pdfORcdf.answer == "cdf":
        return
    else:
        print(f"[{colors.RED}ERROR{colors.ENDC}] You have to type {colors.BLUE}pdf{colors.ENDC} or {colors.BLUE}cdf{colors.ENDC}")
        pdfORcdf()

print()
pdfORcdf()

def sla():
    print(f"[{colors.BLUE}INFO{colors.ENDC}] single({colors.BLUE}s{colors.ENDC}) / list({colors.BLUE}l{colors.ENDC}) / all({colors.BLUE}a{colors.ENDC}): ", end='')
    sla.value = str(input())

sla()
slav = sla.value
print()

def binomialpdf(n=n, k=k, p=p, sla=slav, roundon=r, printit=True):
    #print(n, k, p, sla, roundon, printit)
    binomialpdf.result = 0
    if sla == "s":
        #calculate the binomial coefficient
        bc = (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))
        #calculate the hit probability
        hp = p**k
        #calculate the riveting probability
        rp = (1-p)**(n-k)

        #calculate the result with round
        if roundon == -1: 
            binomialpdf.result = bc * hp * rp
        else:
            binomialpdf.result = round(bc * hp * rp, roundon)
        if printit == True:
            print(f"[{colors.GREEN}RESULT{colors.ENDC}] {colors.GRAY}P(X = k) ={colors.ENDC} " + str(binomialpdf.result))
    if sla == "a":
        x = 0
        binomialpdf.highestresult = 0
        while x <= n:
            #calculate the binomial coefficient
            bc = (math.factorial(n) / (math.factorial(x) * math.factorial(n-x)))
            #calculate the hit probability
            hp = p**x
            #calculate the riveting probability
            rp = (1-p)**(n-x)

            #calculate the result with round
            if roundon == -1: 
                binomialpdf.result = bc * hp * rp
            else:
                binomialpdf.result = round(bc * hp * rp, roundon)

            if binomialpdf.result > binomialpdf.highestresult:
                binomialpdf.highestresult = binomialpdf.result
                binomialpdf.highestresultx = x

            if printit == True:
                print(f"[{colors.GREEN}RESULT{colors.ENDC}] {colors.GRAY}P(X = {colors.BLUE}" + str(x) + f"{colors.ENDC}) ={colors.ENDC} " + str(binomialpdf.result))
            x += 1

def binomialcdf(n=n, k=k, p=p, sla=slav, roundon=r, printit=True):
    x = 0
    binomialcdf.sumofp = 0
    if sla == "s":
        while x <= k:
            binomialpdf(n, x, p, "s", r, False)
            binomialcdf.sumofp += binomialpdf.result
            x += 1
        if printit == True:
            print(f"[{colors.GREEN}RESULT{colors.ENDC}] {colors.GRAY}P(X <= {colors.BLUE}" + str(k) + f"{colors.ENDC}) ={colors.ENDC} " + str(binomialcdf.sumofp))
    elif sla == "a":
        while x <= n:
            y = 0
            binomialcdf.sumofp = 0
            while y <= x:

                bc = (math.factorial(n) / (math.factorial(y) * math.factorial(n-y)))
                hp = p**y
                rp = (1-p)**(n-y)

                result = bc * hp * rp
                binomialcdf.sumofp += result

                y += 1
            if printit == True:
                if roundon == -1:
                    print(f"[{colors.GREEN}RESULT{colors.ENDC}] {colors.GRAY}P(X <= {colors.BLUE}" + str(x) + f"{colors.ENDC}) ={colors.ENDC} " + str(round(binomialcdf.sumofp, 15)))
                else:
                    binomialcdf.sumofp = round(binomialcdf.sumofp, roundon)
                    print(f"[{colors.GREEN}RESULT{colors.ENDC}] {colors.GRAY}P(X <= {colors.BLUE}" + str(x) + f"{colors.ENDC}) ={colors.ENDC} " + str(round(binomialcdf.sumofp, 15)))
            x += 1

def hist():
    print(f"\n[{colors.BLUE}INFO{colors.ENDC}] Do you want print out the histogram? ({colors.BLUE}y{colors.ENDC}/{colors.BLUE}n{colors.ENDC}): ", end='')
    answer = str(input())
    if answer == "y":
        if pdfORcdf.answer == "pdf":
            print()
            onevalue = binomialpdf.highestresult / 100
            x = 0
            while x <= n:
                xvalue = ""
                binomialpdf(n, x, p, "s", -1, False)
                countvalue = round(binomialpdf.result / onevalue)
                for i in range(countvalue):
                    xvalue += "#"
                if x < 10:
                    if x == binomialpdf.highestresultx:
                        print(f"[  {colors.CYAN}" + str(x) + f"{colors.ENDC}] " + xvalue)
                    else:
                        print(f"[  {colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                elif x < 100:
                    if x == binomialpdf.highestresultx:
                        print(f"[ {colors.CYAN}" + str(x) + f"{colors.ENDC}] " + xvalue)
                    else:
                        print(f"[ {colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                else:
                    if x == binomialpdf.highestresultx:
                        print(f"[{colors.CYAN}" + str(x) + f"{colors.ENDC}] " + xvalue)
                    else:
                        print(f"[{colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                x += 1
        elif pdfORcdf.answer == "cdf":
            print()
            onevalue = 0.01
            x = 0
            while x <= n:
                xvalue = ""
                binomialcdf(n, x, p, "s", -1, False)
                countvalue = round(binomialcdf.sumofp / onevalue)
                for i in range(countvalue):
                    xvalue += "#"
                if x < 10:
                    print(f"[  {colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                elif x < 100:
                    print(f"[ {colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                else:
                    print(f"[{colors.BLUE}" + str(x) + f"{colors.ENDC}] " + xvalue)
                x += 1
    elif answer == "n":
        return
    else:
        print(f"[{colors.RED}ERROR{colors.ENDC}] You have to type {colors.BLUE}y{colors.ENDC} or {colors.BLUE}n{colors.ENDC}")
        hist()

if pdfORcdf.answer == "pdf":
    binomialpdf()
    hist()
elif pdfORcdf.answer == "cdf":
    binomialcdf()
    hist()