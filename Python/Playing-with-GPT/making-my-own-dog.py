class Dog:
    def __init__(self,name,age):
        self.name=name #강아지의 이름
        self.age=age #강아지의 나이
    
    def bark(self):
        print(f"{self.name}가 멍멍 짖어요")

    def intro(self):
        print(f"안녕 나는 {self.age}살, {self.name}")


#인스턴스 만들기
dog1=Dog('콩이',2)
dog2=Dog('초코',5)

#동작시키기
dog1.bark()
dog1.intro()

        