class Projectile:
    def __init__(self, x, y, x_vel, y_vel):
        self.y_vel = y_vel
        self.x_vel = x_vel
        self.y = y
        self.x = x
        self.y_max = 0

    def increase_step(self):
        self.y += self.y_vel
        self.x += self.x_vel

        if self.y > self.y_max:
            self.y_max = self.y

        self.y_vel -= 1
        if self.x_vel > 0:
            self.x_vel -= 1
        if self.x_vel < 0:
            self.x_vel += 1

    def check(self, x_t1, x_t2, y_t1, y_t2):
        if self.x in range(x_t1, x_t2 + 1) and self.y in range(y_t1, y_t2 + 1):
            return 1
        if self.x > x_t2 or self.y < y_t1:
            return -1
        return 0


def answer():
    x_t1 = 56
    x_t2 = 76
    y_t1 = -162
    y_t2 = - 134
    n = 0
    for x_vel in range(0, 90):
        for y_vel in range(165, -163, -1):
            new_projectile = Projectile(0, 0, x_vel, y_vel)
            while new_projectile.check(x_t1, x_t2, y_t1, y_t2) == 0:
                new_projectile.increase_step()
            if new_projectile.check(x_t1, x_t2, y_t1, y_t2) == 1:
                n += 1
    return n


print(answer())