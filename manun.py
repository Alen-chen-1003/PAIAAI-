import pickle
import os
import pygame
import csv
class MLPlay:
    def __init__(self, player, *args, **kwargs):
        self.r_sensor_value = 0
        self.l_sensor_value = 0
        self.f_sensor_value = 0
        self.r_t_sensor_value =0
        self.l_t_sensor_value =0
        self.left_PWM = 0
        self.right_PWM = 0
        self.feature = []
        self.target = []
        self.i =12
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        if scene_info['status'] == "GAME_PASS":
            with open(os.path.join(os.path.dirname(__file__), 'feature'+str(self.i)+'.pickle'), 'wb') as f:
                    pickle.dump(self.feature, f)
            with open(os.path.join(os.path.dirname(__file__), 'target'+str(self.i)+'.pickle'), 'wb') as f:
                    pickle.dump(self.target, f)
            with open(os.path.join(os.path.dirname(__file__), 'feature' + str(self.i) + '.csv'), 'w', newline='') as f:
                    csv.writer(f, delimiter=',').writerows(self.feature)
            # 可以將收集的馬達數據，打開來看
            with open(os.path.join(os.path.dirname(__file__), 'target' + str(self.i) + '.csv'), 'w', newline='') as f:
                    csv.writer(f,delimiter =',').writerows(self.target)
        elif pygame.K_UP in keyboard:
            self.left_PWM = 255
            self.right_PWM = 255
        elif pygame.K_RIGHT in keyboard:
            self.left_PWM = 255
            self.right_PWM = -255
            self.feature.append([scene_info['F_sensor'], scene_info['L_sensor'], scene_info['R_sensor'], scene_info['L_T_sensor'], scene_info['R_T_sensor']])
            self.target.append(str(1))
        elif pygame.K_LEFT in keyboard:
            self.left_PWM = -255
            self.right_PWM = 255
            self.feature.append([scene_info['F_sensor'], scene_info['L_sensor'], scene_info['R_sensor'], scene_info['L_T_sensor'], scene_info['R_T_sensor']])
            self.target.append(str(2))
        elif pygame.K_DOWN in keyboard:
            self.left_PWM = -150
            self.right_PWM = -150
        else:
            self.left_PWM = 255
            self.right_PWM = 255
            self.feature.append([scene_info['F_sensor'], scene_info['L_sensor'], scene_info['R_sensor'], scene_info['L_T_sensor'], scene_info['R_T_sensor']])
            self.target.append(str(3))
        
        return [{'left_PWM': self.left_PWM, 'right_PWM': self.right_PWM}]
    def reset(self):
        self.i +=1
        pass
