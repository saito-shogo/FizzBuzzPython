import unittest
# app,testのパッケージに__init__.pyを置いてテスト実行時に読み込まれるようにしておく
# テスト実行する際のカレントディレクトリはsrc
# 参考：https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure/24266885#24266885
import app.number as number

# unittest.TestCaseを継承して作成（assertXxx()も継承できる）
class TestNumber(unittest.TestCase):

  # スキップしてほしいテストの書き方
  # @unittest.skipIf(この中がTrueでスキップ)
  # @unittest.skipUnless(この中がFalseでスキップ)
  @unittest.skip("スキップの理由をかく")
  def test_スキップするテスト(self) -> None:
    self.assertTrue(False)

  # numberの動作確認用テスト（1-100まで）
  def test_normalNumbers(self) -> None:
    targetList = {1,2,4,7,8,11,13,14,16,17,19,22,23,26,28,29,31,32,34,37,38,41,43,44,46,47,49,52,53,56,58,59,61,62,64,67,68,71,73,74,76,77,79,82,83,86,88,89,91,92,94,97,98}
    for target in targetList:
      self.__assertNormalNumber(target)

  def test_fizzNumbers(self) -> None:
    targetList = {3,6,9,12,18,21,24,27,33,36,39,42,48,51,54,57,63,66,69,72,78,81,84,87,93,96,99}
    for target in targetList:
      self.__assertFizzNumber(target)

  def test_buzzNumbers(self) -> None:
    targetList = {5,10,20,25,35,40,50,55,65,70,80,85,95,100}
    for target in targetList:
      self.__assertBuzzNumber(target)
    
  def test_fizzBuzzNumbers(self) -> None:
    targetList = {15,30,45,60,75,90}
    for target in targetList:
      self.__assertFizzBuzzNumber(target)

  # 各番号の種類によってテストするためのメソッド
  def __assertNormalNumber(self, normalNumber:int) -> None:
    target = number.Number(normalNumber)
    self.assertFalse(target.isFizz(), "number:" + str(normalNumber))
    self.assertFalse(target.isBuzz(), "number:" + str(normalNumber))
    self.assertFalse(target.isFizzBuzz(), "number:" + str(normalNumber))

  def __assertFizzNumber(self, fizzNumber:int) -> None:
    target = number.Number(fizzNumber)
    self.assertTrue(target.isFizz(), "number:" + str(fizzNumber))
    self.assertFalse(target.isBuzz(), "number:" + str(fizzNumber))
    self.assertFalse(target.isFizzBuzz(), "number:" + str(fizzNumber))

  def __assertBuzzNumber(self, buzzNumber:int) -> None:
    target = number.Number(buzzNumber)
    self.assertFalse(target.isFizz(), "number:" + str(buzzNumber))
    self.assertTrue(target.isBuzz(), "number:" + str(buzzNumber))
    self.assertFalse(target.isFizzBuzz(), "number:" + str(buzzNumber))

  def __assertFizzBuzzNumber(self, fizzBuzzNumber:int) -> None:
    target = number.Number(fizzBuzzNumber)
    self.assertTrue(target.isFizz(), "number:" + str(fizzBuzzNumber))
    self.assertTrue(target.isBuzz(), "number:" + str(fizzBuzzNumber))
    self.assertTrue(target.isFizzBuzz(), "number:" + str(fizzBuzzNumber))

# テストを実際に動かすための決まり文句？
if __name__ == "__main__":
  unittest.main()