import pandas as pd
import numpy as np
import statistics


class CommonFunc:

    @staticmethod
    def calc_mean_variance(list):
        """
        :param list
        :return: [標本平均, 標本分散]
        """
        return [statistics.mean(list), statistics.variance(list)]