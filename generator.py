print("INPUT COMMANDS HERE")
commands = []
inital_command = []

def command_convert(string):
    return string.replace('\\\\\\\\\\\\\\"', '\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"').replace('\\\\\\"', '\\\\\\\\\\\\\\\\\\"').replace('\\"', '\\\\\\\\"').replace('"', '\\\\\\"')

def inital_command_convert(string):
    return string.replace('\\\\\\\\\\\\\\"', '\\\\\\\\\\\\\\\\\\\\\\"').replace('\\\\\\"', '\\\\\\\\\\"').replace('\\"', '\\\\"').replace('"', '\\"')

inital_command.append(r'gamerule commandBlockOutput false')

while True:
    commands.append(input())
    if commands[-1] == '':
        commands.remove(commands[-1])
    elif commands[-1].startswith('INIT:'):
        if commands[-1][5] == ' ':
            inital_command.append(commands[-1][6:])
        else:
            inital_command.append(commands[-1][5:])

        commands.remove(commands[-1])
    elif commands[-1] == 'end':
        commands = commands[:-1]
        break

commands2 = []
commands2.append(r'setblock ~-2 ~ ~ oak_wall_sign[facing=west]{Text1:"[\"\"]",Text2:"{\"text\":\"DESTROY\",\"bold\":true,\"color\":\"red\",\"clickEvent\":{\"action\":\"run_command\",\"value\":\"fill ~ ~-1 ~1 ~%s ~1 ~-1 air\"}}",id:"Sign"}' %(len(commands) + 3))
for command in commands:
    commands2.append(command)

result = ''

for init_command in inital_command:
    result += ',{id:"command_block_minecart",Command:"%s"}' %(inital_command_convert(init_command))

x = 4
for command in commands2:
    if x - 4 == 0:
        result += ',{id:"command_block_minecart",Command:"setblock ~%s ~-2 ~ repeating_command_block[facing=east]{Command:\\"%s\\",auto:1b}"}' %(x, command_convert(command))
    else:
        result += ',{id:"command_block_minecart",Command:"setblock ~%s ~-2 ~ chain_command_block[facing=east]{Command:\\"%s\\",auto:1b}"}' %(x, command_convert(command))

    x += 1
    
result = 'summon falling_block ~ ~1  ~ {BlockState:{Name:"stone"},Time:100,Passengers:[{id:"falling_block",BlockState:{Name:"sand"},Time:0,DropItem:0b,HurtEntities:0b,Passengers:[{id:"falling_block",BlockState:{Name:"redstone_block"},Time:100,Passengers:[{id:"falling_block",BlockState:{Name:"sand"},Time:0,DropItem:0b,HurtEntities:0b,Passengers:[{id:"falling_block",BlockState:{Name:"activator_rail"},Time:100,Passengers:[{id:"command_block_minecart",Command:"setblock ~2 ~-3 ~ command_block[facing=up]{Command:\\"execute positioned ~-2 ~3 ~ run kill @e[type=command_block_minecart,distance=..1]\\", auto:1b}"},{id:"command_block_minecart",Command:"setblock ~2 ~-2 ~ chain_command_block[facing=up]{Command:\\"fill ~ ~-1 ~ ~-3 ~2 ~ air\\", auto:1b}"},{id:"command_block_minecart",Command:"fill ~3 ~-3 ~1 ~%s ~-3 ~-1 blue_terracotta"},{id:"command_block_minecart",Command:"fill ~3 ~-1 ~1 ~%s ~-1 ~-1 blue_terracotta"},{id:"command_block_minecart",Command:"fill ~3 ~-2 ~1 ~%s ~-2 ~-1 green_stained_glass hollow"}' %(x, x, x) + result
result += ']}]}]}]}]}'
print(result)
                                                                                                                            
input()
