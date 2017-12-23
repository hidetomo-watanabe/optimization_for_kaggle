import configparser
import numpy as np
import myfuncs


class Optimizer(object):
    def __init__(self, start_path='./start.csv', config_path='./config.ini'):
        with open(start_path, 'r') as f:
            self.start = f.read().strip().split('\n')
        self.current = self.start
        self.cp = configparser.SafeConfigParser()
        self.cp.read(config_path)

    def get_current(self):
        return self.current

    def get_current_scores(self):
        scores = []
        for target in self.current:
            score = eval(
                'myfuncs.%s' % self.cp.get('score', 'evaluation'))(
                target)
            scores.append(score)
        return scores

    def _crossover_with_two_points(self, targets):
        n = 2
        output = []
        for val in targets:
            val_trans = []
            nums = np.sort(np.random.choice(list(range(len(val))), n))
            if nums[0] == nums[1]:
                nums[1] += 1
            val_trans.append(val[: (nums[0] + 1)])
            for i in val[(nums[0] + 1): (nums[1] + 1)]:
                val_trans.append(str(abs(int(i) - 1)))
            val_trans.append(val[(nums[1] + 1):])
            output.append(''.join(val_trans))
        return output

    def go_to_next_generation(self):
        next_generation = self._crossover_with_two_points(self.current)
        self.current = next_generation
        return self.current

if __name__ == '__main__':
    pass
