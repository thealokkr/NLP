#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap
import random
import qBotLib

print "\n You won't believe but i am a bot. Ask me anything\n";

while 1:
    
    qBotLib.resetBotParts();

    question=raw_input('\n> ');
    
    if qBotLib.isQuestionProfane(question)==1:
        print qBotLib.proFaneMsg_array[random.randint(0,1)];

    elif qBotLib.isQuestionOverriden(question)!=-1:
        print qBotLib.overridenQAns[qBotLib.isQuestionOverriden(question)];

    else:
        
        waeo = wap.WolframAlphaEngine(qBotLib.appid, qBotLib.server);
        queryStr = waeo.CreateQuery(question);
        wap.WolframAlphaQuery(queryStr, qBotLib.appid);
        result = waeo.PerformQuery(queryStr);
        result = wap.WolframAlphaQueryResult(result);

        for pod in result.Pods():
            waPod = wap.Pod(pod);
            title = waPod.Title()[0];
            if  title == "Result":
                qBotLib.findAnswer(waPod);
                qBotLib.updateNoAnsFlag(1);
                break;

            #Check if we have any reply from Knowledge engine
        if qBotLib.noAns!=1:
            print qBotLib.preDefinedMsg_array[random.randint(0,1)];

