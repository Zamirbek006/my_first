# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
#
# dis_width = 800
# dis_height = 600
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 30
#
# font_style = pygame.font.SysFont(None, 50)
# score_font = pygame.font.SysFont(None, 35)
#
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# def game_loop():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_List = []
#     Length_of_snake = 1
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(blue)
#             message("You lost! Press Q-Quit or C-Play Again", red)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         game_loop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# game_loop()



# import time
#
#
#
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # замер времени начала
#         resultat = func(*args, **kwargs)  # выполнение функции
#         end_time = time.time()  # замер времени окончания
#         execution_time = end_time - start_time  # вычисление времени выполнения
#         print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
#         return resultat  # возврат результата выполнения функции
#     return wrapper
#
#
# @measure_time
# def example_function(seconds):
#     time.sleep(seconds)  # имитация работы с задержкой
#     return "Функция завершена"
#
# result = example_function(2)
# print(result)


# x = 1
# while True:
#     if len(str(x)) == 1:
#         x += 2
#     else:
#         break
# print(x)


# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
# do_operation(5, 4, lambda a, b: a + b)
# do_operation(5, 4, lambda a, b: a * b)


# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#     elif choice == 2:
#         return lambda a, b: a - b
#     else:
#         return lambda a, b: a * b
#
# operation = select_operation(1)
# print(operation(10,6))
#
# operation = select_operation(2)
# print(operation(10, 6))
#
# operation = select_operation(3)
# print(operation(10, 6))

































































