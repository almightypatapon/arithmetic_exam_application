import random


class TaskGenerator:
    numbers_range = {'simple': range(2, 10), 'squares': range(11, 30)}
    level_description = {'simple': f'simple operations with numbers {numbers_range["simple"][0]}-{numbers_range["simple"][-1]}',
                         'squares': f'integral squares of {numbers_range["squares"][0]}-{numbers_range["squares"][-1]}'}
    operations_handler = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b}

    def task(self, squares=False):
        if not squares:
            a, b = random.choice(self.numbers_range['simple']), random.choice(self.numbers_range['simple'])
            operation = random.choice([*self.operations_handler.keys()])
            return a, b, operation
        else:
            a = random.choice(self.numbers_range['squares'])
            return a

    @staticmethod
    def get_answer():
        while True:
            try:
                return int(input())
            except ValueError:
                print('Incorrect format.')

    def get_level(self):
        while True:
            level = input(f'Which level do you want? Enter a number:\n'
                          f'1 - {self.level_description["simple"]}\n'
                          f'2 - {self.level_description["squares"]}\n')
            if level in ['1', '2']:
                return False if level == '1' else True
            else:
                print('Incorrect format.')

    def solve_task(self, squares=False):
        if not squares:
            a, b, operation = self.task()
            print(f'{a} {operation} {b}')
            key = self.operations_handler[operation](a, b)
        else:
            a = self.task(True)
            print(a)
            key = self.operations_handler['*'](a, a)
        answer = self.get_answer()
        if answer == key:
            print('Right!')
            return 1
        else:
            print('Wrong!')
            return 0

    def save_to_file(self, score, no_of_tasks, squares=False):
        filename = 'results.txt'
        level_info = f'1 ({self.level_description["simple"]})' if not squares else f'2 ({self.level_description["squares"]})'
        name = input('What is your name?\n')
        try:
            file = open(filename, 'a')
        except FileNotFoundError:
            file = open(filename, 'w')
        file.write(f'{name}: {score}/{no_of_tasks} in level {level_info}.\n')
        file.close()
        print(f'The results are saved in {filename}.')

    def exam(self, no_of_tasks):
        score = 0
        level = self.get_level()
        for _ in range(no_of_tasks):
            score += self.solve_task(level)
        print(f'Your mark is {score}/{no_of_tasks}.', end=' ')
        if input('Would you like to save the result? Enter yes or no.\n').lower() in ['y', 'yes']:
            self.save_to_file(score, no_of_tasks, level)


task = TaskGenerator()
task.exam(5)
