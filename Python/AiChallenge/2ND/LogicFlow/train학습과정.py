#학습과정

#패키지 임포트

#haper-parameter 선언 (10바퀴 돌릴거야 같은 학습선언)
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor,Resize,Normalize,Compose,DataLoader


##데이터 불러오기 : CIFAR10 
#전처리하는 transform을 설정
transform=Compose(Resize(32,32),ToTensor(),Normalize())
#주방보조(Dataset)
train_dataset = CIFAR10(root='../data',train=True,transform=transform,download=True)
test_dataset = CIFAR10(root='../data',train=False,transform=transform,download=True)
#셰프(Dataloader)
train_dataloader=DataLoader(train_dataset,batch_size=100,num_workers=0)
test_dataloader=DataLoader(test_dataset,batch_size=100,num_workers=0)

## 네트워크 선언 (두가지가 필요하다고 했음)
# class 설계도 필요함. nn.Module
    #__init__ 메소드
        # CIFAR10 이미지를 활용
        # Layer1~5, output layer 모듈 선언
    # forward 메소드 ⭐
        # Layer1~5 통과
        # 크기 변화
        # Output Layer 통과
        # 출력

#haper parameter로 AI 모델 객체 생성 

#Loss함수 필요
#Optimizer 필요

#내가 선언한 학습 횟수만큼 (for loop)
    #데이터 네트워크에 넣어줘야하는데

    #Loss계산
    #Loss back propagation
    #Optimizer로 최적화 진행

    #어느 정도 횟수마다
        #학습이 잘 되는지 Loss값 확인
        #평가도 진행
        #평가 결과가 좋으면 
        #저장하고