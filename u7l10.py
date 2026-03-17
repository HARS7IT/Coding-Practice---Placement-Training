class FrequencyCounter:
  def __init__(self, numbers):
    self.numbers = numbers
    self.frequency = {}

  def count_freq(self):
    for num in self.numbers:
      if num in self.frequency:
        self.frequency[num] += 1
      else:
        self.frequency[num] = 1
  
  def display(self):
    for num, freq in self.frequency.items():
      print(f"{num} : {freq}")

  
numbers = [1,2,3,3,3,5,6,7,7,8]
f = FrequencyCounter(numbers)
f.count_freq()
f.display()