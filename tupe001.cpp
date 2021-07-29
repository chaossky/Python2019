// tuple example
// 필요한 라이브러리를 인클루드 한다.
#include <iostream>     // std::cout
#include <tuple>        // std::tuple, std::get, std::tie, std::ignore

int main ()
{
//튜플을 만들고 첫번째는 정수, 두번째는 캐릭터 형식으로 지정하고
// 튜플의 이름을 foo 라고 지정하고 값을 지정한다.
  std::tuple<int,char> foo (10,'x');

//튜플의 들어간 내용을 출력하기 위해서는 get 메소드<튜플에 저장 된 순서>(튜플이름)
//으로 꺼내서 본다.
  std::cout << "foo contains: ";
  std::cout << std::get<0>(foo) << ' ';
  std::cout << std::get<1>(foo) << '\n';
  
//튜플
std::tuple<int,int> bindae (100,20);
std::cout << "bindae contains: ";
  std::cout << std::get<0>(bindae) << ' ';
  std::cout << std::get<1>(bindae) << '\n';

//튜플내의 자료형을 일일히 지정하지 않고
// auto 그리고 그저 값을 직접 입력하여서 make_tuple() 하고 각각의
//자료를 집어 넣었다.

  auto bar = std::make_tuple ("test", 3.1, 14, 'y');
  std::cout << "bar contains: ";
  std::cout << std::get<0>(bar) << ' ';
  std::cout << std::get<1>(bar) << ' ';
  std::cout << std::get<2>(bar) << ' ';
  std::cout << std::get<3>(bar) << '\n';

auto baro = std::make_tuple ('c',"vool",40,0.9);
  std::cout << "baro contains: ";
  std::cout << std::get<0>(baro) << ' ';
  std::cout << std::get<1>(baro) << ' ';
  std::cout << std::get<2>(baro) << ' ';
  std::cout << std::get<3>(baro) << '\n';

  std::get<2>(bar) = 100;                                    // access element

  int myint; char mychar;

  std::tie (myint, mychar) = foo;                            // unpack elements
  std::tie (std::ignore, std::ignore, myint, mychar) = bar;  // unpack (with ignore)

  mychar = std::get<3>(bar);

  std::get<0>(foo) = std::get<2>(bar);
  std::get<1>(foo) = mychar;

  std::cout << "foo contains: ";
  std::cout << std::get<0>(foo) << ' ';
  std::cout << std::get<1>(foo) << '\n';

  return 0;
}