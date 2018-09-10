
# Copyright 2016 Alok Kumar. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import wap
import random


server = 'http://api.wolframalpha.com/v2/query.jsp'
#Replace the appID with wolfram license ID
appid = 'XXXXXXXX'

# Array Paradize
preDefinedMsg_array=["\n I don't feel like answering this question","\nSeriously, you don't know even this\n"]
proFaneMsg_array=["\n Is this what your mother has taught you \n","\n please be mindful of your language\n"]

profane_words={'fuck':'dummy value','sex':'dummy value','sexy':'dummy','dumb':'dummy','stupid':'dummy'}

overridenQAns=["\n I told you. I am a bot. \n","\n qBot-pronounced as que-bot \n","\n It is a secret but i can tell you. Kepler!\n"]


#Flags
noAns=0;


def resetBotParts():
    #Little bit of home cleaning
    global noAns;
    noAns=0;

def updateNoAnsFlag(val):
    global noAns;
    noAns=val;


def isSingleResult(plaintext):
    answers=plaintext.split("|")
    if len(answers) ==1:
            return 1;
    else:
        return 0;


def isQuestionProfane(question):
    words=question.split(" ");
    for word in words:
        if profane_words.has_key(word.lower()):
            return 1

def isQuestionOverriden(str):

    if(str.lower().find('who')!=-1) and  (str.lower().find('created')!=-1) and (str.lower().find('you')!=-1):
        return 2;
    elif (str.lower().find('who')!=-1) and  (str.lower().find('you')!=-1):
        return 0;
    elif(str.lower().find('what')!=-1) and  (str.lower().find('your')!=-1) and (str.lower().find('name')!=-1):
        return 1;
    else:
        return -1;


def findAnswer(waPod):
    for subpod in waPod.Subpods():
        waSubpod = wap.Subpod(subpod);
        plaintext = waSubpod.Plaintext()[0];
        if isSingleResult(plaintext)==1:
            print plaintext+ "\n";
        
        else:
            print "\n I am not sure. I can think of following things \n. "
            print plaintext + "\n"

