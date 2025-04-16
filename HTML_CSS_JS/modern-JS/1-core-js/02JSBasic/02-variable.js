let message1 = "졸리당!";
alert(message1);

//다양한 변수선언 코드 스타일
// let user = "a";
// let age = 25;
// let message = "Hello";

// let user2 = "b",
//   age2 = 25,
//   message2 = "world";

// let user3 = "c"
//   ,age3 = 25
//   ,message3 = "!!";

//값이 변경되면, 이전 데이터는 변수에서 제거됩니다.
let lunchset;
lunchset = "🍎";
lunchset = "🥭";
alert(lunchset);

//변수 복사
let hello = "무야호! hello world";
let message;
message = hello;
//이제 두 변수는 같은 데이터값
alert(hello);
alert(message);

//상수
const COLOR_RED = "#F00";
const COLOR_BLUE = "#00F";

//불린형
let isGreater = 4 > 1;
alert(isGreater);

//null 값
//다른 언어와 성격이 다름, 다른언어는 '존재하지 않은 객체','널포인터'
//js에선 알수없거나, 값이 비어있음을 뜻한다.
let ageNull = null;

//undefined 값
//undefined 값도 null 값처럼 자신만의 자료형을 형성합니다.
//undefined는 '값이 할당되지 않은 상태’를 나타낼 때 사용합니다.
// 변수는 선언했지만, 값을 할당하지 않았다면 해당 변수에 undefined가 자동으로 할당됩니다.
let ageUndefined;
alert(ageUndefined);

// 개발자가 변수에 undefined를 명시적으로 할당하는 것도 가능하긴 합니다.
// 하지만 이렇게 undefined를 직접 할당하는 걸 권장하진 않습니다. 
// 변수가 ‘비어있거나’ ‘알 수 없는’ 상태라는 걸 나타내려면 null을 사용하세요. undefined는 값이 할당되지 않은 변수의 초기값을 위해 예약어로 남겨둡시다.

