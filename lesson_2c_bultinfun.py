# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: Python_Foundations
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: lesson_2c_bultinfun
 * Date: 10/3/15
 * Time: 9:52 PM
 * To change this template use File | Settings | File Templates.
"""
num_list = [4, 2, 6, 3, 7, 4]

minmax_list = []
for num in num_list:
    minmax_list.append(float(num-min(num_list))/float(max(num_list)-min(num_list)))
print minmax_list
