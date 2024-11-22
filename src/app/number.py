from typing import Final

class Number:
  # FizzBuzz用定数の宣言(TODO:staticにする)
  __numberOfFizz: Final[int] = 3
  __numberOfBuzz: Final[int] = 5

  # クラス変数
  __number: Final[int]

  # コンストラクタ
  def __init__(self, number:int):
    self.__number = number

  # 特定の値で割り切れるか
  def __isMultipleOf(self, devisor:int) -> bool:
    return (self.__number % devisor) == 0

  # Fizz、Buzz、FizzBuzzの判定メソッド
  def isFizz(self) -> bool:
    return self.__isMultipleOf(self.__numberOfFizz)

  def isBuzz(self) -> bool:
    return self.__isMultipleOf(self.__numberOfBuzz)

  def isFizzBuzz(self) -> bool:
    return self.isFizz() & self.isBuzz()

  def getNumber(self) -> int:
    return self.__number
