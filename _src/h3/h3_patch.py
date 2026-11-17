# Chèn scratchpad/h3/h3.js vào src.html giữa /* H3_DATA_BEGIN */ … /* H3_DATA_END */ (tạo marker lần đầu)
import os
SP='/tmp/claude-0/-home-claude/c42ce2af-05ed-5ab0-9ae7-40fe1ca5a6a5/scratchpad/h3/h3.js'
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','src.html')
s=open(P,encoding='utf-8').read(); js=open(SP,encoding='utf-8').read()
B,E='/* H3_DATA_BEGIN */','/* H3_DATA_END */'
if B not in s:
    k=s.index('/* GC_DATA_END */')+len('/* GC_DATA_END */')
    s=s[:k]+'\n'+B+'\n'+E+s[k:]
i=s.index(B)+len(B); j=s.index(E)
s=s[:i]+'\n'+js+s[j:]
open(P,'w',encoding='utf-8').write(s); print('ok',len(js))
