
# ----- 코드 정의 ------
class Member:
    name = ''
    username = ''
    password = ''

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
    
    def __str__(self):
        return f"Member 인스턴스 : {self.name} {self.username}"

    def __repr__(self):
        return f"{self.name} {self.username}"
        
    def display(self):
        print(self.name)
        



class Post:
    title = ''
    content = ''
    author = ''
    def __init__(self,title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"post 인스턴스 : {self.title} {self.content} {self.author}"

    def __repr__(self):
        return f"{self.title} {self.content} {self.author.username}"

# ----- 코드 실행 ------
p1 = Member('이준승','커피마스터','123')
p2 = Member('권진우','호박덜렁이','456')
p3 = Member('한승협','백엔드마스터','789')
p4 = Member('이은규','제부','1010')

Members = []
members_list = [p1, p2, p3, p4]

for member in members_list:
    Members.append(member)
print(Members)


l1 = Post('하루 1잔 커피가 몸에 좋은 이유','커피를 하루 1∼3잔 마시면 커피를 마시지 않는 사람보다 심혈관질환·호흡기 질환·당뇨병으로 인한 사망률이 각각 20%, 32%, 47% 감소했다',p1)
l2 = Post('제목','컨텐츠',p1)
l3 = Post('제목','컨텐츠',p1)
l4 = Post('제목','컨텐츠',p2)
l5 = Post('제목','컨텐츠',p2)
l6 = Post('제목','컨텐츠',p2)
l7 = Post('제목','컨텐츠',p3)
l8 = Post('제목','컨텐츠',p3)
l9 = Post('제목','컨텐츠',p3)
l10 = Post('제목','컨텐츠',p4)
l11 = Post('제목','컨텐츠',p4)
l12 = Post('제목','컨텐츠',p4)




posts = []
post_list = [l1, l2, l3, l4,l5,l6,l7,l8,l9,l10,l11,l12]
for list in post_list:
    posts.append(list)
print(posts)



# TODO : 코드 구현이 필요합니다.