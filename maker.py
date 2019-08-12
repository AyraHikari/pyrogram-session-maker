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
	api_id = input("Insert api_hash: ")
	if api_id:
		break
	print("Invaild api_hash!")

with pyrogram.Client(f"my.session", api_id=api_id, api_hash=app_hash) as generation:
	session = generation.export_session_string()
	print(f"Done!\nYour session string is:\n\n`{session}`")
	print("\n\nAlso you can copy my.session to anywhere.\nNever share this to anyone!")
