import pygame

pygame.init()


object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
object3 = pygame.Rect((0, 0), (50, 50))
object4 = pygame.Rect((100, 100), (30, 50))


print(object1.colliderect(object2))
print(object1.colliderect(object3))
print(object2.colliderect(object3))

object5 = object1.move(100, 100)
print(object1.topleft)
print(object5.topleft)

object1.move_ip(100, 100)
print(object1.topleft)

print(object1.collidepoint(50, 75))

lst = [object4, object3, object2]
print(object1.collidelist(lst))

object1.update((30, 30), (50, 50))
print(object1.topleft)
print(object1.size)