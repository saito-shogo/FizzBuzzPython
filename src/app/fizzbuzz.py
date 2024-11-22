import number

class FizzBuzz:
  # 定数
  fizz: str = "Fizz"
  buzz: str = "Buzz"
  type: int = 0

  # 初期値、終了値
  start: int
  end: int

  def __init__(self, start, end) -> None:
    self.start = start
    self.end = end

  # FizzBuzzの結果表示
  def run(self) -> None:
    current = self.start
    while(current <= self.end):
      currentNumber = number.Number(current)
      self.__printNumber(currentNumber)
      # pythonには'x++'のような演算子がない
      current += 1

  def __printNumber(self, targetNumber:number.Number) -> None:
    match(self.type):
      case 0:
        print(self.__getNumber(targetNumber))
      case 1:
        print(self.__getNumberVerConcat(targetNumber))
      case _:
        return

  def __getNumber(self, targetNumber:number.Number) -> str:
    if (targetNumber.isFizzBuzz()):
      return self.fizz + self.buzz
    if (targetNumber.isFizz()):
      return self.fizz
    if (targetNumber.isBuzz()):
      return self.buzz
    return str(targetNumber.getNumber())

  def __getNumberVerConcat(self, targetNumber:number.Number) -> str:
    result: str = ""
    if (targetNumber.isFizz()):
      result += self.fizz
    if (targetNumber.isBuzz()):
      result += self.buzz

    return str(targetNumber.getNumber()) if result == "" else result
