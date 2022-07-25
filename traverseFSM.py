# -*- coding: utf-8 -*-
"""
Created on Sun April 11 19:26:59 2022

@author: root
"""

import re
#print ("hello")


class state:
    def __init__(self):
        self.name = ""
        self.start = False;
        self.end=False;
        
class transition:
    def __init__(self):
        self.isfrom=0;
        self.to=0;
        self.trigger=""
        self.output="";
        

        


# Using readlines()
#C:\Users\root\Downloads\learningFFSM-master\learningFFSM-master\FFSM_diff\Benchmark_SPL\vm\fsm
#fsm_vm_10.txt
# the first line contains the available features
 
directoryNam="C:\\Users\\root\\Downloads\\learningFFSM-master\\learningFFSM-master\\FFSM_diff\\Benchmark_SPL\\vm\\fsm"
fileName= "fsm_vm_10.txt"
tracesFile = open(directoryNam+'\\'+fileName, 'r')
Lines = tracesFile.readlines()
del Lines[0] 

count = 0
source_state=[];
triggers=[]
dest_state=[]

transitions=[]
# Strips the newline character
for line in Lines:
    line=line.strip()
    c_trans=transition();     
    transtionLine= re.split("-- |->",line)
    source_state.append(transtionLine[0].strip());
    c_trans.isfrom=transtionLine[0].strip()
    triggers.append(transtionLine[1].split('/')[0].strip());
    c_trans.trigger=transtionLine[1].split('/')[0].strip();
    c_trans.output=transtionLine[1].split('/')[1].strip();
    dest_state.append(transtionLine[2].strip());
    c_trans.to=transtionLine[2].strip();
    transitions.append(c_trans);

total_states=source_state+dest_state;    
total_states= list(dict.fromkeys(total_states))  
total_traces=[]
print (total_states)


def printTrans(trns):
    #print(str(trns.isfrom)+"--"+str(trns.trigger)+"/"+str(trns.output)+"-->"+str(trns.to))
    print(str(trns.isfrom)+"--"+str(trns.trigger)+"/"+str(trns.output)+"-->"+str(trns.to))

#for trns in transitions:
#    printTrans(trns)


def get_outgoingTransitions(thisState):
    outgoingTransitions=[]
    for trns in transitions:
        if trns.isfrom==thisState:
            outgoingTransitions.append(trns)
    return outgoingTransitions

def rec_Travers(currentState, path, depth):
    #get list of outgoing transitions from currentState
    outTrans=get_outgoingTransitions(currentState)    
    #print ("out="+str(len(outTrans)));
    if (depth==0):
        total_traces.append(path)
        return 
    currnetDeptH=depth
    for trns in outTrans:
        #printTrans(trns)
        currentPath=path.copy()
        currentPath.append(trns)    
        rec_Travers(trns.to, currentPath, currnetDeptH-1)
        #machine = Machine(states=total_states)
#machine.states.pop('initial')
startPath=[]
for stts in total_states:
    #print(stts)
    rec_Travers(currentState=stts, path=startPath, depth=4)
    #print(stts)


all_traces=[]    
for pth in total_traces:
    #print("------------")    
    s_trc="";
    for trns in pth:
        s_trc=s_trc+("--"+str(trns.trigger)+"/"+str(trns.output)+"-->")
    #print( s_trc)
    all_traces.append(s_trc)
    all_traces= list(dict.fromkeys(all_traces))  
    
for trc in all_traces:
    print(trc)
    
    
    
    
        