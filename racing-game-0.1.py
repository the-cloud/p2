# racing game by @thecloud_1

import mcpi.minecraft as minecraft
import microbit
import time
import random

mc = minecraft.Minecraft.create()

def clear_path(mc):
    x, y, z = mc.player.getPos()
    for back_lane in range(5):
        mc.setBlock(x - 2 + back_lane, y - 1, z - 1, 0)
    for rows in range(5):
        i = 0
        for length in range(150):
            mc.setBlock(x - 2 + rows, y - 1, z + i, 0)
            i += 1


def finish_line(x, y, z, mc):
    y -= 2
    z += 149
    for rows in range(5):
        mc.setBlock(x - 2 + rows, y, z, 152)


def obstacle(x, y, mc):
    x1 = x
    y1 = y
    pos = mc.player.getPos()
    loss = random.randint(0, 5)
    mc.setBlock(x1 - 2 + loss, y1, pos.z + 5, 46)


def race(mc):
    pos = mc.player.getPos()
    x = microbit.accelerometer.get_x()/1000
    y = microbit.accelerometer.get_y()/1000
    pos.x += x
    pos.z += y
    if mc.getBlock(pos.x, pos.y, pos.z) == 0:
        mc.player.setPos(pos.x, pos.y, pos.z)

def run(mc):
    x, y, z = mc.player.getPos()
    finish_line(x, y, z, mc)
    clear_path(mc)
    time.sleep(1)
    x, y, z = mc.player.getPos()
    some = 0
    while True:
        race(mc)
        time.sleep(0.02)
        some += 1
        if some == 10:
            obstacle(x, y, mc)
            some = 0
        pos = mc.player.getPos()
        if mc.getBlock(pos.x, pos.y - 1, pos.z) == 152:
            break
run(mc)
