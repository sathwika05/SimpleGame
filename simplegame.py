print("Hello, welcome")
ans=input('Are you ready to play (yes/no): ')
score=0
total_q=4
if ans.lower()=='yes':
    ans=input('1.what is the best programming language?')
    if(ans.lower()=='python'):
        score+=1
        print('Correct')
    else:
        print('Incorrect')
    ans=input('2.what is 2+8+9-1?')
    if(ans=='18'):
        score+=1
        print('Correct')
    else:
        print('Incorrect')
    ans=input('3.what is better a 1050 ti 0r a 1060 (graphic card)?')
    if(ans.lower()=='1050ti'):
        score+=1
        print('Correct')
    else:
        print('Incorrect')
    ans=input('4.who is Miss World 2017?')
    if(ans.lower()=='manushi'):
        score+=1
        print('Correct')
    else:
        print('Incorrect')
print('Thank you for playing, you got ',score,'Questions correct')
mark=(score/total_q)*100
print("Mark: ",str(mark)+'%')
print('Good Bye')
