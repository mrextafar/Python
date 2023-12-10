from gmpy2 import mpz
import math

def expected_value(n):
  """
  Находит ожидаемое значение произведения всех шестиугольных чисел, записанных в гусенице из n пазлов.

  Args:
    n: Количество пазлов в гусенице.

  Returns:
    Ожидаемое значение произведения, по модулю 987654319.
  """

  # Вероятность формирования сегмента длиной k.

  def p(k):
    return mpz(math.factorial(k)) / (mpz(math.factorial(n)) * mpz(math.factorial(n - k)))

  # Ожидаемое значение произведения при заданной длине сегмента k.

  def e(k):
    return mpz(math.prod([i * (2 * i - 1) for i in range(1, k + 1)])) * (n - k + 1) / n

  # Сумма по всем возможным длинам сегментов.

  return sum([p(k) * e(k) for k in range(1, n)]) % 987654319

print(expected_value(100))
