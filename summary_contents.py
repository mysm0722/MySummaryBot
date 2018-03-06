from __future__ import print_function
from textrankr import TextRank
import sys

#textrank = TextRank("나는 프로그래머 입니다. 자바 프로그래머, 그냥 프로그래머");
#print(sys.argv[1]);
textrank = TextRank(sys.argv[1]);
print(textrank.summarize())
