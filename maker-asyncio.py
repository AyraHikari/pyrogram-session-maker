import asyncio

try:
	import pyrogram
except ModuleNotFoundError:
	print("You need to install pyrogram first!\nSee: https://github.com/AyraHikari/pyrogram-session-maker")
	exit(1)

print("\n\nYou need to register to get app_id and api_hash in here: https://my.telegram.org/apps")
input("Press any key to continue")

while True:
	api_id = input("\nInsert app_id: ")
	if str(api_id).isdigit():
		break
	print("Invaild app_id!")

while True:
	app_hash = input("Insert api_hash: ")
	if app_hash:
		break
	print("Invaild api_hash!")

app = pyrogram.Client(f"my.session", api_id=api_id, api_hash=app_hash)

async def start_app():
	await app.start()
	session = app.export_session_string()
	print(f"Done!\nYour session string is:\n\n`{session}`")
	print("\n\nAlso you can copy my.session to anywhere.\nNever share this to anyone!")

asyncio.get_event_loop().run_until_complete(start_app())
