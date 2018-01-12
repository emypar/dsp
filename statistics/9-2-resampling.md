[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

>> ```
>> Preg Length Actual Stat=0.078037
>> Birth Weight Actual Stat=0.124761
>> Comparison Table:
>>              Preg Length p-val  Birth Weight p-val
>> Simulation                                        
>> Permutation             0.1654                 0.0
>> Resampling              0.1696                 0.0
>> ```
>>
>> **Conclusion:** The p-values returned by both simulation methods are very close
>> to each other and they lead to the same interpretation:  
>>  - pregnancy lengthdifference is statistically insignificant 
>>  - birth weight length is statisticallysignificant
>>
>> **Code:** [9-2-resampling.ipynb](https://nbviewer.jupyter.org/github/emypar/dsp/blob/master/statistics/9-2-resampling.ipynb)