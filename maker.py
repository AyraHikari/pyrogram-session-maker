import os, asyncio

try:
	import pyrogram
except ModuleNotFoundError:
	print("You need to install pyrogram first!\nSee: https://github.com/AyraHikari/pyrogram-session-maker")
	exit(1)

# Cleanup
try:
	os.remove("my.session")
except:
	pass
try:
	os.remove("bot.session")
except:
	pass


print("\n\nYou need to register to get app_id and api_hash in here: https://my.telegram.org/apps")
input("Press any key to continue")


while True:
	print("You want to make session for user bot or real bot?")
	print("1 = user bot")
	print("2 = real bot")
	createbot = input("[1/2] ")
	if str(createbot).isdigit():
		createbot = int(createbot)
		break
	print("Invaild selection!\n")


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




if pyrogram.__version__.split(".")[-1] in ("asyncio", "asyncio-dev"):
	if createbot == 1:
		app = pyrogram.Client("my", api_id=api_id, api_hash=app_hash)
		ses = "my.session"
		sestxt = "my.txt"
	elif createbot == 2:
		bot_token = input("Insert bot token: ")
		app = pyrogram.Client("bot", api_id=api_id, api_hash=app_hash, bot_token=bot_token)
		ses = "bot.session"
		sestxt = "bot.txt"

	async def start_app():
		await app.start()
		session = app.export_session_string()
		print(f"Done!\nYour session string is:\n\n{session}")
		print(f"\n\nSession string will saved as {sestxt}, Also you can copy {ses} to session dir if need.\nNever share this to anyone!")
		open(sestxt, "w").write(str(session))

	asyncio.get_event_loop().run_until_complete(start_app())
else:
	if createbot == 1:
		app = pyrogram.Client("my", api_id=api_id, api_hash=app_hash)
		ses = "my.session"
		sestxt = "my.txt"
	elif createbot == 2:
		bot_token = input("Insert bot token: ")
		app = pyrogram.Client("bot", api_id=api_id, api_hash=app_hash, bot_token=bot_token)
		ses = "bot.session"
		sestxt = "bot.txt"

	with app as generation:
		session = generation.export_session_string()
		print(f"Done!\nYour session string is:\n\n{session}")
		print(f"\n\nSession string will saved as {sestxt}, Also you can copy {ses} to session dir if need.\nNever share this to anyone!")
		open(sestxt, "w").write(str(session))
