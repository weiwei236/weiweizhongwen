# Chèn scratchpad/h4/h4.js vào src.html giữa /* H4_DATA_BEGIN */ … /* H4_DATA_END */ và nối HSK4 vào LEVELS/GRAMMAR. Chạy lại được.
import os
SP='/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/h4/h4.js'
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','src.html')
s=open(P,encoding='utf-8').read(); js=open(SP,encoding='utf-8').read()
B,E='/* H4_DATA_BEGIN */','/* H4_DATA_END */'
if B not in s:
    k=s.index('/* H3_DATA_END */')+len('/* H3_DATA_END */')
    s=s[:k]+'\n'+B+'\n'+E+s[k:]
i=s.index(B)+len(B); j=s.index(E)
s=s[:i]+'\n'+js+s[j:]
s=s.replace(' hsk4:{name:"HSK 4", total:0, lessons:{}},',' hsk4:{name:"HSK 4", total:20, lessons:H4_LESSONS},')
if 'GRAMMAR.hsk4' not in s:
    a='GRAMMAR.hsk3 = H3_GRAMMAR;'; assert s.count(a)==1; s=s.replace(a,a+' GRAMMAR.hsk4 = H4_GRAMMAR;')
open(P,'w',encoding='utf-8').write(s); print('ok',len(js))
