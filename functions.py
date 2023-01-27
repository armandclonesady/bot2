import os
import asyncio

def getAllModules():
    allModules = []
    for files in os.listdir('./modules'):
        if files.endswith('.py'):
            allModules.append("modules."+files.removesuffix('.py'))

    return allModules

async def reloadAllModules(client):
    for module in getAllModules():
        await asyncio.sleep(3)
        client.remove(module)
        await asyncio.sleep(3)
        client.load(module)
        print(f"Reloaded {module}")

def getAllServers(client):
    allServers = []
    for guild in client.guilds:
        allServers.append(guild)
    return allServers